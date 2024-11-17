string=input("Enter a palindrome:")
if(string==string[::-1]):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")