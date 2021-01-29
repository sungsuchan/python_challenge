#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
python function.

"""

#%%
# def로 함수 만들기.

def say_hello():
    print('hello world')

say_hello()
#%%
# 함수 안의 argument 설정하기.

def print_max(a, b):
    if a>b:
        print(a,'is maximum')
    elif a==b:
        print(a,'is equal to', b)
    else:
        print(b,'is maximum')
        
print_max(3,4)

x =5
y =7

print_max(x,y)
#%%
# 함수 안의 변수와 밖의 변수 일치 시키기, global.

x=50

def func():
    global x
    print('x is', x)
    x=2
    print('Changed global x to',x)
    
func()
print('Value of x is', x)
#%%
# 함수 안에 default value 설정하기.

def say(message, times =1):
    print(message*times)

say('Hello')
say('World', 5)
#%%
# keyword arguments.

def func(a, b=5, c=10):
    print('a is', a, 'and b is',b,'and c is',c)

func(3,7)
func(25,c=24)
func(c=50, a=100)
#%%
# 함수 안에 varargs parameters 설정하기.

def total(a=5, *numbers, **phonebook):
    print('a', a)
    for single_item in numbers:
        print('single_item', single_item)
    for first_part, second_part in phonebook.items():
        print(first_part,second_part)
        
total(10,1,2,3,Jack=1123,John=2231,Inge=1560)

#%%
# return 사용하기.

def maximum(x,y):
    if x >y:
        return x
    elif x==y:
        return 'The numbers are equal'
    else:
        return y

print(maximum(2,3))
#%%
# DocStrings.

def print_max(x,y):
    '''Prints the maximum of two numbers.
    
    The tow values must be integers.'''
    x= int(x)
    y= int(y)
    
    if x>y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')

print_max(3,5)
print(print_max.__doc__)














