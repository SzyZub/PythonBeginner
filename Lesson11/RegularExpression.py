import re 
fname = input("Enter file: ")
handle = open(fname)
sum = 0
for line in handle:
    lst = re.findall("[0-9]+", line)
    if len(lst) == 0: 
        continue
    for i in lst:
        num = float(i)
        sum = sum + num
print(sum)
