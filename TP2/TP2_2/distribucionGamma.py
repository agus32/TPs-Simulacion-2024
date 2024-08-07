import matplotlib.pyplot as plt
import numpy as np
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from generators import GLCGenerator

glc = GLCGenerator(10, 2**31-1, 12345, 1103515245)

'''
    Distribucion Gamma
    Explicacion: surge de la suma de k variables aleatorias exponenciales.
    No se puede generar explicitamente una funcion
    
    Paso 1: elegir k y 𝜃 acordes.
    k: parametro de forma. Indica cuantas variables aleatorias exponenciales se suman para formar la distribución gamma
    𝜃: parametro de escala. afecta la "anchura" de la distribución
    x: cantidad de valores a generar.
        
    Paso 2: generar r con el GLCGenerator. 
    r: valor aleatorio que varia entre 0 y 1
    
    Metodo: -1/lamda * sumatoria entre 1 a k de log ri. Donde r es una variable de la distribucion exponencial.  
'''
def distribucion_gamma(k, theta, x):
    values = []
    for _ in range(x):
        sum_exponential = 0
        for _ in range(k):
            sum_exponential += -np.log(glc.random())  
        values.append(sum_exponential * theta)
    return values

k = 3
theta = 1 
gamma_values = distribucion_gamma(k, theta, 100000)

# Graficar la distribución gamma
def grafica_distribucionGamma():
    plt.hist(gamma_values, bins=50, density=True, alpha=0.6, color='b')
    plt.title('Distribución Gamma (k=3, theta=1)')
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')
    plt.show()
