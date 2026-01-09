# class Student:
#     def __init__(self, name):
#         self.name = name  # public variable

#     def display(self):
#         print("Student Name:", self.name)  # public method

# obj = Student("Adit")
# obj.display()
# print(obj.name)  # Accessible+



# class Student:
#     def __init__(self, name, marks):
#         self.name = name 
#         self._marks = marks  # protected variable

# class Result(Student):
#     def show(self):
#         print("Marks =", self._marks)

# obj = Result("Adit", 85)
# obj.show()
# print(obj.name)
# print(obj._marks)  # Allowed but not recommended

class AIPA:
    def __init__(self, name, tools,register):
        self.name = name 
        self._tools=tools
        self.__register=register

    def classregister(self):
        print("Access:", self.__register)

R=AIPA("AIPA","Almirah","Class Register")
R.classregister()
print(R.name,R._tools,R.__register)
