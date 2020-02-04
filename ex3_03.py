score=input("Enter Score:")
try:
    iscore=float(score)
except:
    print("Wrong input-input numerical num")
    quit()

if iscore>=0.9:
    print("A")
elif iscore>=0.8:
    print("B")
elif iscore>=0.7:
    print("C")
elif iscore>=0.6:
    print("D")
else :
    print("F")
