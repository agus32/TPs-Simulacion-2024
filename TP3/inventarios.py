import random
import matplotlib.pyplot as plt

INF = 1.0e30

setup_cost=0
shortage_cost=0 # p
holding_cost=0
unit_cost=0
s=3
S=10

max_time = 36

mean_interdemand = 0.8

inv_level = 10
sim_time = 0.0
amount = 0

I_plus  = [max(inv_level, 0)]
I_minus = [max(-inv_level, 0)]
inv_levels = [inv_level]
times = [0.0]

time_next_event: dict[str, float] = {
    "demand": random.expovariate(mean_interdemand),
    "order_arrival": INF,
    "evaluation": 1
}

def random_empiric():
    r = random.random()
    
    if r < 1/6:
        return 1
    elif r < 1/2:  # 1/6 + 1/3 = 1/2
        return 2
    elif r < 5/6:  # 1/2 + 1/3 = 5/6
        return 3
    else:
        return 4

def demand():
    global inv_level

    inv_level -= random_empiric()
    time_next_event["demand"] = sim_time + random.expovariate(mean_interdemand) 

def order_arrival():
    global inv_level

    inv_level += amount
    time_next_event["order_arrival"] = INF

def evaluation():
    global amount 

    if inv_level < s: 
        amount = S - inv_level;
        # total_ordering_cost += setup_cost + incremental_cost * amount;
        time_next_event["order_arrival"] = sim_time + random.uniform(0.5, 1)
    time_next_event["evaluation"] += 1.0

def update_graph_values():
    I_plus.append(max(inv_level, 0)+0.1)
    I_minus.append(max(-inv_level, 0)+0.1)
    inv_levels.append(inv_level)
    times.append(sim_time)

def get_next_event_type() -> str:
    min = INF
    event = ""
    for k in time_next_event:
        if time_next_event[k] < min:
            min = time_next_event[k]
            event = k

    return event

def graph():
    plt.plot(times, inv_levels, marker=',')
    plt.plot([i+0.1 for i in times], I_plus, linestyle=':', marker=',', color='red')
    plt.plot([i+0.1 for i in times], I_minus, marker=',', color='green')
    plt.title('Inventario vs Tiempo')
    plt.xlabel('Tiempo (Meses)')
    plt.ylabel('Inventario')
    plt.grid(True)
    plt.show()

def main():
    global sim_time

    while sim_time < max_time:
        next_event = get_next_event_type()
        
        if next_event == "demand":
            sim_time = time_next_event["demand"]
            update_graph_values()
            demand()
        elif next_event == "order_arrival":
            sim_time = time_next_event["order_arrival"]
            update_graph_values()
            order_arrival()
        elif next_event == "evaluation":
            sim_time = time_next_event["evaluation"]
            evaluation()
        update_graph_values()

        print(sim_time)

if __name__ == "__main__":
    main()
    graph()
