s='abcdefghijklmn'

#range()
for i in range(0, len(s), 2):
    print s[i]

#enumerate()
for(index, char) in enumerate(s):
    print index
    print char

#zip(), equal length
ta = [1,2,3]
tb = [9,8,7]
tc = ['a','b','c']

for (a,b,c) in zip(ta,tb,tc):
    print(a,b,c)

zipped = zip(ta,tb)
print(zipped)

na, nb = zip(*zipped)
print(na,nb)


#loop object,  next() method
#save space, efficient
f = open('test.txt')
f.next()
f.next()

#generator, create self-defined loop
def gen():
    a = 100
    yield a
    a = a*8
    yield a
    yield 1000

for i in gen():
    print i

#generator expression
G = (x for x in range(4))

#
#List comprehension
xl = [1,3,5]
yl = [9,12,13]
L  = [ x**2 for (x,y) in zip(xl,yl) if y > 10]
print L

