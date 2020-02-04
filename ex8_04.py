fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    f=line.split()
    for word in f:
        lst.append(word)
lst.sort()
print(lst)
