#List
'''
1)	List is an ordered sequence of items.

2)	We can have different data types under a list. E.g we can have integer, float and string items in a same list.
'''
#List Creation
list1 = []	# Empty List
print(type(list1))
list2 = [10,30,60]	# List of integers numbers
list3 = [10.77,30.66,60.89]	# List of float numbers
list4 = ['one','two' , "three"]	# List of strings
list5 = ['Asif', 25 ,[50, 100],[150, 90]]	# Nested Lists
list6 = [100, 'Asif', 17.765]	# List of mixed data types
list7 = ['Asif', 25 ,[50, 100],[150, 90] , {'John' , 'David'}]
len(list6) #Length of list
list2[0] # Retreive first element of the list
list4[0] # Retreive first element of the list
list4[0][0] # Nested indexing - Access the first character of the first list ele
list4[0][0] # Nested indexing - Access the first character of the first list ele
list5[-1] # Last item of the list

#List Slicing
mylist = ['one' , 'two' , 'three' , 'four' , 'five' , 'six' , 'seven' , 'eight']
mylist[0:3] # Return all items from 0th to 3rd index location excluding the item
mylist[2:5] # List all items from 2nd to 5th index location excluding the item 
mylist[:3] # Return first three items
mylist[:2] # Return first two items
mylist[-3:] # Return last three items
mylist[-2:] # Return last two items
mylist[-1] # Return last item of the list
mylist[:] # Return whole list


#Add , Remove & Change Items
mylist = ['one' , 'two' , 'three' , 'four' , 'five' , 'six' , 'seven' , 'eight']
mylist.append('nine') # Add an item to the end of the list
mylist
mylist.insert(9,'ten') # Add item at index location 9
mylist
mylist.insert(1,'ONE') # Add item at index location 1
mylist
mylist.remove('ONE') # Remove item "ONE"
mylist
mylist.pop() # Remove last item of the list
mylist
mylist.pop(8) # Remove item at index location 8
mylist
del mylist[7] # Remove item at index location 7
mylist
mylist.clear() # Empty List / Delete all items in the list
mylist
del mylist # Delete the whole list
mylist

#Copy List
mylist = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
mylist1 = mylist # Create a new reference "mylist1"
id(mylist) , id(mylist1) # The address of both mylist & mylist1 will be the same
mylist2 = mylist.copy() # Create a copy of the list
id(mylist2) # The address of mylist2 will be different from mylist because mylist
mylist[0] = 1
mylist
mylist1 # mylist1 will be also impacted as it is pointing to the same list
mylist2 # Copy of list won't be impacted due to changes made on the original lis


#join lists
list1 = ['one', 'two', 'three', 'four']
list2 = ['five', 'six', 'seven', 'eight']
list3 = list1 + list2 # Join two lists by '+' operator
list3

list1.extend(list2) #Append list2 with list1
list1


#List Membership
list1
'one' in list1 # Check if 'one' exist in the list
'ten' in list1 # Check if 'ten' exist in the list

if 'three' in list1: # Check if 'three' exist in the list
print('Three is present in the list')
else:
print('Three is not present in the list')

print('eleven is present in the list')
else:
print('eleven is not present in the list')


#Reverse & Sort List
list1
list1.reverse() # Reverse the list
list1
list1 = list1[::-1] # Reverse the list
list1
mylist3 = [9,5,2,99,12,88,34]
mylist3.sort()	# Sort list in ascending order
mylist3
mylist3 = [9,5,2,99,12,88,34]
mylist3.sort(reverse=True) # Sort list in descending order
mylist3


#Loop through a list
list1
for i in list1: 
  print(i)
for i in enumerate(list1): 
   print(i)

#Count
list10 =['one', 'two', 'three', 'four', 'one', 'one', 'two', 'three']
list10.count('one') # Number of times item "one" occurred in the list.
list10.count('two') # Occurence of item 'two' in the list
list10.count('four') #Occurence of item 'four' in the list

#All / Any
'''

The all() method returns:

  True - If all elements in a list are true
  False - If any element in a list is false

The any() function returns True if any element in the list is True. If not, any() returns False.

'''
L1 = [1,2,3,4,0]
all(L1) # Will Return false as one value is false (Value 0)
any(L1) # Will Return True as we have items in the list with True value
L2 = [1,2,3,4,True,False]
all(L2) # Returns false as one value is false
any(L2) # Will Return True as we have items in the list with True value
L3 = [1,2,3,True]
all(L3) # Will return True as all items in the list are True
any(L3) # Will Return True as we have items in the list with True value


#List Comprehensions

'''List Comprehensions provide an elegant way to create new lists.
It consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses.
'''
mystring = "WELCOME"
mylist = [ i for i in mystring ] # Iterating through a string Using List Compreh
mylist

mylist1 = [ i for i in range(40) if i % 2 == 0] # Display all even numbers betwe
mylist1

mylist2 = [ i for i in range(40) if i % 2 == 1] # Display all odd numbers betwee
mylist2

mylist3 = [num**2 for num in range(10)] # calculate square of all numbers betwee
mylist3

mylist3 = [num**2 for num in range(10)] # calculate square of all numbers betwee
mylist3

#List all numbers divisible by 3 , 9 & 12 using nested "if" with List Comprehens
mylist4 = [i for i in range(200) if i % 3 == 0 if i % 9 == 0 if i % 12 == 0] mylist4

# Odd even test
l1 = [print("{} is Even Number".format(i)) if i%2==0 else print("{} is odd number

# Extract numbers from a string
mystr = "One 1 two 2 three 3 four 4 five 5 six 6789" numbers = [i for i in mystr if i.isdigit()]
numbers

# Extract letters from a string
mystr = "One 1 two 2 three 3 four 4 five 5 six 6789" numbers = [i for i in mystr if i.isalpha()]
numbers



