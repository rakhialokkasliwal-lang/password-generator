





print("===================")
print("PASSWORD GENERATOR")
print("===================")
import random 
import string

length = int(input("Enter password length: "))

if length < 5:
    print("password is too short")
    
elif length < 8:
    print("Medium password")
else:
    print("Strong password")

use_numbers = input("Include numbers? (yes/no): ").lower().strip()
use_symbols = input("Include symbols? (yes/no): ").lower().strip()

characters = string.ascii_letters

if use_numbers == "yes":
    characters += string.digits

if use_symbols == "yes":
    characters += string.punctuation

count = int(input("How many passwords to generate: "))

for i in range(count):
    password = ""
    for j in range(length):
        password += random.choice(characters)
    print("Password", i+1, ":", password)
input("press enter to exit")
