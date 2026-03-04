import math
class estadistica:
    def __init__(self,lista):
        self.__datos=lista

    def promedio(self):
        n=len(self.__datos)
        sum=0
        for i in range (n):
            sum=sum+self.__datos[i]
        return sum/n
    def desviacion(self):
        prom=self.promedio()
        n=len(self.__datos)
        num=0
        for i in range (n):
            num=num+(self.__datos[i]-prom)**2
        return math.sqrt(num/(n-1))
    
while True:
    print("ingrese 10 numeros: ")
    lista=[]
    for i in range (10):
        numero = float(input(f"Número {i+1}: "))
        lista.append(numero)
    calcular=estadistica(lista)
    print("el promedio es: ", calcular.promedio())
    print("la desviacion es: ", calcular.desviacion())
            
