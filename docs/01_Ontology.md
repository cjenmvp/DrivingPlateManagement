# 01_Ontology (데이터 정체성 및 가치 정의)

VP Stage 드라이빙 플레이트 라이브러리는 단순한 파일의 집합이 아닌, 가상 프로덕션의 핵심 자산으로 다음과 같이 정의됩니다.

---

## 💎 1. 자산의 위계 (Value Hierarchy)

### **[Tier 1] 송출용 마스터 (The Final Truth)**
- **Z:\2_DrivingPlate_Library_nclc**: Disguise 미디어서버 송출을 위한 NotchLC 최종본.
- **X:\04_DrivingPlate_Library_h265**: 편집 및 품질 보정이 끝난 원본 마스터(H265).
- **가치**: 가장 높은 우선순위. 100% 무결성과 상세 인덱싱이 필수입니다.

### **[Tier 2] 리뷰 및 고객용 에셋 (The Interface)**
- **X:\05_DrivingPlate_Multiview**: 클라이언트 리뷰용 10분할 멀티뷰어.
- **가치**: 대외적 소통과 빠른 컨택을 위한 얼굴 역할을 합니다.

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

---
*기록자: Antigravity AI*
