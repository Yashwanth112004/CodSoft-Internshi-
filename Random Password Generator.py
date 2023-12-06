import string
import random
print("PASSWORD GENERATOR")
while(True):
    length=int(input("Enter Length of your Password: "))
    letters=input("Do the Password need Letters(yes/no): ").lower()=='yes'
    numbers=input("Do the Password need Numbers(yes/no): ").lower()=='yes'
    special_symbols=input("Do the Password need Symbols(yes/no): ").lower()=='yes'
    characters=""
    if letters:
        characters += string.ascii_letters
    if numbers:
        characters += string.digits
    if special_symbols:
        characters += string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    print("Random Generated Password: ",password)
 