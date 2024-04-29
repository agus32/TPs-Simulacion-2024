import random
import sys
import matplotlib.pyplot as plt
import numpy as np

def color_ruleta(numero):
    if numero == 0:
        return 'verde'
    elif (numero >= 1 and numero <= 10) or (numero >= 19 and numero <= 28):
        return 'rojo' if numero % 2 != 0 else 'negro'
    elif (numero >= 11 and numero <= 18) or (numero >= 29 and numero <= 36):
        return 'rojo' if numero % 2 == 0 else 'negro'

def simular_martingala(num_tiradas, num_corridas,dinero_inicial):
    dinero_historico = [[] for _ in range(num_corridas + 1)]
    tiradas = [[] for _ in range(num_corridas + 1)]

    
    for i in range (num_corridas+1):
        dinero_actual = dinero_inicial
        apuesta = 1
        for j in range(num_tiradas + 1):
            if dinero_actual < apuesta:
                break  # No hay dinero para seguir apostando
            dinero_actual -= apuesta
            valor = random.randint(0, 36)
            if color_ruleta(valor) == 'rojo':# Ganó la apuesta
                dinero_actual += apuesta*2
                apuesta = 1  
            else:# Perdió la apuesta
                apuesta *=2 
            dinero_historico[i].append(dinero_actual)
            tiradas[i].append(j)
    return tiradas, dinero_historico

# si ganas disminuis x fichas/dinero de tu apuesta. si perdes aumentas x 
def simular_dalambert(num_tiradas, num_corridas,dinero_inicial):
    dinero_historico_dalambert = [[] for _ in range(num_corridas + 1)]
    tiradas_dalambert = [[] for _ in range(num_corridas + 1)]

    # definimos el valor de x. suele ser un valor chico. 
    ficha = dinero_inicial/500
    for i in range (num_corridas+1):
        dinero_actual = dinero_inicial
        apuesta = ficha
        for j in range(num_tiradas + 1):
            if dinero_actual < apuesta:
                break  # No hay dinero para seguir apostando
            
            dinero_actual -= apuesta
            valor = random.randint(0, 36)
            
            if color_ruleta(valor) == 'rojo': # gano
                dinero_actual += apuesta*2
                apuesta -= ficha # disminuye la apuesta
            else: # perdio
                apuesta += ficha # aumenta disminuye la apuesta
                
            dinero_historico_dalambert[i].append(dinero_actual)
            tiradas_dalambert[i].append(j)
    return tiradas_dalambert, dinero_historico_dalambert

if len(sys.argv) != 9 or sys.argv[1] != "-c" or sys.argv[3] != "-n" or sys.argv[5] != "-e" or sys.argv[7] != "-d" or int(sys.argv[6]) not in range(37) or int(sys.argv[4]) > 10:
    print("Entrada incorrecta: python simulacion_ruleta.py -c <num_tiradas> -n <num_corridas -e <num_elegido> -d <dinero_inicial>")
    sys.exit(1)

num_tiradas = int(sys.argv[2])
num_corridas = int(sys.argv[4])
valor_elegido = int(sys.argv[6])
dinero_inicial = int(sys.argv[8])

tiradas, dinero_historico = simular_martingala(num_tiradas,num_corridas, dinero_inicial)
tiradas_dalambert, dinero_historico_dalambert = simular_dalambert(num_tiradas,num_corridas, dinero_inicial)
# martingala
plt.figure(figsize=(13, 6))
plt.xlabel('n (número de tiradas)')
plt.ylabel('cc (cantidad de capital)')
plt.title('Evolución del flujo de caja vs número de tiradas')


for i in range(num_corridas):
    color = np.random.rand(3,)
    plt.plot(tiradas[i], dinero_historico[i], color=color, label=f'Corrida {i + 1}')

plt.axhline(dinero_inicial, color='red', linestyle='--', label='Flujo de caja inicial')
plt.legend()
plt.show()

# d'alambert
plt.figure(figsize=(13, 6))
plt.xlabel('n (número de tiradas)')
plt.ylabel('cc (cantidad de capital)')
plt.title('Evolución del flujo de caja vs número de tiradas')


for i in range(num_corridas):
    color = np.random.rand(3,)
    plt.plot(tiradas_dalambert[i], dinero_historico_dalambert[i], color=color, label=f'Corrida {i + 1}')

plt.axhline(dinero_inicial, color='red', linestyle='--', label='Flujo de caja inicial')
plt.legend()
plt.show()