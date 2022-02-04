from bs4 import BeautifulSoup
import urllib.request as req

out = open("news.txt", "w", encoding = "utf-8")

url = "https://news.daum.net/breakingnews"
result = req.urlopen(url)
soup = BeautifulSoup(result, "html.parser")

news = soup.select("strong.tit_thumb")

for list in news:
    a = list.select_one("a")
    print("링크 : "+a.get('href'))
    out.write("링크 : "+a.get('href') + "\n")

    title =a.string
    print("제목 : "+title)
    out.write("제목 : "+title+"\n")

out.close()