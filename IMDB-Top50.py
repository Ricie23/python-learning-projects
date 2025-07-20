import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/115.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

movies = []
table = soup.select("li.ipc-metadata-list-summary-item")

for row in table:
    title_column = row.find("h3", class_="ipc-title__text")
    rating_column = row.find("span", class_="ipc-rating-star--rating")

    title = title_column.text
    rating = rating_column.text

    movies.append({"title": title, "rating": rating})

for movie in movies:
    print(f"Movie: {movie['title']}, Rating: {movie['rating']}")


