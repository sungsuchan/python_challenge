#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
python Modules.
"""

#%%
import sys

print('The command line arguments are:')
for i in sys.argv:
    print(i)

print('\n\nThe PYTHONPATH is', sys.path, '\n')
#%%
from math import sqrt
print("Square root of 16 is", sqrt(16))
#%%
if __name__ == '__main__':
    print('This program is being run by ifself')
else:
    print('I am being imported from another module')
#%%
def say_hi():
    print('Hi, this is mymodule speaking.')
__version__ = '0.1'
#%%
from python_basic4_modules import say_hi, __version__

say_hi()
print('Version',__version__)
#%%
import sys

dir(sys) 
