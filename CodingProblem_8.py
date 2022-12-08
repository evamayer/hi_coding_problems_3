password = str(input("Enter password: "))

def password_check(password):
    has_lower = False
    has_upper = False
    has_number = False
    has_length = False
    if len(password) >= 8:
        has_length = True
    for ch in password:
        if ch >= "A" and ch <= "Z":
            has_upper = True
        elif ch >= "a" and ch <= "z":
            has_lower = True
        elif ch >= "0" and ch <= "9":
            has_number = True

    if has_lower and has_upper and has_number and has_length:
        return True

    return False

print(password_check(password))