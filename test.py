
s1 = (2, 1.3, 'xxx') #tuple, unchangeble

s2 = [True, 5, '!']  #list

a = 1

def change_integer(a):
    a = a + 1
    return a

print change_integer(a)
print a


b = [1,2,3]

def change_list(b):
    #passed the pointer
    b[0] = b[0] + 1
    return b

print change_list(b)
print b


class Bird(object):
    have_feather = True
    way_of_repro = "egg"
    #first argument should be self when def a method!
    def move(self, dx, dy):
        position = [0,0]
        position[0] = position[0] + 1
        position[1] = position[1] + 1
        return position

summer = Bird()
print summer.way_of_repro

#inheritance
class chicken(Bird):
   way_of_move = "walk" 

class Human(object):
    laugh = 'haha'
    def __init__(self, input_gender):
        self.gender = input_gender
    def show_laugh(self):
        print self.laugh
    def laugh_3th(self):
        for i in range(3):
            self.show_laugh()
    def printG(self):
        print self.gender 

li_lei = Human("boy")          
li_lei.laugh_3th()
li_lei.printG()


