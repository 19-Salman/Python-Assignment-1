number=30
number_found=False
while not number_found:
    input_number=int(input("Enter a number:"))
    if input_number==number:
        number_found=True
        print("The correct number is guessed.")
    else:
        print("Sorry! The correct number isn't guessed. ")