
# En este archivo van todas cosas orientadas a la mecanica de la ruleta.

def color_ruleta(numero):
    if numero == 0:
        return 'verde'
    elif (numero >= 1 and numero <= 10) or (numero >= 19 and numero <= 28):
        return 'rojo' if numero % 2 != 0 else 'negro'
    elif (numero >= 11 and numero <= 18) or (numero >= 29 and numero <= 36):
        return 'rojo' if numero % 2 == 0 else 'negro'