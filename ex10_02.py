name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fp = open(name)
tmlst=list()
tmdic=dict()

for line in fp:
    if line.startswith('From '):
        wd=line.split()
        tm=wd[5].split(':')
        tmlst.append(tm[0])
    else:
        continue

for k in tmlst:
    tmdic[k]=tmdic.get(k,0)+1

for k,v in sorted(tmdic.items()):
    print(k, v)
