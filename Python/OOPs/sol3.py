'''
Define a class car with attributes brand mdoel and price. 
Add a method display info() to print car details
'''

class Car:
    def __init__(self, brand, model, price):
        # Init attributes of the car
        self.brand = brand
        self.model = model
        self.price = price
    
    def display_info(self):             # Method to display car details
        print(f"Car Brand: {self.brand}")
        print(f"Car Model: {self.model}")
        print(f"Car Price: ${self.price:,.2f}")

# Example usage
if __name__ == "__main__":
    car = Car("Tesla", "Model S", 89999)
    
    # car details
    car.display_info()