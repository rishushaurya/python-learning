# input = A function that prompts user to enter user data and promnpt tehm to return in the form of string 
#input("WHAT IS YOUR NAME? :") this will only take input
name =input("WHAT IS YOUR NAME? :")# then we any variable to store that string in

#age=input("ENTER YOUR AGE :")this will store that in string so we cant add or substract so we will use typecasting to cange its adata type
# we can do age = int(age) but its easier to do

# age=int(input("WHAT IS YOUR AGE :"))
# print(f"your name is {name}")

age=int(input(f"your name is {name} so give your age :"))
age =age+1

print(f"HAPPY BIRTHDAY NOW YOU ARE {age}")