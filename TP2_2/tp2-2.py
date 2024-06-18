import matplotlib.pyplot as plt
import numpy as np
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from TP2_1.generators import GLCGenerator
from distribucionUniforme import grafica_distribucionUniforme
from distribucionExponencial import grafica_distribucionExponencial
from distribucionGamma import grafica_distribucionGamma
from distribucionNormal import grafica_distribucionNormal
from distribucionBinomial import grafica_distribucionBinomial
from distribucionHipergeometrica import grafica_distribucionHipergeometrica
from distribucionPoisson import grafica_distribucionPoisson
from distribucionEmpiricaDiscreta import grafica_distribucionEmpiricaDiscreta

glc = GLCGenerator(10, 2**31-1, 12345, 1103515245)


exit()
grafica_distribucionUniforme()
grafica_distribucionExponencial()
grafica_distribucionGamma()
grafica_distribucionNormal()
#pascal
grafica_distribucionBinomial()
grafica_distribucionHipergeometrica()
grafica_distribucionPoisson()
grafica_distribucionEmpiricaDiscreta()