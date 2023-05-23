from bs4 import BeautifulSoup
import requests

# HTML From File
# with open("index.html", "r") as f:
# 	doc = BeautifulSoup(f, "html.parser")
#
# tags = doc.find_all("p")[0]
#
# print(tags.find_all("b"))

# HTML From Website
url = "https://en.wikipedia.org/wiki/Interstellar_(film)"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

prices = doc.find_all("a",href=True)
# print(doc.prettify())
print(prices[4].text)
