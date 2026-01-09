# class GrandFather:
#     def house(self):
#         print("Grandfather's house")

# class Father(GrandFather):
#     def car(self):
#         print("Father's car")

# class Son(Father):
#     def bike(self):
#         print("Son's bike")

# s = Son()
# s.house()
# s.car()
# s.bike()

class Music:
    def play(self):
        print("Playing music")

class Sports:
    def game(self):
        print("Playing football")

class Student(Music, Sports):
    pass

s = Student()
s.play()
s.game()

