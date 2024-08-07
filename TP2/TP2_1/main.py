import sys
import random
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from generators import CuadradosMedios, GLCGenerator
from tests import bit_map, monobit, media_test, varianza_test

generators = {
    "cm": CuadradosMedios,
    "glc": GLCGenerator,
    "lib": random.Random
}

generators_args = {
    "cm": ["-n"],
    "glc": ["-m", "-c", "-a"],
    "lib": []
}

tests = {
    "bitmap": bit_map,
    "monobit": monobit,
    "media": media_test,
    "varianza": varianza_test
}

def USAGE():
    print("""
        python cli.py -G <generador> -S <seed> <...args> -N <int> -T <test>

        Parametros opcionales:
          --save-image
            Guarda el resultado del test en results/ con un nombre adecuado

        -N: cantidad de números que vamos a generar
        
        -S: Semilla del generador
    
        -T: Test a realizar
              bitmap
              monobit
              media
              varianza

        -G: Generador utilizado

          cm: Cuadrados Medios
              -n: precisión 
          glc: Generador lineal congruencial
              -m: modulo
              -a: multiplicador
              -c: incremento
          lib: Libreria random de python
    """)

def get_arg(arg: str):
    try:
        index = sys.argv.index(arg)
    except ValueError:
        print(f"No se encuentra el argumento {arg}")
        USAGE()
        exit(1)

    if len(sys.argv) < index+1:
        print(f"No se encuentra el argumento {arg}")
        USAGE()
        exit(1)

    return sys.argv[index+1]

def main() -> int:
    if len(sys.argv) < 8:
        print("No hay suficientes argumentos")
        USAGE()
        exit(1)

    gen_name = get_arg("-G")
    seed = int(get_arg("-S"))
    N = int(get_arg("-N"))
    test_name = get_arg("-T")

    if gen_name not in generators:
        print(f"{gen_name} no es un generador válido")
        USAGE()
        exit(1)

    if test_name not in tests:
        print(f"{test_name} no es un test válido")
        USAGE()
        exit(1)

    args = {}
    for arg_name in generators_args[gen_name]:
        args[arg_name.replace('-', '')] = int(get_arg(arg_name))

    generator_class = generators[gen_name]
    g = generator_class(seed, **args)

    values = []
    for _ in range(N):
        values.append(g.random())

    if "--save-image" in sys.argv:
        save_func = tests[test_name](values, show_plot=False)
        save_func(f"results/{gen_name}_{test_name}.png", format="png")
        return 0

    tests[test_name](values)
    
    return 0

if __name__ == "__main__":
    main()
