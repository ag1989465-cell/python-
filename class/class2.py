# create a class laptop with attrributes: brand ,ram ,price
# create 2 object with different values
class laptop:
    brand="default"
    ram="8 Gb"
    price="4500"
    def __init__(self,name):
        self.name=name
        print("inside init function")
l1=laptop("raju")
l1.brand="hp"
l1.price=5200
print(l1.name)
print(l1.brand)
print(l1.price)
print(l1.ram)

l2=laptop("suresh")
print(l2.brand)
print(l2.price)
print(l2.ram)
print(l1.brand)
