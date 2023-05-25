name = input("Enter file:")
handle = open(name)
dic = dict()
lst = list()
name = None
count = None
for line in handle:
    if line.startswith("From "):
        lst = line.split()
        dic[lst[1]] = dic.get(lst[1], 0) + 1
        
        
for x,y in dic.items():
    if count is None or y > count:
        count = y
        name = x
        
print(name, count)
    