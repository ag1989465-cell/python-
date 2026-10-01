class teacher:
    def __init__(self,salary):
        self.salary=salary
class student:
    def __init__(self,gpa):
        self.gpa=gpa
class teachingassistant(teacher,student):
    def __init__(self,salary,gpa,name):
        super().__init__(salary)
        student.__init__(self,gpa)
        self.name=name
ta1=teachingassistant(50000,3.5,"Anuj")
print(ta1.salary,ta1.gpa,ta1.name)