def decorator(F):
    def new_F(a,b):
        print("input", a, b)
        return F(a,b)
    return new_F

@decorator
def square_sum(a,b):
    return a**2 + b**2

print(square_sum(3,4))

#decorator with argument
def pre_str(pre=''):
    #old decorator
    def decorator(F):
        def new_f(a,b):
            print(pre + "input", a, b)
            return F(a,b)
        return new_f
    return decorator

@pre_str("^_^")
def square_diff(a,b):
    return a**2-b**2

#decorate class
def decorator(aClass):
    class newClass:
        def __init__(self,age):
            self.total_display = 0
            self.wrapped = aClass(age)
        def display(self):
            self.total_display += 1
            print("total display", self.total_display)
            self.wrapped.display()
    return newClass

@decorator
class Bird:
    def __init__(self, age):
        self.age = age
    def display(self):
        print("my age is", self.age)

engle = Bird(5)
for i in range(3):
    engle.display()

