import math

height=float(input("ENTER THE HEIGHT OF THE TRIANGLE :"))
base=float(input("ENTER THE BASE OF THE TRIANGLE :"))
h=math.sqrt(pow(height ,2)+pow(base ,2))

print(f"your hypotenous is {round(h,2)}")