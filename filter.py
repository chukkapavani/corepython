#Filter
'''
It is used to filter the iterables/sequence as per the conditions.

Filter function filters the original iterable and passes the items that returns True for the function provided to filter.
It is normally used with Lambda functions to filter list, tuple, or sets. filter() method takes two parameters:
  function - function tests if elements of an iterable returns true or false
  iterable - Sequence which needs to be filtered, could be sets, lists, tuples, or any iterators
'''
'''
Syntax:filter(function,iterable)
'''

list1 = [1,2,3,4,5,6,7,8,9]
def odd(n):
if n%2 ==1: return True else: return False
odd_num = list(filter(odd,list1)) # This Filter function filters list1 and passe
odd_num

list1 = [1,2,3,4,5,6,7,8,9]
# The below Filter function filters "list1" and passes all odd numbers using lam
odd_num = list(filter(lambda n: n%2 ==1 ,list1)) odd_num


list1 = [1,2,3,4,5,6,7,8,9,10]
even = list(filter(lambda n: n%2 ==0 ,list1)) # Filter even numbers from the lis
odd = list(filter(lambda n: n%2 !=0 ,list1))	# Filter odd numbers from the li
print('	')
print(even) print(odd)
print('	')
list2 = ['one' , 'TWO' , 'three' , 'FOUR']
upper = list(filter(lambda x: x.isupper() , list2)) # filter uppercase strings f
lower = list(filter(lambda x: x.islower() , list2)) # filter lowercase strings f
print(upper)
print(lower)
print('	')
list3 = ['one' , 'two2' , 'three3' ,'88' , '99' , '102']
numeric = list(filter(lambda x:x.isnumeric(), list3)) # filter numbers from the
alpha = list(filter(lambda x:x.isalpha(), list3))
alphanum = list(filter(lambda x:x.isalnum(), list3)) # filtr numbers & character
print(alpha)
print(numeric) print(alphanum)
print('	')


