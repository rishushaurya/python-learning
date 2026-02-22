# format specifiers = {value:flags} format a value based on what
# flags are inserted
# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# : = insert a space before positive numbers
# :, = comma separator

a=-89786132.861
b=9878.9867821347
c=789213.879821

#print(f"A= {a:.3f}")
#print(f"B= {b:.3f}") # this will print the value till 3 floting didgits but it will round them up too
#print(f"C= {c:.3f}")

#print(f"A= {a:30}")
#print(f"B= {b:30}") # this will give the number size to 30
#print(f"C= {c:30}")

#print(f"A= {a:030}")
#print(f"B= {b:030}") # this will give the number size to 30 but with 0 patted
#print(f"C= {c:030}")

#print(f"A= {a:<}")
#print(f"B= {b:<}") # this will adjust to left alingment same with right ,^ this wikll align them in between
#print(f"C= {c:<}")

#print(f"A= {a:<+030}")
#print(f"B= {b:<+030}") # this will give the number their original symbols 
#print(f"C= {c:<+030}")

#print(f"A= {a:==}")
#print(f"B= {b:==}") # this will give the number size to 30
#print(f"C= {c:==}")

print(f"A= {a:+,}")
print(f"B= {b:+,}") #  comma separator
print(f"C= {c:+,}")