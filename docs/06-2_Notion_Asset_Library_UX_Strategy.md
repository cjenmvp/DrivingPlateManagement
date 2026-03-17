# 06-2. Notion Asset Library UX 전략 (프론트엔드)

## 1. 개요
본 문서는 VP Asset Library의 클라이언트 접점(UX/UI) 구성을 정리한 전략서입니다. 
데이터베이스(로컬 SQLite)와 연동하여 최종적으로 클라이언트에게 드라이빙 플레이트(멀티뷰어)를 어떻게 제공할 것인지에 대한 설계 가이드라인을 담고 있습니다.

## 2. 채택된 전략: Notion Gallery View + YouTube Embed
가장 무거운 영상 데이터 호스팅은 구글(유튜브)에 맡기고, 클라이언트가 영상을 찾고 스펙을 확인하는 프론트엔드 UX는 예쁜 노션(Notion)으로 꾸미는 비용/효율 최적화 전략입니다.

### 2.1 통합 아키텍처 흐름
1. **스토리지 (Local)**: 시스템이 `X:\05_DrivingPlate_Multiview` 영상을 자동으로 유튜브에 업로드 (또는 수동 업로드 후 URL 확보).
2. **데이터베이스 (Local SQLite)**: 영상의 메타데이터(FPS, 해상도, 장소, 시간대 등)와 **`Youtube URL`** 속성을 DB에 기록.
3. **노션 동기화 (Agentic Sync)**: Agent/Script가 로컬 DB의 정보를 읽어 Notion의 **"드라이빙 소스" 데이터베이스**에 행(Row)으로 자동 추가 및 업데이트.
4. **클라이언트 뷰 (Notion)**: 갤러리 뷰(Gallery View) 형태로 예쁘게 배열된 카드들을 클릭하여, 상세 페이지 내 임베드된 유튜브 멀티뷰어를 버퍼링 없이 감상.

### 2.2 장점 (Why this approach?)
- **Zero Storage Cost**: 수십 기가바이트의 4K 멀티뷰어 영상을 노션에 직접 올리지 않으므로, 노션 용량을 전혀 차지하지 않습니다. (텍스트 형태의 URL만 저장)
- **Zero Buffering**: 구글(유튜브) 서버의 강력한 스트리밍 인프라를 활용하여 클라이언트에게 끊김 없는 재생 경험을 제공합니다.
- **보안 유지**: 유튜브 영상을 **'일부 공개(Unlisted)'**로 설정하여, 유튜브 검색에는 노출되지 않고 오직 링크(노션 권한)를 가진 사람만 볼 수 있게 통제합니다.
- **자동화 용이**: 데이터베이스 속성(Property)만 업데이트하면 되므로 향후 완전 자동화 파이프라인의 종착역으로 적합합니다.

## 3. Notion 데이터베이스 스키마 요구사항 (드라이빙 소스 DB)
향후 파이프라인(`update_db.py` 등)을 통해 정보가 주입될 타겟 Notion DB의 핵심 속성(Property) 구조입니다.

| Property (속성명) | Type (타입) | Description (설명) |
| :--- | :--- | :--- |
| **이름 (Title)** | Title | 씬 이름 (예: `231015_Night_Seoul_City_01`) |
| **URL (유튜브)** | URL | 클라이언트용 멀티뷰어 링크 (페이지 내부에 임베드도 가능) |
| **Time (시간대)** | Select | Day, Night, Sunset 등 |
| **Location (장소)** | Select | Seoul, Highway, Tunnel 등 |
| **Weather (날씨)** | Select | Clear, Rain, Snow 등 |
| **Speed (속도)** | Select | Low, Medium, High |
| **Status (상태)** | Status | Ready, Processing, Internal_Only 등 |

## 4. Next Step 연계
이 프론트엔드(Notion) 전략이 승인됨에 따라, 백엔드 역할을 할 로컬 DB(SQLite) 구축을 위한 `init_db.py` 설계 시 영상 엔티티(Asset Table)에 반드시 `youtube_url` 컬럼이 포함되어야 합니다. (이후 `update_db.py` 작동 시 연동)

---
*기록자: Antigravity AI*
