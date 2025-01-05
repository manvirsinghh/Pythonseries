# map() function
# syntax:
# map(function,iterable)
# Parameter:

# function: The function we want to apply to every element of the iterable.
# iterable: The iterable whose elements we want to process.
# Note: We can also pass multiple iterables if our function accepts multiple arguments.
#example
a=['1','2','3']
res=map(int,a)
print(list(res))
