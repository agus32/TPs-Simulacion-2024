## Uso
`python cli.py -G <generador> -S <seed> <...args> -N <int> -T <test>`

-N: cantidad de números que vamos a generar

-S: Semilla del generador

-T: Test a realizar
    bitmap

-G: Generador utilizado

    cm: Cuadrados Medios
        -n: precisión 
    glc: GLC
        -m: modulo
        -a: multiplicador
        -c: incremento

## [Ejemplos](./examples.md)

## Instalacion 
`python -m venv .venv`
`source .venv/bin/activate`
`pip install -r requirements.txt`

### Eliminar el entorno
`deactivate`
`rm -r .venv/`
