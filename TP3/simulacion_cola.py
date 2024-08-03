import sys
import numpy as np
import matplotlib.pyplot as plt


if len(sys.argv) != 7 or sys.argv[1] != "-p" or sys.argv[3] != "-c" or sys.argv[5] != "-t":
    print("Entrada incorrecta: python simulacion_cola.py -p <factor de utilizacion> -c <numero de corridas> -t <tiempo de simulacion>")
    sys.exit(1)

factor_utilizacion = float(sys.argv[2])
num_corridas = int(sys.argv[4])
tiempo_simulacion = int(sys.argv[6])


if(float(sys.argv[2]) <= 0.0 or float(sys.argv[2]) > 1.25):
    print("Factor de utilizacion no valido")
    sys.exit(1)

# Parámetros de la simulación
mu = 1.0  # Tasa de servicio
lambda_ = factor_utilizacion * mu  # Tasa de arribo ajustada

# Función para simular el sistema M/M/1
def simulate_mm1(lambda_, mu, simulation_time, rng):
    arrival_times = np.cumsum(rng.exponential(1 / lambda_, int(lambda_ * simulation_time * 2)))
    service_times = rng.exponential(1 / mu, int(lambda_ * simulation_time * 2))
    
    # Inicialización de variables
    clock = 0.0
    server_busy = False
    num_in_system = 0
    num_in_queue = 0
    total_time_in_system = 0
    total_time_in_queue = 0
    num_customers_served = 0
    utilization = 0
    state_times = []
    state_counts = np.zeros(int(simulation_time + max(service_times)) + 1)
    
    arrival_index = 0
    departure_index = 0
    next_arrival = arrival_times[arrival_index]
    next_departure = float('inf')
    
    while clock < simulation_time:
        if next_arrival < next_departure:
            clock = next_arrival
            if not server_busy:
                server_busy = True
                next_departure = clock + service_times[departure_index]
                utilization += next_departure - clock
            else:
                num_in_queue += 1
            arrival_index += 1
            next_arrival = arrival_times[arrival_index]
        else:
            clock = next_departure
            if num_in_queue > 0:
                num_in_queue -= 1
                next_departure = clock + service_times[departure_index]
                utilization += next_departure - clock
            else:
                server_busy = False
                next_departure = float('inf')
            total_time_in_system += clock - arrival_times[departure_index]
            total_time_in_queue += clock - arrival_times[departure_index] - service_times[departure_index]
            num_customers_served += 1
            departure_index += 1
        
        num_in_system = (num_in_queue + 1) if server_busy else num_in_queue
        if int(clock) < len(state_counts):
            state_counts[int(clock)] += 1
        state_times.append((clock, num_in_system))
    
    avg_num_in_system = total_time_in_system / simulation_time
    avg_num_in_queue = total_time_in_queue / simulation_time
    avg_time_in_system = total_time_in_system / num_customers_served
    avg_time_in_queue = total_time_in_queue / num_customers_served
    utilization /= simulation_time
    
    return {
        'avg_num_in_system': avg_num_in_system,
        'avg_num_in_queue': avg_num_in_queue,
        'avg_time_in_system': avg_time_in_system,
        'avg_time_in_queue': avg_time_in_queue,
        'utilization': utilization,
        'state_times': state_times,
        'state_counts': state_counts / simulation_time
    }

# Realizar las simulaciones
results = []
rng = np.random.default_rng()  # Inicializar el generador de números aleatorios
for _ in range(num_corridas):
    result = simulate_mm1(lambda_, mu, tiempo_simulacion, rng)
    results.append(result)

# Graficar los resultados
metrics = ['avg_num_in_system', 'avg_num_in_queue', 'avg_time_in_system', 'avg_time_in_queue', 'utilization']
for metric in metrics:
    values = [result[metric] for result in results]
    plt.plot(range(1, num_corridas + 1), values, label=f'λ = {lambda_:.2f}')
    plt.xlabel('Corrida')
    plt.ylabel(metric.replace('_', ' ').capitalize())
    plt.title(f'Histórico de {metric.replace("_", " ").capitalize()}')
    plt.legend()
    plt.show()

# Graficar la distribución del número de clientes en cola
plt.figure()
avg_state_counts = np.mean([result['state_counts'] for result in results], axis=0)
plt.plot(avg_state_counts, label=f'λ = {lambda_:.2f}')
plt.xlabel('Número de clientes en el sistema')
plt.ylabel('Probabilidad')
plt.title('Distribución del número de clientes en el sistema')
plt.legend()
plt.show()