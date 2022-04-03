from ursina import *

class TestClass:
    def __init__(self, **kwargs):
        self.hp = 10

    def get_a(self):
        return 'a'


    def get_b(self):
        return 'b'
    def set_b(self, value):
        print('set b to:', value)


    def set_hp(self, value):
        print('set hp')



print([e for e in dir(TestClass) if not e.startswith('__')])

e = TestClass()
print(e.a)
print(e.b)
e.b = 2
print(e.b)

print(e.hp)