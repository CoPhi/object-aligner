#!/usr/bin/env python3
from aligner import ObjectAligner
from stringsimeval import StringSimEval

a = ["riccio", "cacio", "doccia", "doge"]
b = ["ricciolo", "cacio", "cavallo", "doccia", "doge"]

algn = ObjectAligner(simEval=StringSimEval(), nullObj="–")
a_list, b_list, c_list = algn.align(a,b)
for i, c in enumerate(c_list):
    print(f'{a_list[i]:<10}{b_list[i]:<10}{str(c):>10}')

    

