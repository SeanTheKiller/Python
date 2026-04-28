#Question 1
def y_value(m, x , c):
    return m * x + c

num1 = float(input("Enter m: "))
num2 = float(input("Enter x: "))
num3 = float(input("Enter c: "))

result = y_value(num1, num2, num3)
print(f"The value of y = {result}\n")

#Question 2
def area(b, h):
    return 1/2 * b * h

num4 = float(input("Enter base: "))
num5 = float(input("Enter height: "))

result = area(num4, num5)
print(f"The area of the triangle = {result}\n")

#Question 3
def simple_interest(p, r, t):
    return (p * r * t)/100

num6 = float(input("Enter principal (P): "))
num7 = float(input("Enter rate (R): "))
num8 = float(input("Enter time (T): "))

result = simple_interest(num6, num7, num8)
print(f"The simple interest = {result}\n")

#Question 4
def circle(r):
    return 22/7 * r**2

num9 = float(input("Enter radius: "))

result = circle(num9)
print(f"The area of the circle = {result:.2f}\n")

#Question 5
def square_cube(n):
    square = n**2
    cube = n**3
    return square, cube

num10 = float(input("Enter a number: "))

square, cube = square_cube(num10)
print(f"Square = {square}")
print(f"Cube = {cube}")