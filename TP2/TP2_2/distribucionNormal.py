import matplotlib.pyplot as plt
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from generators import GLCGenerator

glc = GLCGenerator(10, 2**31-1, 12345, 1103515245)

'''
    Distribucion Normal
    
    Paso 1: elegir mu, sigma, K, x.
    media:  es la media de la distribución normal.
    desvio: es la desviación estándar de la distribución normal.
    K: Indica cuantas variables aleatorias exponenciales se suman
    x: cantidad de valores a generar.
        
    Paso 2: generar r con el GLCGenerator. 
    r: valor aleatorio que varia entre 0 y 1
    
    Metodo: 
'''
def generador_normal(media, desvio, K, x):
    values = []
    for _ in range(x):
        sum_normal = 0
        for _ in range(K):  
            sum_normal += glc.random()
        sum_normal = ( sum_normal - (K/2) ) 
        multiplicar = desvio * pow((12/K), 0.5)
        values.append(sum_normal * multiplicar + media)
    return values


K = 5
media = 10
desvio = 2 
x = 100000  

valores_normales = generador_normal(media, desvio, K, x)

# Graficar la distribución normal 
def grafica_distribucionNormal():
    plt.hist(valores_normales, bins=50, density=True, alpha=0.6, color='b')
    plt.title('Distribución Normal Generada por GLC')
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')
    plt.show()
