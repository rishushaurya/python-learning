# indexing = accessing the elements of a sequence usingf []
# [start : end : step]


rishu :int= "1234-5678-9012"

print(rishu[0]) #will print the index which we want
print(rishu[0 : 4]) # strting is inclusive as it include the 0th posion no. and ending position is exclusive 
# or print(rishu[ :4 ])  this will give the same value asd the fist one cause python thinks you want to strat from 0
print(rishu[1 :6])

print(rishu[4 : ])# if you just put the colum,n then python will think you need till the end

print(rishu[-1]) # this will print the last digit 
print(rishu[-4])
print(rishu[::3]) # this is the step one python will print all the bdigits in diffrence of 3(actually it will print the every 3rd character) , as we havent defined starting and ending so it will assume you want all

print(rishu[2:8:2])#  tjis will skip one and will print every 2nd character 




print(f"your credit card number :- XXXX-XXXX-{rishu[-4:]}")

print(f"{rishu[::-1]}") # this will reverse the number 
print(f"{rishu[::-2]}")  # this will reverse and print every 2nd digit



hell="boi","my","yo","1","2","3"
print(f"{hell[::-1]}")