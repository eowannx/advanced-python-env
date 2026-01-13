class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Encapsulation (private)

    def introduce(self):
        return f"Hi, I am {self.name}."

class Student(Person): # Inheritance
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self): # Overriding / Polymorphism
        return f"Hi, I am {self.name}, student ID: {self.student_id}."

def main():
    person = Person("John", 40)
    student = Student("Alice", 20, "S987")

    # Demonstrating polymorphism
    for member in [person, student]:
        print(member.introduce())

if __name__ == "__main__":
    main()