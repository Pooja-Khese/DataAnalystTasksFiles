class Student:
    
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new student in database")
    

#Creating an instance outside the class
s1 = Student("Karan", 95)
print(s1.name, s1.marks)

s2 = Student("Manasi", 87)
print(s2.name, s2.marks)

# class Car:
#     Color = "Blue"
#     Brand = "Mercedes"

# car1 = Car()
# print(car1.Color)
# print(car1.Brand)