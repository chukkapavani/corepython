'''
Container

Containers are data structures that hold data values.

They support membership tests which means we can check whether a value exists in the container or not.
Generally containers provide a way to access the contained objects and to iterate over them.

Examples of containers include tuple, list, set, dict, str
'''
list1 = ['asif' , 'john' , 'Michael' , 'Basit']

'asif' in list1 # Membership check using 'in' operator
------------------------------------------------------------------
assert 'john' in list1 # If the condition returns true the program does nothing
---------------------------------------------------------------------------------------------
assert 'john1' in list1 # If the condition returns false, Assert will stop 
--------------------------------------------------------------------------------------------
mydict = {'Name':'Asif' , 'ID': 12345 , 'DOB': 1991 , 'Address' : 'Hilsinki'} mydict
-----------------------------------------------------------------------------------------------------
'Asif' in mydict # Dictionary membership will always check the keys
---------------------------------------------------------------------------------------------
'Name' in mydict # Dictionary membership will always check the keys
----------------------------------------------------------------------------------------------
'DOB' in mydict
--------------------

mystr = 'asifbhat'

'as' in mystr # Check if substring is present















