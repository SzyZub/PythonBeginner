fname = "Lesson8/" + input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    tem = line.split()   
    for i in tem:
        if not i in lst:
            lst.append(i)
    lst.sort()
print(lst)