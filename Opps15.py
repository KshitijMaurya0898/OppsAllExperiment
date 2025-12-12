# PROGRAM 15: Swap two numbers using a function

def swap(a, b):
    a, b = b, a
    return a, b

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Before swapping: x =", x, ", y =", y)

x, y = swap(x, y)

print("After swapping: x =", x, ", y =", y)
