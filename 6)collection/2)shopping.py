print("HELLO THIS IS BOB THE SHOPPING cart HELPER")
bob=input("HELLO WHAT YOU WANNA DO ? :")
bob=bob.lower()
total=0
bag=[]
price=[]
while bob!="q":
    if bob=="hello" or bob=="hi" :
        print("OH DEAR !!! I CAN HELP YOU WITH SHOPPING CART !!!")
    
    elif bob=="shopping cart" or bob=="shopping" or bob=="s":
        item=int(input("ENTER HOW MANNY THINGS YOU WANNA BUY  :"))

        for x in range(item):
            bag.append( input("WHAT YOU WANNA BUY ? :"))
            price.append(int(input("ENTER THE PRICE OF THAT ITEM :")))
            #bag[x]=input("WHAT YOU WANNA BUY ? :")
            #price[x]=float(input("ENTER THE PRICE OF THAT ITEM :"))    you cant do this way

        for y in range(item):
            print(f"{bag[y]} costs {price[y]} ")
            
            total+=price[y]

        print(f"hence your total is {total}")

    bob=input("HELLO WHAT YOU WANNA DO ? :")

    