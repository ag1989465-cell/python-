# class Laptop:
#     storage_type="ssd"

#     def __init__(self,RAM,storage):
#         self.RAM=RAM
#         self.storage=storage

#     def get_info(self):#instance method
#         print(f"laptop has {self.RAM} RAM & {self.storage} {self.storage_type} ")

# l1=Laptop("16gb","512gb")
# l2=Laptop("8gb","256gb")
# l1.get_info()


###########################################################################
# class Laptop:
#     storage_type="ssd"

#     def __init__(self,RAM,storage):
#         self.RAM=RAM
#         self.storage=storage
#     @classmethod          #decorator
#     def get_storage_type(cls):
#        print(f"storage type = {cls.storage_type}")

#     def get_info(self):#instance method
#         print(f"laptop has {self.RAM} RAM & {self.storage} {self.storage_type} ")

#     @staticmethod
#     def calc_discount(price,discount):
#         Final_price=price-(discount* price /100)
#         printf(f"Discount price ={Final_price}")


# l1=Laptop("16gb","512gb")
# Laptop.get_storage_type()
# l1.get_storage_type()


#######################################################
class Laptop:
    storage_type="ssd"

    def __init__(self,RAM,storage):
        self.RAM=RAM
        self.storage=storage

    @staticmethod
    def calc_discount(price,discount):
        Final_price=price-(discount* price /100)
        print(f"Discount price ={Final_price}")


    def get_info(self):#instance method
        print(f"laptop has {self.RAM} RAM & {self.storage} {self.storage_type} ")

l1=Laptop("16gb","512gb")

l1.calc_discount(40_000,10) #40_000=40000