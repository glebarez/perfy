# perfy
Perfy - a lightweight profiling tool

Mark your functions and methods as trace-enabled with **@perfy** decorator:
```python
@perfy
def trace_this_function():
    # do something
```
Also, you can trace certain blocks of your code using **with** statement:
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
    for _ in range(10):
        with perfy('sleep loop body'): # <-- use with-statement to track arbitrary block of code
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
----------------------------------Perfy report----------------------------------
            Function/Method                  Time(sec.)         Calls(count)    
--------------------------------------------------------------------------------
main                                           0.359                 1          
   └ sleep loop body                           0.213                 10         
      └ func_sleep                             0.213                 10         
   └ custom named block                        0.146                 1          
      └ inner block                            0.043                 1          
         └ func_sleep                          0.043                 2          
--------------------------------------------------------------------------------
```

