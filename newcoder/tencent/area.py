from math import sqrt

import numpy as np
from scipy.integrate import quad

n = int(input())
for i in range(n):
    A,B,C = [int(i) for i in input().split(' ')]
    delt = 4*A**2/(B**2) - (8*A*C/B)
    if delt <= 0:
        print(0)
    else:
        x1,x2 = ((2*A/B) - delt**0.5)*0.5 , ((2*A/B) + delt**0.5)*0.5
        print ((x1**3 / (6*A) - x1**2 /(2*B) + x1*C/B) - x2**3 / (6*A) + x2**2 / (2*B) - x2*C/B)
'''
1
1 1 -6

'''