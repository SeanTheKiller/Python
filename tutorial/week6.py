#Q1
sum = 0
for i in range(1, 51, 1):
    sum += i
    print(f"Sum of the first 50 numbers is: {sum}")

#Q2
num = 2
while (num <= 100):
    print(num)
    num+=2

#Q3
value = 0
nonnegative = 0

while value >= 0:
    value = int(input("Enter a number (negative to stop): "))
    if value >0:
        nonnegative = value
print(f"Last non negative is: {nonnegative}")

#4
for i in range(1, 6, 1):
    for j in range(1, 6, 1):
        print("x  ", end=" ")
    print()

#5
import random 
for i in range(1, 6, 1):
    guess = int(input(f"Guess the number (attempt {i}): "))
    secret = random.randint(1, 100)
    if guess == secret:
        print("You got it!")
        break
    else:
        print("Better luck next time!")
    
    if guess > secret:
        print("Too High!")
    elif guess < secret:
        print("Too Low!")

#6
attempt = 0
correct_pin = 1234
for i in range(1, 4):
    pin = int(input("Please enter your PIN: "))
    attempt += 1

    if pin == correct_pin:
        print("Withdrawal successful")
        break
    else:
        print("Incorrect PIN")

    if attempt >= 3:
        print("Card blocked")
        break

