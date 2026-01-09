# class Animal:
#     def sound(self):
#         return "Some generic sound"

# class Dog(Animal):
#     def sound(self):
#         return "Bark"

# class Cat(Animal):
#     def sound(self):
#         return "Meow"

# animals = [ Cat(), Animal()]
# for animal in animals:
#     print(animal.sound())

class Vehicle:
    def start(self):
        print("Vehicle is starting")

class Bike(Vehicle):
    def start(self):
        print("Bike is starting with self start")

class Car(Vehicle):
    def start(self):
        print("Car is starting with push button")

v = Vehicle()
b = Bike()
c = Car()

v.start()
b.start()
c.start()

# class Teacher:
#     def work(self):
#         print("Teaches students")

# class Doctor:
#     def work(self):
#         print("Treats patients")

# class Engineer:
#     def work(self):
#         print("Builds software")

# people = [Teacher(), Doctor(), Engineer()]

# for p in people:
#     p.work()
