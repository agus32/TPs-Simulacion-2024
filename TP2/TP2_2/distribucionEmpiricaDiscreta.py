import matplotlib.pyplot as plt
import numpy as np
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from generators import GLCGenerator

glc = GLCGenerator(10, 2**31-1, 12345, 1103515245)

def generador_empiricaDiscreto(M, N, I, P, glc):
    X = np.zeros(M)
    for L in range(N):
        R = glc.random()
        for J in range(M):
            if P[I-1, J] >= R:
                break
        I = J + 1
        X[I-1] += 1
    return X

M = 10   # numero de categorías
N = 1000  # umero de muestras
I = 1   # categoria inicial
P = np.random.rand(M, M)  # matriz de probabilidades

# Normalizar la matriz de probabilidades
P = P / P.sum(axis=1, keepdims=True)

valores_ed = generador_empiricaDiscreto(M, N, I, P, glc)

# Graficar la distribución de poisson 
def grafica_distribucionEmpiricaDiscreta():
    plt.hist(valores_ed, bins=50, density=True, alpha=0.6, color='b')
    plt.title('Distribución Empirica Discreta Generada por GLC')
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')
    plt.show()
