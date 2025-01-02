#args & kwargs

'''
*args

  When we are not sure about the number of arguments being passed to a function then we can use *args as function parameter.
  *args allow us to pass the variable number of Non Keyword Arguments to function.
  We can simply use an asterisk * before the parameter name to pass variable length arguments.
  The arguments are always passed as a tuple.
  We can rename it to anything as long as it is preceded by a single asterisk (*). It's best practice to keep naming it args to make it immediately recognizable.


**kwargs

**kwargs allows us to pass the variable number of Keyword Arguments to the function. We can simply use an double asterisk ** before the parameter name to pass variable length arguments.
The arguments are passed as a dictionary.
We can rename it to anything as long as it is preceded by a double asterisk (**). It's best practice to keep naming it kwargs to make it immediately recognizable.
'''

def add(a,b,c):
return a+b+c
print(add(10,20,30)) # Sum of two numbers

print(add(1,2,3,4)) '''This will throw below error as this function will only ta If we want to make argument list dynamic then *args wil come in picture'''

def some_args(arg_1, arg_2, arg_3): print("arg_1:", arg_1)
print("arg_2:", arg_2) print("arg_3:", arg_3)
my_list = [2, 3]
some_args(1, *my_list)

def add1(*args):
  return sum(args)
print(add(1,2,3))
print(add(1,2,3,4)) # *args will take dynamic argument list. So add() function
print(add(1,2,3,4,5))
print(add(1,2,3,4,5,6))
print(add(1,2,3,4,5,6,7))


list1 = [1,2,3,4,5,6,7]
tuple1 = (1,2,3,4,5,6,7)
add1(*list1) , add1(*tuple1) #tuple & list items will be passed as argument list

list1 = [1,2,3,4,5,6,7]
list2 = [1,2,3,4,5,6,7]
list3 = [1,2,3,4,5,6,7]
list4 = [1,2,3,4,5,6,7]
add1(*list1 , *list2 , *list3 , *list4 ) #All four lists are unpacked and each i

def UserDetails(*args): 
 print(args)
UserDetails('Asif' , 7412 , 41102 , 33 , 'India' , 'Hindi')
''' For the above example we have no idea about the parameters passed e.g 7412 , In such cases we can take help of Keyworded arguments (**kwargs) '''

def UserDetails(**kwargs): 
print(kwargs)
UserDetails(Name='Asif' , ID=7412 , Pincode=41102 , Age= 33 , Country= 'India'

def UserDetails(**kwargs):
for key,val in kwargs.items():
print("{} :- {}".format(key,val))
UserDetails(Name='Asif' , ID=7412 , Pincode=41102 , Age= 33 , Country= 'India'

mydict = {'Name': 'Asif', 'ID': 7412, 'Pincode': 41102, 'Age': 33, 'Country': 'I
UserDetails(**mydict)

def UserDetails(licenseNo, *args , phoneNo=0 , **kwargs): # Using all four argu
print('License No :- ', licenseNo) j=''
for i in args: j = j+i
print('Full Name :-',j)
print('Phone Number:- ',phoneNo)
for key,val in kwargs.items():
print("{} :- {}".format(key,val))
name = ['Asif' , ' ' , 'Ali' , ' ','Bhat']
mydict = {'Name': 'Asif', 'ID': 7412, 'Pincode': 41102, 'Age': 33, 'Country': 'I
UserDetails('BHT145' , *name , phoneNo=1234567890,**mydict )

def UserDetails(licenseNo, *args , phoneNo=0, **kwargs): # Using all four argume
print('Nothing')


def UserDetails(licenseNo, **kwargs , *args): # This will fail. *args MUST come
print('Nothing')

#The below function will fail. Default argument/positional argument (licenseNo)
def UserDetails(ID = 1, licenseNo, *args): print('Nothing')

