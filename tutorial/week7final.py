#Question 1
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

def add_two_num(a, b):
    return a + b

print(f"Sum of {num1} and {num2} =", add_two_num(num1, num2),"\n")

#Question 2
def max_three_num(a, b, c):
    if a > b and a > c:
        largest = a
    elif b > a and b > c:
        largest = b
    else:
        largest = c

    return largest

num3 = float(input("Enter 1st number: "))
num4 = float(input("Enter 2nd number: "))
num5 = float(input("Enter 3th number: "))

print("Maximum is",max_three_num(num3, num4, num5),"\n")



#Question 3
def cel_to_fah(c):
    return ((9/5)*c)+32

num6 = float(input("Enter temperature in Celsius: "))
print(f"Temperature in Fahrenheit: {cel_to_fah(num6):.2f} \n")

#Question 4
def area_cir(r):
    return 22/7 * r **2, 2 * 22/7 * r

num7 = float(input("Enter radius: "))
print(f"Area = {area_cir(num7)[0]:.2f} \nCircumference = {area_cir(num7)[1]:.2f}")

#Question 5
def total_grade(a, b ,c):
    average = (a + b + c)/3
    total_grading = a + b + c

    if average > 80:
        return total_grading, average, "A"
    elif average > 60:
        return total_grading, average, "B"
    elif average > 40:
        return total_grading, average, "C"
    else:
        return total_grading, average, "Fail"
    
        
num8 = float(input("Enter marks in 1st subject: "))
num9 = float(input("Enter marks in 2nd subject: "))
num10 = float(input("Enter marks in 3rd subject: "))

print(f"Total = {total_grade(num8, num9 ,num10)[0]}\nAverage = {total_grade(num8, num9 ,num10)[1]}\nGrade = {total_grade(num8, num9 ,num10)[2]}")

