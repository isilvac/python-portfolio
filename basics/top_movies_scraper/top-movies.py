from bs4 import BeautifulSoup
import requests
import re

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(response.text, "html.parser")
all_titles = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")
movie_titles = [movie.getText() for movie in all_titles][::-1]

with open(file="./data/movies.txt", mode="w", encoding="utf-8") as file:
    for movie in movie_titles:
        movie = re.sub(pattern='  ', repl=' ', string=movie)
        file.write(f"{movie}\n")
