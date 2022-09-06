import utiles
from utiles.util1 import inueron:


obj=inueron('sharavanaraj','tamilkidi',1995)
print(obj.yob1)
print(obj._Person2__name1)
print(obj._surname1)


class Person1:
    # no underscore its public and one underscore its protected and two underscore its private
    def __init__(self,name,surname,yob):
        self.__name1=name
        self._surname1=surname
        self.yob1=yob

shiv=Person1('shiv','rajkumar',1998)


print(shiv._surname1)
print(shiv._Person1__name1)ron