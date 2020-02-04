largest=None
smallest=None

while True:
    num = input('Enter a Number:')
    if num=='done':
        break
    else:
        try:
            fnum=int(num)
            if largest==None:
                largest=fnum
            elif fnum<largest:
                largest=fnum
            if smallest==None:
                smallest=fnum
            elif fnum<smallest:
                smallest=fnum
        except:
            print('Invalid input')
            continue
    continue
print ('Maximum is',largest)
print ('Minimum is',smallest)
