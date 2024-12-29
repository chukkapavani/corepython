#Tuples
'''
1.	Tuple is similar to List except that the objects in tuple are immutable which means we cannot change the elements of a tuple once assigned.
2.	When we do not want to change the data over time, tuple is a preferred data type.
3.	Iterating over the elements of a tuple is faster compared to iterating over a list.

'''
#Tuple Creation
tup1 = ()	# Empty tuple
tup2 = (10,30,60)	# tuple of integers numbers
tup3 = (10.77,30.66,60.89)	# tuple of float numbers
tup4 = ('one','two' , "three")	# tuple of strings
tup5 = ('Asif', 25 ,(50, 100),(150, 90))	# Nested tuples
tup6 = (100, 'Asif', 17.765)	# Tuple of mixed data types
tup7 = ('Asif', 25 ,[50, 100],[150, 90] , {'John' , 'David'} , (99,22,33))
len(tup7) #Length of list

#Tuple Indexing
tup2[0] # Retreive first element of the tuple
tup4[0] # Retreive first element of the tuple
tup4[0][0] # Nested indexing - Access the first character of the first tuple ele
tup4[-1] # Last item of the tuple
tup5[-1] # Last item of the tuple


#Tuple Slicing
mytuple = ('one' , 'two' , 'three' , 'four' , 'five' , 'six' , 'seven' , 'eight')
mytuple[0:3] # Return all items from 0th to 3rd index location excluding the ite
mytuple[2:5] # List all items from 2nd to 5th index location excluding the item
mytuple[:3] # Return first three items
mytuple[:2] # Return first two items
mytuple[-3:] # Return last three items
mytuple[-2:] # Return last two items
mytuple[-1] # Return last item of the tuple
mytuple[:] # Return whole tuple

#Remove & Change Items
mytuple
del mytuple[0] # Tuples are immutable which means we can't DELETE tuple items
mytuple[0] = 1 # Tuples are immutable which means we can't CHANGE tuple items
del mytuple # Deleting entire tuple object is possible



#Loop through a tuple
mytuple
for i in mytuple: 
 print(i)
for i in enumerate(mytuple): 
 print(i)


#count
mytuple1 =('one', 'two', 'three', 'four', 'one', 'one', 'two', 'three')
mytuple1.count('one') # Number of times item "one" occurred in the tuple.
mytuple1.count('two') # Occurence of item 'two' in the tuple
mytuple1.count('four') #Occurence of item 'four' in the tuple

#Tuple Membership
mytuple
'one' in mytuple # Check if 'one' exist in the list
'ten' in mytuple # Check if 'ten' exist in the list

if 'three' in mytuple: # Check if 'three' exist in the list
print('Three is present in the tuple')
else:
print('Three is not present in the tuple')


if 'eleven' in mytuple: # Check if 'eleven' exist in the list
print('eleven is present in the tuple')
else:
print('eleven is not present in the tuple')

#Index Position
mytuple
mytuple.index('one') # Index of first element equal to 'one'
mytuple.index('five') # Index of first element equal to 'five'
mytuple1
mytuple1.index('one') # Index of first element equal to 'one'

#Sorting
mytuple2 = (43,67,99,12,6,90,67)
sorted(mytuple2) # Returns a new sorted list and doesn't change original tuple
sorted(mytuple2, reverse=True) # Sort in descending order











