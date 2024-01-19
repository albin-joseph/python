import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://www.billboard.com/charts/hot-100/'

year = input("WHich year do you want to travel to? Type the date in the format YYYY-MM-DD: ")
request_url = f"{BASE_URL}{year}/"

response = requests.get(url=request_url)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
all_songs = soup.select("li ul li h3")
song_titles = [song.getText().strip() for song in all_songs]

print(song_titles)