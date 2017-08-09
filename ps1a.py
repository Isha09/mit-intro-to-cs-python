#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 15:45:55 2017
MIT 6.0001 Problem set 1
@author: esha
"""
portion_down_payment = 0.25
current_savings = 0
#Annual return
r = 0.04
num_of_months = 0

annual_salary = int(input("Enter your annual salary:"))

portion_saved = float(input("Enter the percent of your salary to save, as a decimal:"))

total_cost = int(input("Enter the cost of your dream home:"))

monthly_salary = annual_salary/12

monthly_fixed_saving = portion_saved * monthly_salary

down_payment_amount = 0.25 * total_cost

while(current_savings < down_payment_amount):
    num_of_months += 1
    current_savings = current_savings + monthly_fixed_saving + (current_savings*r/12)
    
print("Number of month:",num_of_months)
    
