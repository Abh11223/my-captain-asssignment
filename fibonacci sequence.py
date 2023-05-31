# -*- coding: utf-8 -*-
"""
Created on Wed May 31 17:18:24 2023

@author: Abhishek kumar
"""

# python program for fibonacci numbers
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 13

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i),end=", ")