import random

secret = random.randint(1,10)

num = int(input("Enter number: "))

while secret != num:
    print("Wrong Number!")
    num = int(input("Enter number: "))

print(f"Congratulations! you have guessed it, {secret}")