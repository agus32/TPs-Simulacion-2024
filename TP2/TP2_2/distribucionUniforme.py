import matplotlib.pyplot as plt
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from generators import GLCGenerator

glc = GLCGenerator(10, 2**31-1, 12345, 1103515245)

'''
    Distribucion Uniforme
    Explicacion.
    Paso 1: Definir la funcion uniforme que toma 3 valores. 
    a: rango inferior
    b: rango superior
    x: cantidad de valores uniformes a generar.
    
    Paso 2: generar r con el GLCGenerator. 
    r: valor aleatorio que varia entre 0 y 1  
'''
def distribucion_uniforme(a, b, x):
    values = []
    for _ in range(x):
        values.append(glc.random())
    return [a + (b - a) * v for v in values]

uniform_values = distribucion_uniforme(100, 120, 100000)
# grafica distribución uniforme
def grafica_distribucionUniforme():
    plt.hist(uniform_values, bins=50, density=True, alpha=0.6, color='g')
    plt.title('Distribución Uniforme entre 0 y 1')
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')
    plt.show()
