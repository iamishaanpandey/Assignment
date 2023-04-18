#Exception Handling
try:
    f = open("texting.txt","r")
except Exception as e:              #Exception is a superclass
    print("this is my print")


#Example-2
try:
    f = open("texting.txt","w")
    f.write("This is my file")
except Exception as e:              
    print("this is my print")
else:                            #Else block only runs if try condition is satisfied
    f.close()
    print("This will be executed once the try block is executed")

#Example-3
try:
    f = open("texting2.txt","w")
    f.write("This is my file")
finally:                        #Finally will execute itself in any situation
    print("Finally will execute itself in any situation")

#Custom Exception Handling
#This code has error at line number 41. Exception not working. Please rectify the code
# class validateage(Exception):
#     def __init__(self, msg):
#         self.msg = msg
# def validateage(age):
#     if age<0 :
#         raise validateage("Entered age is negative")
#     elif age>200:
#         raise validateage("Entered age is very very high") 
#     else:
#         print("Age is valid")

# try:
#     age = int(input("enter your age"))
#     validateage(age)
# except validateage as e:
#     print(e)

#List of general use exceptions
try:
    a = 10/0
except ZeroDivisionError as e:
    print(e)

#Example-2
# try:
#     int("sudh")
# except TypeError as e:
#     print(e)

# #Example-3
# try:
#     int("sudh")
# except:
#     print("This will catch an error")

#Example-4
# try:
#     import sudh
# except ImportError as e:
#     print(e)
    
#Example-5
try:
    d = {"key1":"Ishaan","1":"Nikhil"}
    print(d["key2"])
except KeyError as e:
    print(e)

#Example-5
try:
    "Ishaan".test()
except AttributeError as e:
    print(e)

#Example-6
try:
    l = [1,2,3,4,5]
    print(l[6])
except IndexError as e:
    print(e)

#Example-7
try:
    123+"Ishaan"
except TypeError as e:
    print(e)

#Example-8
try:
    with open("text.txt", "r") as r:
        f.read()
except FileNotFoundError as e:
    print(e)

#Best Practice in exception handling

# 1) use always a specific exception 
try:
    10/0
except ZeroDivisionError as e:
    print(e)

# 2) Print always a proper message
try:
    10/0
except ZeroDivisionError as e:
    print("I am trying to handle a zero division error",e)

# 3) Always log your error
import logging
logging.basicConfig(filename="error.log",level=logging.ERROR)
try:
    10/0
except ZeroDivisionError as e:
    logging.info("I am trying to handle a zero division error",e)

# 4) Document all the error
# 5) Cleanup all the resources
try:
    with open("text.txt","w") as f:
        f.write("This is my data of the file")
except FileNotFoundError as e:
    logging.error("I am handling a file not found {}".format(e))
finally:
    f.close()

