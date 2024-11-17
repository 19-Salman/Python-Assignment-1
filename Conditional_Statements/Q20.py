x=int(input("Enter a number:"))
for i in range(2,x):
    if(x%i==0):
        print("The entered number is not prime.")
        break
else:
    print("The entered number is prime.") 