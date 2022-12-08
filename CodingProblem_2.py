from math import sqrt

print("Please enter the values of a, b and c!")
a = float(input("Value a: "))
if a == 0:
    a = int(input("Please enter a non-zero value: "))
b = float(input("Value b: "))
c = float(input("Value b: "))

discriminant = b ** 2 - 4 * a * c

if discriminant < 0:
    print("no real roots")
elif discriminant == 0:
    x = -b / (2 * a)
    print("one real root: x =", x)
else:
    x1 = round((-b + sqrt(discriminant)) / (2 * a), 5)
    x2 = round((-b - sqrt(discriminant)) / (2 * a), 5)
    print("two real roots: x1 =", x1, "x2 =", x2)
