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
                
if __name__ == '__main__':
    # run top-level function
    main()

    # let perfy print report
    perfy.report()