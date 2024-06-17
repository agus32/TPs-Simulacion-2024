import matplotlib.pyplot as plt
import numpy as np
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from TP2_1.generators import GLCGenerator

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
            r = glc.next()
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
plt.hist(valores_hipergeometricos, bins=50, density=True, alpha=0.6, color='r', label='GLC Generado')
plt.title('Distribución Hipergeométrica')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.legend()
plt.show()

exit()

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
        values.append(glc.next())
    return [a + (b - a) * v for v in values]

uniform_values = distribucion_uniforme(100, 120, 100000)

# grafica distribución uniforme
plt.hist(uniform_values, bins=50, density=True, alpha=0.6, color='g')
plt.title('Distribución Uniforme entre 0 y 1')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.show()



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
        values.append(glc.next()) 
    return [-(1/lambd) * np.log(v) for v in values]

lambd = 0.5  
exponential_values = distribucion_exponencial(lambd, 100000)

# grafica distribución exponencial
plt.hist(exponential_values, bins=50, density=True, alpha=0.6, color='b')
plt.title('Distribución Exponencial')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.show()



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
            sum_exponential += -np.log(glc.next())  
        values.append(sum_exponential * theta)
    return values

k = 3
theta = 1 
gamma_values = distribucion_gamma(k, theta, 100000)

# Graficar la distribución gamma
plt.hist(gamma_values, bins=50, density=True, alpha=0.6, color='b')
plt.title('Distribución Gamma (k=3, theta=1)')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.show()



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
        for _ in range(k):  
            sum_normal += glc.next()
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
plt.hist(valores_normales, bins=50, density=True, alpha=0.6, color='b')
plt.title('Distribución Normal Generada por GLC')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.show()
 
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
            r = glc.next()
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
plt.hist(valores_binomiales, bins=30, density=True, alpha=0.6, color='b', label='GLC Generado')
plt.title('Distribucion Binomial')
plt.xlabel('Número de éxitos')
plt.ylabel('Frecuencia relativa')
plt.legend()
plt.show()
