class Coordenada:
    # Método constructor
    def __init__(self, x, y):
        self.__X = x
        self.__Y = y

    # Método de acceso
    def getX(self):
        return self.__X

    def setX(self, x):
        self.__X = x

    def getY(self):
        return self.__Y

    def setY(self, y):
        self.__Y = y

    # Método para mostrar la coordenada
    def mostrarCoordenada(self):
        print("(",self.__X,",",self.__Y, ")")
