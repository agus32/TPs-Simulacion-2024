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


# Si perdes -> aumentas x fichas/dinero a tu apuesta.
# Si ganas -> disminuis x fichas/dinero a tu apuesta. 
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


# Si perdes -> sumas el valor de tus dos últimas apuestas. 
# Si ganas -> retrocedes dos posiciones en la serie (o te mantenes en 1).
def simular_fibonacci(num_tiradas, num_corridas, dinero_inicial):
    dinero_historico = [[] for _ in range(num_corridas + 1)]
    apuestas_historico = [[] for _ in range(num_corridas + 1)]  # historial de apuestas
    tiradas = [[] for _ in range(num_corridas + 1)]

    for i in range (num_corridas+1):
        dinero_actual = dinero_inicial
        
        # las primeras 2 tiradas se realizan con un valor fijo predeterminado.
        apuesta = dinero_inicial/500        
        
        # definimos flag para saber si la segunda tirada resultó ganadora o perdedora. False -> perdedora, True -> ganadora
        flag = False
        # calculamos los resultados de las dos primeras tiradas
        for j in range(2):
            dinero_actual -= apuesta
            valor = random.randint(0, 36)    
            if color_ruleta(valor) == 'rojo': # gano 
                dinero_actual += apuesta*2
                if j == 1:
                    flag = True
            dinero_historico[i].append(dinero_actual)
            apuestas_historico[i].append(apuesta) 
            tiradas[i].append(j)
        
        if flag: # si la segunda tirada resulto ganadora, la tercera apuesta es igual a la primera
            apuesta = dinero_inicial/500
        else: # si la segunda tirada resulto perdedora, la tercera apuesta es la suma de las dos anteriores
            apuesta = apuestas_historico[i][0] + apuestas_historico[i][1]  
        apuestas_historico[i].append(apuesta) 
        

        # a partir de la tercera tirada se aplica la regla de fibonacci
        j=2
        for j in range(num_tiradas + 1):
             
            if dinero_actual < apuesta:
                break  # No hay dinero para seguir apostando
            
            dinero_actual -= apuesta
            valor = random.randint(0, 36)
            
            if color_ruleta(valor) == 'rojo': # gano retroceder dos posiciones
                dinero_actual += apuesta*2
                apuesta = apuestas_historico[i][j-1]  
            else: # perdio sumar las dos ultimas apuestas
                apuesta = apuestas_historico[i][j] + apuestas_historico[i][j-1]  
            
            dinero_historico[i].append(dinero_actual)
            apuestas_historico[i].append(apuesta)  
            tiradas[i].append(j)
    return tiradas, dinero_historico

def simular_paroli(num_tiradas, num_corridas,dinero_inicial):
    dinero_historico_paroli = [[] for _ in range(num_corridas + 1)]
    tiradas_paroli = [[] for _ in range(num_corridas + 1)]

    
    for i in range (num_corridas+1):
        auxiliar_paroli = 1
        dinero_actual = dinero_inicial
        apuesta = 1
        for j in range(num_tiradas + 1):
            if dinero_actual < apuesta:
                break  # No hay dinero para seguir apostando
            dinero_actual -= apuesta
            valor = random.randint(0, 36)
            if color_ruleta(valor) == 'rojo':# Ganó la apuesta, por ende duplica la apuesta
                dinero_actual += apuesta*2
                if auxiliar_paroli != 3: # Si gana 3 veces consecutivas vuelve a la apuesta inicial
                    apuesta *= 2
                    auxiliar_paroli += 1
                else:
                    auxiliar_paroli = 1

            else:# Perdió la apuesta, entonces vuelve a la apuesta inicial
                apuesta = 1
            dinero_historico_paroli[i].append(dinero_actual)
            tiradas_paroli[i].append(j)
    return tiradas_paroli, dinero_historico_paroli
