def arm(n,le):
    if n==0:
        return 0
    return pow(n%10,le) + arm(n//10,le)
user_number=input("Enter a number : ")
length=len(user_number)
if int(user_number)==arm(int(user_number),length):
    print("Yes, it is a armstrong number : ",user_number)
    
else:
    print("No, it is not a armstrong number : ",user_number)