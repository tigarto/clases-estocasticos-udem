# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 14:37:10 2023

@author: b12s301e19
"""

"""
X ~ H(r,b,n)
r = 80
b = 100
n = 50
"""

import scipy.stats as stats
import scipy.special as special


def probHiper(x , r, b , n):
    return (special.binom(r,x)*special.binom(b,n - x))/special.binom(r+b,n)
    

# Ejemplo 1. gomitas

x1 = 35
r1 = 80
b1 = 100
n1 = 50

P1_35 = probHiper(x = x1, r = r1, b = b1, n = n1)
print("P(X=35) = {0:.4f}".format(P1_35))

# Ejemplo 2. letras

x2 = 4
r2 = 44
b2 = 56
n2 = 7

P2_4 = probHiper(x = x2, r = r2, b = b2, n = n2)
print("P(X=4) = {0:.4f}".format(P2_4))


# Ejemplo 3. DVD

x3 = 2
r3 = 10
b3 = 90
n3 = 12

P3_2 = probHiper(x = 2, r = r3, b = b3, n = n3)
P3_1 = probHiper(x = 1, r = r3, b = b3, n = n3)
P3_0 = probHiper(x = 0, r = r3, b = b3, n = n3)

P3_lq2 = P3_2 + P3_1+ P3_0
print("P(X<=2) = {0:.4f}".format(P3_lq2))