# print("Hello world")

# print("shailesh") #in-line print 


# print("shailesh \n yadav") #next line print

# print("""SDSFCDSC absbdkxcjanjcn sjkndx,mx nckdc
#       adclkjidlsamjl;kmcx;dasc
#       alkdjnclkjasm;oxlkcds;c

# """) #multi line print




# print("The multiplication of 5 & 3 is :",5*3)
# print(f'Sum of 5 & 3 is : {5+3}')



# x=1
# y=2
# z=6

# c=x+y

# d=z+y

# # print("The sum of ",z,"and",y,"is",d) # normal print statement
# print(f"The sum of {z} and {y} is {d}") # f-string

# x=10.5
# name='Shailesh'
# y=5.7
# print(type(x))
# print(type(name))
# print(type(y))

# x="10"
# y="10"
# # z=int(y)
# print(x==y)

# a=5
# b=3

# print(a<b)

# name="Shailesh"

# print(type(name))

# x=input("Enter your name : ")

# print("Hello",x)

# a=input("Enter first Namer:")
# b=input("Enter Second Last Name:")
# c=a+" "+b
# print("Full Name is :",c)

# a=float(input("Enter first number:"))
# b=float(input("Enter Second number:"))

# c=a+b

# print("The sum of two numbers is:",c)

#Operator in Python

#arithmetic operator

# x=10
# y=5
# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y)
# print(x%y)
# print(x**y)
# print(x//y)



#comparative operator

# x=10
# y=5
# print(x==y)
# print(x!=y)
# print(x>y)
# print(x<y)
# print(x>=y)
# print(x<=y)

#logical operator

# a=5
# b=6
# c=7

# # print(ab and c>b)
# print(a>b or c>a)
# print(a>b)

# x=True
# y=True

# print(x and y)
# print(x or y)
# print(not x)

#asignment operator 

# x=10
# y=5

# x+=y
# print(x)
# x-=y
# print(x)
# x*=y
# print(x)
# x/=y
# print(x)
# x%=y
# print(x)
# x**=y
# print(x)
# x//=y
# print(x)


# a=20.5
# b=3

# print(a//b)


#conditional statement if elif else

# weather="breezy"

# if weather=="Sunny":
#     print("Take Umbrella")
# elif weather=="breezy":
#     print("Take Jacket")
# else:
#     print("stay at home")

# marks=int(input("Enter your marks:"))  

# if marks>=90:
#     print("A")
# elif marks>=80:
#     print("B")
# elif marks>=70:
#     print("C")
# elif marks>=60:

#     print("D")
# else:
#     print("Fail")

# vehicle=input("Enter your vehicle: ")

# if vehicle in ("XUV","Sedan","Nano","Nexon","Bike"):
#     print("Its is a 4-wheel vehicle")
# elif vehicle in("Bullet","Apache","Splendor","Scooty"):
#     print("Its is a 2-wheel vehicle")
# else:
#     print("Unknown vehicle")

# marks=int(input("Enter your marks:"))

# if marks>=40:
#     if marks>=90:
#         print("A")
#     elif marks>=80:
#         print("B")
#     elif marks>=70:
#         print("C")
#     elif marks>=60:
#         print("D")
# else:
#     print("Fail")

# age=int(input("Enter your age:"))
# citizenship=input("Enter your citizenship:")

# if age>=18: 
#     if citizenship=="Indian":
#         print("Eligible for voting")
#     else:
#         print("Not Indian citizen")
# else:
#     print("Not eligible for voting")

# if age>=18 and citizenship=="Indian":
#     print("Eligible for voting")
# else:
#     print("Not eligible for voting")

# Institute=input("Enter your Institute:")

# if Institute=="NSTIW":
#     print("Welcome to NSTIW")
#     Trade=input("Enter your Trade:")
#     if Trade=="AIPA":
#         print("Lab no.15")
#     elif Trade=="COPA":
#         print("Lab no.13")
#     elif Trade=="EM":
#         print("Lab no.14")
#     elif Trade=="Cosmetology":
#         print("Lab no.7")
#     else:
#         print("Enter Valid Trade.")
# else:
#     print("Not a students on NSTIW")
# name="Shailesh"
# for i in range(4,11):
#     print(i)


