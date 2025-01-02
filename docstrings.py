'''
Docstrings

1)	Docstrings provide a convenient way of associating documentation with functions, classes, methods or modules.
2)	They appear right after the definition of a function, method, class, or module.
'''
def square(num):
'''Square Function :- This function will return the square of a number'''
return num**2

square(2)

square.__doc__	  # We can access the Docstring using __doc__method

def evenodd(num):
'''evenodd Function :- This function will test whether a numbr is Even or Od
if num % 2 == 0:
print("Even Number")
else:
print("Odd Number")
evenodd(3)
evenodd(2)
evenodd.__doc__





