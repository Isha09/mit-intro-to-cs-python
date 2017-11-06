#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 14:52:43 2017

@author: esha

Prog: Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. 
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
For example, if s = 'azcbobobegghakl', your program should print: Number of vowels: 5
"""
s = str(input("Enter any string:"))
count = 0
for ch in s:
  if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
    count += 1
print('Number of vowels:',count)

