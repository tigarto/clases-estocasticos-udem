# -*- coding: utf-8 -*-

import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""
Definición de la VA Uniforme: X ~ Uniforme(k,l)

X: El numero de puntos de la cara que cae arriba

# Parametros
k 
l
"""

k = 1
l = 6
X = stats.randint(low = k, high = l + 1)
x = np.arange(11)

# PFM
PFM_X = X.pmf(k = x)
CDF_X = X.cdf(x = x)


print("X =",x)
print("P(X = x) =",PFM_X)
print("P(X < x) =",CDF_X)


# Grafica de la PMF

plt.plot(x, CDF_X, 'rs', ms=10)
plt.vlines(x, 0, CDF_X, colors='r', lw = 5, alpha=0.5)
plt.xlabel("Numero de puntos de la cara que cae arriba")

plt.plot(x, PFM_X, 'bs', ms=10)
plt.vlines(x, 0, PFM_X, colors='b', lw = 5, alpha=0.5)
plt.xlabel("Numero de puntos de la cara que cae arriba")




