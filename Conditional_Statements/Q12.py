temp_in_cel=int(input("Enter temperature in celsius :"))
if(temp_in_cel>=30):
    print("The given temperature is hot.")
elif(temp_in_cel<30 and temp_in_cel>=20) :
    print("The given temperature is moderate.")
elif(temp_in_cel==0):
    print("The given temperature is freezing temperature.")
