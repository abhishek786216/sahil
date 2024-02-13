num1=int(input("Enter number 1st : "))
num2=int(input("Enter number 2nd : "))
for i in range(min(num1,num2),0,-1):
    if(num1%i==0 and num2%i==0):
        print(f"HCF of {num1} and {num2} is : {i}")
        break
    