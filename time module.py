import time

current_time=time.time()
print(current_time)

print(time.sleep(2))

#strptime(string, format)

# Description: Parses a string representing a time according to a format and returns a struct_time.

import time
time_str = "2025-01-05 14:43:42"
parsed_time = time.strptime(time_str, "%Y-%m-%d %H:%M:%S")
print(parsed_time)  # e.g., time.struct_time(tm_year=2025, tm_mon=1, tm_mday=5, tm_hour=14, tm_min=43, tm_sec=42, ...)


#how to empty functions in python 
def func():
    pass
func()


#return statement:-A return statement is used to end the execution of the function call and it “returns” the value of the expression following the return keyword to the caller. The statements after the return statements are not executed. If the return statement is without any expression, then the special value None is returned.
#  A return statement is overall used to invoke a function so that the passed statements can be executed.
def sum(a,b):
    return a+b
res=sum(20,30)
print(res)
# print(sum(20,30))

# When the return statement is executed, the function terminates and 
# the specified value is returned to the caller. If no value is specified, the function returns None by default.

def square(numbers):
     return [n **2 for n in numbers]


res=square([1,2,3,4,5])
print(res)


