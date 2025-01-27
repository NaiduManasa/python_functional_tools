from functools import reduce
import operator

s=[2, 3, 4, 7, 9]

print(reduce(operator.add, s))

print(reduce(operator.mul, s))