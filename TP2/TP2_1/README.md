## Uso
```text
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
    glc: GLC
        -m: modulo
        -a: multiplicador
        -c: incremento
    lib: Libreria random de python
```

## [Ejemplos](./examples.md)

## Instalacion 
1. Inicializar entorno virtual
```bash
python -m venv .venv
```

2. Activar el entorno virtual
```bash
source .venv/bin/activate
```

3. Instalar requerimientos
```bash
pip install -r requirements.txt`
```

### Eliminar el entorno
```bash
deactivate
```
```bash
rm -r .venv/
```
