import sys
import numpy as np
import matplotlib.pyplot as plt

# Verificación de argumentos de línea de comandos
if len(sys.argv) != 11 or sys.argv[1] != "-T" or sys.argv[3] != "-r" or sys.argv[5] != "-Q" or sys.argv[7] != "-p" or sys.argv[9] != "-c":
    print("Entrada incorrecta: python simulacion_inventarios.py -T <tiempo_simulacion> -r <nivel_reorden> -Q <cantidad_pedido> -p <num_corridas> -c <costos>")
    sys.exit(1)

try:
    tiempo_simulacion = int(sys.argv[2])
    nivel_reorden = int(sys.argv[4])
    cantidad_pedido = int(sys.argv[6])
    num_corridas = int(sys.argv[8])
    costos = list(map(float, sys.argv[10].split(',')))
    if len(costos) != 4:
        raise ValueError("Debe proporcionar exactamente cuatro costos")
except ValueError as e:
    print(f"Error en los argumentos: {e}")
    sys.exit(1)

c, k, p, h = costos

# Distribución empírica de la demanda
demanda_empirica = np.array([0, 1, 2, 3, 4])
probabilidad_empirica = np.array([1/6, 1/3, 1/3, 1/6, 0])

# Función para generar la demanda
def generar_demanda(rng):
    return rng.choice(demanda_empirica, p=probabilidad_empirica)

# Función para simular el sistema de inventarios
def simulate_inventory(T, r, Q, c, k, p, h, rng):
    inventario = 50
    costo_orden = 0
    costo_mantenimiento = 0
    costo_faltante = 0

    costo_orden_hist = []
    costo_mantenimiento_hist = []
    costo_faltante_hist = []
    costo_total_hist = []

    for t in range(1, T + 1):
        demanda = generar_demanda(rng)
        inventario -= demanda

        if inventario < 0:
            costo_faltante += abs(inventario) * p
            inventario = 0

        costo_mantenimiento += inventario * h

        if inventario <= r:
            costo_orden += k + Q * c
            inventario += Q

        costo_orden_hist.append(costo_orden)
        costo_mantenimiento_hist.append(costo_mantenimiento)
        costo_faltante_hist.append(costo_faltante)
        costo_total_hist.append(costo_orden + costo_mantenimiento + costo_faltante)

    return {
        'costo_orden': costo_orden_hist,
        'costo_mantenimiento': costo_mantenimiento_hist,
        'costo_faltante': costo_faltante_hist,
        'costo_total': costo_total_hist
    }

# Realizar las simulaciones
results = []
rng = np.random.default_rng()  # Inicializar el generador de números aleatorios
for _ in range(num_corridas):
    result = simulate_inventory(tiempo_simulacion, nivel_reorden, cantidad_pedido, c, k, p, h, rng)
    results.append(result)

# Promediar los resultados de las corridas
prom_costo_orden = np.mean([result['costo_orden'] for result in results], axis=0)
prom_costo_mantenimiento = np.mean([result['costo_mantenimiento'] for result in results], axis=0)
prom_costo_faltante = np.mean([result['costo_faltante'] for result in results], axis=0)
prom_costo_total = np.mean([result['costo_total'] for result in results], axis=0)

# Graficar los resultados
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(prom_costo_orden, label='Costo de Orden')
plt.xlabel('Tiempo')
plt.ylabel('Costo')
plt.title('Costo de Orden')
plt.legend()

plt.subplot(2, 2, 2)
plt.plot(prom_costo_mantenimiento, label='Costo de Mantenimiento')
plt.xlabel('Tiempo')
plt.ylabel('Costo')
plt.title('Costo de Mantenimiento')
plt.legend()

plt.subplot(2, 2, 3)
plt.plot(prom_costo_faltante, label='Costo de Faltante')
plt.xlabel('Tiempo')
plt.ylabel('Costo')
plt.title('Costo de Faltante')
plt.legend()

plt.subplot(2, 2, 4)
plt.plot(prom_costo_total, label='Costo Total')
plt.xlabel('Tiempo')
plt.ylabel('Costo')
plt.title('Costo Total')
plt.legend()

plt.tight_layout()
plt.show()
