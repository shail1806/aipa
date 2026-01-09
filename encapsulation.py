# class BankAccount:
#     def __init__(self,name,balance):
#         self.name=name
#         self.__balance=balance

#     def add_amount(self,amount):
#         self.__balance += amount

#     def withdraw(self,amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#     def show_balance(self):
#         return self.__balance

# x=BankAccount("shailesh",1000) 

# x.add_amount(300)

# x.withdraw(500)
# print(x.show_balance())



class ATM:
    def __init__(self,pin,balance):
        self.__pin=pin
        self.__balance=balance
    def check_balance(self,pin):
        if pin == self.__pin:
            return self.__balance
        else:
            return "Incorrect Pin"

x=ATM(1806,15000)
print(x.check_balance(1806))