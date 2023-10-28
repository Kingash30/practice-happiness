import random

print("Welcome to your password generator")

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!()-.?[]_`~;:!@#$%^&*+='

number = input("Amount of passwords to generate: ")
number = int(number)

length = input("Input your passwords length: ")
length = int(length)

print("\nHere are your passwords: ")

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)