import sys
class A123():
    def abc(self):
        print(123)

class C123():
    def abc1(self):
        print(123)

class B123(A123, C123):
    def __init__(self):
        print([func for func in dir(__class__.__name__) if not func.startswith("__")])
        print([func for func in dir(B123) if  not func.startswith("__")])
        def bbc(self):
            print(1)

B123()
