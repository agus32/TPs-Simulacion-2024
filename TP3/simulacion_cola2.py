import random
import queue

def simular_mm1(lambda_, mu, tiempo_simulacion):
    # Inicialización de variables
    tiempo_actual = 0.0
    tiempo_proxima_llegada = random.expovariate(lambda_)
    tiempo_proxima_salida = float('inf')
    num_clientes_en_sistema = 0
    num_clientes_en_cola = 0
    tiempo_acumulado_en_sistema = 0.0
    tiempo_acumulado_en_cola = 0.0
    tiempo_total_ocupado = 0.0

    cola = queue.Queue()

    while tiempo_actual < tiempo_simulacion:
        if tiempo_proxima_llegada < tiempo_proxima_salida:
            # Evento de llegada
            tiempo_actual = tiempo_proxima_llegada
            num_clientes_en_sistema += 1

            if num_clientes_en_sistema > 1:
                num_clientes_en_cola += 1
                cola.put(tiempo_actual)
            else:
                tiempo_proxima_salida = tiempo_actual + random.expovariate(mu)
                tiempo_total_ocupado += tiempo_proxima_salida - tiempo_actual

            tiempo_proxima_llegada = tiempo_actual + random.expovariate(lambda_)
        else:
            # Evento de salida
            tiempo_actual = tiempo_proxima_salida
            num_clientes_en_sistema -= 1

            if num_clientes_en_sistema > 0:
                tiempo_llegada_cola = cola.get()
                num_clientes_en_cola -= 1
                tiempo_acumulado_en_cola += tiempo_actual - tiempo_llegada_cola
                tiempo_proxima_salida = tiempo_actual + random.expovariate(mu)
                tiempo_total_ocupado += tiempo_proxima_salida - tiempo_actual
            else:
                tiempo_proxima_salida = float('inf')

        # Actualizar estadísticas
        tiempo_acumulado_en_sistema += num_clientes_en_sistema * (min(tiempo_proxima_llegada, tiempo_proxima_salida) - tiempo_actual)

    # Calcular métricas
    promedio_num_en_sistema = tiempo_acumulado_en_sistema / tiempo_simulacion
    promedio_num_en_cola = tiempo_acumulado_en_cola / tiempo_simulacion
    utilizacion = tiempo_total_ocupado / tiempo_simulacion

    return {
        'promedio_numero_en_sistema': promedio_num_en_sistema,
        'promedio_numero_en_cola': promedio_num_en_cola,
        'utilizacion': utilizacion,
    }

# Ejemplo de uso
resultados = simular_mm1(2, 3, 1000)
print(resultados)
