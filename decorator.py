'''
Decorator
Decorator is very powerful and useful tool in Python as it allows us to wrap another function in order to extend the behavior of wrapped function without permanently modifying it.
In Decorators functions are taken as the argument into another function and then called inside the wrapper function.
Advantages -

Logging & debugging
Access control and authentication
'''
def subtract(num1 , num2): res = num1 - num2
print('Result is :- ', res)

subtract(4,2) subtract(2,4)
-------------------------------------------------------------------------
''' We now want subtract() function to always subtract lower number from higher So when we pass (2,4) it should perform 4-2 not 2-4. To acheive this we will


def sub_decorator(func):
def wrapper(num1,num2):
if num1 < num2:
num1,num2 = num2,num1
return func(num1,num2)
return wrapper
sub = sub_decorator(subtract) sub(2,4)
------------------------------------------------------------------------------------------
@sub_decorator	# we can use @ syntax for decorating a function in one step
def subtract(num1 , num2): res = num1 - num2
print('Result is :- ', res) subtract(2,4)
----------------------------------------------------------------------------------------------------
def InstallLinux():
print('Linux installation has started \n')

def InstallWindows():
print('Windows installation has started \n')

def InstallMac():
print('Mac installation has started \n')


InstallLinux() InstallWindows() InstallMac()

print()


''' Now suppose if we want to print message :- "Please accept terms & conditions then easy way will be to create one decorator function which will present th



def InstallDecorator(func):
def wrapper():
print('Please accept terms & conditions')
return func()
return wrapper()

@InstallDecorator	# we can use @ syntax for decorating a function in one step
def InstallLinux():
print('Linux installation has started \n')

@InstallDecorator
def InstallWindows():
print('Windows installation has started \n ')

@InstallDecorator
def InstallMac():
print('Mac installation has started \n')
-------------------------------------------------------------------------------------------------------------------
# Apply multiple decorator on a single function

def InstallDecorator1(func):
def wrapper():
print('Please accept terms & conditions...\n') func()
return wrapper

def InstallDecorator2(func):
def wrapper():
print('Please enter correct license key...\n')
return func()
return wrapper


def InstallDecorator3(func):
def wrapper():
print('Please enter partitioning choice...\n')
return func()
return wrapper

@InstallDecorator1 @InstallDecorator2 @InstallDecorator3 def InstallLinux():
print('Linux installation has started \n')

InstallLinux()
-----------------------------------------------------------------------------------------------
