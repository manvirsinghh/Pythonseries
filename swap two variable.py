# def swap_two_numbers(a,b):
#     temp=a
#     a=b
#     b=temp
#     print("a:",a)
#     print("b:",b)

# a=3
# b=5
# swap_two_numbers(a,b)

#2nd way 
a=4
b=5
print("before swapping:")
print("a:",a)
print("b:",b)
print("after swapping:")
a=a+b
b=a-b
a=a-b
print(a)
print(b)

#3rd way
a=6
b=7
print("before swapping:")
print("a:",a)
print("b:",b)
print("after swapping:")
a=a^b
b=a^b
a=a^b
print(a)
print(b)



