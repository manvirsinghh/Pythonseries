# # #ist method
# # string="manvir"
# # print(string[::-1]) #using slice method


# # # #using for loop
# # def reversestr(string):
# #     str=""
# #     for i in string:
# #         str=i+str
# #         return str
# #         string="manvir"
# #     reversestr(string)


# #     #append the elemnet to list
# # list=[1,2,3,4,5,6]
# # list.append(7)
# # print(list)
# # list.insert(7,8)
# # print(list)
# # list.extend([9,10,11])
# # print(list)


# # #print largest of three numbers
# # num1=int(input("enter the value of num1:"))
# # num2=int(input("enter the value of num2"))
# # num3=int(input("enter the value of num3"))
# # if num1>num2 and num1>num3:
# #     print("num1 is largest  amongest them")
# # elif num2>num3 and num2>num1:
# #     print("num2 is largest among others")
# # else:
# #     print("num3 is largest among others")

#     #to check no is prime or not
# num = int(input("Enter the value: "))

# if num <= 1:
#     print("Not prime")
# else:
#     # Loop to check if num is divisible by any number from 2 to num-1
#     for i in range(2, num):
#         if num % i == 0:
#             print("False")
#             break  # Stop the loop once a divisor is found
#     else:
#         print("True")  # If no divisor is found, num is prime

   
#    #factorial of number
#    #ist method
# import  math
# print(math.factorial(5))

#2nd way
def fact(num):
    if num<0:
        print("invalid number")
        return
    elif num==0:
        return 1
    else:
        return num*fact(num-1)
num=5
result=fact(5)
print(result)


#if we want to take input for number then it can be done as follows:
def fact(num):
    if num<0:
        return 
    elif num==0 or num==1:
        return 1
    else:
        return num*fact(num-1)
num=int(input("enter the value :"))
result=fact(num)
print(result)


#display multiplication table

num=int(input("enter the number :"))
print(f"multiplication table of {num} is:")
for i in range(0,11):
    print(f"{num} *{i}=",num*i)


