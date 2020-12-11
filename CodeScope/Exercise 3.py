# Create a Student class and initialize it with name and roll number. Make methods to :
# 1. Display - It should display all information of the student.
# 2. setAge - It should assign age to student
# 3. setGrades - It should assign grades to the student.


class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number

    def display(self):
        print(f"Student: {self.name}\n"
              f"Roll Number: {self.roll_number}\n"
              f"Age: {self.age}\n"
              f"Grades: {self.grades}")

    def setAge(self, age):
        self.age = age

    def setGrades(self, *grades):
        self.grades = grades


andrew = Student("Andrew", 10)
andrew.setAge(20)
andrew.setGrades(50, 100, 75)
andrew.display()