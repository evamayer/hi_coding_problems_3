print("Please enter the ages of each member of your group then finish with an empty line when done.")
age_string = input("Enter the age of the first memeber of your group:\n")

admission_total = 0

while age_string != "":
    age = int(age_string)
    
    if age < 3:
        price = 0

    if age >= 3 and age < 13:
        price = 14

    if age >= 13 and age < 65:
        price = 23

    if age >= 65:
        price = 18
        
    admission_total = admission_total + price
    age_string = input("Enter the next member's age: \n")
    
print(f"The total admission cost for your group is: ${admission_total}")