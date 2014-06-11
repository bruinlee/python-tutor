re = iter(range(5))

try:
    for i in range(100):
        print re.next()
except StopIteration:
    print "end", i
else:
    print "else"
finally:
    print "final block"

#raise exception
print "1"
raise StopIteration
print "2"
