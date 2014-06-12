#without context manager
f = open("test.txt", "w")
print(f.closed)
f.write("hello")
f.close()
print(f.closed)

#with context manager
with open("test.txt", "w") as f1:
    print(f1.closed)
    f1.write("ok")
print(f1.closed)

#customized object, used for context manager
class VOW(object):
    def __init__(self, text):
        self.text = text
    def __enter__(self):
        self.text = "I: " + self.text
    def __exit__(self, exc_type, exc_value, traceback):
        self.text = self.text + "!"

vow1 = VOW("!!!")
print vow1.text


with VOW("I'm fine") as myvow:
    print(myvow)


