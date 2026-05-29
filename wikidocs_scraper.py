import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
import os

class WikiDocsScraper:
    def __init__(self, base_url="https://wikidocs.net/book/1"):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        self.content = []
        self.visited_urls = set()

    def get_menu_links(self):
        """좌측 메뉴의 모든 링크를 추출합니다."""
        try:
            print("메인 페이지에서 메뉴 링크 추출 중...")
            response = self.session.get(self.base_url, timeout=10)
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # 좌측 네비게이션 메뉴 찾기
            nav_menu = soup.find('nav', class_='book-nav') or soup.find('div', class_='side-bar')
            
            if nav_menu is None:
                print("메뉴를 찾을 수 없습니다. 대체 방법을 시도합니다.")
                # 모든 링크 추출
                links = []
                for a in soup.find_all('a'):
                    href = a.get('href', '')
                    if '/book/1/' in href or '/page/' in href:
                        full_url = urljoin(self.base_url, href)
                        links.append((full_url, a.get_text(strip=True)))
            else:
                links = []
                for a in nav_menu.find_all('a'):
                    href = a.get('href', '')
                    if href:
                        full_url = urljoin(self.base_url, href)
                        link_text = a.get_text(strip=True)
                        links.append((full_url, link_text))
            
            # 중복 제거
            unique_links = []
            seen_urls = set()
            for url, text in links:
                if url not in seen_urls:
                    unique_links.append((url, text))
                    seen_urls.add(url)
            
            print(f"추출된 링크: {len(unique_links)}개")
            return unique_links
        except Exception as e:
            print(f"메뉴 링크 추출 오류: {e}")
            return []

    def scrape_page(self, url, title):
        """개별 페이지의 컨텐츠를 스크래핑합니다."""
        if url in self.visited_urls:
            print(f"이미 방문함: {title}")
            return
        
        try:
            print(f"스크래핑 중: {title}")
            response = self.session.get(url, timeout=10)
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # 페이지 제목
            page_title = soup.find('h1') or soup.find('title')
            title_text = page_title.get_text(strip=True) if page_title else title
            
            # 메인 컨텐츠 추출
            main_content = soup.find('article') or soup.find('div', class_='post-content') or soup.find('div', class_='wiki-content')
            
            if main_content:
                # 불필요한 요소 제거
                for element in main_content.find_all(['script', 'style', 'nav', 'button']):
                    element.decompose()
                
                content_text = main_content.get_text(separator='\n', strip=True)
            else:
                content_text = soup.get_text(separator='\n', strip=True)
            
            # 컨텐츠 저장
            self.content.append(f"\n{'='*80}\n제목: {title_text}\nURL: {url}\n{'='*80}\n\n{content_text}\n")
            self.visited_urls.add(url)
            
            # 요청 간 지연 (서버 부하 방지)
            time.sleep(1)
            
        except Exception as e:
            print(f"스크래핑 오류 [{title}]: {e}")

    def scrape_all(self):
        """모든 메뉴 항목을 스크래핑합니다."""
        links = self.get_menu_links()
        
        if not links:
            print("스크래핑할 링크가 없습니다.")
            return
        
        total_links = len(links)
        for idx, (url, title) in enumerate(links, 1):
            print(f"[{idx}/{total_links}] ", end="")
            self.scrape_page(url, title)
        
        print(f"\n총 {len(self.visited_urls)}개 페이지 스크래핑 완료!")

    def save_to_file(self, filename="wikidocs_content.txt"):
        """스크래핑한 컨텐츠를 파일로 저장합니다."""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("="*80 + "\n")
                f.write("위키독스 (https://wikidocs.net/book/1) 컨텐츠 다운로드\n")
                f.write("="*80 + "\n\n")
                f.writelines(self.content)
            
            file_size = os.path.getsize(filename) / 1024 / 1024  # MB
            print(f"파일 저장 완료: {filename} ({file_size:.2f} MB)")
            return filename
        except Exception as e:
            print(f"파일 저장 오류: {e}")

def main():
    print("위키독스 컨텐츠 다운로더")
    print("-" * 80)
    
    # 스크래퍼 생성
    scraper = WikiDocsScraper()
    
    # 모든 컨텐츠 스크래핑
    scraper.scrape_all()
    
    # 파일 저장
    if scraper.content:
        output_file = scraper.save_to_file("wikidocs_python_book.txt")
        print(f"\n다운로드 완료! 파일: {output_file}")
    else:
        print("\n스크래핑된 컨텐츠가 없습니다.")

if __name__ == "__main__":
    main()
