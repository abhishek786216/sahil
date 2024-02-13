import functools
size=int(input("Enter size of list : "))
l1=[]
for i in range(size):
    num=(input())
    l1.append(num)
    
# l2=l1.copy() #u can use also l1=l2 no need to use to use copy function
# print(l1)
# print(l2)
# l2=l1[::-1]#very important to use the reverse for anything
# print(l1)
# print(l2)
# print(l1.count(3))#functon to use the count number of particular variable
# print(sum(l1))
# pro=lambda x,y: x*y #this anomous function give the product oof  two number
# print(functools.reduce(pro,l1))#first use add functools then use the reduce function
# print(max(l1))
# idx=l1.index(max(l1))#nice question 
# l1[idx]=0
# print(max(l1))
# l2=[]
# for i in range(len(l1)):
#     for j in range(len(l1)):
#         if l1[i]==l1[j] and i!=j:
#             l2.append(l1[i])

# s1=set(l2)
# l2=list(s1)
# print(l1)
# print(l2)
# string=" ".join(l1)#nice question
# print(string)
# for i in range(len(l1),0,-1):
#     print(i,end=" ")
# for i in range(-10,0,1):
#     print(i)