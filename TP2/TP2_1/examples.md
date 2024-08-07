# Pruebas que se pueden realizar

## GLC:

### Bit Map
`python main.py -G glc -S 123482913 -m 2147483647 -a 1103515245 -c 12345 -n 10 -N 262144 -T bitmap`

### media
`python main.py -G glc -S 123482913 -m 2147483647 -a 1103515245 -c 12345 -n 10 -N 262144 -T media`

### varianza
`python main.py -G glc -S 123482913 -m 2147483647 -a 1103515245 -c 12345 -n 10 -N 262144 -T varianza`

## Cuadrados medios:

### Bit Map
`python main.py -G cm -S 44504050138512839321 -n 20 -N 262144 -T bitmap`

## Libreria random de python

### Bit map
`python main.py -G lib -S 12398149 -N 262144 -T bitmap`
