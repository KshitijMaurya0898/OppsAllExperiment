# PROGRAM 24: Division with Exception Handling + Unit Test

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero!"

# Unit test function
def test_division():
    print("Running Tests...")
    
    # Test 1: normal division
    result1 = divide(10, 2)
    print("Test 1 (10/2):", "Pass" if result1 == 5 else "Fail")

    # Test 2: division by zero
    result2 = divide(5, 0)
    print("Test 2 (5/0):", "Pass" if result2 == "Error: Cannot divide by zero!" else "Fail")


# Taking user input
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Result:", divide(a, b))

# Run unit tests
test_division()
