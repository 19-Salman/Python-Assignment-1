x=1
while(x<=50):
    for i in range(2,51):
        if(x%i==0):
            i+=1
            break
    else:
        print(x)       

