#password generator project
import random
import string
print("password generator system:")
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['1','2','3','4','5','6','7','8','9']
symbols=['@','&','^','$','#','!']
no_letters=int(input("enter the number of letters:"))
no_numbers=int(input("enter the numbers you want:"))
no_symbols=int(input("entr the number of symbols: "))
# password="" 
password_list=[]
for i in range(1,no_letters+1):
    i=random.choice(letters)
    password_list+=i


for i in range(1,no_numbers+1):
    i=random.choice(numbers)
    password_list+=i

for i in range(1,no_symbols+1):
    i=random.choice(symbols)
    password_list+=i

print(password_list)

# print(password)


#we can shuffle password using list by making list of password


#2 way to make password generator project using random module and string module
import random
import string
print("welcome to password generator")
password=""
letters=[random.choice(string.ascii_letters) for i in range(int(input("enter how many letters")))]
numbers=[random.choice(string.digits) for i in range(int(input("how many digits")))]
symbols=[random.choice(string.punctuation) for i in range (int(input("how many punctuation")))]
key=letters+numbers+symbols
random.shuffle(key)
for i in key:
    password=password+i
print(password)