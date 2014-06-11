def f(a,b,c=10):
    return a+b+c

print(f(1,2,3))
print(f(1,c=3,b=2))

#packing pass
def func(*name):
    print type(name)
    print name

func(1,4,6)
func(5,6,7,1,2,3)

def funcc(**dic):
    print type(dict)
    print dict

funcc(a=1,b=9)

args=(1,3,4) #tuple
func(*args)

dict = {'a':1, 'b':2, 'c':3}
funcc(**dict)


