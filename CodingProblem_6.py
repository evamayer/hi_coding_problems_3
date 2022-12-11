from math import sqrt

print("Please enter the values of a and b!")
a = float(input("Value a: "))
b = float(input("Value b: "))

def calculate_hypotenuse(a, b):
    hypotenuse = sqrt(a ** 2 + b ** 2)
    return hypotenuse

print("The hypotenuse of your triangle is", round(calculate_hypotenuse(a, b), 4))

