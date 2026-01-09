# def add(a,b):
#     return a+b

# print(add(10,5))

# print(add(10,156))

# def aipa():
#     print("Prayagraj is a state in Uttar Pradesh")
# aipa()

# aipa("Prayagraj","Uttar Pradesh")
# x="Is a state in "
# print(aipa("Prayagraj is a state in ","Uttar Pradesh"))

# def sub(a,b):
#     return a-b

# sub(10,5)

# print(sub(10,5))

# x=3
# y=12
# z=x+y

# add(3+12)


# def div(a,b):
#     if b!=0:
#         return a/b
#     else:
#         return "0"
# print(div(10,0))


# def multi(a,b):
#     return a*b

# print(multi(10,6))

# def div(a,b):
#     return a/b

# print(div(10,0))
# import shailesh

# print(shailesh.cude(8))


# print(add(10,5))
# print(sub(10,5))
# print(div(10,5))
# print(multi(10,5))

# def xyz(*args):
#     print("Trade List")
#     for i in args:
#         print(i)
# xyz("AIPA","COPA","EM","Cosmetology")

# def abc(*args):
#     print("Sum of marks: ")
#     sum=0
#     for i in args:
#         sum+=i
#     return sum


# num=input("Enter your number:")

# added_list=[int(x) for x in num.split()]
# print(abc(*added_list))

# def student_info(**kwargs):
#     print("Student Details:")
#     for key, value in kwargs.items():
#         print(key , value)


# student_info(name="Adit", age=20, course="Python", city="Prayagraj")


# def Largest(*args):
#     return max(args)

# large=input("Enter number:")
# ln=[int(x)for x in large.split()]
# print(Largest(*ln))

# def avg(*args):
#     average=sum(args)/len(args)
#     return average
# num=input("Enter Numbers")
# final_avg=[int(x) for x in num.split()]
# print(avg(*final_avg))


# def mix(nsti,opening=1992,*trade,**details):
#     print(nsti)
#     print(opening)
#     if trade:
#         print("Tades in Nsti:",trade)
#     if details:
#         for key,value in details.items():
#             print(key,value)
# mix("NSTI",1992,"AIPA","COPA","EM","Cosmetology",phone=9876543210,pin=212002,email="nstiwallahabad@gmail.com")



# college="NSTIW"
# def globals():
#     college="Allahabad"
#     print(college)

# globals()
# print(college)

# name="Shailesh "
# def gk():
#     global name
#     name="Yash"
#     print(name)
# gk()
# print(name)

# for num in range(2, 20):
#     # Assume number is prime until shown it is not
#     is_prime = True
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num)

# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)
# num=int(input("Enter number:"))
# print("factorial of",num,"is:",factorial(num))
