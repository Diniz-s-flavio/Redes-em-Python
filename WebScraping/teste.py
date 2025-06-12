import requests
from bs4 import BeautifulSoup

url = "https://www.ifgoiano.edu.br/home/index.php/urutai.html"
response = requests.get(url)

if response.status_code == 200:
    print("Page fetched successfuly")
else:
    print("Error fdd")

soup = BeautifulSoup(response.content, "html.parser")
# print(soup)

# x = soup.find(id = "")
# y = soup.find_all(class_ = "")
# z = soup.find_all("")

title = soup.find("h1").text
print(title)

description = soup.find("p", class_="description").text
print(description)

description = soup.find_all("p", class_="description")
print(description)