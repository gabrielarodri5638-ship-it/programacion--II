class ecuacionlineal:
    def __init__(self,a,b,c,d,e,f):
        self.__a=a
        self.__b=b
        self.__c=c
        self.__d=d
        self.__e=e
        self.__f=f

    def solucion(self):
        denominador=(self.__a*self.__d)-(self.__b*self.__c)
        if denominador !=0:
            return True
        else:
            return False
    def getX(self):
        num=(self.__e*self.__d)-(self.__b*self.__f)
        dem=(self.__a*self.__d)-(self.__b*self.__c)
        return num/dem
    def getY(self):
        num=(self.__a*self.__f)-(self.__e*self.__c)
        dem=(self.__a*self.__d)-(self.__b*self.__c)
        return num/dem
while True: 
    A=float(input("ingrese coeficiente A: "))
    B=float(input("ingrese coeficiente B: "))
    C=float(input("ingrese coeficiente C: "))
    D=float(input("ingrese coeficiente D: "))
    E=float(input("ingrese coeficiente E: "))
    F=float(input("ingrese coeficiente F: "))
    
    ecuacion=ecuacionlineal(A,B,C,D,E,F)
    if ecuacion.solucion(): 
        print("X= ",ecuacion.getX(),"Y= ",ecuacion.getY())
    else:
        print("LA ECUACION NO TIENE SOLUCION ERROR !!!!!")
