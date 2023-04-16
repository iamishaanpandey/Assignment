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

#Decorators
def testing():
    print("This is testing")

def deco(func):
    def inner_deco():
        print("This is the start of my function")
        func()
        print("This is the end of my function")
    return inner_deco

@deco
def testing1():
    print(6+7)
print(testing1())

import time
def timer_test(func):
    def timer_test_inner():
        start  = time.time()
        func()
        end = time.time()
        print(end-start)
    return timer_test_inner

@timer_test
def timer_test2():
    print(45+96)
print(timer_test2())


@timer_test
def time_test3():
    for i in range(100000):
        pass    

#Class-Methods
class pwskills:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        
    @classmethod                          #Pass data in a class without using __init__ method
    def details(cls,name,email):
        return cls(name,email)
    
    def student_details(self):
        print(self.name,self.email,)

pw = pwskills("Mohan","Mohan@gmail.com")
print(pw.student_details())

#Example-2
class pwskills4:

    mob_num = 9876543210                 #class variable

    def __init__(self,name,email):
        self.name = name
        self.email = email
        
    @classmethod
    def change_num(cls,mob_num1):
        pwskills4.mob_num = mob_num1
        
    @classmethod                    
    def details(cls,name,email):
        return cls(name,email)
    
    def student_details(self):
        print(self.name,self.email,pwskills4.mob_num)

pw_obj = pwskills4("Ishaan","Ishaan@gmail.com")
print(pw_obj.student_details())

pw = pwskills4.details("Rohan","Rohan@gmail.com")
print(pw_obj.student_details())

print(pwskills4.mob_num)
pwskills4.change_num(1234567890)
print(pwskills4.mob_num)

#Example-3
class pwskills3:

    mob_num = 9876543210                 #class variable

    def __init__(self,name,email):
        self.name = name
        self.email = email
        
    @classmethod
    def change_num(cls,mob_num1):
        pwskills4.mob_num = mob_num1
        
    @classmethod                    
    def details(cls,name,email):
        return cls(name,email)
    
    def student_details(self):
        print(self.name,self.email,pwskills4.mob_num)

def course_details(cls, course_name):
    print("Course name is", course_name)

pwskills3.course_details = classmethod(course_details)
print(pwskills3.course_details("data science masters"))

def mentor(cls , list_of_mentor):
    print(list_of_mentor)

pwskills3.mentor = classmethod(mentor)
print(pwskills3.mentor(["zulfikar","sugandha","annu singh"]))

del pwskills3.change_num                  #deletes a class_method
delattr(pwskills3 ,"student_details")     #deleting a class_method

#Static Method
class pwskills7:
    def student_details(self,name,mail_id,phone_num):
        print(name,mail_id,phone_num)

pw = pwskills7()
pw.student_details("Ishaan","Ishaan@gmail.com",9354740459)

#Example-2                                                    #Repeats same values for many objects. Reusability in increased 
class pwskills8:
    def student_details(self,name,mail_id,phone_num):
        print(name,mail_id,phone_num)

    @staticmethod
    def mentor_class(list_mentor):
        pwskills8.mentor_id(["sudh@gmail.com","krish@gmail.com"])
        print(list_mentor)
    
    @staticmethod
    def mentor_id(mail_mentor):
        print(mail_mentor)

    @classmethod
    def class_name(cls):
        cls.mentor_class()

pwskills8.mentor_class(["Sudh","Krish"])

#Special magic functions & dunder method
a = 100
a.__add__(5)

class pwskills9:
    
    def __new__(cls):
        print("This is my new")
    
    def __init__(self):
        self.mobile_number = 123456789
pw1 = pwskills9()

#Example-2
class pwskills10:
    
    def __init__(self):
        self.mobile_number = 123456789

    def __str__(self):
        return "This is magic call of str"
pw1 = pwskills10()
print(pw1)

#Property Decorators Getters, Setters, And Deletes
class pwskills11:
    def __init__(self,course_price,course_name):
        self.__course_price = course_price
        self.course_name = course_name

    @property
    def course_price_access(self):
        return self.__course_price
    
    @course_price_access.setter
    def course_price_set(self,price):
        if price<3500:
            pass
        else:
            self.__course_price = price

    @course_price_access.deleter
    def delete_course_price(self):
        del self.__course_price

pw11 = pwskills11(3700,"DSM")
pw11.course_price_set = 4500
print(pw11.course_price_access)




