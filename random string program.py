#how to generate random string  of letters in python
import random
import string

random_str="".join(random.choices(string.ascii_letters,k=10))
print(random_str)

#how to generate random string with letters and digits
random_str1="".join(random.choices(string.ascii_letters+string.digits,k=12))
print(random_str1)

#how to generate the random string with letters,digits and special characters
random_str3="".join(random.choices(string.ascii_letters+string.digits+string.punctuation,k=12))
print(random_str3)

#how to generate secret random string 
import secrets
import string

secret_str4="".join(secrets.choice(string.ascii_letters+string.digits)for i in range(12))
print(secret_str4)

#Use random.choices() for quick random string generation for general purposes.
# Use secrets.choice() for generating secure strings, like passwords or tokens.