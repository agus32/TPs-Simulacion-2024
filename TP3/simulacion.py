import numpy as np
import queue

lambda_  = 1  
simulation_time = 1000
mu = 1.5 

rng = np.random.default_rng()
arrivals = rng.exponential(1 / lambda_, int(lambda_ * simulation_time * 2))
services = rng.exponential(1 / mu, int(lambda_ * simulation_time * 2))

print(arrivals)
print(services)

def simulate():
    state = False
    len_queue = 0
    cant_delayed = 0
    total_delay = 0
    clock = 0.0

    i = 0
    j = 0
    next_arrival = arrivals[i]
    next_departure = float('inf')

    q = queue.Queue()

    while clock < simulation_time:
        clock += min(next_arrival, next_departure)
        if next_arrival < next_departure:
            next_arrival = clock + arrivals[i] 
            i += 1
            q.put(next_arrival)
        if next_departure < next_arrival:
            q.get()
    
        if q.empty():
            next_departure = clock + services[j] 
            j += 1
        e = q.get()
