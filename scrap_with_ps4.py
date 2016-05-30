import requests
from bs4 import BeautifulSoup

url= ""
r = requests.get(url)

soup = BeautifulSoup(r.content)

links = soup.find_all("a")

for link in links:
	print " href="  link.get("href"), link.text)
