# PROGRAM 10: Division with Zero Handling

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

try:
    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide a number by zero!")
