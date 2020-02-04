def computepay(h,r):
    if h<40:
        pay=h*r
    else:
        pay=r*(40+1.5*(h-40))
    return pay

hrs = input("Enter Hours:")
rate= input("Enter Rate:")
h=float(hrs)
r=float(rate)
p = computepay(h,r)
print(p)
