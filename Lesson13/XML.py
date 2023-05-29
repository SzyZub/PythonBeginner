import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
#bypassing certificate
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

sum = 0
url = "http://py4e-data.dr-chuck.net/comments_1811737.xml"

handle = urllib.request.urlopen(url, context=ctx)
hand = handle.read().decode()
info = ET.fromstring(hand)
numbers = info.findall("comments/comment/count")
for item in numbers:
    num = item.text
    sum = int(num) + sum

print(sum)