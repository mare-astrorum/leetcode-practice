#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 14:26:02 2019

@author: ai
"""

import re

input_s = "100\n200\n50\n3\n[5, 2, 3]"

hiring cost, salary, severence fee, num_of_months, min, empl

L = ["100", "200", "50", "3", "[5, 2, 3]"]

def create_int_list(input_s)

    L = input.split("\n")
    find_nums = re.findall("[0-1]+", L[4]
    L.pop(4)
    
integer_list = []
for i in L:
    value = int(i)
    integer_list.append(value)



integer_list = [100, 200, 50, 3]
find_nums = [5, 9, 2]

hiring = integer_list[0]
salary = integer_list[1]
severance = integer_list[2]

1 5-0*100, 5*200  = 500+1000 = 1500 
2 (9-5)*100, 9*200 = 700 + 1800
3 2-9*200, (9-2)*50 = 400 + 350


def minumum_cost(find_nums):
    tot_emp = 0
    expense_list = []


    for new_emp in find_nums:
            #5
        if new_emp - tot_emp > 0:
            additional_hired = new_emp - tot_emp #5
            tot_hir_fee = additional_hired * hiring
            tot_salary = new_emp * salary
            tot_expense = tot_hir_fee + tot_salary
            expense_list.append(tot_expense)
            tot_emp = new_emp

        elif new_emp - tot_emp < 0:
            fired = tot_emp - new_emp #5
            tot_sev_fee = fired * severance
            tot_salary = new_emp * salary
            tot_expense = tot_hir_fee + tot_salary
            tot_emp = new_emp
            expense_list.append(tot_expense)
        elif new_emp - tot_emp == 0:
            tot_expense = new_emp * salary
            expense_list.append(tot_expense)


    return expense_list
    

    
