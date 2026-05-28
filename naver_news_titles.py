import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

url = (
    "https://search.naver.com/search.naver?"
    "where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%B0%98%EB%8F%84%EC%B2%B4&ackey=65xcqh9k"
)

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    )
}

response = requests.get(url, headers=headers, timeout=15)
response.raise_for_status()
response.encoding = "utf-8"

soup = BeautifulSoup(response.text, "html.parser")

news_items = soup.select('div.fds-news-item-list-desk a[data-heatmap-target=".tit"]')
if not news_items:
    news_items = soup.select('a[data-heatmap-target=".tit"]')

wb = Workbook()
ws = wb.active
ws.title = "Naver News"
ws.append(["No", "Title", "URL"])

seen = set()
row = 1
for a in news_items:
    title = a.get_text(" ", strip=True)
    href = a.get("href", "")
    if not title or title in seen:
        continue
    seen.add(title)
    row += 1
    ws.append([row - 1, title, href])
    print(f"{row - 1}. {title}")
    print(f"   {href}")

output_file = "naver_result.xlsx"
wb.save(output_file)
print(f"Saved {output_file}")
