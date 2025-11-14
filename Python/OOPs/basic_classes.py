"""Simple Student class demo

Creates two Student objects and displays their details.
"""

class Student:
	def __init__(self, name: str, age: int):
		self.name = name
		self.age = age

	def display(self) -> None:
		print(f"Name: {self.name}, Age: {self.age}")


def main() -> None:
	s1 = Student("Ayush Raj", 20)
	s2 = Student("Ronaldo", 22)

	s1.display()
	s2.display()


if __name__ == "__main__":
	main()
