import matplotlib.pyplot as plt
import numpy as np
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from generators import GLCGenerator
glc = GLCGenerator(10, 2**31-1, 12345, 1103515245)

'''
    Distribucion Exponencial
    Explicacion.
    Paso 1: Definir la funcion exponencial que toma 2 valores. 
    lambda: parámetro de tasa de la distribución exponencial.
    x: cantidad de valores a generar.
    
    Paso 2: generar r con el GLCGenerator. 
    r: valor aleatorio que varia entre 0 y 1
'''
def distribucion_exponencial(lambd, x):
    values = []
    for _ in range(x):
        values.append(glc.random()) 
    return [-(1/lambd) * np.log(v) for v in values]

lambd = 0.5  
exponential_values = distribucion_exponencial(lambd, 100000)

# grafica distribución exponencial
def grafica_distribucionExponencial():
    plt.hist(exponential_values, bins=50, density=True, alpha=0.6, color='b')
    plt.title('Distribución Exponencial')
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')
    plt.show()
