#Dictionary
'''
Dictionary is a mutable data type in Python.
A python dictionary is a collection of key and value pairs separated by a colon (:) & enclosed in curly braces {}.
Keys must be unique in a dictionary, duplicate values are allowed.
'''
#Create Dictionary
mydict = dict() # empty dictionary
mydict
mydict = {}	# empty dictionary
mydict
mydict = {1:'one' , 2:'two' , 3:'three'} # dictionary with integer keys
mydict
mydict = dict({1:'one' , 2:'two' , 3:'three'}) # Create dictionary using dict()
mydict
mydict = {'A':'one' , 'B':'two' , 'C':'three'} # dictionary with character keys
mydict
mydict = {1:'one' , 'A':'two' , 3:'three'} # dictionary with mixed keys
mydict
mydict.keys() # Return Dictionary Keys using keys() method
mydict.values() # Return Dictionary Values using values() method
mydict.items() # Access each key-value pair within a dictionary
mydict = {1:'one' , 2:'two' , 'A':['asif' , 'john' , 'Maria']} # dictionary with
mydict
mydict = {1:'one' , 2:'two' , 'A':['asif' , 'john' , 'Maria'], 'B':('Bat' , 'ca mydict
mydict = {1:'one' , 2:'two' , 'A':{'Name':'asif' , 'Age' :20}, 'B':('Bat' , 'cat','hat')}
 mydict
keys = {'a' , 'b' , 'c' , 'd'}
mydict3 = dict.fromkeys(keys)	# Create a dictionary from a sequence of keys
mydict3
keys = {'a' , 'b' , 'c' , 'd'} value = 10
mydict3 = dict.fromkeys(keys , value) # Create a dictionary from a sequence of
mydict3

keys = {'a' , 'b' , 'c' , 'd'} value = [10,20,30]
mydict3 = dict.fromkeys(keys , value) # Create a dictionary from a sequence of
mydict3

value.append(40)
 mydict3

#Accessing Items
mydict = {1:'one' , 2:'two' , 3:'three' , 4:'four'} 
mydict
mydict[1] # Access item using key
mydict.get(1) # Access item using get() method
mydict1 = {'Name':'Asif' , 'ID': 74123 , 'DOB': 1991 , 'job' :'Analyst'} mydict1
mydict1['Name'] # Access item using key
mydict1.get('job') # Access item using get() method


#Add, Remove & Change Items
mydict1 = {'Name':'Asif' , 'ID': 12345 , 'DOB': 1991 , 'Address' : 'Hilsinki'}
 mydict1

mydict1['DOB'] = 1992 # Changing Dictionary Items
mydict1['Address'] = 'Delhi'
 mydict1

dict1 = {'DOB':1995}
mydict1.update(dict1) 
mydict1

mydict1['Job'] = 'Analyst' # Adding items in the dictionary
mydict1

mydict1.pop('Job') # Removing items in the dictionary using Pop method
mydict1

mydict1.popitem() # A random item is removed

mydict1

del[mydict1['ID']] # Removing item using del method
mydict1

mydict1.clear() # Delete all items of the dictionary using clear method
mydict1

del mydict1 # Delete the dictionary object
mydict1


#Copy Dictionary

mydict = {'Name':'Asif' , 'ID': 12345 , 'DOB': 1991 , 'Address' : 'Hilsinki'} mydict
mydict1 = mydict # Create a new reference "mydict1"
id(mydict) , id(mydict1) # The address of both mydict & mydict1 will be the same
mydict2 = mydict.copy() # Create a copy of the dictionary
id(mydict2) # The address of mydict2 will be different from mydict because mydic
mydict['Address'] = 'Mumbai'
mydict
mydict1 # mydict1 will be also impacted as it is pointing to the same dictionary
mydict2 # Copy of list won't be impacted due to the changes made in the original

#Loop through a Dictionary
mydict1 = {'Name':'Asif' , 'ID': 12345 , 'DOB': 1991 , 'Address' : 'Hilsinki' , 'Job':'Analyst'}
mydict1

for i in mydict1:
print(i , ':' , mydict1[i]) # Key & value pair
for i in mydict1:
print(mydict1[i]) # Dictionary items


#Dictionary Membership
mydict1 = {'Name':'Asif' , 'ID': 12345 , 'DOB': 1991 , 'Job': 'Analyst'} 
mydict1

'Name' in mydict1 # Test if a key is in a dictionary or not.

'Asif' in mydict1 # Membership test can be only done for keys.
'ID' in mydict1
'Address' in mydict1


#All / Any
'''
The all() method returns:

  True - If all all keys of the dictionary are true
  False - If any key of the dictionary is false

The any() function returns True if any key of the dictionary is True. If not, any() returns False.
'''
mydict1 = {'Name':'Asif' , 'ID': 12345 , 'DOB': 1991 , 'Job': 'Analyst'} 
mydict1
all(mydict1) # Will Return false as one value is false (Value 0)
any(mydict1) # Will Return True as we have items in the dictionary with True va
mydict1[0] = 'test1' 
mydict1
all(mydict1) # Returns false as one value is false
any(mydict1) # Will Return True as we have items in the dictionary with True value


#Dictionary Comprehension
double = {i:i*2 for i in range(10)} #double each value using dict comprehension
double
square = {i:i**2 for i in range(10)} 
square

key = ['one' , 'two' , 'three' , 'four' , 'five'] 
value = [1,2,3,4,5]
mydict = {k:v for (k,v) in zip(key,value)} # using dict comprehension to create
mydict

mydict1 = {'a':10 , 'b':20 , 'c':30 , 'd':40 , 'e':50}
mydict1 = {k:v/10 for (k,v) in mydict1.items()} # Divide all values in a diction
mydict1

str1 = "Natural Language Processing"
mydict2 = {k:v for (k,v) in enumerate(str1)} # Store enumerated values in a dict
mydict2

str1 = "abcdefghijklmnopqrstuvwxyz"
mydict3 = {i:i.upper() for i in str1} # Lower to Upper Case
mydict3


#Word Frequency using dictionary
mystr4 = "one two three four one two two three five five six seven six seven one
mylist = mystr4.split() # Split String into substrings
mylist
mylist1 = set(mylist) # Unique values in a list
mylist1 = list (mylist1) mylist1

# Calculate frequenct of each word
count1 = [0] * len(mylist1) mydict5 = dict()
for i in range(len(mylist1)):
for j in range(len(mylist)):
if mylist1[i] == mylist[j]: count1[i] += 1
mydict5[mylist1[i]] = count1[i] print(mydict5)
