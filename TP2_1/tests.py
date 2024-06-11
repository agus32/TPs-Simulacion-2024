import math
import scipy.stats as stats
import matplotlib.pyplot as plt
from PIL import Image

def bit_map(values: list[int], width=512, heigth=512, show_plot=True):
    assert len(values) >= width*heigth, f"La lista de valores tiene que tener {width*heigth} de largo"

    img = Image.new('RGB', (width, heigth), "black")
    pixels = img.load()
    
    k = 0
    for i in range(img.size[0]):    
        for j in range(img.size[1]):
            color = int(values[k] * 256)
            pixels[i, j] = (color, color, color) 
            k += 1
    
    if show_plot:
        img.show()

    return img.save

def media_test(values: list[float], show_plot=True):
    sequence_length = len(values)
    media = sum(values) / sequence_length
    
    # Media esperada para números en el intervalo [0, 1]
    media_esperada = 0.5
    
    # Calcular el intervalo de confianza
    alfa = 0.05  # nivel de significancia para 95% de confianza
    z = stats.norm.ppf(1 - alfa / 2)
    std_error = math.sqrt((1/12) / sequence_length)  # Desviación estándar de la media esperada
    
    lower_bound = media_esperada - z * std_error
    upper_bound = media_esperada + z * std_error
    
    result = "passed" if lower_bound <= media <= upper_bound else "failed"
    
    plt.figure(figsize=(10, 6))
    
    plt.hist(values, bins=50, alpha=0.75, label='Generated Numbers')
    plt.axvline(media, color='r', linestyle='--', label='Calculated Media')
    plt.axvline(media_esperada, color='g', linestyle='-', label='Expected Media')
    
    # Anotaciones
    plt.xlabel('Generated Numbers')
    plt.ylabel('Frequency')
    plt.title(f'Media Test: {result} (Media: {media:.5f})')
    plt.legend()
    plt.grid(True)
    
    if show_plot:
        plt.show()
    return plt.savefig

def varianza_test(values: list[float], show_plot=True):
    media = sum(values) / len(values)
    sequence_length = len(values)
    
    varianza = sum((x - media) ** 2 for x in values) / (sequence_length - 1)
    
    varianza_esperada = 1 / 12

    # Calcular el intervalo de confianza
    alfa = 0.05  # nivel de significancia para 95% de confianza
    chi2_lower = stats.chi2.ppf(alfa / 2, df=sequence_length - 1)
    chi2_upper = stats.chi2.ppf(1 - alfa / 2, df=sequence_length - 1)
    
    lower_bound = (sequence_length - 1) * varianza_esperada / chi2_upper
    upper_bound = (sequence_length - 1) * varianza_esperada / chi2_lower
    
    # Determinar si el generador pasa la prueba
    result = "passed" if lower_bound <= varianza <= upper_bound else "failed"
    
    # Graficar los resultados
    plt.figure(figsize=(10, 6))
    
    plt.hist(values, bins=50, alpha=0.75, label='Generated Numbers')
    plt.axvline(media, color='r', linestyle='--', label='Media')
    
    # Anotaciones
    plt.xlabel('Generated Numbers')
    plt.ylabel('Frequency')
    plt.title(f'Varianza Test: {result} (Varianza: {varianza:.5f}, Media: {media:.5f})')
    plt.legend()
    plt.grid(True)
   
    if show_plot:
        plt.show()
    return plt.savefig

def monobit(values, show_plot=True):
    bits = []
    for v in values:
        bits.append(1 if v >= 0.5 else 0)

    ones_count = sum(bits)
    bits_count = len(bits)
    
    zeroes_count = bits_count - ones_count
    S_n = ones_count - zeroes_count
    V = S_n / math.sqrt(bits_count)
    
    # Calculate the p-value
    p_value = stats.norm.sf(abs(V)) * 2  # two-sided test
    
    # Check if p-value is within the acceptable range (e.g., 0.01 to 0.99)
    if 0.01 < p_value < 0.99:
        result = "passed"
    else:
        result = "failed"
    
    # Plot the results
    plt.figure(figsize=(10, 6))
    
    # Proportion of '1's over the sequence
    proportions = [sum(bits[:i+1]) / (i+1) for i in range(bits_count)]
    plt.plot(proportions, label='Proportion of 1s')
    plt.axhline(0.5, color='r', linestyle='--', label='Expected Proportion')
    
    # Annotations
    plt.xlabel('Number of bits')
    plt.ylabel('Proportion of 1s')
    plt.title(f'Monobit Test: {result} (p-value: {p_value:.5f}, V: {V:.5f})')
    plt.legend()
    plt.grid(True)
   
    if show_plot:
        plt.show()
    return plt.savefig
