class bird(object):
    feather = True
'''
class chicken(bird):
    fly = False
    def __init__(self, age):
        self.age = age

summer = chicken(2)
print(bird.__dict__)
print(chicken.__dict__)
print(summer.__dict__)
'''
class chicken(bird):
    fly = False
    def __init__(self, age):
        self.age = age
    def getAdult(self):
        if self.age > 1.0: return True
        else: return False
    adult = property(getAdult)   # property is built-in
summer = chicken(2)

print(summer.adult)
summer.age = 0.5
print(summer.adult)
