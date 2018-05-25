#Ejercicio3
# Los arrays `u` y `v` representan dos series en funcion del tiempo `t`.
# Grafique las dos series de datos en una misma imagen 'serie.png'
# Calcule la covarianza entre `u` y `v` e imprima su valor.

import numpy as np
import matplotlib.pyplot as plt


t = np.array([0.,0.1,0.2,0.3,0.4,0.5,0.6, 0.8, 0.9])
u = np.array([12.,45.,6.,78.,34.,22.,-10.,31.,-27.])
v = np.array([3.,11.,1.3,37.,11.,6.,-23.,7.,7.])

#grafica

plt.plot(u,v)
plt.savefig('serie.png')
plt.show()

#covarianza

def covarianza(u,v):

    u_mean = np.mean(u)
    v_mean = np.mean(v)

    sumatoria = 0

    for i in range(0, len(u)):
        sumatoria += ((u[i] - u_mean) * (v[i] - v_mean))

    return sumatoria/(len(u)-1)