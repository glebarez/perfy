""" Perfy is a simple performance tracer for your Python code.
You can mark your functions and methods as trace-enabled with @perfy decorator.\n
Or, you can trace certain blocks of your code using with-statement like this:
    with perfy('name of your choice'):
        # your code here
        
Moreover, perfy.report() prints out a formatted view, showing call stack of traced blocks, total time taken, and count of calls
"""

from contextlib import contextmanager
from copy import deepcopy
from functools import wraps
from time import perf_counter

__version__ = '0.28'

# dict-key aliases
_TIME = '#'
_COUNT = '~'

class Perfy():
    '''Perfy - a simple performance tracer
    see module-level docstring for detailed usage'''
    
    # repeat version to be accessible in case of perfy module import-hidden behind perfy instance
    __version__ = __version__

    def __init__(self):
        self._stack = {}       # stack of calls, with traced numbers
        self._sp = self._stack # set current stack pointer

    # context manager implementation
    @contextmanager
    def _context_manager(self, descr):
        # initialize current stack segment, ifn
        if descr not in self._sp:
            self._sp[descr] = {_TIME:0, _COUNT:0}
        
        # stash current stack pointer and get deeper
        _upper_sp  = self._sp
        self._sp = self._sp[descr]
        
        # start performance counter
        t0 = perf_counter()
        yield
        # calculate time taken
        s = perf_counter() - t0

        # update numbers
        self._sp[_TIME] += s
        self._sp[_COUNT] += 1
        
        # restore stack pointer
        self._sp = _upper_sp
    
    # decorator implementation
    def _decorator(self, f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            with self._context_manager(f.__name__):
                return f(*args, **kwargs)
        return wrapped
    
    # unified entry point for user
    def __call__(self, attr):
        if callable(attr):
            return self._decorator(attr)
        else:
            return self._context_manager(attr)

    # resets stack and timers to initial state
    def reset(self):
        self.__init__()
    
    # prints a report
    def report(self):
        print('\n{0:-^80}\n'.format(' Perfy report '))
        print('{:^35}{:>15}{:>15}{:>15}'.format('Function/Method', 'Time(sec.)', 'Calls(count)', 'Avg(sec.)'))
        print('{:-^80}'.format(''))
        if self._stack:
            self._report(deepcopy(self._stack), level = 0)
        else:
            print('{:^80}'.format('Empty'))
        print('{:-^80}'.format(''))
    
    # inner recursive implementation of report prinitng
    def _report(self, stack, level):
        for name, stats in sorted(stack.items(), key = lambda x:x[1][_TIME], reverse = True):
            _time = stats.pop(_TIME)
            _count = stats.pop(_COUNT)
            _avg = round(_time/_count,3) if _count else 0
            print('{:35}{:>15.3f}{:>15,d}{:>15.3f}'.format(
                '   ' * level + ('└ ' if level else '') + name, _time, _count,_avg))
            self._report(stats, level + 1)

# a module-level instance for convenience
perfy = Perfy()
