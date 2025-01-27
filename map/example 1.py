num=int(input("enter a number:"))
a = [1, 2, 3, 4]

# basic way
lst=[]
for i in range(0,len(a)):
    lst.append(a[i]*num)
    
# using map function
def mul(val):
    return val*num
n = map(mul, a)

# using map function with lambda
b=map(lambda x: x*num, a)

print(lst)
print(list(n))
print(list(b))