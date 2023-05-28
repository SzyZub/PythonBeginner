import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
sum = 0
url = "http://py4e-data.dr-chuck.net/comments_1811735.html"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup("span")
for tag in tags: 
    sum = sum + int(tag.contents[0])
print(sum)
