#web1.py
#code for crawling web pages

from bs4 import BeautifulSoup

page = open("chap09_test.html", "rt",encoding="utf-8").read()

soup = BeautifulSoup(page, "html.parser")

#print(soup.prettify())

#print(soup.find_all("p",class_="outer-text"))

#print(soup.find_all("p",attrs={"class":"outer-text"}))

for item in soup.find_all("p"):
    title=item.text.strip()
    title=title.replace("\n","")
    print(title)


