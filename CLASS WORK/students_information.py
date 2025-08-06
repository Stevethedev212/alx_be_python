#students information
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def student_info(self):
        # Display the student's information
       print(f"My name is {self.name} and I am {self.age} years old.")
    # Create an instance (object) of Student
student1 = Student("Stephen", 20)

# Call the method to display the student's info
student1.student_info()