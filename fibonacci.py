# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 00:13:34 2021

@author: kcs
"""

nterms = int(input("How many terms? "))
# first two terms
n1, n2 = 0, 1
count = 0
#check if number of terms is valid
if nterms <= 0:
    print("Please enter a positive integer")
    #if there is only one term, return n1
elif nterms == 1:
    print("Fibonacci sequence upto", nterms,":")
    print(n1)
    #generate fibnocci sequence
else:
    print("Fibonacci sequence:")
    while count < nterms:
        print(n)
        nth = n1 + n2
        #update values
        n1 = n2
        n2 = nth
        count += 1