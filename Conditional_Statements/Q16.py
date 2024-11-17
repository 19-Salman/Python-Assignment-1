a=int(input("Enter first side of a triangle:"))
b=int(input("Enter second side of a triangle:"))
c=int(input("Enter third side of a triangle:"))
if(a==b==c):
    print("This triangle is an equilateral triangle.")
elif(a==b or b==c or c==a):
     print("This triangle is an isosceles triangle.")
else:
    print("This triangle is a scalene triangle.")
