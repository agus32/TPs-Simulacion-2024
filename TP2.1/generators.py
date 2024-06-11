class CuadradosMedios():
    def __init__(self, seed, n):
        s = seed
        for _ in range(n):
            assert s > 0, f"La semilla no puede tener menos de {n} digitos"
            s = s // 10 #Division truncando el resultado

        self.seed = seed
        self.n = n
        self.x = seed

    def next(self) -> float:
        next_x = self.x**2

        digits = 0
        while next_x > 0:
            next_x = next_x // 10
            digits += 1

        gap = (digits - self.n) // 2 #Cuantos digitos tenemos que sacar de cada lado
        self.x **= 2
        self.x = self.x % (10**(digits-gap)) #Sacamos los primeros gap digitos
        self.x = self.x // 10**gap #Sacamos los ultimos gap digitos

        max_value = 10**(self.n+1) - 1
        return self.x / max_value

    def next_n(self, n) -> list[int]:
        values = []
        for _ in range(n):
            values.append(self.next())
        return values
    
class GLCGenerator():
    def __init__(self, seed, m, c, a):
        assert m > 0, "El modulo debe ser > 0"
        assert a < m, "El multiplicador debe ser menor al modulo"
        assert a > 0, "El multiplicador debe ser > 0"
        assert c < m, "El incremento debe ser menor al modulo"
        assert c >= 0, "El incremento debe ser >= 0"
        assert seed < m, "La semilla debe ser menor al modulo"
        assert seed >= 0, "La semilla debe ser >= 0"

        self.seed = seed
        self.x = seed
        self.module = m
        self.c = c
        self.a = a

    def seed(self, seed):
        self.seed = seed

    def next(self) -> float:
        self.x = (self.a*self.x + self.c) % self.module 
        return self.x / self.module

    def next_n(self, n) -> list[int]:
        values = []
        for _ in range(n):
            values.append(self.next())
        return values

if __name__ == "__main__":
    glc = GLCGenerator(10, 2**31-1, 12345, 1103515245)
    values = glc.next_n(1000)
    for v in values:
        assert v < 1 and v > 0, "numero fuera del rango"

    cm = CuadradosMedios(44504050138512839321, 20)
    values = cm.next_n(10000)
    print(values)
    for v in values:
        assert v < 1 and v > 0, "numero fuera del rango"
