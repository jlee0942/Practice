fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line2=line.rstrip()
    lst.append(line2)
    lst.split()
lst.sort()
print(lst)
