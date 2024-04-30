import random
from ruleta import color_ruleta

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
    dinero_historico = [[] for _ in range(num_corridas + 1)]
    tiradas = [[] for _ in range(num_corridas + 1)]

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
                
            dinero_historico[i].append(dinero_actual)
            tiradas[i].append(j)
    return tiradas, dinero_historico

