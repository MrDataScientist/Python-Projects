
import requests
from bs4 import BeautifulSoup

url= "http://www.yellowpages.com/nashport-oh/mip/coffee-time-office-coffee-service-13629601?lid=13629601"
r = requests.get(url)

soup = BeautifulSoup(r.content)

links = soup.find_all("a")

for link in links:
	print " href="  %link.get("href"), link.text)
g_data = soup.find_all("div")

for item in g_data:
	print item.contents[0].find_all("a",{"class":"business-name"})[0].text
	print item.contents[1].find_all("p",{"class":"adr"})[0].text
	try:
		print item.contents[1].find_all("span",{"itemprop":"address"})[0].text
		print item.contents[1].find_all("span",{"class":"addressLocality"})[0].text
	except:
		pass
	try:
		print item.contents[1].find_all("li",{"class":"primary"})[0].text
	except:
		pass

