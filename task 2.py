# Python program gor generating a password
import string
import random

all_characters = string.ascii_letters + string.digits + string.punctuation

length = int(input("Enter the length of the password: "))

password = ''.join(random.choices(all_characters, k=length))

print("Your password is:", password)
