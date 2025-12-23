'''
OOPS has four main principles:
1. Encapsulation
2. Abstraction
3. Inheritance
4. Polymorphism

Inheritance has different levels:
1. Single Level Inheritance
2. Multi Level Inheritance
3. Hierarchical Inheritance
4. Multiple Inheritance
5. Hybrid Inheritance

'''

# Single Level Inheritance:

# single level inheritence
class ParentA:
    def parentMethod(self):
        print("Parent Method")
        
class Child(ParentA):
    def childMethod(self):
        print("Child Method")
# creating objects
cobj = Child()
cobj.childMethod()
cobj.parentMethod()
print("\n")


# Multi Level Inheritance:
# A child inherits from a parent class, and then another class inherits from that child class.
class GrandParent:
    def grandParentMethod(self):
        print("Grand Parent Method")
class ParentB(GrandParent):
    def parentMethod(self):
        print("Parent Method")
class ChildB(ParentB):
    def childMethod(self):
        print("Child Method")
# creating objects
cbobj = ChildB()
cbobj.childMethod()
cbobj.parentMethod()
cbobj.grandParentMethod()
print("\n")

# Hierarchical Inheritance:
# Multiple classes inherit from a single parent class.
class ParentC:
    def parentMethod(self):
        print("Parent Method")
class ChildC1(ParentC):
    def child1Method(self):
        print("Child 1 Method")
class ChildC2(ParentC):
    def child2Method(self):
        print("Child 2 Method")
# creating objects
cc1obj = ChildC1()
cc1obj.child1Method()
cc1obj.parentMethod()
cc2obj = ChildC2()
cc2obj.child2Method()
cc2obj.parentMethod()
print("\n")

# Multiple Inheritance:
# A class inherits from more than one parent class.
class ParentD1:
    def parent1Method(self):
        print("Parent 1 Method")
class ParentD2:
    def parent2Method(self):
        print("Parent 2 Method")
class ChildD(ParentD1, ParentD2):
    def childMethod(self):
        print("Child Method")
# creating objects
cdobj = ChildD()
cdobj.childMethod()
cdobj.parent1Method()
cdobj.parent2Method()
print("\n")