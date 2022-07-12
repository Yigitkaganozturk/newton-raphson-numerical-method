# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 18:43:13 2022

@author: yiitk
"""
'''
this program finds an approximate value for the given polynomial function's one of the roots
it finds the value by using newton raphson method
to make the program work it is necessary to give the terms of the function you want to use 
program takes powers and coefficents of the function's terms then it takes a random number from user and finds a approxsimate
root of the function. as long as it finds an approximate value it prints the numbers taht are tried.
the value miscalculation in the 19th line means that the acceptable amount of deflection from the root of the function if you want
the progtam to find a more valid root approximation you can enter a more smaller number than given number (0.001)

'''
value_derivative=[]
valufn=[]
miscalculation=0.001
while True:
    a=input('to enter a function term, press e ')
    if a=='e':
        coefficient=float(input('enter the coefficient of the term you give '))
        power=float(input('enter the power of the term you give '))
        valufn.append([coefficient,power])
        value_derivative.append([coefficient*(power),(power-1)])
    else:
        break

def fn(x):
    function=0
    for i in range(len(valufn)):
        function+= valufn[i][0]*(x**valufn[i][1])
    return function
def fnderivative(x):
    fonksiyon=0
    for i in range(len(valufn)):
        fonksiyon+= value_derivative[i][0]*(x**value_derivative[i][1])
    return fonksiyon
h=int(input('give a number randomly '))
while True:
    if abs(fn(h)) >= miscalculation:
        print(f'x = {h}; y = {fn(h)}')
        print('------------------------------')
        h-=(fn(h)/fnderivative(h))
            
    else:
        print(f'approximate root {h}; the value of the function when x is approximate root {fn(h)}')
        break
