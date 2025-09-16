import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

res = requests.get(url=URL)
res_html = res.text

soup = BeautifulSoup(res_html, "html.parser")

h2_doms = soup.find_all(name="h2")

movie_titles = [movie.text for movie in h2_doms]

for title in movie_titles[::-1]:
    print(title)

with open("top100_movies.txt", mode="w", encoding="utf-8") as file:
    for movie_title in movie_titles[::-1]:
        file.write(f"{movie_title}\n")

