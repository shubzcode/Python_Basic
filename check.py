def get_single_digit(number):
    if len(number) == 1 and number.isdigit():
        return True
    else:
        return False

while True:
    input_number = input("Enter a number:  ")
    if get_single_digit(input_number):
        print("Valid single digit")
        break
    else:
        print("Not a Valid single Digit. try Again. ")
print("Single Digit you enter is :", input_number)