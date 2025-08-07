# Base class
class Animal:
    def eat(self):
        print("This animal is eating.")

    def sleep(self):
        print("This animal is sleeping.")

# Subclass
class Dog(Animal):
    def bark(self):
        print("The dog is barking.")

# Creating instances
animal1 = Animal()
dog1 = Dog()

# Demonstrate Animal methods
print("Animal instance:")
animal1.eat()
animal1.sleep()

print("\nDog instance:")
dog1.eat()      # Inherited from Animal
dog1.sleep()    # Inherited from Animal
dog1.bark()     # Defined in Dog
