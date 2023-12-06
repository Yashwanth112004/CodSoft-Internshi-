while(1):
    a = int(input("Enter a Number: "))
    b = int(input("Enter another Number: "))
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Find the Remainder")
    print("6. Power with base and exponent")
    print("7. Floor Division")
    
    c = int(input("Choose the Operation to be performed from Above: "))
    
    if c == 1:
        print("Result:", a + b)
    elif c == 2:
        print("Result:", a - b)
    elif c == 3:
        print("Result:", a * b)
    elif c == 4:
        if b != 0:
            print("Result:", a / b)
        else:
            print("Cannot divide by zero.")
    elif c == 5:
        if b != 0:
            print("Result:", a % b)
        else:
            print("Cannot find remainder when dividing by zero.")
    elif c == 6:
        print("Result:", a ** b)
    elif c == 7:
        if b != 0:
            print("Result:", a // b)
        else:
            print("Cannot perform floor division by zero.")
    else:
        print("Invalid choice. Please choose a number from 1 to 7.")
