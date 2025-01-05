'''
Classes & Objects

  A Class is an object constructor or a "blueprint" for creating objects.
  Objects are nothing but an encapsulation of variables and functions into a single entity.   Objects get their variables and functions from classes.
  To create a class we use the keyword class.
  The first string inside the class is called docstring which gives the brief description about the class.
  All classes have a function called	which is always executed when the class is being initiated.
  We can use	function to assign values to object properties or other operations that are necessary to perform when the object is being created
  The self parameter is a reference to the current instance of the class and is used to access class variables.
  self must be the first parameter of any function in the class
  The super() builtin function returns a temporary object of the superclass that allows us to access methods of the base class.
  super() allows us to avoid using the base class name explicitly and to enable multiple inheritance.
'''
# Create a class with property "var1"
class myclass: var1 = 10

obj1 = myclass() # Create an object of class "myclass()"
print(obj1.var1)



# Create an employee class
class Employee:
def   init  (self, name, empid): #   init  () function is used to assign value
self.name = name
self.empid = empid
def greet(self): # Class Method
print("Thanks for joining ABC Company {}!!".format(self.name)) emp1 = Employee("Asif", 34163) # Create an employee object
print('Name :- ',emp1.name)
print('Employee ID :- ',emp1.empid) emp1.greet()



emp1.name = 'Basit' # Modify Object Properties
emp1.name


del emp1.empid	# Delete Object Properties
emp1.empid


del emp1 # Delete the object
emp1


emp2 = Employee("Michael", 34162) # Create an employee object
print('Name :- ',emp2.name)
print('Employee ID :- ',emp2.empid) emp2.greet()

emp2.country = 'India' #instance variable can be created manually
emp2.country




