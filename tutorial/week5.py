#1
user_input = int(input("Enter an integer: "))

if user_input >= 0:
    print("Positive")

elif user_input <= 0:
    print("Negative")

else:
    print("Zero")

#2
print()
num = int(input("Enter a number: "))

if num % 2 == 0: # % means for even
    print("Even")

else:
    print("Odd")

#3
print()
first_num = int(input("Enter a number: "))
second_num = int(input("Enter a number: "))

if first_num == second_num:
    print("Both numbers are equal")

elif first_num > second_num:
    print(f"a: {first_num} is greater than b: {second_num}")

else:
    print(f"b: {second_num} is greater than a: {first_num}")

#4
print()
num4 = int(input("Enter first number: "))
num5 = int(input("Enter second number: "))
num6 = int(input("Enter thid number: "))

if num4 > num5 and num4 > num6: #"this" bigger than that and "this" bigger than that
    print(f"First number is largest: {num4}")

elif num5 > num4 and num5 > num6: #"this" bigger than that and "this" bigger than that
    print(f"Second number is largest: {num5}")

else:
    int(input("Enter an integer: "))

#5
num7 = int(input("Enter an integer: "))

if num7 % 5 == 0:
    print("Divisible by 5")

else:
    print("Not Divisible by 5")

#6
print()
num8 = int(input("Enter first number: "))
operator = input("Enter operator: ")
num9 = int(input("Enter second number: "))

if operator == "+":
    print(f"Result: {num8 + num9}")

elif operator == "-":
    print(f"Result: {num8 - num9}")

elif operator == "*":
    print(f"Result: {num8 * num9}")

else:
    (f"Result: {num8 / num9}")

#7
hour = int(input("Enter the hour: "))
minute = int(input("Enter the minute: "))

if hour > 5 and hour <= 11 and minute <60:
    print("10% off")
