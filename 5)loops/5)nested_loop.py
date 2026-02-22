# nested loop= loop inside loop
#import time

#print("THIS IS THE TABLE")

#user=int(input("ENTER THE IN WHOS TABLE YOU WANT :"))
#for x in range (1, 11):
 #       new=user*x
  #      print(f"{user} * {x} = {new}")
   #     #time.sleep(1)


#for y in range (3):
 #   for z in range (11):
  #      print(z,end="")

   # print("\n")


row=int(input("ENTER THE NUMBER OF ROWS :"))
column=int(input("ENTER THE NUMBER OF column :"))
symbol=input("ENTER THE symbol :")



for x in range( row):
    print("\n")
    for y in range( column):
        print(symbol, end="")
   
