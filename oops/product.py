class product:
    count=0
    def __init__(self,name,price):
        self.name=name
        self.price=price
        product.count +=1
        
    def get_detail(self):
        print(f"{self.name} is the product and price={self.price}")

    @classmethod
    def get_count(cls):
        print(f"the no product created ={cls.count}")

    @staticmethod
    def discount(price,discount):
        price=price-(price*discount/100)
        print(f"{price} this discount is occur ")
p1=product("samansung",50000)
p2=product("nokia",2000)
p2=product("realme",3000)
p2.get_detail()
product.get_count()
print(f"the total product has been created ={product.count}")
p1.discount(50000,10)
