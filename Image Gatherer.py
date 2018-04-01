from bs4 import BeautifulSoup
import urllib2
import requests
import urllib
website = "https://minecraft.net/"
html_page = urllib2.urlopen(website)
soup = BeautifulSoup(html_page, "html.parser")
images = []
links = []

for img in soup.findAll('img'):    
    images.append(img.get('src'))    
    for link in images:
        links.append(website+link[3:])
        for i in links:
            urllib.urlretrieve(i, "filename.png")

print("The links:" + str(links))

