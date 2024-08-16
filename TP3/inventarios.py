import random
import matplotlib.pyplot as plt

INF = 1.0e30
max_time = 36

mean_interdemand = 0.8
s = 7   # Cantidad en la que se realiza pedido
S = 10  # Capacidad del inventario

setup_cost = 7      # k
shortage_cost = 10  # p
holding_cost = 5    # h
unit_cost = 3       # i

inv_level = 10
sim_time = 0.0
amount = 0  # Cantidad a pedir (Z)

shortages_costs: list[float] = [0]  # I-
holding_costs: list[float] = [0]    # I+
unit_costs: list[float] = [0]       # iZ
total_costs: list[float] = [0]      # C

I_plus = [max(inv_level, 0)]
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
        amount = S - inv_level
        # total_ordering_cost += setup_cost + incremental_cost * amount;
        time_next_event["order_arrival"] = sim_time + random.uniform(0.5, 1)
    time_next_event["evaluation"] += 1.0


def update_graph_values():
    i_plus = max(inv_level, 0)+0.1
    i_minus = max(-inv_level, 0)+0.1

    I_plus.append(i_plus)
    I_minus.append(i_minus)
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


def update_prom_values():
    unit_costs.append(amount * unit_cost)
    i_plus = I_plus[len(I_plus) - 1]
    i_minus = I_minus[len(I_minus) - 1]

    holding_costs.append(i_plus * holding_cost)
    shortages_costs.append(i_minus * shortage_cost)
    total_costs.append(amount * unit_cost + i_plus * holding_cost + i_minus * shortage_cost)


def graph_inventory():
    plt.plot(times, inv_levels, marker=',', label='Inv. level')
    plt.plot([i+0.1 for i in times], I_plus, linestyle=':', marker=',', color='r', label='I+')
    plt.plot([i+0.1 for i in times], I_minus, marker=',', color='g', label='I-')

    plt.title('Inventario vs Tiempo')
    plt.xlabel('Tiempo (Meses)')
    plt.ylabel('Inventario')
    plt.grid(True)
    plt.legend()
    plt.show()


def graph_costs():
    plt.plot(total_costs, color='b', linestyle='--',
             label=f'Avg. Total cost = {calc_prom(total_costs, sim_time):.2f}')
    plt.plot(holding_costs, color='r', linestyle='--',
             label=f'Avg. Holding cost = {calc_prom(holding_costs, sim_time):.2f}')
    plt.plot(shortages_costs, color='g', linestyle='--',
             label=f'Avg. Shortage cost = {calc_prom(shortages_costs, sim_time):.2f}')
    plt.plot(unit_costs, color='orange', linestyle='--',
             label=f'Avg. Unit cost = {calc_prom(unit_costs, sim_time):.2f}')
    # plt.axhline(y=setup_cost, color='blue', label=f'Setup cost = {setup_cost:.2f}')

    plt.title('Costos vs Tiempo')
    plt.xlabel('Tiempo (Meses)')
    plt.ylabel('Costos')
    plt.grid(True)
    plt.legend()
    plt.show()


def calc_prom(values: list[float], n: int):
    prev = values[0]
    sum = 0.0
    for level in values:
        if level != prev:
            sum += level
            prev = level

    return sum / n


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
        update_prom_values()

        print(sim_time)


if __name__ == "__main__":
    main()
    graph_inventory()
    graph_costs()
