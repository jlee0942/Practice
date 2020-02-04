fname = input("Enter file name: ")
fh = open(fname)
lst = list()
i=0
for line in fh:
    f=line.split()
    for word in f:
        lst.append(word)

lst.sort()
while i<(len(lst)-1):
    if lst[i]==lst[i+1]:
        lst.remove(lst[i+1])
    else:
        i=i+1

print(lst)
