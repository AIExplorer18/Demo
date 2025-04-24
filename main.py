class Student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    def display_info(self):
        return f"Name:{self.name} \nAge:{self.age}\nGrade:{self.grade}"
s1 = Student("hassan",12,"d")
print(s1.display_info())
