# 01_Ontology (데이터 정체성 및 가치 정의)

VP Stage 드라이빙 플레이트 라이브러리는 단순한 파일의 집합이 아닌, 가상 프로덕션의 핵심 자산으로 다음과 같이 정의됩니다.

---

## 💎 1. 자산의 위계 (Value Hierarchy)

### **[Tier 1] 송출용 마스터 (The Final Truth)**
- **Z:\2_DrivingPlate_Library_nclc**: Disguise 미디어서버 송출을 위한 NotchLC 최종본.
- **X:\04_DrivingPlate_Library_h265**: 편집 및 품질 보정이 끝난 원본 마스터(H265).
- **가치**: 가장 높은 우선순위. 100% 무결성과 상세 인덱싱이 필수입니다.

### **[Tier 2] 리뷰 및 고객용 에셋 (The Interface)**
- **X:\05_DrivingPlate_Multiview**: 클라이언트 리뷰용 10분할 멀티뷰어 영상 파일.
- **Notion VP Asset Library (드라이빙 소스 DB)**: 클라이언트가 접근하여 검색하고 감상하는 웹 프론트엔드. 
  - **Youtube URL 연동**: 무거운 멀티뷰어 영상은 유튜브(일부 공개)에 업로드하고, Notion 갤러리 뷰에 임베드하여 제로 용량, 고속 스트리밍 UX 제공.
- **가치**: 대외적 소통과 빠른 컨택을 위한 얼굴 역할을 합니다. (로컬 DB의 메타데이터와 자동 동기화 목표)

### **[Tier 3] 제작 맥락 및 워크플로우 (The Context)**
- **X:\02_PrProj_Driving / d3 projects**: 영상이 만들어진 기술적 흔적.
- **X:\07_Topaz_Render**: AI를 통한 화질 개선 및 프레임 보간 과정물.
- **가치**: 자산의 역사(History)를 보존하고 재작업 시 효율을 제공합니다.

### **[Tier 4] 원천 기록 및 백업 (The Origin)**
- **X:\01_DrivingPlate_Original**: 촬영 원본.
- **가치**: 만약을 위한 최후의 보루. 마스터 입고 완료 시 아카이빙 대상으로 분류됩니다.

---

## 🎯 2. 비즈니스 정체성 선언
우리는 **"촬영부터 송출까지, 데이터의 손실 없이 고화질 드라이빙 경험을 VP Stage에 즉각 공급하는 파이프라인"**을 구축합니다.

1. **품질 중심**: 모든 최종 자산은 NotchLC와 H265(Golden Master)로 보존된다.
2. **편의 중심**: 모든 팀원이 복잡한 경로를 뒤지지 않고 DB를 통해 즉시 원하는 소스를 찾는다.
3. **영속성 중심**: 작업자의 변경과 무관하게 모든 데이터의 히스토리(Context)를 보존한다.


## 🎬 3. 시스템 아키텍처 및 LED Wall 인프라

### 3.1 disguise 미디어 서버 및 송출 파이프라인
- **디렉터 머신**: disguise director (`vx1`)
- **액터 머신 (총 10대)**
: `cam1(vx2)=xR전용 및 Sync용 백업머신 실제 ledwall담당하지않음`, 
`m1(vx3)`, `m2(vx4)`, `m3(vx5)`, `m4(vx6)`, `c1(vx7)`, `c2(vx8)`, `c3(vx9)`, `p(vx10)`, `s(v11)`
- **네트워크 및 동기화**:
  - 디스가이즈 머신들은 100G 네트워크로 연결되어 있으며, 디렉터 머신 기준으로 SyncBackPro를 통해 각 액터 머신이 자체 동기화합니다.
  - 본 매니지먼트 시스템 개발 목표: 10G 스토리지 네트워크(172.16.1.101)와 연동하여 필요 소스를 `Z:\2_DrivingPlate_Library_nclc`에서 심볼릭 링크(Symbolic Link)로 디렉터 머신에 제공하고, 이후 디렉터가 액터 머신으로 SyncBack하는 자동화 솔루션 구축.
  - **오토메이션 폴백(Fallback)**: 만약 `Z:\2_DrivingPlate_Library_nclc`에 소스가 없다면 원본 자산인 `X:\04_DrivingPlate_Library_h265`를 랜더링하여 공급하는 파이프라인까지 연동 계획. 심볼릭 링크 방식이 실패할 경우, 스토리지에서 디렉터 머신으로 직접 파일을 전송합니다.

