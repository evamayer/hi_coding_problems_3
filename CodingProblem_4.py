from tabulate import tabulate

degrees_celsius = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
degrees_fahrenheit = []

for i in degrees_celsius:
    calculation = (i * 1.8) + 32
    degrees_fahrenheit.append(round(calculation))

table = zip(degrees_celsius, degrees_fahrenheit)
columns = ["Celsius", "Fahrenheit"]

print(tabulate(table, headers=columns, tablefmt="fancy_grid"))