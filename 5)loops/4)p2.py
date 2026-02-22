import time

#for x in range (10 , 0 ,-1):
 #   print(x)
  #  time.sleep(1) # use to make time sleep 

#print("times up")


user=int(input("ENTER THE AMOUNT OF TIME IN SECONDS :"))

for x in range (user,0,-1):

    second=int(x%60)
    minutes=int(x/60)%60
    hour=int(x/3600)
    print(f"{hour}:{minutes}:{second}")
    time.sleep(1)