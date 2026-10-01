# class employee:
#     start_time="10 am"
#     end_time="6 pm"
#     def change_time(self,new_end_time):
#         self.end_time=new_end_time
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age

#     def get_info(self):#instance method
#         print(f"Employee name is {self.name} & age is {self.age}")
# class manager(employee):#child class
#     def __init__(self, name, age, department):
#         self.department=department
#         super().__init__(name, age)
        

#     def get_info(self):#instance method
#         print(f"Manager name is {self.name} & age is {self.age} & department is {self.department}")
# m1=manager("John",30,"IT")
# m1.change_time("7 pm")
# print(m1.name,m1.start_time,"to",m1.end_time)

###################################
#multilevel inheritance
class employee:
    start_time="10 am"
    end_time="6 pm"
class Adminstaff(employee):
    def __init__(self,role):
        self.role=role
class Accountant(Adminstaff):
    def __init__(self, salary,role):
        self.salary=salary
        super().__init__(role)
acc1 =Accountant(50000,"CA")
print(acc1.salary,acc1.role,acc1.start_time,acc1.end_time)