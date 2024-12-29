#sets
'''
1)	Unordered & Unindexed collection of items.

2)	Set elements are unique. Duplicate elements are not allowed.

3)	Set elements are immutable (cannot be changed).

4)	Set itself is mutable. We can add or remove items from it.
'''
#Set Creation
myset = {1,2,3,4,5} # Set of numbers
myset
len(myset) #Length of the set
my_set = {1,1,2,2,3,4,5,5}
my_set	# Duplicate elements are not allowed.
myset1 = {1.79,2.08,3.99,4.56,5.45} # Set of float numbers
myset1
myset2 = {'Asif' , 'John' , 'Tyrion'} # Set of Strings
myset2
myset3 = {10,20, "Hola", (11, 22, 32)} # Mixed datatypes
myset3
myset3 = {10,20, "Hola", [11, 22, 32]} # set doesn't allow mutable items like li
myset3
myset4 = set() # Create an empty set
print(type(myset4))
my_set1 = set(('one' , 'two' , 'three' , 'four'))
 my_set1

#Loop through a Set
myset = {'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight'}
for i in myset: 
print(i)

for i in enumerate(myset): 
 print(i)

#Set Membership
myset
'one' in myset # Check if 'one' exist in the set
'ten' in myset # Check if 'ten' exist in the set

if 'three' in myset: # Check if 'three' exist in the set
print('Three is present in the set')
else:
print('Three is not present in the set')

if 'eleven' in myset: # Check if 'eleven' exist in the list
print('eleven is present in the set')
else:
print('eleven is not present in the set')

#Add & Remove Items
myset
myset.add('NINE') # Add item to a set using add() method
myset
myset.update(['TEN' , 'ELEVEN' , 'TWELVE']) # Add multiple item to a set using
myset
myset.remove('NINE') # remove item in a set using remove() method
myset
myset.discard('TEN') # remove item from a set using discard() method
myset
myset.clear() # Delete all items in a set
myset
del myset # Delete the set object
myset


#Copy Set
myset = {'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight'} 
myset
myset1 = myset # Create a new reference "myset1"
myset1
id(myset) , id(myset1) # The address of both myset & myset1 will be the same as
my_set = myset.copy() # Create a copy of the list
my_set
id(my_set) # The address of my_set will be different from myset because my_set 
myset.add('nine')
 myset
myset1 # myset1 will be also impacted as it is pointing to the same Set
my_set # Copy of the set won't be impacted due to changes made on the original


#Set Operation
#Union
A = {1,2,3,4,5}
B = {4,5,6,7,8}
C = {8,9,10}
A | B # Union of A and B (All elements from both sets. NO DUPLICATES)
A.union(B) # Union of A and B
A.union(B, C) # Union of A, B and C.
"""
Updates the set calling the update() method with union of A , B & C.

For below example Set A will be updated with union of A,B & C. """
A.update(B,C) A

#Intersection
A = {1,2,3,4,5}
B = {4,5,6,7,8}
A & B # Intersection of A and B (Common items in both sets)

"""
Updates the set calling the intersection_update() method with the intersection o

For below example Set A will be updated	with the intersection of A & B. """
A.intersection_update(B) A


#Difference
A = {1,2,3,4,5}
B = {4,5,6,7,8}
A - B # set of elements that are only in A but not in B
A.difference(B) # Difference of sets
B- A # set of elements that are only in B but not in A
B.difference(A)

"""
Updates the set calling the difference_update() method with the difference of se

For below example Set B will be updated	with the difference of B & A. """
B.difference_update(A) B


#Symmetric Difference
A = {1,2,3,4,5}
B = {4,5,6,7,8}
A ^ B # Symmetric difference (Set of elements in A and B but not in both.
A.symmetric_difference(B) # Symmetric difference of sets

"""
Updates the set calling the symmetric_difference_update() method with the symmet

For below example Set A will be updated	with the symmetric difference of A & B. """
A.symmetric_difference_update(B) A


#Subset , Superset & Disjoint
A = {1,2,3,4,5,6,7,8,9}
B = {3,4,5,6,7,8}
C = {10,20,30,40}
B.issubset(A) 
A.issuperset(B) 
C.isdisjoint(A) 
B.isdisjoint(A) 


#Other Builtin functions
A
sum(A)
max(A)
min(A)
len(A)
list(enumerate(A))
D= sorted(A,reverse=True) 
D
sorted(D)