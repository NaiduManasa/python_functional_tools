# to know wether a number is even or not
s=[1, 2, 76, 123, 89, 97, 643]

# basic way
lst=[]
for i in range(len(s)):
    if(s[i]%2 == 0):
        lst.append(s[i])

# using filter function
def even(num):
    return num%2 == 0
n=filter(even, s)

# using filter function with lambda
b=filter(lambda x: x%2 == 0,s)

print(lst)
print(list(n))
print(list(b))