x = float(input("Please enter some values and 0 to quit: "))
while x == 0:
    x = float(input("Please enter another, non-zero number: "))
average = 0
total = 0
i = 1
while x != 0:
    total = total + x
    average = total / i
    x = float(input("Enter the next value: "))
    i += 1

print("The average of your numbers is:", average)