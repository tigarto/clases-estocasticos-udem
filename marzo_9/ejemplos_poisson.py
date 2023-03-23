# -*- coding: utf-8 -*-


import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# -------------------------------------------------------------------
"""
Definición de la VA Poisson: X ~ Poisson(alpha)

X: número de panes puestos en la estantería en cinco minutos

# Parametros
a = 5 (alpha)
"""

l = 12/30
T = 5
a = l*T

X = stats.poisson(mu = 2)
P_eq_3 = X.pmf(k = 3)
print("P(X=3) = {0:2f}".format(P_eq_3))
print()

# -------------------------------------------------------------------

"""
Definición de la VA Poisson: Y ~ Poisson(alpha)

Y: número de cheques en blanco en cinco un dia

# Parametros
a = 5 (alpha)
"""

l = 6
T = 1
a = l*T

Y = stats.poisson(mu = a)
"""
P_lt_5 = Y.pmf(k = 4) + Y.pmf(k = 3) + Y.pmf(k = 2) + \
         Y.pmf(k = 1) + Y.pmf(k = 0)

P_lt_5 = sum(Y.pmf(k = [0,1,2,3,4]))
"""

P_lt_5 = Y.cdf(x = 4)

print("P(Y < 5) = {0:2f}".format(P_lt_5))
print()
# -------------------------------------------------------------------

"""
Definición de la VA Poisson: Y ~ Poisson(alpha)

Z: número de llamadas recibidas en quice minutos

# Parametros
a = 0.75 (alpha)
"""

l = 6/120
T = 15
a = l*T

Z = stats.poisson(mu = a)
"""
P_gt_1 = 1 - sum(Z.pmf([0,1]))
"""

P_gt_1 = 1 - Z.cdf(1)

print("P(Z > 1) = {0:2f}".format(P_gt_1))

# Grafica de la PFM (z = [0,1,2,3,4,5,6,7,8,9])

print("-----------  PFM ----------------")
z = np.arange(10)
PFM_z =  Z.pmf(k=z)
print("z =",z)
print("P(Z = z) =",PFM_z)
print("-----------  CDF ----------------")
CDF_z =  Z.cdf(x = z)
print("z =",z)
print("P(Z <= z) =",CDF_z)

# Grafica de la PMF
plt.plot(z, PFM_z, 'bs', ms=10)
plt.vlines(z, 0, PFM_z, colors='b', lw = 5, alpha=0.5)
plt.xlabel("Numero de botellas de vino binagre")
plt.ylabel("Probabilidad")

plt.plot(z, CDF_z, 'rs', ms=10)
plt.vlines(z, 0, CDF_z, colors='r', lw = 5, alpha=0.5)
plt.xlabel("Numero de llamadas")
plt.ylabel("Probabilidad acumulada")



