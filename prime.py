def primer(n):
    for i in range(2,n):
        if(n%i==0):
            return None
    print(n,end=" " )
    return
        
num=int(input("Enter number : "))
for i in range(2,num+1):
    primer(i)
    