# num=int(input("Enter your number:"))

# for i in range(1,11):
#     print(num,"X",i,"=",num*i)
# else:
#     print("Table Completetd.")


# for i in range (10):
#     print("* " * i)

# for i in "Shailesh":
#     print(i)

# for i in range(1,5):
#     print("Shailesh"+str(i)).

# for i in range(2,20,2):
#     print(i)
# else:
#     print("Even mumbers")

# num=5
# fact=1
# for i in range(1,num+1):
#     fact=fact*i
#     print(fact)

# num = int(input("Enter a number: "))
# fact = 1
# for i in range(1, num + 1):
#     fact = fact * i
# print("Factorial =", fact)

# for i in range(10,0,-1):
#     print(i)
# num=int(input("Enter your number:"))
# for i in range(1,num +1):
#     sq=i*i
#     print(sq)

# num=int(input("Enter your number:"))
# total=0
# for i in range(1,num+1):
#     total=total+i
#     print(total)

# num=int(input("Enter your number:"))

# while num>0:
#     print(num)
#     num-=1
# print("LOOP ENDS HERE")

# apple=10

# while apple>0:
#     print("Eat apple:",apple)
#     apple-=1
# print("Finished!")


# password=""

# while password !="Shailesh@1234":
#     password=input("Enter your password:")
# print("Login Successful")

# import time
# num=5

# while num>0:
#     print(num)
#     num-=1
#     time.sleep(2)
# print("Time's Up")

# x=1

# while x>0:
#     x +=1
#     print(x)

# money=0

# while money <1000:
#     money +=50
#     print("Added money:",money)
# print("Contribnution Done Rs.1000")

# classname=1

# while classname<=4:
#     print("Class:",classname)
#     if classname==1:
#         end=5
#     elif classname==2:
#         end=8
#     elif classname==3:
#         end=10
#     elif classname==4:
#         end=12
#     for i in range(1,end+1):
#         print(i,end=" ")
#     print("\nAttendance Done")

#     classname +=1
# print("Exit")

# import time
# for round in range(1,4):
#     print("Round:",round)
#     count=3
#     while count>0:
#         print("Countdown:",count)
#         count -=1
#         time.sleep(1)
#     print("Round:",round,"Completed!\nNext Round :")
# print("All round completed ! ") 

    
# for i in range(1,11):
#     if i==5:
#         continue
#     print(i,end=" ")    

#Atm Withdrawl
# user =1
# OriginalBalance={1:1000,2:5000,3:6000}
# while user<=3:
#     print("User:",user)
#     balance=OriginalBalance[user]
#     for i in range(1,4):
#         amount=int(input("Enter your amount:"))
#         if amount <=balance:
#             balance=balance+amount
#             print("Remaining Balance:",balance)
#         # else:
#         #     print("Insufficient Balance")
#     print("User:",user,"Transanction Completed")
#     user +=1

#Restaurant Bill

# customer=1

# while customer<=2:
#     print("Customer:",customer)
#     total=0
#     for i in range(1,4):
#         amount=int(input("Enter your amount:"))
#         total=total+amount
#     print("Total Bill:",total)
#     print("Next Customer")
#     customer +=1

#Loan AMount
# customer=1

# while customer <=2:
#     print("Customer:",customer)
#     LoanAmount=int(input("Enter your Loan Amount:"))
#     rate=int(input("Enter your rate:"))
#     year=int(input("Enter your year:"))
#     for i in range(year):
#         amount=LoanAmount*(rate/100)
#         LoanAmount=LoanAmount+amount
#     print("Loan Amount:",LoanAmount)
#     print("Next Customer")
#     customer +=1

# Transfer statement

# for i in range (1,11):
#     if i==3:
#         continue #skips the number 
#     if i==5:
#         continue
#     if i ==7:
#         continue

#     print(i)

# for i in range (1,11):
#     if i==5:
#         break
#     print(i)

# for i in range(1,10):
#    pass
#    for i in range(1,10):
#         print(i)
        
# for i in range(1,10):
#     if i==3:
#         pass
#     print(i)


def cude(a):
    return a**3
