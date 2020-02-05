name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
lst=list()
who=dict()
for line in handle:
    sd=line.split()
    if line.startswith('From '):
        frm=sd[1]
        lst.append(frm)
    else:
        continue
for word in lst:
    who[word]=who.get(word,0)+1

lrgstk=None
lrgstv=None

for k,v in who.items():
    if v >lrgstv or lrgstv is None:
        lrgstk=k
        lrgstv=v
print(lrgstk, lrgstv)
        
