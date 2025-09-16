from bs4 import BeautifulSoup

# import lxml # xml을 parsing 할 때는 lxml을 사용.


with open("website.html", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

# print(soup.title)           # 태그가 포함된 값을 반환
# print(soup.title.name)      # 태그명을 반환
# print(soup.title.string)    # 태그 안의 문자열을 반환.

# print(soup)               # soup로 읽은 전체 html을 반환.
# print(soup.prettify())    # 들여쓰기 해서 이쁘게 반환.

# print(soup.p)             # 이런식으로 쓰면 가장 먼저 만나는 태그를 가져옴.

all_anchors = soup.find_all(name="a")  # html 파일 내의 모든 a태그 요소를 반환. 배열모양.. type은 배열이 아니다.
print(all_anchors)
print(type(all_anchors))

for a_tags in all_anchors:
    # print(a_tags.getText())
    print(a_tags.get(key="href"))

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading)
print(section_heading.getText())

company_url = soup.select_one(selector="p a")
print(company_url)

name = soup.select_one(selector="#name")
print(name)

heading = soup.select_one(selector=".heading")
print(heading)
