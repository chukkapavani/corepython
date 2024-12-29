#Variables-A Python variable is a reserved memory location to store values.A variable is created the moment you first assign a value to it.

p = 30

'''
id() function returns the “identity” of the object. The identity of an object - Is an integer
-	Guaranteed to be unique
-	Constant for this object during its lifetime.
'''
id(p)

hex(id(p)) # Memory address of the variable

p = 20 #Creates an integer object with value 20 and assigns the variable p to p
q = 20 # Create new reference q which will point to value 20. p & q will be poi
r = q # variable r will also point to the same location where p & q are pointin
p , type(p), hex(id(p)) # Variable P is pointing to memory location '0x7fff6d71a


q , type(q), hex(id(q))

r , type(r), hex(id(r))

p = 20
p = p + 10 # Variable Overwriting
p

#Variable Assigment
intvar = 10 # Integer variable
floatvar = 2.57 # Float Variable
strvar = "Python Language" # String variable

print(intvar)
print(floatvar) print(strvar)

#Multiple Assignments
intvar , floatvar , strvar = 10,2.57,"Python Language" # Using commas to separat
print(intvar)
print(floatvar) print(strvar)

p1 = p2 = p3 = p4 = 44 # All variables pointing to same value
print(p1,p2,p3,p4)





