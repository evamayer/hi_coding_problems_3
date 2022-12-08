#Write a program that reads an integer from the user. Then your program should
#display a message indicating whether the integer is even or odd and if the number is a prime or a non-prime.

number = int((input("Please enter an integer: ")))

def number_checker(number):
    if number % 2 == 0:
        print("Your number is even and therefore not a prime.")
    else:
        if number == 1:
            print("Your number is odd and not a prime.")
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    print("Your number is odd and not a prime.")
                    return        
            print("Your number is a prime.")                
                        
number_checker(number)
            