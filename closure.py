def line_conf():
    def line(x):
        return 2*x + 1
    return line

my_line = line_conf()
print(my_line(5))

#closure
def line_con():
    b = 15
    def lin(x):
        return 2*x + b
    return lin

b = 5
my_lin = line_con()
print(my_lin(5)) #print 25

def linee(a,b):
    def line(x):
        return a*x + b
    return line

line1 = linee(1,1)
line1 = linee(4,5)


#parrallel programming
