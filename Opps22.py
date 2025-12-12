# PROGRAM 22: Multiply using *args

class Maths:
    def multiply(self, *args):
        result = 1
        for num in args:
            result *= num
        return result


m = Maths()

# Testing different cases
print("Multiply 2 numbers:", m.multiply(5, 3))
print("Multiply 3 numbers:", m.multiply(2, 4, 6))
print("Multiply any number of inputs:", m.multiply(1, 2, 3, 4, 5))
