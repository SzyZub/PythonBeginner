import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
name = None
lst = list()
url = "http://py4e-data.dr-chuck.net/known_by_Mariella.html"
for i in range(7):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup("a")
    url = tags[17].get("href")
    lst = url.split("_")
    lst = lst[2].split(".")
    print(lst[0])



