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
    
# try:
#     print("Hello")
# except:
#     print("Error")

def main():
    try:
        print("Choose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")

        choice = input("Enter your choice (1/2/3/4): ")

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            result = num1 + num2
            print(f"The result of addition is: {result}")

        elif choice == '2':
            result = num1 - num2
            print(f"The result of subtraction is: {result}")

        elif choice == '3':
            result = num1 * num2
            print(f"The result of multiplication is: {result}")

        elif choice == '4':
            if num2==0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            result = num1 / num2
            print(f"The result of division is: {result}")

        else:
            print("Invalid choice! Please select a valid operation.")

    except ValueError:
        print("Error: Please enter valid numbers only.")

    except ZeroDivisionError as e:
        print(f"Error: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    else:
        print("Operation completed successfully!")

    finally:
        print("Program execution finished.")

if __name__ == "__main__":
    main()
