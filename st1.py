# import itertools
# dictionary={
#     'one':1,
#     'two': 2,
#     'three':3,
#     'four':4,
#     'five':5,
#     'six':6,
#     'seven':7,
#     'eight':8,
#     'nine':9,
#     'zero':0
# }
# num1=input("Enter string : ")
# l1=num1.split()
# l2=[]
# for i in l1:
#     l2.append(dictionary[i])
# print(''.join(map(str,l2)))
name=input("Enter only one word to rotation : ")
word=int(input("Enter which no. of word you want to rotate : "))
length=len(name)-1
s1=name[:word]
end=name[-word:]
wordr=name
for i in range(word):
    name.replace(f"{name[i]}"," ")
    wordr.replace(f"{wordr[length-i]}"," ")
    
print("left rotation : ",name+s1)
print("right rotation : ",end+wordr)