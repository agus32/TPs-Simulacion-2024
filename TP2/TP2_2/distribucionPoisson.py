import matplotlib.pyplot as plt
import numpy as np
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from generators import GLCGenerator

glc = GLCGenerator(10, 2**31-1, 12345, 1103515245)

'''
   Distribucion de Poisson 
'''
def generador_poisson(lam):
    values = []
    for _ in range(num_experimentos):
        L = np.exp(-lam)
        k = 0
        p = 1.0
        while p > L:
            k += 1
            p *= glc.random()
        values.append(k - 1)
    return values

lam = 5 # donde lam es lambda
num_experimentos = 100
valores_poisson = generador_poisson(lam)

# Graficar la distribución de poisson 
def grafica_distribucionPoisson():
    plt.hist(valores_poisson, bins=50, density=True, alpha=0.6, color='b')
    plt.title('Distribución Poisson Generada por GLC')
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')
    plt.show()
