a=float(input("ENTER THE NUMBER A :"))
b=float(input("ENTER THE NUMBER B :"))
c=str(input("WHAT YOU WANNA DO 1) + = addition \n2) - = substraction \n3) * = multiplication \n4) / = division  :"))

if c=="+":
    #d=a+b
    #print(f"your value for {a}+{b}={d}")
    print(f"your value for {a+b=}")

elif c=="-":
    d=a-b
    print(f"your value for {a}+{b}={d}")    


elif c=="*":
    d=a*b
    print(f"your value for {a}*{b}={d}")


elif c=="/":
   e=input("what you want 1 = A/B \n 2 = B/A :")  
   if e=="1":
       if b == 0:
        print("SORRY CANT DIVIDE BY ZERO")
       else:
          d=a/b

          print(f"your value for {a}/{b}={d}")  

   elif e=="2":
       if a == 0:
        print("SORRY CANT DIVIDE BY ZERO")
       else:
          d=b/a
          print(f"your value for {b}/{a}={d}")        

   else:
      print("invalid input :(") 

else:
      print("invalid input :(")       