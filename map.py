#Map
'''
  The map() function applies a given function to each item of an iterable (list, tuple etc.) and returns a list of the results.
map() function takes two Parameters :

function : The function to execute for each item of given iterable.

  iterable : It is a iterable which is to be mapped.

Returns : Returns a list of the results after applying the given function to each item of a given iterable (list, tuple etc.)
'''
#Syntax:map(function,iterable)

def twice(n):
return n*2
doubles = list(map(twice,odd_num)) # The map function will apply user defined "t
doubles

doubles = list(map(lambda n:n*2,odd_num)) # This map function will double all it
doubles

from functools import reduce
def add(a,b):
return a+b
sum_all = reduce(add,doubles) # This reduce function will perform sum of all ite
sum_all

#The below reduce() function will perform sum of all items in the list using lam
sum_all = reduce(lambda a,b : a+b,doubles) 
sum_all

# Putting all together
sum_all = reduce(lambda a,b : a+b,list(map(lambda n:n*2,list(filter(lambda n: n% 
sum_all




