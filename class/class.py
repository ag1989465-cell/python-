# # class Dog:
# #     species = "Canine"  # Class attribute

# #     def __init__(self, name, age):
# #         self.name = name  # Instance attribute
# #         self.age = age  # Instance attribute

# # # Creating an object of the Dog class
# # dog1 = Dog("Buddy", 3)
# # print(dog1.name) 
# # print(dog1.species)


# class Animal:
#     legs ="animal must have 4 legs "   # Class attribute
#     eyes = 2  # Class attribute
#     def __init__(self, name):
#         self.name = name

#     def info(self):
#         print("Animal name:", self.name)

# class Dog(Animal):
#     def sound(self):
#         print(self.name, "sound barks")

# class Cat(Animal):
#     def sound(self):
#         print(self.name, "sound meows")
# s1=Dog("tommy")
# s1.sound()
# print(s1.legs)

# e=Cat("kitty")
# e.sound()
# # Inherited method  
# print (e.legs)
# e.info()




class father:
    def __init__(self):
        print("i am a father")
    def father(self):
        fathername=""  #not write father(self,fathername)--->child class
        print(self.fathername)
class mother:
    def __init__(self):
        print("this side mother here")
    def mother(self):
        self.mothername="gita"
        print(self.mothername)
class son(father,mother):
    def __init__(self):
        print("i am the son ")
    def parents(self):
        print("father",self.fathername)
        
s1=son()
s1.fathername="ram"
print(s1.fathername)


