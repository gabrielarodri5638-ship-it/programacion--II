import time
import random
class Cronometro:
    def __init__(self):
        self.__inicia = time.time() * 1000
        self.__finaliza = self.__inicia
    def get_inicia(self):
        return self.__inicia
    def get_finaliza(self):
        return self.__finaliza
    def inicia(self):
        self.__inicia = time.time() * 1000
    def detener(self):
        self.__finaliza = time.time() * 1000
    def lapsoDeTiempo(self):
        return int(self.__finaliza - self.__inicia)
print("TEST DE ORDENACIÓN")
cantidad = 10000 
print(f"Generando {cantidad} números...")
numeros = [random.randint(1, 1000000) for _ in range(cantidad)]
reloj = Cronometro()
reloj.inicia() 
print("Ordenando por selección... espera unos segundos...")
n = len(numeros)
for i in range(n):
    min_idx = i
    for j in range(i + 1, n):
        if numeros[j] < numeros[min_idx]:
            min_idx = j
    numeros[i], numeros[min_idx] = numeros[min_idx], numeros[i]
reloj.detener()
print("Punto de inicio:", reloj.get_inicia(), "ms")
print("Punto de fin:   ", reloj.get_finaliza() ,"ms") 
print("TIEMPO TOTAL:   ", reloj.lapsoDeTiempo() ,"milisegundos")
