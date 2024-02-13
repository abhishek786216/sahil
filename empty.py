# l1=[5, 6, [], 3, [], [], 9]
# l2=[]
# for i in l1:
#     if i==[]:
#         continue  
#     else:
#         l2.append(i)
        
# print(l2)
# l1=["name",'age','salary','id']
# l2=['Abhishek',20,400000,231212001]
# di=dict(zip(l1,l2))#how to use zip function 
# for x,y in di.items():
#     print(x,y)
# l1=[['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]
# l2=[]
# l3=[]
# for i in range(len(l1)):
#     l2.append(l1[i][0:2])
#     l3.append(l1[i][2:4])
# t1=tuple(l2)
# t2=tuple(l3)
# di=dict(zip(t1,t2))
# print(l2,l3)

# l1=[[1, 2], [3, 4], [5, 6]]
# l2=[[3, 4], [5, 7], [1, 2]]
# l3=[]
# for i in l1:
#     if i not in l2:
#         l3.append(i)
# print(l3)
# import random
# from itertools import chain
# l1=[[4, 5, 5], [2, 7, 4], [8, 6, 3]]
# print(random.choice(list(chain.from_iterable(l1))))
# l1=[1, 2, 2, 5, 8, 4, 4, 8]
# l2=set(l1)
# print((l2))
import functools
l1=[1, 3, 5, 6, 3, 5, 6, 1]
l2=set(l1)
l1=list(l2)
print(functools.reduce(lambda x,y : x*y,l1))