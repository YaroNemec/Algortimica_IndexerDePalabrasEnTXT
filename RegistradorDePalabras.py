import ListaSimplementeEnlazada
import PalabraC
import PalabrasC


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
        if self.VectorPalabras[palabra.Llave()].first.value is None:
            self.VectorPalabras[palabra.Llave()].añadir(palabra)
        else:
            puntero = self.VectorPalabras[palabra.Llave()].first
            while True:
                if puntero.value.Letras == palabra.Letras:
                    puntero.value.Repeticiones += 1
                    puntero.value.Lineas().añadir(self.NumeroDeLinea)
                    break
                if puntero.siguiente is None:
                    self.VectorPalabras[palabra.Llave()].añadir(palabra)
                    puntero.value.Lineas().añadir(self.NumeroDeLinea)
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
                self.NumeroDeLinea += 1
                palabraN = PalabraC.Palabra()
            else:
                palabraN.Letras += mensaje[i]
    def ImprimirVdL(self):
        for i in range(0,self.m):
            if self.VectorPalabras[i].first.value is None:
                pass
            else:
                puntero = self.VectorPalabras[i].first
                while True:
                    print(puntero.value.Letras," se repite ", puntero.value.Repeticiones,"Aparece en las lineas :" , puntero.value.Lineas().Str() + " , ")
                    if puntero.siguiente is  None:
                        break
                    puntero = puntero.siguiente
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