import urllib.request, urllib.parse, urllib.error
import json

sum = 0
url = "http://py4e-data.dr-chuck.net/comments_1811738.json"
handle = urllib.request.urlopen(url)
hand = handle.read().decode()
info = json.loads(hand)
for item in info["comments"]:
    num = int(item["count"])
    sum = sum + num
print(sum)
 