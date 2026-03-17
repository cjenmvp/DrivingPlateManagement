# 03_SOP (표준 업무 절차)

본 문서는 드라이빙 소스의 촬영부터 최종 송출용 라이브러리 입고까지의 단계별 표준 작업 절차를 정의합니다.

---

## 🔄 데이터 생애 주기 (Data Lifecycle)

### 1단계: 입고 및 백업 (Ingest)
- **작업**: 촬영 완료된 원본을 `X:\01_DrivingPlate_Original`에 복사.
- **규칙**: 표준 명명 규칙(`YYMMDD_...`)에 따라 폴더명 즉시 수정.

### 2단계: 가편집 및 화질 보정 (Processing)
- **작업**: `X:\02_ing`에서 작업 시작 → `X:\02_PrProj_Driving`에 프로젝트 저장.
- **품질 향상**: 업스케일 및 FPS 변환 필요 시 `X:\07_Topaz_Render`를 경유.

### 3단계: 골든 마스터 생성 (Mastering)
- **H265 마스터**: 최종 편집본을 `X:\04_DrivingPlate_Library_h265`에 추출.
- **멀티뷰**: 고객 확인용 10분할 영상을 `X:\05_DrivingPlate_Multiview`에 추출.

### 4단계: 송출용 컨버팅 (Deployment)
- **작업**: AME를 사용하여 NotchLC로 변환.
- **최종 입고**: 변환된 파일을 `Z:\2_DrivingPlate_Library_nclc`로 이동.
- **프록시**: 가벼운 프리뷰용 파일을 `X:\06_DrivingPlate_Library_nclc_proxy`에 입고.

### 5단계: DB 업데이트 및 아카이빙 (Indexing)
- **DB**: 에이전트(Antigravity)를 통해 `library.db`에 최신 메타데이터 반영.
- **백업**: 입고가 완료된 `X:\01_Original`의 데이터는 분기별로 저속 스토리지로 이전.

---

## ⚠️ 필수 체크리스트 (SOP Checklist)
- [ ] 폴더명이 규칙에 맞게 작성되었는가?
- [ ] 비선호 각도(01, 05, 07, 11)는 별도 분리되었는가?
- [ ] Z: 드라이브에 NotchLC 코덱으로 입고되었는가?
- [ ] X: 드라이브에 대응하는 프록시가 생성되었는가?

---
*기록자: Antigravity AI*
