# class bankaccount:
#     def __init__(self,name,balance):
#         self.name=name # public 
#         self._balance=balance #protected (_balance)
#             # __balance=balance #private
#     def deposit(self,amount):
#         self._balance+=amount
#         print(f"Deposited {amount}. New balance is {self._balance}")

#     def withdraw(self,amount):
#         if amount>self._balance:
#             print("Insufficient balance")
#         else:
#             self._balance-=amount
#             print(f"Withdrew {amount}. New balance is {self._balance}")

#     def get_balance(self):# getter method
#         # print(f"Current balance is {self._balance}")
#         return self._balance
#     def set_balance(self,balance):# setter method
#         self._balance=balance
#         # print(f"Balance updated to {self._balance}")
# acc1=bankaccount("John",1000)
# print(acc1.name,acc1._balance) #accessing protected member  (not occur in c++,java)


#########################################################################
class bankaccount:
    def __init__(self,name,balance):
        self.name=name # public 
        self.__balance=balance #private - data mangling
    def get_balance(self):# getter method
        return self.__balance
    def set_balance(self,balance):# setter method
        self.__balance=balance
acc1=bankaccount("John",1000)
print(acc1.name,acc1.get_balance()) #accessing private member using getter method