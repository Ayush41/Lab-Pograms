''' 
base calss person with constructor name,age method dispay()
subclass student inherites person


'''
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age  = age
        print("PErson constructor called")
    def display(self):
        print(f"Name   :{self.name}")
        print(f"Age    :{self.age}")

class Student(Person):
    def __init__(self,name,age,student_id):
        super().__init__(name,age)
        self.student_id = student_id
        print(">>Student constructor called")
        
    # Method overriding
    def display(self):
        print("--Student Detailes--")
        print(f"ID     :{self.student_id}")
        print(f"name   :{self.name}")
        print(f"Age    :{self.age}")
# main execution
if __name__ == "__main__":
    print("Initilaizing objects")
    s1 = Student("Rahul",20,"1103698")
    s2 = Student("Raj",21,"1103667")
    
    s1.display()
    s2.display()
