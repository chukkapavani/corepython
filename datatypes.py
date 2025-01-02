#Data Types
#Numeric
#Integer
val1 = 10 # Integer data type
print(val1)
print(type(val1)) # type of object
print(sys.getsizeof(val1)) # size of integer object in bytes
print(val1, " is Integer?", isinstance(val1, int)) # val1 is an instance of int


#Float

val2 = 92.78 # Float data type
print(val2)
print(type(val2)) # type of object
print(sys.getsizeof(val2)) # size of float object in bytes
print(val2, " is float?", isinstance(val2, float)) # Val2 is an instance of floa


#complex

val3 = 25 + 10j # Complex data type
print(val3)
print(type(val3)) # type of object
print(sys.getsizeof(val3)) # size of float object in bytes
print(val3, " is complex?", isinstance(val3, complex)) # val3 is an instance of

sys.getsizeof(int()) # size of integer object in bytes
sys.getsizeof(float()) # size of float object in bytes
sys.getsizeof(complex()) # size of complex object in bytes


#Boolean
bool1 = True
bool2 = False
print(type(bool1))
print(type(bool2))
isinstance(bool1, bool)

bool(None)
bool (False)


#Strings

#String Creation
str1 = "HELLO PYTHON"
print(str1)

mystr = 'Hello World' # Define string using single quotes
print(mystr)

mystr = "Hello World" # Define string using double quotes
print(mystr)

mystr = '''Hello
World '''	# Define string using triple quotes
print(mystr)

mystr = """Hello
World""" # Define string using triple quotes
print(mystr)

mystr = """Hello
World""" # Define string using triple quotes
print(mystr)


mystr2 = 'Woohoo '
 mystr2 = mystr2*5
 mystr2

len(mystr2) # Length of string








