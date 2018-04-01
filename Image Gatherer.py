from bs4 import BeautifulSoup
import urllib2
import requests
import urllib
website = "https://www.python.org/"
html_page = urllib2.urlopen(website)
soup = BeautifulSoup(html_page, "html.parser")
images = []
links = []

for img in soup.findAll('img'):    
    images.append(img.get('src'))    
    for link in images:
        links.append(website+link[1:])
        for i in links:
            dawd = i[i.rfind("/")+1:]
            urllib.urlretrieve(i, dawd)  

print("The links:" + str(links))
