import random
from ruleta import color_ruleta

def simular_martingala(num_tiradas, num_corridas,dinero_inicial, capital_infinito):
    dinero_historico = [[] for _ in range(num_corridas)]
    tiradas = [[] for _ in range(num_corridas)]
    frecuencia_historica = [[] for _ in range(num_corridas)]


    
    for i in range (num_corridas):
        dinero_actual = dinero_inicial
        apuesta = 1
        ganadas = 0
        dinero_historico[i].append(dinero_inicial)
        tiradas[i].append(0)
        for j in range(1,num_tiradas + 1):
            if dinero_actual < apuesta and not capital_infinito:
                break  # No hay dinero para seguir apostando
            dinero_actual -= apuesta
            valor = random.randint(0, 36)
            if color_ruleta(valor) == 'rojo':# Ganó la apuesta
                dinero_actual += apuesta*2
                apuesta = 1
                ganadas += 1
            else:# Perdió la apuesta
                apuesta *=2 
            dinero_historico[i].append(dinero_actual)
            tiradas[i].append(j)
            frecuencia_historica[i].append(ganadas/j)
    return tiradas, dinero_historico, frecuencia_historica


# Si perdes -> aumentas x fichas/dinero a tu apuesta.
# Si ganas -> disminuis x fichas/dinero a tu apuesta. 
def simular_dalambert(num_tiradas, num_corridas,dinero_inicial, capital_infinito):
    dinero_historico = [[] for _ in range(num_corridas)]
    tiradas = [[] for _ in range(num_corridas)]
    frecuencia_historica = [[] for _ in range(num_corridas)]

    # definimos el valor de x. suele ser un valor chico. 
    ficha = dinero_inicial/500
    for i in range (num_corridas):
        dinero_actual = dinero_inicial
        apuesta = ficha
        ganadas = 0
        dinero_historico[i].append(dinero_inicial)
        tiradas[i].append(0)
        for j in range(1,num_tiradas + 1):
            if dinero_actual < apuesta and not capital_infinito:
                break  # No hay dinero para seguir apostando
            dinero_actual -= apuesta
            valor = random.randint(0, 36)
            
            if color_ruleta(valor) == 'rojo': # gano
                dinero_actual += apuesta*2
                if apuesta > ficha:
                    apuesta -= ficha # disminuye la apuesta
                ganadas += 1
            else: # perdio
                apuesta += ficha # aumenta la apuesta              
            dinero_historico[i].append(dinero_actual)
            tiradas[i].append(j)
            frecuencia_historica[i].append(ganadas/j)
    return tiradas, dinero_historico, frecuencia_historica


# Si perdes -> sumas el valor de tus dos últimas apuestas. 
# Si ganas -> retrocedes dos posiciones en la serie (o te mantenes en 1).
def simular_fibonacci(num_tiradas, num_corridas, dinero_inicial, capital_infinito):
    dinero_historico = [[] for _ in range(num_corridas)]
    apuestas_historico = [[] for _ in range(num_corridas)]  # historial de apuestas
    tiradas = [[] for _ in range(num_corridas)]
    frecuencia_historica = [[] for _ in range(num_corridas)]
    
    for i in range (num_corridas):
        dinero_actual = dinero_inicial
        
        # las primeras 2 tiradas se realizan con un valor fijo predeterminado.
        apuesta = dinero_inicial/500        
        
        # definimos flag para saber si la segunda tirada resultó ganadora o perdedora. False -> perdedora, True -> ganadora
        flag = False
        
        ganadas = 0
        dinero_historico[i].append(dinero_inicial)
        tiradas[i].append(0)
        apuestas_historico[i].append(0)
        # calculamos los resultados de las dos primeras tiradas
        for j in range(1,3):
            dinero_actual -= apuesta
            valor = random.randint(0, 36)    
            if color_ruleta(valor) == 'rojo': # gano 
                dinero_actual += apuesta*2
                ganadas +=1
                if j == 2:
                    flag = True
            dinero_historico[i].append(dinero_actual)
            apuestas_historico[i].append(apuesta) 
            tiradas[i].append(j)
            frecuencia_historica[i].append(ganadas/j)
        
        if flag: # si la segunda tirada resulto ganadora, la tercera apuesta es igual a la primera
            apuesta = dinero_inicial/500
        else: # si la segunda tirada resulto perdedora, la tercera apuesta es la suma de las dos anteriores
            apuesta = apuestas_historico[i][1] + apuestas_historico[i][2]  
        apuestas_historico[i].append(apuesta) 
        

        # a partir de la tercera tirada se aplica la regla de fibonacci
        
        for j in range(3,num_tiradas + 1):
             
            if dinero_actual < apuesta and not capital_infinito:
                break  # No hay dinero para seguir apostando
            
            dinero_actual -= apuesta
            valor = random.randint(0, 36)
            
            if color_ruleta(valor) == 'rojo': # gano retroceder dos posiciones
                dinero_actual += apuesta*2
                apuesta = apuestas_historico[i][j-1]  
                ganadas +=1
            else: # perdio sumar las dos ultimas apuestas
                apuesta = apuestas_historico[i][j] + apuestas_historico[i][j-1]  
            
            dinero_historico[i].append(dinero_actual)
            apuestas_historico[i].append(apuesta)  
            tiradas[i].append(j)
            frecuencia_historica[i].append(ganadas/j)
    return tiradas, dinero_historico, frecuencia_historica

def simular_paroli(num_tiradas, num_corridas,dinero_inicial, capital_infinito):
    dinero_historico = [[] for _ in range(num_corridas)]
    tiradas = [[] for _ in range(num_corridas)]
    frecuencia_historica = [[] for _ in range(num_corridas)]

    
    for i in range (num_corridas):
        auxiliar_paroli = 1
        dinero_actual = dinero_inicial
        apuesta = 1
        ganadas = 0
        dinero_historico[i].append(dinero_inicial)
        tiradas[i].append(0)
        for j in range(1,num_tiradas + 1):
            if dinero_actual < apuesta and not capital_infinito:
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
                ganadas += 1
            else:# Perdió la apuesta, entonces vuelve a la apuesta inicial
                apuesta = 1
            dinero_historico[i].append(dinero_actual)
            tiradas[i].append(j)
            frecuencia_historica[i].append(ganadas/j)
    return tiradas, dinero_historico, frecuencia_historica
