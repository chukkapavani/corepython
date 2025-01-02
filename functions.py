#Functions
'''
  A function is a block of organized code written to carry out a specified task.
  Functions help break our program into smaller and modular chunks for better readability.   Information can be passed into a function as arguments.
  Parameters are specified after the function name inside the parentheses.
  We can add as many parameters as we want. Parameters must be separated with a comma.   A function may or may not return data.
  In Python a function is defined using the def keyword

Parameter VS Argument
  A parameter is the variable listed inside the parentheses in the function definition.   An argument is the value that is sent to the function when it is called.

Three types of functions in Python:-
  Built-in function :- Python predefined functions that are readily available for use like min() , max() , sum() , print() etc.
  User-Defined Functions:- Function that we define ourselves to perform a specific task.
  Anonymous functions : Function that is defined without a name. Anonymous functions are also called as lambda functions. They are not declared with the def keyword.
'''
'''
Syntax:def FunctionName(parameters):
	"""Function DocString"""
	statement(s)
	return[expression]
'''
def myfunc():
print("Hello Python Lovers")
myfunc()

def details(name,userid,country): # Function to print User details
print('Name :- ', name)
print('User ID is :- ', userid) print('Country :- ',country)
details('Asif' , 'asif123' , 'India')

def square (n): #function to find square of a number
n= n*n
return n
square (10)

def even_odd (num): #Even odd test
""" This function will check whether a number is even or odd"""
if num % 2 ==0:
print (num, ' is even number')
else:
print (num, ' is odd number')
even_odd(3) even_odd(4)
print(even_odd.  doc  ) # Print function documentation string

def fullname (firstname , middlename ,lastname): #Concatenate Strings
fullname = "{} {} {}".format(firstname,middlename,lastname) print (fullname)
fullname('Asif' , 'Ali' , 'Bhat')

def fullname (firstname , middlename ,lastname): #Concatenate Strings
fullname = "{} {} {}".format(firstname,middlename,lastname) print (fullname)
fullname(lastname = 'Bhat' , middlename='Ali' , firstname='Asif') # Keyword Argu

fullname ('Asif') # This will throw error as function is expecting 3 arguments.

def myfunc(city = 'Mumbai'):
print('Most Populous City :- ', city)
myfunc() # When a function is called without an argument it will use default val

var1 = 100 # Variable with Global scope.
def myfunc():
print(var1) # Value 100 will be displayed due to global scope of var1
myfunc()
print(var1)

def myfunc1():
var2 = 10 # Variable with Local scope
print(var2)
def myfunc2():
print(var2) # This will throw error because var2 has a local scope. Var2 is
myfunc1() myfunc2()

list1 = [11,22,33,44,55]
def myfunc(list1):
del list1[0]
print('"List1" before calling the function:- ',list1)
myfunc(list1) # Pass by reference (Any change in the parameter within the funct
print('"List1" after calling the function:- ',list1)


var1 = 100 # Variable with Global scope.
def myfunc():
var1 = 99 # Local scope
print(var1)
myfunc()
print(var1) # The original value of var1 (100) will be retained due to global sc

list1 = [11,22,33,44,55]
def myfunc(list1):
list1.append(100)
print('"List1" before calling the function:- ',list1)
myfunc(list1) # Pass by reference (Any change in the parameter within the funct
print('"List1" after calling the function:- ',list1)


list1 = [11,22,33,44,55]
def myfunc(list1):
list1 = [10,100,1000,10000] # link of 'list1' with previous object is broken
print('"List1" before calling the function:- ',list1)
myfunc(list1) # Pass by reference (Any change in the parameter within the funct
print('"List1" after calling the function:- ',list1)

def swap(a,b): temp = a
a = b	# link of 'a' with previous object is broken now as new object is
b = temp	# link of 'b' with previous object is broken now as new object is
a = 10
b = 20
swap(a,b) a,b

def factorial(num): # Calculate factorial of a number using recursive function
if num <=1 :
return 1
else:
return num * factorial(num-1)
factorial(4)

def add(num): # Sum of first n natural numbers
if num == 0:
return 0
else:
return num + add(num-1)
add(5) # Sum of first five natural numbers (1,2,3,4,5)

def fiboacci(num):
if num <= 1:
return num
if num == 2:
return 1
else:
return(fiboacci(num-1) + fiboacci(num-2))
nums = int(input("How many fibonacci numbers you want to generate -"))
for i in range(nums):
print(fiboacci(i)) # Generate Fibonacci series


