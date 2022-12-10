def calculate_charge(item_number):
    shipping_charge = 10.95 + ((item_number - 1) * 2.95)
    return round(shipping_charge, 2)

item_number = int((input("Please enter the number of items you are purchasing: ")))
print(f"Your shipping charge is ${calculate_charge(item_number)}.")
