from bs4 import BeautifulSoup
import requests
import datetime

# import lxml # xml을 parsing 할 때는 lxml을 사용.

res = requests.get(url="https://news.naver.com/section/101")

# naver 크롤러 규칙은 아래와 같다...
naver_robots = """  User-agent: *
                    Disallow: /
                    Allow : /$
                    Allow : /.well-known/privacy-sandbox-attestations.json  """

html_text = res.text

# print(res.text)
soup = BeautifulSoup(html_text, "html.parser")

print(soup.title)

headline_news = soup.find_all(name="a", class_="sa_text_title _NLOG_IMPRESSION")

article_titles = []
article_links = []
for news in headline_news:
    news_title = news.getText()
    news_link = news.get(key="href")
    article_titles.append(news_title)
    article_links.append(news_link)
index = 0
print("##################")
print("이 시간 주요 경제뉴스")
print("##################")
for title in article_titles:
    index += 1
    print(f"{index}. {title.replace("\n", "")}")
