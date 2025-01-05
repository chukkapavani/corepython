'''
File Management

Python has several built-in modules and functions for creating, reading, updating and deleting files.
 order of file operation:-open file->read/write->close file
'''
#Open File

fileobj = open('test1.txt') # Open file in read/text mode
fileobj = open('test1.txt', 'r') # Open file in read mode
fileobj = open('test1.txt', 'w') # Open file in write mode
fileobj = open('test1.txt', 'a') # Open file in append mode


#close file
fileobj.close()



#read file
fileobj = open('test1.txt')
fileobj.read() #Read whole file
fileobj.read() #File cursor is already at the end of the file 

fileobj.seek(0) # Bring file cursor to initial position.
fileobj.read()

fileobj.seek(7) # place file cursor at loc 7
fileobj.read()

fileobj.seek(0)
fileobj.read(16) # Return the first 16 characters of the file

fileobj.tell() # Get the file cursor position
------------------------------------------------------------------------------
fileobj.seek(0)
print(fileobj.readline()) # Read first line of a file.
 print(fileobj.readline()) # Read second line of a file.
 print(fileobj.readline()) # Read third line of a file.
---------------------------------------------------------------------------------
fileobj.seek(0)
fileobj.readlines() # Read all lines of a file.
-----------------------------------------------------------------------------------
# Read first 5 lines of a file using readline()
fileobj.seek(0)

count = 0
for i in range(5):
if (count < 5):
print(fileobj.readline())
else:
break
count+=1
-------------------------------------------------------------------------------------
# Read first 5 lines of a file using readlines()
fileobj.seek(0)

count = 0
for i in fileobj.readlines():
if (count < 5): print(i)
else:
break
count+=1
--------------------------------------------------------------------------



#Write File
fileobj = open('test1.txt', 'a')

fileobj.write('THIS IS THE NEW CONTENT APPENDED IN THE FILE') # Append content t

fileobj.close()
fileobj = open('test1.txt') fileobj.read()
----------------------------------------------------------------------------------
fileobj = open("test1.txt", "w")

fileobj.write("NEW CONTENT ADDED IN THE FILE. PREVIOUS CONTENT HAS BEEN OVERWRIT

fileobj.close()
fileobj = open('test1.txt') fileobj.read()
--------------------------------------------------------------------------------------------------
fileobj = open("test2.txt", "w") # Create a new file

fileobj.write("First Line\n")
 fileobj.write("Second Line\n")
 fileobj.write("Third Line\n") 
fileobj.write("Fourth Line\n")
 fileobj.write("Fifth Line\n")
 fileobj.close()
fileobj = open('test2.txt')
 fileobj.readlines()
----------------------------------------------------------------------------------------------------------------

#Delete file
os.remove("test3.txt") # Delete file
os.rmdir('folder1/') # Delete folder
os.rmdir('folder1/')

