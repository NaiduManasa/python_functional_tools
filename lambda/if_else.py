# to know even or odd using lambda
x=int(input("enter a number:"))
n=lambda x: "even" if x%2 == 0 else "odd"
print(n(x))