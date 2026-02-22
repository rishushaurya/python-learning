# response = input("DO YOU LIKE FOOD: ")

# if response == "Y" or response == "y" or response == "yes" or response == "Yes":
   #  print("yes sirr!")
# else:
  #   print("whaaattt")

response = input("DO YOU LIKE FOOD: ")
response=response.lower()

if  response == "y" or response == "yes" :
    print("yes sirr!")
else:
    print("whaaattt")

  

# response = input("DO YOU LIKE FOOD: ")

# if response.lower() in ["y", "yes"]:
    # print("yes sirr!")
# else:
   #  print("whaaattt")

online = True

if online:# we can directly put cause bool works as true or false it self
    print("user is online")
else:
    print("user is not online")    