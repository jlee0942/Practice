fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line2=line.rstrip()
    line2.split()
    lst=lst+line2
lst.sort()
print(lst)
