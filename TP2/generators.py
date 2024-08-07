class CuadradosMedios():
    def __init__(self, seed, n):
        s = seed
        for _ in range(n):
            assert s > 0, f"La semilla no puede tener menos de {n} digitos"
            s = s // 10 #Division truncando el resultado

        self.n = n
        self.x = seed

    def _get_count_digits(self, x: int) -> int:
        digits = 0
        while x > 0:
            x = x // 10 #Division truncando el resultado
            digits += 1
        return digits

    def random(self) -> float:
        next_x = self.x**2

        digits = self._get_count_digits(next_x)

        gap = (digits - self.n) // 2 #Cuantos digitos tenemos que sacar de cada lado
        self.x **= 2
        self.x = self.x % (10**(digits-gap)) #Sacamos los primeros gap digitos
        self.x = self.x // 10**gap #Sacamos los ultimos gap digitos

        digits = self._get_count_digits(self.x)

        max_value = 10**digits - 1
        return self.x / max_value
    
class GLCGenerator():
    def __init__(self, seed, m, c, a):
        assert m > 0, "El modulo debe ser > 0"
        assert a < m, "El multiplicador debe ser menor al modulo"
        assert a > 0, "El multiplicador debe ser > 0"
        assert c < m, "El incremento debe ser menor al modulo"
        assert c >= 0, "El incremento debe ser >= 0"
        assert seed < m, "La semilla debe ser menor al modulo"
        assert seed >= 0, "La semilla debe ser >= 0"

        self.x = seed
        self.module = m
        self.c = c
        self.a = a  
    
    
    def seed(self, seed):
        self.seed = seed

    def random(self) -> float:
        self.x = (self.a*self.x + self.c) % self.module 
        return self.x / self.module

if __name__ == "__main__":
    glc = GLCGenerator(10, 2**31-1, 12345, 1103515245)
    for _ in range(1000):
        v = glc.random()
        assert v < 1 and v > 0, "numero fuera del rango"

    cm = CuadradosMedios(44504050138512839321, 20)
    for _ in range(1000):
        v = cm.random()
        assert v < 1 and v > 0, "numero fuera del rango"
