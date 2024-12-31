'''Indentation

Indentation refers to the spaces at the beginning of a code line. It is very important as Python uses indentation to indicate a block of code.If the indentation is not correct we will endup with
IndentationError error.'''

p = 10
if p == 10:
print ('P is equal to 10') # correct indentation

# if indentation is skipped we will encounter "IndentationError: expected an ind
p = 10
if p == 10:
print ('P is equal to 10')

for i in range(0,5):
print(i)	# correct indentation

# if indentation is skipped we will encounter "IndentationError: expected an ind
for i in range(0,5): print(i)


for i in range(0,5): print(i) # correct indentation but less readable

j=20
for i in range(0,5):
print(i) # inside the for loop
print(j) # outside the for loop


