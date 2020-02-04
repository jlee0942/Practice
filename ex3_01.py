hrs=input("Enter Hours:")
h=float(hrs)
hrate=input("Enter Rate:")
fhrate=float(hrate)
if h<=40:
    pay=fhrate*h
else:
    pay=fhrate*(40+(h-40)*1.5)
print("Pay:",pay)
