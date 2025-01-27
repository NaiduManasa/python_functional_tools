a=int(input("enter the number to print table:"))
n=list(lambda val=x: val*a for x in range(1,11))
for i in n:
    print(i())