# perfy
Perfy - a lightweight profiling tool for Python

Mark your functions and methods as trace-enabled with **@perfy** decorator:
```python
@perfy
def trace_this_function():
   # do something
```
Also, you can trace arbitrary blocks of your code using **with** statement:
```python
with perfy('name of your choice'):
   # your code here
```

After running your code, print report using
```python
perfy.report()
```

## Example:
```python
from time import sleep
from perfy import perfy

@perfy # <-- use decorator to track function calls
def func_sleep():
   sleep(.02)
    

def sleep_loop():
   with perfy('sleep loop'): # <-- use with-statement to track arbitrary block of code
      for _ in range(10):
         func_sleep()

# you can nest with-blocks and decorated function calls in any order:
@perfy # <-- a decorator on a top level function
def main():
   sleep_loop() # <-- this functions has a traced block inside

   with perfy('custom named block'): # <-- traced block
      sleep(.1)

      with perfy('inner block'): # <-- nested traced block
         func_sleep()
         func_sleep() 
```
For above code perfy.report() will output:
```
--------------------------------- Perfy report ---------------------------------

          Function/Method               Time(sec.)   Calls(count)      Avg(sec.)
--------------------------------------------------------------------------------
main                                         0.343              1          0.343
   └ sleep loop                              0.203              1          0.203
      └ func_sleep                           0.203             10          0.020
   └ custom named block                      0.141              1          0.141
      └ inner block                          0.041              1          0.041
         └ func_sleep                        0.040              2          0.020
--------------------------------------------------------------------------------

