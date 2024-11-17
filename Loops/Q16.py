num=(input("Enter an integer:"))
digit_sum=0
for digit in num:
    if digit.isdigit():
        digit_sum+=int(digit)
print(f"The sum of the digits is = {digit_sum}")