'''
Rectangle then area and preimeter
area = l*b
perimeter = 2(l+B)
'''
class Rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return self.length * self.breadth
    
    def perimeter(self):
        return 2*(self.length * self.breadth)

# Main Section
if __name__ == "__main__":
    print("REctangle calculation program")
    
    rect1 = Rectangle(4,10)
    print(f"Area       :{rect1.area()}")
    print(f"Perimeter  :{rect1.perimeter()}")
    
    l = float(input("Enter lenght of rec2:"))
    b = float(input("Enter breadth of rec2:"))
    
    rect2 = Rectangle(l,b)
    print(f"Area             :{rect2.area()}")
    print(f"perimeter        :{rect2.perimeter()}")
