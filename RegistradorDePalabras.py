import ListaSimplementeEnlazada

class Registrador:

    def __init__(self):
        pass

class VectorDeListas:
    VectorPalabras = [Palabras() for i in range(5000)]
    def __init__(self):
        pass
    def añadirPalabra(self, palabra, NumeroDeLinea):#Donde palabra es un objeto de tipo Palabra()
        if self.VectorPalabras[palabra.Llave()].vacio(): 
            self.VectorPalabras[palabra.Llave()].añadir(palabra)
        else:
            puntero = self.VectorPalabras[palabra.Llave()].first()
            while True:
                if puntero.value.Letras == palabra.Letras:
                    puntero.value.Repeticiones += 1
                    puntero.value.Lineas.añadir(NumeroDeLinea)
                    break
                if puntero.siguiente is None 
                    self.VectorPalabras[palabra.Llave()].añadir(palabra)
                    break
                puntero = puntero.siguiente


class Palabra():
    Repeticiones = 0
    Lineas = ListaSimplementeEnlazada.Lista1Enlace
    Letras= ""
    def __init__(self):
        pass
    def Llave(self):#FunciónHash 
        pass

class Palabras(ListaSimplementeEnlazada.Lista1Enlace):
    def __init__(self):
        pass