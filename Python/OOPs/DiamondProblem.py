'''
Diamong Problem in Python OOPs

The Diamond Problem is a specific ambiguity that arises in Multiple Inheritance when a class inherits from two classes that define the same method, or when those two classes share a common base class.

It is called the "Diamond Problem" because the inheritance diagram looks like a diamond shape.


'''

class A:
    def show(self):
        print("Class A method called")
class B(A):
    def show(self):
        print("Class B method called")
class C(A):
    def show(self):
        print("Class C method called")

class D(B,C):
    pass

dobj = D()
dobj.show()
# In this example, class D inherits from both B and C, which in turn inherit from A.
# When we call the show method on an instance of D, Python uses the Method Resolution Order (MRO) to determine which show method to invoke.
# According to the MRO, Python will first look in D, then B, then C
# and finally A. Since B is listed before C in the inheritance list of D, the show method from B is called.
print(D.mro())
