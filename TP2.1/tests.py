import math
import scipy.stats as stats
import matplotlib.pyplot as plt
from PIL.Image import Image

from generators import CuadradosMedios, GLCGenerator

def bit_map(values: list[int], width=512, heigth=512):
    assert len(values) >= width*heigth, f"La lista de valores tiene que tener {width*heigth} de largo"

    img = Image.new('RGB', (width, heigth), "black")
    pixels = img.load()
    
    k = 0
    for i in range(img.size[0]):    # For every pixel:
        for j in range(img.size[1]):
            color = int(values[k] * 256)
            pixels[i, j] = (color, color, color) # Set the colour accordingly
            k += 1

    img.show()

def monobit_test(values):
    bits = []
    for v in values:
        bits.append(1 if v >= 0.5 else 0)

    ones_count = sum(bits)

    bits_count = len(bits)
    
    # Calculate the test statisti
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
    
    plt.show()
    
    return p_value

if __name__ == "__main__":
    glc = GLCGenerator(10, 2**31-1, 12345, 1103515245)
    values = glc.next_n(1000)
    monobit_test(values)
