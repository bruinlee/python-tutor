#variable
#variable name is reference

#immutable object
a = 3
a = 'at'

#mutable object
l1 = [1,2,3]
l2 = l1
l1 = 1

l3 = [1,2,3]
l4 = l3
l3[0] = 10
print l4

def f(x):
    x = 100
    print x

a = 1
f(a)
print a

def ff(x):
    x[0] = 100
    print x

a = [1,2,3]
ff(a)
print a
