fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    if line.startswith('From '):
        address=line.split()
        count=count+1
        print(address[1])
    else : continue
#   line=line.rstrip()
#   address=line.split()
#   if  len[address]<1 or (글자수)adress[0]!=('From '):
#      continue
#   else:........
#
print("There were", count, "lines in the file with From as the first word")
