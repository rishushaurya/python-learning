print("THIS IS A TEMPERATURE CONVERTER")

b=input("WHAT YOU WANT\n1 == celcius to kelvin\n2 == kelvin to celcius :")
a=float(input("ENTER YOUR TEMPERATURE :"))
if b=="1":
    print(round(a+273 , 2 ))
elif b=="2":
    print(round(a-273 , 2 ))
    
else:
    print("something went wrong")  