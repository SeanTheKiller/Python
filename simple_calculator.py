def add(a, b):
     return a + b

def subtract(a, b):
    return a - b

def addition(a, b):
    return a * b

def division(a, b):
    return a / b


while True:
    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit")
    user_input = int(input("Select Number for Math Engine: "))
    if user_input == 1:
        num1 = float(input("Enter 1st number: "))
        num2 = float(input("Enter 2nd number: "))
        result = add(num1, num2)
        print(f"The sum of {num1} + {num2} is equal to {result}")

    elif user_input == 2:
        num1 = float(input("Enter 1st number: "))
        num2 = float(input("Enter 2nd number: "))
        result = subtract(num1, num2)
        print(f"The subtract of {num1} - {num2} is equal to {result}")

    elif user_input == 3:
        num1 = float(input("Enter 1st number: "))
        num2 = float(input("Enter 2nd number: "))
        result = addition(num1, num2)
        print(f"The sum of {num1} x {num2} is equal to {result}")

    elif user_input == 4:
        num1 = float(input("Enter 1st number: "))
        num2 = float(input("Enter 2nd number: "))
        result = division(num1, num2)
        print(f"The sum of {num1} / {num2} is equal to {result}")

    elif user_input == 5:
        break

    else:
        print("Invalid input")

