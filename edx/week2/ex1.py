#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 14:52:43 2017

@author: esha

In this problem, you'll create a program that guesses a secret number!

The program works as follows: you (the user) thinks of an integer between 0 (inclusive) 
and 100 (not inclusive). The computer makes guesses, and you give it input - 
is its guess too high or too low? Using bisection search, the computer will guess the user's secret number!
"""
num = print('Please think of a number between 0 and 100!')
h = 100
l = 0
c = int((h + l)/2)
while (l <= h):
 print('Is your secret number ',str(c) + '?')
 guess = str(input('Enter h to indicate the guess is too high. Enter l to indicate the guess is too low. Enter c to indicate I guessed correctly.'))
 if guess == 'h' or guess == 'l' or guess == 'c':
     if guess == 'c':
         print('Game over. Your secret number was:',str(c))
         break
     elif guess == 'l':
         l = c
         c = int((h + l)/2)
     elif guess == 'h':
        h = c
        c= int((h + l)/2)
 else:
     print('Sorry, I did not understand your input.')
