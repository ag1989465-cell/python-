# Polymorphism in Python
#function overriding
class employee:
    def deginaation(self):
        print("degination=Employee")
class Teacher(employee):
    def deginaation(self):
        print("degination=Teacher")
t1=Teacher()
t1.deginaation()#function overriding
#Duck typing
#WALK LIKE A DUCK, QUACK LIKE A DUCK
class Teacher:
    def degination(self):
        print("degination=Teacher")
class Accountant:
    def degination(self):
        print("degination=Accountant")
t1=Teacher()
t1.deginaation()

a1=Accountant()
a1.deginaation()