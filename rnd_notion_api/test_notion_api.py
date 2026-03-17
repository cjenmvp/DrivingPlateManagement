import os
from dotenv import load_dotenv
from notion_client import Client

# 환경 변수 로드 (.env 파일에서 API Key 및 Page ID 가져오기)
load_dotenv()

NOTION_TOKEN = os.getenv("NOTION_API_KEY")
PAGE_ID = os.getenv("NOTION_PAGE_ID")

def test_notion_connection():
    if not NOTION_TOKEN or NOTION_TOKEN in ["", "your_integration_secret_here"]:
        print("❌ 오류: .env 파일에 NOTION_API_KEY가 올바르게 설정되지 않았습니다.")
        return
        
    try:
        # Notion 클라이언트 초기화
        notion = Client(auth=NOTION_TOKEN)
        print("🔄 Notion API 연결 테스트를 시작합니다...")
        
        # 특정 페이지 ID가 주어지지 않은 경우, 연동이 허용된 전체 페이지 검색
        if not PAGE_ID or PAGE_ID in ["", "your_notion_page_id_here"]:
            print("⚠️ 특정 NOTION_PAGE_ID가 입력되지 않았습니다.")
            print("🔍 현재 API 키에 읽기 권한이 부여된 모든 페이지를 검색합니다...\n")
            
            search_results = notion.search()
            results = search_results.get("results", [])
            
            if not results:
                print("❌ 접근 가능한 페이지(또는 데이터베이스)가 없습니다.")
                print("💡 Notion에서 원하는 페이지 우측 상단의 '...' -> [연결 추가]를 통해 통합 앱을 추가해주세요.")
                return
                
            print("✅ 연결 성공! 아래 페이지들에 대한 접근 권한이 확인되었습니다:")
            print("-" * 50)
            for item in results:
                item_type = item.get("object")
                item_id = item.get("id")
                
                # 페이지 제목 추출 (Notion API 구조에 따라 다를 수 있음)
                title = "제목 없음"
                if item_type == "page" and "title" in item.get("properties", {}):
                    title_prop = item["properties"]["title"].get("title", [])
                    if title_prop:
                        title = title_prop[0].get("plain_text", "제목 없음")
                        
                elif item_type == "database" and "title" in item:
                    title_prop = item.get("title", [])
                    if title_prop:
                         title = title_prop[0].get("plain_text", "제목 없음")
                
                print(f"[타입: {item_type.upper()}] {title}")
                print(f" -> ID: {item_id}")
                print(f" -> URL: {item.get('url')}")
                print("-" * 50)
                
            print("\n💡 앞으로 특정 페이지 데이터만 뽑아오려면, 위 목록 중 원하는 페이지의 ID를 복사하여 .env의 NOTION_PAGE_ID에 입력해주세요.")

        else:
            # 특정 페이지 ID가 주어진 경우, 해당 페이지만 조회
            print(f"🔄 페이지 ID 기반으로 정보를 조회합니다: {PAGE_ID}")
            response = notion.pages.retrieve(page_id=PAGE_ID)
            
            print("✅ 성공적으로 특정 페이지 정보를 가져왔습니다!")
            print("-" * 50)
            print(f"Page ID: {response.get('id')}")
            print(f"URL: {response.get('url')}")
            print("-" * 50)
            print("이제 이 스크립트를 확장하여 페이지 내의 블록 텍스트(예: 1.68mm 파워 등 스펙 수치)를 파싱할 수 있습니다!")
        
    except Exception as e:
        print("❌ API 연결 또는 데이터 조회 중 오류가 발생했습니다:")
        print(e)

if __name__ == "__main__":
    test_notion_connection()
