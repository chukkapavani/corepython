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

#String Indexing
str1
str1[0] # First character in string "str1"
str1[len(str1)-1] # Last character in string using len function
str1[-1] # Last character in string
str1[6] #Fetch 7th element of the string
str1[5]

#String Slicing
str1[0:5] # String slicing - Fetch all characters from 0 to 5 index location
str1[6:12] # String slicing - Retreive all characters between 6 - 12 index loc 
str1[-4:] # Retreive last four characters of the string
str1[-6:] # Retreive last six characters of the string
str1[:4] # Retreive first four characters of the string
str1[:6] # Retreive first six characters of the string

#Update & Delete String
str1
#Strings are immutable which means elements of a string cannot be changed 
str1[0:5] = 'HOLAA'

del str1 # Delete a string
print(srt1)

#String concatenation
s1 = "Hello"
 s2 = "Asif"
 s3 = s1 + s2
 print(s3)

s1 = "Hello"
 s2 = "Asif"
s3 = s1 + " " + s2
print(s3)

#Iterating through a String
mystr1 = "Hello Everyone"

# Iteration
for i in mystr1: 
  print(i)


for i in enumerate(mystr1):
  print(i)

list(enumerate(mystr1)) # Enumerate method adds a counter to an iterable

#String Membership
mystr1 = "Hello Everyone"
print ('Hello' in mystr1) # Check whether substring "Hello" is present in string
 print ('Everyone' in mystr1) # Check whether substring "Everyone" is present in
 print ('Hi' in mystr1) # Check whether substring "Hi" is present in string "mysr


#String Partitioning
"""
The partition() method searches for a specified string and splits the string int

-	The first element contains the part before the argument string.

-	The second element contains the argument string.

-	The third element contains the part after the argument string. """

str5 = "Natural language processing with Python and R and Java" L = str5.partition("and")
print(L)


"""
The rpartition() method searches for the last occurence of the specified string containing three elements.

-	The first element contains the part before the argument string.

-	The second element contains the argument string.

-	The third element contains the part after the argument string. """

str5 = "Natural language processing with Python and R and Java" L = str5.rpartition("and")
print(L)


#String Functions
mystr2 = "	Hello Everyone" 
mystr2

mystr2.strip() # Removes white space from begining & end

mystr2.rstrip() # Removes all whitespaces at the end of the string

mystr2.lstrip() # Removes all whitespaces at the begining of the string

mystr2 = "*********Hello Everyone***********All the Best**********" 
mystr2

mystr2.strip('*') # Removes all '*' characters from begining & end of the string
mystr2.rstrip('*') # Removes all '*' characters at the end of the string
mystr2.lstrip('*') # Removes all '*' characters at the begining of the string

mystr2 = "	Hello Everyone"
mystr2.lower() # Return whole string in lowercase
mystr2.upper() # Return whole string in uppercase
mystr2.replace("He" , "Ho") #Replace substring "He" with "Ho"
mystr2.replace(" " , "") # Remove all whitespaces using replace function
mystr5 = "one two Three one two two three"
mystr5.count("one") # Number of times substring "one" occurred in string.
mystr5.count("two") # Number of times substring "two" occurred in string.
mystr5.startswith("one") # Return boolean value True if string starts with "one
mystr5.endswith("three") # Return boolean value True if string ends with "three"
mystr4 = "one two three four one two two three five five six seven six seven one
mylist = mystr4.split() # Split String into substrings
mylist


# Combining string & numbers using format method
item1 = 40
item2 = 55
item3 = 77
res = "Cost of item1 , item2 and item3 are {} , {} and {}" print(res.format(item1,item2,item3))

# Combining string & numbers using format method
item1 = 40
item2 = 55
item3 = 77
res = "Cost of item3 , item2 and item1 are {2} , {1} and {0}" print(res.format(item1,item2,item3))

str2 = " WELCOME EVERYONE "
str2 = str2.center(100) # center align the string using a specific character as
print(str2)

str2 = " WELCOME EVERYONE "
str2 = str2.center(100,'*') # center align the string using a specific character
print(str2)

str2 = " WELCOME EVERYONE "
str2 = str2.rjust(50) # Right align the string using a specific character as the
print(str2)

str2 = " WELCOME EVERYONE "
str2 = str2.rjust(50,'*') # Right align the string using a specific character ('
print(str2)

str4 = "one two three four five six seven"
loc = str4.find("five") # Find the location of word 'five' in the string "str4"
print(loc)

str4 = "one two three four five six seven"
loc = str4.index("five") # Find the location of word 'five' in the string "str4"
print(loc)

mystr6 = '123456789'
print(mystr6.isalpha()) # returns True if all the characters in the text are let
 print(mystr6.isalnum()) # returns True if a string contains only letters or num
 print(mystr6.isdecimal()) # returns True if all the characters are decimals (0-9)
 print(mystr6.isnumeric()) # returns True if all the characters are numeric (0-9)


mystr6 = 'abcde'
print(mystr6.isalpha()) # returns True if all the characters in the text are let
 print(mystr6.isalnum()) # returns True if a string contains only letters or num
 print(mystr6.isdecimal()) # returns True if all the characters are decimals (0-9)
 print(mystr6.isnumeric()) # returns True if all the characters are numeric (0-9)


mystr6 = 'abc12309'
print(mystr6.isalpha()) # returns True if all the characters in the text are let
 print(mystr6.isalnum()) # returns True if a string contains only letters or num
 print(mystr6.isdecimal()) # returns True if all the characters are decimals (0-9
 print(mystr6.isnumeric()) # returns True if all the characters are numeric (0-9)


str6 = "one two three four one two two three five five six one ten eight ten nin
loc = str6.rfind("one") # last occurrence of word 'one' in string "str6"
print(loc)

loc = str6.rindex("one") # last occurrence of word 'one' in string "str6"
print(loc)

txt = "	abc def ghi"
txt.rstrip()

txt = "	abc def ghi"
txt.lstrip()

txt = "	abc def ghi"
txt.strip()

#Using Escape Character
#Using double quotes in the string is not allowed.
mystr = "My favourite TV Series is "Game of Thrones""

#Using escape character to allow illegal characters
 mystr = "My favourite series is \"Game of Thrones\"" 
print(mystr)