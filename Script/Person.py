class Person(object):
    def __init__(self, name, age, high):
        self._name = name
        self._age = age
        self._high = high

    # 访问器 -getter方法
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def high(self):
        return self._high

    # 修改器 setter

    @name.setter
    def name(self, name):
        self._name = 'name:' + name

    @age.setter
    def age(self, age):
        self._age = 11 + age

    @high.setter
    def high(self, high):
        self._high = 100 + high

    @staticmethod
    def printpersondata():
        print('this is static method')
