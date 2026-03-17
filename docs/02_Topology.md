# 02_Topology (드라이브 및 폴더 구조 지도)

본 문서는 드라이빙 플레이트 자산이 저장된 모든 물리적 경로의 역할과 용도를 정의합니다.

---

## 🗺️ 전수 조사 폴더 목록 및 용도 정의

### [X: Drive] - 프리뷰 및 가편집 스토리지
| 폴더명                                    | 용도 (사용자 기입 / User Purpose)                                       | AI 제안 역할             |
| :------------------------------------- | :--------------------------------------------------------------- | :------------------- |
| **00_DrivingPlate_Management_System**  | 전체 파이프라인 가이드 및 DB 관리                                             | Control Tower        |
| **01_DrivingPlate_Original**           | 촬영 원본을 보관,분류,파일명변경                                               | Backup / Safety      |
| **02_DrivingPlate_ing**                | 촬영 원본으로 작업을 하는 공간                                                | Work In Progress     |
| **02_PrProj_Driving**                  | 편집하는 프리미어프로젝트를 저장                                                | Adobe Projects       |
| **04_DrivingPlate_Library_h265**       | **실제 원본에서 편집이 끝난 최종 드라이빙 소스 원본 경로**                              | Golden Master (H265) |
| **05_DrivingPlate_Multiview**          | **편집된 원본 기반 10개 화면 멀티뷰어 (클라이언트용)**                               | Client Review        |
| **05_DrivingPlate_Multiview_log**      | 멀티뷰어인데 LUT적용안한 log영상(굳이 보관할 필요는 없음)                              | Log Multiview        |
| **05_DrvingPlate_LUT**                 | 드라이빙 LOG영상에 필요한 LUT파일                                            | Color Assets         |
| **06_DrivingPlate_Library_nclc_proxy** | 저용량 프록시 (NotchLC 프리뷰용)                                           | Proxy Library        |
| **07_Topaz_Render**                    | 업스케일링, 24P>60P 프레임보간,디노이즈 작업을 하는 TOPAZ AI의 렌더링 장소                | AI Upscaling         |
| **11_AME_Watch**                       | 어도비 미디어인코더를 자동화할때 감시폴더(심볼링링크같은것으로 실제파일경로르 가상으로 만들어서 렌더링걸리면 좋겠다.) | Encode Watcher       |
| **12_AME_Output**                      | 어도비 미디어인코더가 자동화되어서 렌더링 되는 경로                                     | Encode Output        |
| **13_DrivingPlate_Test Source**        | 드라이빙촬영원본인데 테스트로 촬영한 원본                                           | Sandbox              |
| **15_DrivingPlate_SW**                 | 드라이빙플레이트를 관리하는 소프트웨어,개발툴을 모아놓는곳.                                 | Software Assets      |
| **d3 projects**                        | 디스가이즈 프로젝트의 소스를 디스가이즈디자이너로 볼때 필요한 프로젝트경로. 정션폴더, 싱볼릭링크를 활용하면 좋을듯  | Disguise Projects    |
| **test**                               | 임시폴도                                                             | Temp Trash           |

### [Z: Drive] - 고속 마스터 스토리지 (NotchLC)
| 폴더명                             | 용도 (사용자 기입 / User Purpose)                                      | AI 제안 역할            |
| :------------------------------ | :-------------------------------------------------------------- | :------------------ |
| **2_DrivingPlate_Library_nclc** | **미디어서버용 컨버팅 파일(NotchLC) 경로**                                   | Media Server Master |
| **1_Project**                   | 프로젝트별 외부소스 보관장소                                                 | Production          |
| **3_Unreal**                    | 언리얼 프로젝트와 관련 파일 보관                                              | UE Assets           |
| **5_Resource**                  | vp에 필요한 관련 자료 보관                                                | General Assets      |
| **6_VP Making**                 | vp 메이킹영상 모음                                                     | Making Film         |
| **7_Backup**                    | 백업 전용폴더                                                         | Archive             |
| **10_Recording**                | vp에서 카메라로 촬영한  영상 보관                                            | Studio Record       |
| **d3 projects**                 | 디스가이즈 프로젝트의 소스를 디스가이즈디자이너로 볼때 필요한 프로젝트경로. 정션폴더, 싱볼릭링크를 활용하면 좋을듯 | Disguise Master     |

---
*최종 업데이트: 2026-03-17*
