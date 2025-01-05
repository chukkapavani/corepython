'''
Error & Exception Handling

Python has many built-in exceptions (ArithmeticError, ZeroDivisionError, EOFError, IndexError, KeyError, SyntaxError, IndentationError, FileNotFoundError etc) that are raised when your program encounters an error.
When the exception occurs Python interpreter stops the current process and passes it to the calling process until it is handled. If exception is not handled the program will crash.
Exceptions in python can be handled using a try statement. The try block lets you test a block of code for errors.
The block of code which can raise an exception is placed inside the try clause. The code that will handle the exceptions is written in the except clause.
The finally code block will execute regardless of the result of the try and except blocks.

We can also use the else keyword to define a block of code to be executed if no exceptions were raised.
Python also allows us to create our own exceptions that can be raised from the program using the raise keyword and caught using the except clause. We can define what kind of error to raise, and the text to print to the user.
'''

try:
print(100/0) # ZeroDivisionError will be encountered here. So the control wi

except:
print(sys.exc_info()[1] , 'Exception occured') # This statement will be exec

else:
print('No exception occurred') # This will be skipped as code block inside t

finally:
print('Run this block of code always') # This will be always executed
-----------------------------------------------------------------------------------------------------
try:
print(x) # NameError exception will be encountered as variable x is not def

except:
print('Variable x is not defined')
--------------------------------------------------------------------------------------------
try:
os.remove("test3.txt") # FileNotFoundError will be encountered as "test3.txt
except:
print("BELOW EXCEPTION OCCURED")
print(sys.exc_info()[1])

else:
print('\nNo exception occurred')

finally:
print('\nRun this block of code always')
---------------------------------------------------------------------------------------------------
# Handling specific exceptions
try:
x = int(input('Enter first number :- '))
y = int(input('Enter first number :- ')) # If input entered is non-zero th
print(x/y)
os.remove("test3.txt")

except NameError:
print('NameError exception occurred')

except FileNotFoundError:
print('FileNotFoundError exception occurred')

except ZeroDivisionError:
print('ZeroDivisionError exception occurred')
----------------------------------------------------------------------------------------------
# Handling specific exceptions
try:
x = int(input('Enter first number :- '))
y = int(input('Enter first number :- ')) # If the input entered is zero the
print(x/y)
os.remove("test3.txt")

except NameError:
print('NameError exception occurred')

except FileNotFoundError:
print('FileNotFoundError exception occurred')

except ZeroDivisionError:
print('ZeroDivisionError exception occurred')
--------------------------------------------------------------------------------------------------
try:
x = int(input('Enter first number :- '))
if x > 50:
raise ValueError(x) # If value of x is greater than 50 ValueError except
except:
print(sys.exc_info()[0])
-----------------------------------------------------------------------------------------




#Built-in Exceptions
# OverflowError - This exception is raised when the result of a numeric calculat

try:
import math
print(math.exp(1000))
except OverflowError:
print (sys.exc_info())
else:
print ("Success, no error!")
-------------------------------------------------------------------------------------------------
# ZeroDivisionError - This exception is raised when the second operator in a div

try:
x = int(input('Enter first number :- ')) y = int(input('Enter first number :- ')) print(x/y)

except ZeroDivisionError:
print('ZeroDivisionError exception occurred')
----------------------------------------------------------------------------------------
# NameError - This exception is raised when a variable does not exist

try:
print(x1)

except NameError:
print('NameError exception occurred')
-----------------------------------------------------------------------------------------
# AssertionError - This exception is raised when an assert statement fails

try:
a = 50
b = "Asif"
assert a == b
except AssertionError:
print ("Assertion Exception Raised.")
----------------------------------------------------------------------------------------------
# ModuleNotFoundError - This exception is raised when an imported module does no

try:
import MyModule

except ModuleNotFoundError:
print ("ModuleNotFoundError Exception Raised.")
-----------------------------------------------------------------------------------
# KeyError - This exception is raised when key does not exist in a dictionary

try:
mydict = {1:'Asif', 2:'Basit', 3:'Michael'} print (mydict[4])

except KeyError:
print ("KeyError Exception Raised.")
------------------------------------------------------------------------------------------
# IndexError - This exception is raised when an index of a sequence does not exi

try:
mylist = [1,2,3,4,5,6] print (mylist[10])

except IndexError:
print ("IndexError Exception Raised.")
------------------------------------------------------------------------------------------------
# TypeError - This exception is raised when two different datatypes are combined

try:
a = 50
b = "Asif"
c = a/b
except TypeError:
print ("TypeError Exception Raised.")
---------------------------------------------------------------------------------------------------
# AttributeError: - This exception is raised when attribute reference or assignm

try:
a = 10
b = a.upper() print(b)
except AttributeError:
print ("AttributeError Exception Raised.")
-----------------------------------------------------------------------------------------------------------
try:
x = input('Enter first number :- ')


except:
print('ZeroDivisionError exception occurred')

