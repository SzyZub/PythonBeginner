# Use the file name mbox-short.txt as the file name
import os
fname = "Lesson7/" + input("Enter file name: ") 
fh = open(fname)
count = 0
sa = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count += 1 
    nm = line.find(" ")
    numb = line[nm:]
    nmr = float(numb)
    sa = sa + nmr
print("Average spam confidence:", sa/count)
