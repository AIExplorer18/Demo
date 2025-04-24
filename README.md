# Student Class Example

This is my first repository on GitHub. 🎉  
It includes a simple example of a Python class named `Student` that stores and displays student information.

## 🧠 What This Code Does

+ Defines a `Student` class with attributes:
  - `name`
  - `age`
  - `grade`
- Uses a `display_info()` method to neatly return the student's information.
- Creates an instance of `Student` and prints the info.

## 🧾 Code Example

```
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        return f"Name: {self.name} \nAge: {self.age}\nGrade: {self.grade}"

s1 = Student("hassan", 12, "d")
print(s1.display_info())
```
# 🖨 Output

Name: hassan 
Age: 12
Grade: d

