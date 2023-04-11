#Oops = object oriented programming system
#class is a classification whereas obejct is a real world entity

#Defining a class
class test:
    pass
a = test()
print(type(a))

#Example-1
class pwskills:                             #pwskills is a class
    def welcome_msg(self):                  #welcome_msg is a method/function  
        print("Welcome to PwSkills")
rohan = pwskills() 
print(rohan.welcome_msg())                  #rohan is a variable
gaurav = pwskills()
print(gaurav.welcome_msg())

#Example-2
class pwskills1:
    def __init__(self,phone_number,email_id,student_id):                     #__init__ is a constructor
        self.phone_number = phone_number                                     #Self is not a reserve keyword but a pointer
        self.email_id = email_id
        self.student_id = student_id
    
    def return_student_details(self):
        return self.phone_number,self.email_id,self.student_id

rohan = pwskills1(123456789,"rohan@gmail.com",101)
print(rohan.return_student_details())
gaurav = pwskills1(987654321,"gaurav@gmail.com",102)
print(gaurav.return_student_details())
print(rohan.phone_number)

#Polymorphism (same entity behaves differntly under different circumstances)
class data_science:
    def syllabus(self):
        print("This is my syllabus for data science masters")

class web_dev:
    def syllabus(self):
        print("This is my syllabus for web dev")

def class_parcer(class_obj):
    for i in class_obj:
        i.syllabus()
 
data_science = data_science()
web_dev = web_dev()
class_obj = [data_science,web_dev]
print(class_parcer(class_obj))

#Encapsulation 

#Example-1
class test1:
    def __init__(self,a,b):
        self.a = a
        self.b = b

class car:
    def __init__(self,year,make,model,speed):
        self.__year = year                 #__ makes the variable hidden 
        self.__model = model
        self.__speed = 0
        self.__make = make
    def set_speed(self,speed):
        self.__speed = 0 if speed<0 else speed 
    def get_speed(self):
        return self.__speed

c = car(2021,"Toyota","Innova",12)
print(c._car__year)

#Example-2
class bank_account:
    def __init__(self,balance):
        self.__balance = balance
        
    def deposit (self,amount):
        self.__balance = self.__balance+ amount

    def withdraw(self,amount):
        if self.__balance >= amount:
            self.__balance = self.__balance - amount
            return True
        else:
            return False
    def get_balance(self):
        return self.__balance

sudh = bank_account(1000)
print(sudh.get_balance())
sudh.deposit(5000)
print(sudh.get_balance())
sudh.withdraw(300)
print(sudh.get_balance())

#Inheritance

#Example-1
class test2:
    def test_meth(self):
        return "this is my first class"

class child_test(test2):
    pass
child_test_obj = child_test()
print(child_test_obj.test_meth())

#Multilevel inheritance

#Example-2
class class1:
    def test_class1(self):
        return "This is a meth from class1"
class class2(class1):
    def test_class2(self):
        return "This is a meth from class2"
    
class class3(class2):
    pass
obj_class3 = class3()
print(obj_class3.test_class1())

#Example-3
class classs1:
    def test_class1():
        return "This is class-1"
class classs2:
    def test_class2():
        return "This is class-2"
class classs3(classs1,classs2):
    pass

obj_classs3 = classs3()
print(obj_class3.test_class1)  #we are able to call function from class-1 and class-2 also 
print(obj_class3.test_class2)

#Abstraction 
import abc                           #This module provides the infrastructure for defining abstract base classes (ABCs) in Python
class pwskills:
    @abc.abstractmethod             
    def student_details(self):
        pass
    @abc.abstractmethod
    def student_assignment(self):
        pass
    @abc.abstractmethod
    def student_marks(self):
        pass

class student_details(pwskills):
    def student_details(self):
        return "This is a method for taking student details"
    def student_assignment(self):
        return "This is a method for student assignment details"

class data_science_masters(pwskills):
    def student_details(self):
        return "This will return a student details for data science masters"
    def student_assignment(self):
        return "This will give you student assignment details for data science masters"

data_science_masters_obj = data_science_masters()
print(data_science_masters_obj.student_details())

student_details_obj = student_details()
print(student_details_obj.student_details())
