questions=(("who is the prime minister of india ? :"),("in which state banglore is in ? :"))
answers=(("MODI JI","meloni ji","rahul gi","rajiv ji"), ("bihar" , "karnataka" ,"delhi" ,"japan") )
options=("A .","B .","C .","D .")
num=int(0)
k=int(0)
answer=int(0)
for x in questions :
    print(x)
    num=int(0)
    for y in answers[k]:
       
        print(f"{options[num]} {y}")
        num=num+1
    option1=input()
    if option1=="A"or option1=="a":
        answer+=1
    