### 3.2 VP Stage LED Wall (Main & Sub) 스펙 및 물리적 인프라
스튜디오(Stage 5)의 전체 면적은 약 500평(51,000 x 30,800 mm)입니다.
- **층고 스펙**: 지붕(Roof) 19.0m, 차음 천정 15.6m, 바턴(Batten) 11.5m
- **출입구 (Studio Gate)**: 3.7m(W) x 4.7m(H)

#### 주요 LED 구성
- **메인월 (Main Wall)**: 말굽형(Horseshoe) 커브 디자인. 지름 약 20m, 높이 7.3m, 총 길이 52m 규모.
  - **설치 기반**: 18.5m x 15.65m 규모 (높이 47~48cm)의 알루미늄 덧마루(Deck) 위에 설치.
  - **디스플레이**: Samsung Micro LED 'The Wall' (1.68mm Pixel Pitch)
  - **크기 및 해상도**: 51,610 x 7,258 mm / 30,720 x 4,320 px (최대 60FPS 지원, 천장 동시 사용 시 48FPS)
  - **구동 머신**: `m1(vx3)`, `m2(vx4)`, `m3(vx5)`, `m4(vx6)` (총 4대 사용)
- **천장 (Ceiling)**:
  - **특징**: 총 31개의 탈부착 가능한 개구부가 있어 조명 및 세트 설치 용이 (호이스트 구비)
  - **디스플레이**: Samsung LED (2.5mm Pixel Pitch)
  - **크기 및 해상도**: 23,040 x 20,520 mm / 9,216 x 8,208 px (48FPS)
  - **구동 머신**: `c1(vx7)`, `c2(vx8)`, `c3(vx9)` (총 3대 사용)
- **모바일 플러그 (Mobile Plug, 2 Units)**: 메인월 반대쪽에 위치해 절반씩 이동, 문이 닫히는 형태로 360도를 LED Wall로 커버.
  - **디스플레이**: Samsung LED (2.5mm Pixel Pitch)
  - **크기 및 해상도**: 15,360 x 8,640 mm / 6,144 x 3,456 px
  - **구동 머신**: `p(vx10)`
- **서브월 (Sub Wall)**: 직선형(Linear) 디자인. 길이 19,354mm(약 19.4m), 높이 3,629mm(약 3.6m) 규모.
  - **디스플레이**: Samsung Micro LED (1.68mm Pixel Pitch)
  - **크기 및 해상도**: 19,354 x 3,629 mm / 11,520 x 2,160 px (최대 60FPS 지원)
  - **구동 머신**: `s(v11)` (*참고: 기존 메모 상 디렉터인 vx1으로 표기되기도 함)

#### 전원 및 부대 인프라
- **전력 용량**: 총 **900A** 지원 (100A 전력 라인이 스튜디오 내 3개소에 각각 3개씩, 총 9회로 구성됨)
- **차량 이동 슬로프**: 덧마루 위 차량 세팅(Car Shoot)을 위한 메인 슬로프(4.5m) 및 보조 슬로프(1.5m, 3도 경사) 지원

기본 형태, 도면 및 상세 스펙에 대한 세부 정보는 아래 문서들을 참고하시기 바랍니다.
- 🔗 [CJ ENM VP Stage Guide](https://cjenmvp.notion.site/CJ-ENM-VP-Stage-Guide-2e68133b04c04c748104fb9b9d58abf4)
- 🔗 [Main Wall 상세 스펙](https://cjenmvp.notion.site/Main-Wall-1839bebf4ee08009b38de2c852d2619a)
- 🔗 [VP Stage 통합 도면 및 시설 규격](https://www.notion.so/cjenmvp/VP-Stage-1839bebf4ee0803c9177c10b5b4e81f9)

---
*기록자: Antigravity AI*
