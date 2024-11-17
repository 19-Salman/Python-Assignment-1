x=int(input("Enter an integer number:"))
if(x%2==0 and x%3==0):
    print("The entered integer number is divisible by both '2' and '3'")
elif(x%2==0):
    print("The enterd integer number is divisible by '2'")
elif(x%3==0):
    print("The entered integer number is divisible by '3'")