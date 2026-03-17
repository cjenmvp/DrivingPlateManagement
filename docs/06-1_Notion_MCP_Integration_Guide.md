# Notion MCP 연동 및 DB 동기화 가이드 (VP Stage Management)

## 1. 개요
본 문서는 VP Stage의 물리적 인프라 정보(Main Wall, Sub Wall 크기/해상도, 전력 용량 등)를 **Notion** 기반으로 작성 및 관리하고, 이를 **AI 에이전트(Antigravity MCP)** 가 주기적 또는 지시에 따라 읽어들여 **로컬 Database (SQLite)** 로 직접 구조화 및 동기화하는 아키텍처와 설정 방법을 정리한 매뉴얼입니다.

---

## 2. 사전 준비 (Notion API 설정)

1. **Integration Token 발급**
   - Notion 개발자 페이지 (https://www.notion.so/my-integrations) 에서 커스텀 API 통합(Integration) 생성 후 **프라이빗 API 토큰(Secret)** 발급.
2. **Notion 페이지 권한 허용**
   - 데이터를 조회할 Notion 페이지 (예: `VP Stage 도면`)의 우측 상단 `[...]` 메뉴 -> `연결(Connections)` 탭에서 새로 생성한 Integration을 추가하여 읽기 권한을 부여합니다.
3. **보안 및 환경 변수 설정 (`.env`)**
   - 개발 환경 보호를 위해 작업 폴더(예: `rnd_notion_api`) 내에 `.env` 파일을 생성하고 아래와 같이 저장합니다.
     ```env
     NOTION_API_KEY=secret_abc123...
     NOTION_PAGE_ID=1839bebf-4ee0...
     ```
   - `.gitignore` 파일에 `.env`를 추가하여 GitHub 등 버전 관리에 실수로 키가 업로드되지 않도록 방지 필수. (`python-dotenv` 라이브러리로 접근 제어)

---

## 3. Notion MCP 서버 설정 (Antigravity AI)

에이전트(AI)가 파이썬 스크립트 없이도 Notion 내의 데이터를 직접 검색하고 문맥을 파악할 수 있도록 **MCP(Model Context Protocol)** 를 등록합니다.

1. Antigravity AI 설정 메뉴 또는 MCP Store에서 `notion-mcp-server`를 찾아 활성화합니다.
2. 설정 시, 발급받은 `NOTION_API_KEY`를 환경 변수 또는 설정창에 부여하여 커넥션을 맺습니다.
3. 성공적으로 연동될 경우, 에이전트는 `mcp_notion-mcp-server_API-post-search` 나 `retrieve-a-page`, `get-block-children` 도구를 이용해 타겟 페이지의 텍스트와 블록 데이터를 직접 추출할 수 있게 됩니다.

---

## 4. 동기화 프로세스: 에이전트 주도 (Agentic Sync) 구조

기존의 복잡한 파이썬 스케줄러(Cron) 및 크롤링 코드 유지보수 대신, **AI 에이전트가 주도하는 브릿지 방식**을 채택했습니다.

1. **요청 (Trigger)**
   - 사용자: *"Notion에 VP Stage 사이즈 업데이트됐어. DB에 최신화해줘."*
2. **파싱 (Agentic Scrape)**
   - 에이전트는 Notion MCP 서버를 호출해 해당 페이지(VP Stage, Sub Wall 등)의 최신 블록 단위 텍스트 데이터를 읽습니다.
   - 텍스트 내에서 `19.4m`, `1.68 Pitch`, `전력 900A` 등을 정규화/단위 변환(mm 변환 등)하여 JSON 형태의 구조화된 데이터로 파싱합니다.
3. **DB 반영 (Execute Update)**
   - 에이전트가 추출한 데이터를 인자로 넣어서 로컬 파이썬 마이그레이션 스크립트(`update_db_from_notion.py` 등)를 터미널 커맨드로 즉각 실행합니다.
   - 성공적으로 로컬 SQLite 내 `Infrastructure` 테이블이 업데이트됩니다.

---

## 5. 데이터베이스 스키마 기반 (DB Schema Mapping)

`01_Ontology.md` 정보를 바탕으로 구성한 기초 물리 자산(`Infrastructure`) 테이블 구조는 아래와 같습니다.

| 컬럼명 | 타입 | 설명 (Example) |
|---|---|---|
| `id` | INTEGER | 고유 ID (Primary Key) |
| `name` | TEXT | 자산 명칭 (예: "Main Wall", "Sub Wall") |
| `type` | TEXT | 유형 (예: "LED Wall", "Power") |
| `width_mm` | INTEGER | 물리 가로 길이 (예: 51000, 19354) |
| `height_mm` | INTEGER | 물리 세로 길이 (예: 30800, 3629) |
| `resolution_w` | INTEGER | 디스플레이 해상도 (가로) |
| `resolution_h` | INTEGER | 디스플레이 해상도 (세로) |
| `pixel_pitch` | REAL | LED 픽셀 피치 (예: 1.68) |
| `description` | TEXT | 부가 스펙 텍스트 (예: 900A 3개 라인 등 전력 정보) |
| `last_sync_time` | DATETIME | Notion에서 데이터가 갱신된 최종 시간 |

---

## 6. 주요 산출물 (Scripts & Files)

- `rnd_notion_api/.env`, `.gitignore` : 보안 키 관리
- `rnd_notion_api/test_notion_api.py` : Python상 Notion API 연동 여부 및 접근 가능 페이지 리스트 테스트 코드.
- `implementation_plan.md` / `task.md` (Antigravity Brain) : 전체 R&D 오케스트레이션 및 상태 보관 산출물.
