def func(x,y):
    return x + y

def test(f, a, b):
    print 'test'
    print f(a, b)

test(func, 3, 5)

fun = lambda x,y: x+y
print fun(3,4)

#map()
re = map((lambda x: x+3), [1,3,5,6])
print re

#filter() true/false

#reduce()
