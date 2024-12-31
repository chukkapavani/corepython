#Lambda

'''
A lambda function is an anonymous function (function without a name).

Lambda functions can have any number of arguments but only one expression. The expression is evaluated and returned.
  We use lambda functions when we require a nameless function for a short period of time.

'''
Syntax:lambda argument(s):expression

addition = lambda a : a + 10 # This lambda function adds value 10 to an argumen
print(addition(5))

product = lambda a, b : a * b #This lambda function takes two arguments (a,b) an
print(product(5, 6))

addition = lambda a, b, c : a + b + c #This lambda function takes three argumen
print(addition(5, 6, 2))

res = (lambda *args: sum(args)) # This lambda function can take any number of a
res(10,20) , res(10,20,30,40) , res(10,20,30,40,50,60,70)

res1 = (lambda **kwargs: sum(kwargs.values())) # This lambda function can take a
res1(a = 10 , b= 20 , c = 30) , res1(a = 10 , b= 20 , c = 30, d = 40 , e = 50)

res1 = (lambda **kwargs: sum(kwargs.values())) # This lambda function can take a
res1(a = 10 , b= 20 , c = 30) , res1(a = 10 , b= 20 , c = 30, d = 40 , e = 50)

# User defined function to find product of numbers
def product(nums): total = 1
for i in nums: total *= i
return total
# This lambda function can take any number of arguments and return thier product
res1 = (lambda **kwargs: product(kwargs.values()))
res1(a = 10 , b= 20 , c = 30) , res1(a = 10 , b= 20 , c = 30, d = 40 , e = 50)


def myfunc(n):
return lambda a : a + n
add10 = myfunc(10)
 add20 = myfunc(20) 
add30 = myfunc(30)
print(add10(5)) print(add20(5)) print(add30(5))

















