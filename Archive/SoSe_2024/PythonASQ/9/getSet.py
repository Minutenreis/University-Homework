
class foo:
    def __init__(self):
        self._x = 0

    @property
    def x(self):
        print('get foo')
        return self._x
    
    @x.setter
    def x(self, value):
        print('set foo')
        self._x = value
        
    @x.deleter
    def x(self):
        print('del foo')
        del self._x
        
class foo2:
    def __init__(self):
        self._x = 0

    def get_x(self):
        print('get foo2')
        return self._x
    
    def set_x(self, value):
        print('set foo2')
        self._x = value
        
    def del_x(self):
        print('del foo2')
        del self._x
        
    x = property(get_x, set_x, del_x)

x = foo()
x.x = 5
print(x.x)
del x.x

print()

x2 = foo2()
x2.x = 5
print(x2.x)
del x2.x

