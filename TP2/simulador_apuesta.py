import sys
import matplotlib.pyplot as plt
import numpy as np
from apuestas import simular_martingala, simular_dalambert, simular_fibonacci, simular_paroli

#En este archivo ira la entrada de parametros y la visualizacion de los resultados

if len(sys.argv) != 9 or sys.argv[1] != "-c" or sys.argv[3] != "-n" or sys.argv[5] != "-s" or sys.argv[7] != "-d" or int(sys.argv[4]) > 10:
    print("Entrada incorrecta: python simulacion_ruleta.py -c <num_tiradas> -n <num_corridas> -s <estrategia: m/d/f/o> -d <dinero_inicial>")
    sys.exit(1)

num_tiradas = int(sys.argv[2])
num_corridas = int(sys.argv[4])
estrategia = sys.argv[6]
dinero_inicial = int(sys.argv[8])



if(estrategia == "m"):
    tiradas, dinero_historico = simular_martingala(num_tiradas,num_corridas, dinero_inicial)
elif(estrategia == "d"):
    tiradas, dinero_historico = simular_dalambert(num_tiradas,num_corridas, dinero_inicial)
elif(estrategia == "f"):
    tiradas, dinero_historico = simular_fibonacci(num_tiradas,num_corridas, dinero_inicial)
elif(estrategia == "o"):
    tiradas, dinero_historico = simular_paroli(num_tiradas,num_corridas, dinero_inicial)
else:
    print("Estrategia no valida")
    sys.exit(1)


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
