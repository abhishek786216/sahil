name1=input("Enter string : ")
# name2=input("Enter string : ")
# sl1=name1.split()
# sl2=name2.split()
# l3=[]
# for i in sl1:
#     if i not in sl2:
#         l3.append(i)
# for i in sl2:
#     if i not in sl1:
#         l3.append(i)
# print(l3)
# import itertools
# import math
# total_case=(list(itertools.permutations(name1)))

# for i in (total_case):
#     print("".join(i))    
# print(math.factorial(len(name1)))

name1=name1.split()
find=input("Enter which word idx finding : ")
print(name1.index(find)+1)