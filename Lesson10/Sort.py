name = input("Enter file:")
handle = open(name)
dct = dict()
lst = list()
for line in handle:
    if line.startswith("From "):
        num = line.find(":")
        dct[line[num-2:num]] = dct.get(line[num-2:num], 0) + 1
for v, k in dct.items():
    tem = (v, k)
    lst.append(tem)
lst = sorted(lst)
for (v, k) in lst:
    print(v, k)