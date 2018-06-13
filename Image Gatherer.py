from bs4 import BeautifulSoup
import urllib2
import requests
import urllib
website = "https://github.com/"
html_page = urllib2.urlopen(website)
soup = BeautifulSoup(html_page, "html.parser")
images = []
links = []

for img in soup.findAll('img'):    
    images.append(img.get('src'))    
    for link in images:
        if link[:1] == "/" or "\\":
            links.append(website+link)
        else: links.append(link)
        for i in links:
            dawd = i[i.rfind("/") +1:] or i[i.rfind("\\") +1:]
            urllib.urlretrieve(i, dawd)  

print("The links:" + str(links))
