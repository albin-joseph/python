from bs4 import BeautifulSoup
import os

with open(f"{os.getcwd()}/045-day/website.html") as file:
    contents = file.read()
    
soup = BeautifulSoup(contents, 'html.parser')
print(soup.title)

all_acnchor_tag = soup.find_all(name="a")
print(all_acnchor_tag)

for tag in all_acnchor_tag:
    print(tag.get("href"))