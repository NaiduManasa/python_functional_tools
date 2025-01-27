# to find sum of values in a list
from functools import reduce

s=[2, 4, 6, 3, 8, 9]

# basic way
val=0
for i in range(len(s)):
    val += s[i]

# using reduce function
def add(x,y):
    return x+y
n=reduce(add, s)

#using reduce with lambda function
b=reduce(lambda x,y: x+y, s)

print(val)
print(n)
print(b)