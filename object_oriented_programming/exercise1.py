class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"{self.name} has been created. Age: {self.age}")

    def __del__(self):
        print(f"Goodbye, {self.name}!")
