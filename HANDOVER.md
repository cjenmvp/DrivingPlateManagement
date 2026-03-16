# 🤝 AI 에이전트 핸드오버 (HANDOVER)

본 문서는 Antigravity AI(Gemini), Codex, Claude 간의 작업 연속성을 보장하기 위한 실시간 교신 로그입니다. 작업을 시작하는 에이전트는 본 문서를 가장 먼저 읽고, 작업 종료 시 내용을 업데이트해야 합니다.

---

## 📌 현재 상태 (Current Status) - 2026-03-16
- **완료된 작업**:
  - 마스터(Z:) 및 프록시(X:) 드라이브 내 비선호 각도(`01, 05, 07, 11`) 격리 완료.
  - X: 드라이브 내 `00_DrivingPlate_Management_System` 구축 및 GitHub 연동 완료.
  - 라이브러리 운영 가이드 및 7단계 프레임워크 문서화 완료.
  - 기존 엑셀 데이터를 CSV(`library_export.csv`)로 추출 완료.
- **진행 중인 작업**:
  - `01_Original` 폴더(25TB)와 `Z:` 마스터 간의 중복 조사 준비.
  - Supabase DB 스키마 설계 준비.

---

## 🚀 Codex CLI GPT 5.2를 위한 미션 (Next Actions)

**1. Supabase DB 스키마 설계 (SQL)**
- `library_export.csv`와 `master_data.csv`의 구조를 분석하여, 영상 메타데이터를 담을 최적의 PostgreSQL 테이블 스키마를 작성하십시오.
- `folders`, `files`, `metadata`, `projects`, `youtube_links` 등의 관계형 구조를 권장합니다.

**2. Bash 기반 메타데이터 추출 스크립트 고도화**
- `scripts/metadata_extractor.sh` 파일을 확인하고, `ffprobe`를 사용하여 영상의 정확한 `Duration`, `Resolution`, `Bitrate`, `FPS`를 추출하여 JSON으로 출력하는 로직을 완성하십시오.

**3. 중복 체크 알고리즘 작성**
- Z: 드라이브와 X: 드라이브의 파일 크기(Size)와 파일명 패턴을 대조하여 중복된 원본 소스를 식별하는 Bash 스크립트를 작성하십시오.

---

## ⚠️ 주의사항 (Notes)
- **메모리 보호**: 대규모 루프 실행 시 `chunk` 단위로 끊어서 처리하십시오. (한 번에 10개 폴더 권장)
- **경로 참조**: 네트워크 경로인 `X:/`와 `Z:/`를 사용하며, 필요시 UNC 경로(`//172.16.1.61/...`)를 참조하십시오.
- **Git Commit**: 작업 완료 후 반드시 `git commit` 및 `push`를 수행하여 다른 에이전트와 싱크를 맞추십시오.

---
*Next Agent: @Codex-CLI-GPT-5.2*
