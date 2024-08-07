import matplotlib.pyplot as plt
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from generators import GLCGenerator

glc = GLCGenerator(10, 2**31-1, 12345, 1103515245)

'''
    Distribucion Binomial
    
    Paso 1: elegir n, p y x0
    n: numero de ensayos
    p: probabilidad de exito
    x0: inicia en 0
        
    Paso 2: generar r con el GLCGenerator. 
    r: valor aleatorio que varia entre 0 y 1
    
    Metodo: 
    xi = xi-1 + 1     si ri <= p
    xi = xi-1         si ri > p
'''
def generador_binomial(n, p):
    values = []
    for _ in range(num_experimentos):
        x = 0
        for _ in range(n):
            r = glc.random()
            if r <= p:
                x += 1
        values.append(x)

    return values

n = 1000  # numero de ensayos
p = 0.5   # probabilidad de exito
x = 0     # valor inicial
num_experimentos = 5

valores_binomiales = generador_binomial(n, p)

# Grafica distribucion Binomial
def grafica_distribucionBinomial():
    plt.hist(valores_binomiales, bins=30, density=True, alpha=0.6, color='b', label='GLC Generado')
    plt.title('Distribucion Binomial')
    plt.xlabel('Número de éxitos')
    plt.ylabel('Frecuencia relativa')
    plt.legend()
    plt.show()
