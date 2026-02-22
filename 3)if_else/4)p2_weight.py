print("THIS IS A WEIGFHT CONVERTER")

b=input("WHAT YOU WANT\n1 == pond to kg\n2 == kg to pound :")
a=float(input("ENTER YOUR WEIGHT :"))
if b=="1":
    print(round(a/2.20462 , 2 ))
elif b=="2":
    print(round(a*2.20462 , 2 ))
    
else:
    print("something went wrong")        
