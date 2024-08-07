import matplotlib.pyplot as plt
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from generators import GLCGenerator

glc = GLCGenerator(10, 2**31-1, 12345, 1103515245)

'''
    Distribucion Hipergeometrica
    Hay N elementos de clase 1 o clase 2. 
    Np son la cantidad de elementos de la clase 1.
    Nq son la cantidad de elementos de la clase 2.
    Si de la poblacion N se toman n elementos sin reponer, el numero de elementos x
    de la clase 1/2  tendra una distribucion hipergeometrica.
    
    Parametros:
    N: poblacion
    n: muestra
    p: probabilidad de que sea de clase 1
    x: inicia en 0
    
'''
def generador_hipergeometrica(N, n, p, glc, num_experimentos=1000):
    values = []
    for _ in range(num_experimentos):
        x = 0
        N_actual = N
        p_actual = p
        for _ in range(n):
            r = glc.random()
            if r <= p_actual / N_actual:
                x += 1
                p_actual -= 1
            N_actual -= 1
        values.append(x)
    return values

# parametros
N = 1000   # tamaño de la poblacion inicial
n = 50     # tamaño de la muestra
p = 500    # numero de exitos en la poblacion
num_experimentos = 1000

valores_hipergeometricos = generador_hipergeometrica(N, n, p, glc, num_experimentos)

# Graficar distribución hipergeométrica 
def grafica_distribucionHipergeometrica():
    plt.hist(valores_hipergeometricos, bins=50, density=True, alpha=0.6, color='r', label='GLC Generado')
    plt.title('Distribución Hipergeométrica')
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')
    plt.legend()
    plt.show()
