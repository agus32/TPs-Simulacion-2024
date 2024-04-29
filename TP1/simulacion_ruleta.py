import random
import sys
import matplotlib.pyplot as plt
import numpy as np
from numpy import var


if len(sys.argv) != 7 or sys.argv[1] != "-c" or sys.argv[3] != "-n" or sys.argv[5] != "-e" or  int(sys.argv[6]) not in range(37) or int(sys.argv[4])>10000:
    print("Entrada incorrecta: python simulacion_ruleta.py -c <num_tiradas> -n <num_corridas> -e <num_elegido>")
    sys.exit(1)
    
num_tiradas = int(sys.argv[2])
num_corridas = int(sys.argv[4])
valor_esperado =  int(sys.argv[6])

tiradas = [[] for _ in range(num_corridas + 1)]
valores = [[]for _ in range(num_corridas + 1)]
frec_relativa = [[]for _ in range(num_corridas + 1)]
promedio = [[]for _ in range(num_corridas + 1)]
desvio = [[]for _ in range(num_corridas + 1)]
varianza = [[]for _ in range(num_corridas + 1)]


for i in range(num_corridas+1):
    sumador = 0
    contador = 0
    for n in range(num_tiradas+1):
        valor = random.randint(0,36)
        
        sumador = sumador + valor
        if (valor == valor_esperado):
            contador=contador+1
               
        tiradas[i].append(n)
        valores[i].append(valor)
        frec_relativa[i].append(contador)
        promedio[i].append(sumador/(n+1))
        desvio[i].append(np.std(valores[i]))
        varianza[i].append(var(valores[i]))
        

promedio_teorico_esperado = sum(range(37))/37
frecuencia_relativa_esperada = 1/37 * num_tiradas
varianza_esperada = var(range(37))
desvio_teorico_esperado = np.std(range(37))



def graficaFrecuenciaRelativa():
    plt.figure(figsize=(13, 6))
    plt.axhline(frecuencia_relativa_esperada, color='black', linewidth=2,
    label=f'Frecuencia relativa esperada: {round(frecuencia_relativa_esperada,1)}')

    plt.xlabel('n (numero de tiradas)')
    plt.ylabel('fr (frecuencia relativa)')
    plt.title('Grafica de frecuencia relativa del numero X con respecto al numero de tiradas')

    for i in range(num_corridas):
        color = np.random.rand(3,)
        plt.plot(tiradas[i],frec_relativa[i], color=color,label=f'Valor Final Obtenido Corrida {i+1}: {round(frec_relativa[i][-1], 4)}', )
        
    plt.subplots_adjust(right=0.7)
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    plt.show()
def graficaPromedio():
    plt.figure(figsize=(13, 6))
    plt.axhline(promedio_teorico_esperado, color='black', linewidth=2,
    label=f'Valor Teórico Esperado: {promedio_teorico_esperado}')

    plt.xlabel('n (numero de tiradas)')
    plt.ylabel('vp (valor promedio de las tiradas)')
    plt.title('Grafica del valor promedio de las tiradas con respecto al numero de tiradas')

    for i in range(num_corridas):
        color = np.random.rand(3,)
        plt.plot(tiradas[i],promedio[i], color=color,label=f'Valor Final Obtenido Corrida {i+1}: {round(promedio[i][-1], 4)}', )
        
    plt.subplots_adjust(right=0.7)
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        
    
    plt.show()
def graficaDesvio():
    plt.figure(figsize=(13, 6))
    plt.axhline(desvio_teorico_esperado, color='black', linewidth=2,
    label=f'Valor Teórico Esperado: {round(desvio_teorico_esperado,2)}')

    plt.xlabel('n (numero de tiradas)')
    plt.ylabel('vd (valor del desvio estandar)')
    plt.title('Grafica del valor del desvio con respecto al numero de tiradas')

    for i in range(num_corridas):
        color = np.random.rand(3,)
        plt.plot(tiradas[i], desvio[i], color=color,label=f'Valor Final Obtenido Corrida {i+1}: {round(desvio[i][-1], 2)}', )
        
    plt.subplots_adjust(right=0.7)
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    plt.show()
def graficaVarianza():
    plt.figure(figsize=(13, 6))
    plt.axhline(varianza_esperada, color='black', linewidth=2,
    label=f'Varianza esperada: {round(varianza_esperada,2)}')

    plt.xlabel('n (numero de tiradas)')
    plt.ylabel('vv (valor de la varianza)')
    plt.title('Grafica del valor de la varianza con respecto al numero de tiradas')

    for i in range(num_corridas):
        color = np.random.rand(3,)
        plt.plot(tiradas[i],varianza[i], color=color,label=f'Valor Final Obtenido Corrida {i+1}: {round(varianza[i][-1], 4)}', )
        
    plt.subplots_adjust(right=0.7)
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    plt.show()


print(graficaFrecuenciaRelativa())
print(graficaPromedio())
print(graficaDesvio())
print(graficaVarianza())

