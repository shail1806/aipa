# import math

# print(math.pi)
# print(math.sqrt(16))

# import datetime

# now = datetime.datetime.now()
# print("Current:", now)
# print("Year:", now.year)
# print("Month:", now.month)
# print("Day:", now.day)

# today = datetime.date.today()
# print("Today's Date:", today)

# future = today + datetime.timedelta(days=10) 
# print("10 days later:", future) 

# import sys

# print("Python Version:", sys.version)
# print("Executable Path:", sys.executable)
# print("Platform:", sys.platform)


# import random

# # print(random.randint(1, 10))                   # Random integer
# # print(random.random())                         # Random float (0–1)
# # print(random.choice(['Red', 'Green', 'Blue'])) # Random choice from list
# colors = ['Red', 'Green', 'Blue']
# random.shuffle(colors)                         # Shuffle the list
# print(colors)

# import os

# print("Current Directory:", os.getcwd())
# print("Files:", os.listdir())
# os.mkdir("test_folder")   # Create folder
# os.rmdir("test_folder")   # Remove folder

# import time

# print("Current Time:", time.ctime())
# time.sleep(2)    # Pause for 2 seconds
# print("Done waiting!")


# def main():
#     # Task 1: Choose an arithmetic operation
#     print("Choose an operation:")
#     print("1. Addition (+)")
#     print("2. Subtraction (-)")
#     print("3. Multiplication (*)")
#     print("4. Division (/)")

#     choice = input("Enter your choice (1/2/3/4): ")

#     # Task 2: Input two numbers
#     num1 = float(input("Enter first number: "))
#     num2 = float(input("Enter second number: "))

#     # Task 3: Perform operation and display result
#     if choice == '1':
#         result = num1 + num2
#         print(f"The result of addition is: {result}")

#     elif choice == '2':
#         result = num1 - num2
#         print(f"The result of subtraction is: {result}")

#     elif choice == '3':
#         result = num1 * num2
#         print(f"The result of multiplication is: {result}")

#     elif choice == '4':
#         if num2 != 0:
#             result = num1 / num2
#             print(f"The result of division is: {result}")
#         else:
#             print("Error! Division by zero is not allowed.")
#     else:
#         print("Invalid choice! Please select a valid operation.")


# # Calling main function
# if __name__ == "__main__":
#     main()

# import datetime
# import calendar

# day_names=datetime.date.today().weekday()
# day_name=calendar.day_name[day_names]
# print(day_name)

# try:
#     num = int(input("Enter a number: "))
#     print(10 / num)
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# except ValueError:
#     print("Please enter a valid number.")

# class InvalidAgeError(Exception):
#     pass

# try:
#     age = int(input("Enter your age: "))
#     if age < 18:
#         raise InvalidAgeError("You must be 18 or older to register.")
#     print("Registration successful!")
# except InvalidAgeError as e:
#     print("Error:", e)

# class nstiadmission(Exception):
#     pass
# try:
#     x=int(input("enter qualification"))
#     if x<12:
#         raise nstiadmission("you are not eligible for admission")
#     else:
#         print("you are eligible for admission")
# except nstiadmission as shail:
#     print("reason:",shail)


# Step 1: Create a user-defined exception
# class NstiAdmission(Exception):
#     """Raised when Aadhaar number is not 12 digits"""
#     pass

# try:
#     aadhaar = input("Enter your Aadhaar number: ")
#     if len(aadhaar) != 12 :
#         raise NstiAdmission("Invalid Aadhaar number! It must be a 12-digit numeric value.")
#     else:
#         print("Aadhaar number accepted. You are eligible for admission.")

# except NstiAdmission as shail:
#     print("Reason:", shail)
    

