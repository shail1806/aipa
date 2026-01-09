
# f = open("abc.txt", "r")
# data = f.read()     
# print(data)
# f.close()

# f = open("abc.txt", "w")
# f.write("Hello students!\n")
# f.write("Welcome to file handling.\n")


# f = open("xyz.txt", "w")
# f.write("Hello students!\n")
# f.write("Welcome to file handling.\n")

# Task 5
# f = open("xyz.txt", "a")
# f.write("This is an added line.\n")
# f.close()


# with open("xyz.txt", "r") as f:
#     print(f.read())


# with open("xyz.txt", "r") as file:
#     lines = file.readlines()

# word = "This is an added line."
# with open("xyz.txt", "w") as file:
#     for line in lines:
#         if word not in line:
#             file.write(line)


# remove=1
# with open("xyz.txt", "r") as file:
#     lines = file.readlines()

# with open("xyz.txt", "w") as file:
#     for i, line in enumerate(lines):
#         if i != remove:
#             file.write(line)




# with open("xyz.txt", "r") as f:
#     print("First 5 chars:", f.read(5))
#     print("Pointer now at:", f.tell())
#     f.seek(0)  # move pointer to start
#     print("After seek:", f.readline())

#Directory 

import os

# # Create a folder named "myfolder"
os.mkdir("myfolder/subfolder")
# print("Folder created successfully!")

# os.rename("myfolder", "newfolder")
# print("Folder renamed successfully!")

# os.rmdir("newfolder")
# print("Folder deleted successfully!")

# # List files in the current directory
# files = os.listdir()
# print("Files in the current directory:", files)

# # Get the current working directory
# cwd = os.getcwd()
# print("Current working directory:", cwd)

# # Change the current working directory
# os.chdir("/path/to/new/directory")
# print("Current working directory changed to:", os.getcwd())

# import os

# # First, create a folder
# os.mkdir("notes")

# # Create a file inside folder and write text
# with open("notes/myfile.txt", "w") as f:
#     f.write("Hello Students, welcome to Python!")
    

# print("File created and written successfully!")


