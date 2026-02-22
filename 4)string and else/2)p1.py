password=input("ENTER YOUR PASSWORD :")

if len(password) > 12 :
    print("INVALID INPUT ONLY 12 DIGITS ALLLOWERD")


elif password.find(" ")==True :
        print("NO SPACES ALLOWED")

   
elif password.isalpha()==False :
            print("no digits allowed ")
else :
            print(f"your {password=}")