# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 15:08:35 2023

@author: b12s301e19
"""



import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


"""
Definición de la VA hipergeometrica: X ~ H(r,b,n)

X: Numero de botellas de vino binagre

# Parametros
r = 3  # n (exitos)
b = 9
n = 4   # N (muestra)
        # M = r + b (Total)
"""

# X ~ H(r,b,n)
# Muestra: N = 4
# Numero exitos del grupo de interes: n = r = 3
# Tamaño grupo completo: M = r + b = 12

X = stats.hypergeom(N = 4, n = 3, M = 12)

# PFM
x = [0, 1, 2, 3]
PFM = X.pmf(x)

for i in range(len(x)):
    print("x = {0:d} | P(X = {1:d}) = {2:.2f}".format(x[i],x[i],PFM[i]))


# Grafica de la PFM
plt.plot(x, PFM, 'gs', ms=10)
plt.vlines(x, 0, PFM, colors='g', lw = 5, alpha=0.5)
plt.xlabel("Numero de botellas de vino binagre")
plt.ylabel("Probabilidad")


# CDF
CDF = X.cdf(x)

print("-----------------------------------------")

for i in range(len(x)):
    print("x = {0:d} | P(X = {1:d}) = {2:.2f}".format(x[i],x[i],CDF[i]))
    
print()

# Grafica de la PFM
plt.figure()
plt.plot(x, CDF, 'rs', ms=10)
plt.vlines(x, 0, CDF, colors='r', lw = 5, alpha=0.5)
plt.xlabel("Numero de botellas de vino binagre")
plt.ylabel("Probabilidad acumulativa")
