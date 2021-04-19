import ListaSimplementeEnlazada
import PalabraC
import PalabrasC
from colorama import Fore

class Registrador:

    def __init__(self):
        pass

class VectorDeListas:
    VectorPalabras = []
    def __init__(self,m):
        self.m = m
        self.RellenarVector(m)
        self.NumeroDeLinea = 1
    def RellenarVector(self,m):
        for i in range(0, m):
            Nuevo = PalabrasC.Palabras()
            self.VectorPalabras.append(Nuevo)

    def añadirPalabra(self, palabra):#Donde palabra es un objeto de tipo Palabra()
        if self.VectorPalabras[palabra.Llave(self.m)].first.value is None:
            self.VectorPalabras[palabra.Llave(self.m)].añadir(palabra)
            self.VectorPalabras[palabra.Llave(self.m)].first.value.Lineas.añadir(self.NumeroDeLinea)
            self.VectorPalabras[palabra.Llave(self.m)].first.value.Repeticiones += 1
        else:
            puntero = self.VectorPalabras[palabra.Llave(self.m)].first
            while True:
                if puntero.value.Letras.lower() == palabra.Letras.lower():
                    puntero.value.Repeticiones += 1
                    puntero.value.Lineas.añadir(self.NumeroDeLinea)
                    break
                if puntero.siguiente is None:
                    self.VectorPalabras[palabra.Llave(self.m)].añadir(palabra)
                    puntero.siguiente.value.Repeticiones += 1
                    puntero.siguiente.value.Lineas.añadir(self.NumeroDeLinea)
                    break
                puntero = puntero.siguiente
    def CrearPalabra(self, mensaje):
#Si hay un espacio revisar crear una nueva Palabra() 
        palabraN = PalabraC.Palabra()
        for i in range ( 0 , len(mensaje)): #las palabras se separan por espacios " "#y las lineas se separan por "\n"
            if mensaje[i] == " ":
                self.añadirPalabra(palabraN)
                palabraN = PalabraC.Palabra()
            if mensaje[i] == ".":
                self.añadirPalabra(palabraN)
                palabraN = PalabraC.Palabra()
            if mensaje[i] == "\n":
                self.añadirPalabra(palabraN)
                palabraN = PalabraC.Palabra()
                self.NumeroDeLinea += 1
            if mensaje[i] != " " and mensaje[i] != "\n" and mensaje[i] != ".":
                palabraN.Letras += mensaje[i]
            if i == len(mensaje) - 1:
                self.añadirPalabra(palabraN)

    def ImprimirVdL(self):
        for i in range(0,self.m):
            if self.VectorPalabras[i].first.value is not None:
                puntero = self.VectorPalabras[i].first
                while True:
                    print(Fore.WHITE + puntero.value.Letras, end="")
                    t = 15 - len(puntero.value.Letras)
                    m = ""
                    m += " "*t
                    print(Fore.GREEN + m + 'se repite', end=" ")
                    print(Fore.WHITE + str(puntero.value.Repeticiones), end=" ")
                    print(Fore.GREEN + 'veces y Aparece en las lineas :', end=" ")

                    print(Fore.WHITE + puntero.value.Lineas.Str())
                    puntero = puntero.siguiente
                    if puntero is None:
                        break
    def MostrarPalabrasEnMensaje(self, mensaje):
        self.CrearPalabra(mensaje)
        print("El mensaje es: ")
        print(mensaje)
        print("Las palabras en su orden son: ")
        self.ImprimirVdL()




#archivo-salida.py
f = open ('holamundo.txt','r')
mensaje = f.read()
f.close()
Final = VectorDeListas(10)
Final.MostrarPalabrasEnMensaje(mensaje)