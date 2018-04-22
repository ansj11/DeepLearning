class MyBaseClass(object):
    def __init__(self,value):
        self.value=value

class TimesTwo(object):
    def __init__(self):
        self.value *=2

class PlusFive(object):
    def __init__(self):
        self.value += 5

class OneWay(MyBaseClass,TimesTwo,PlusFive):
    def __init__(self,value):
        MyBaseClass.__init__(self,value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)

foo = OneWay(5)
print(foo.value)

class AnotherWay(MyBaseClass,PlusFive,TimesTwo):
    def __init__(self,value):
        MyBaseClass.__init__(self,value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)

foo2=AnotherWay(5)
print(foo2.value)
