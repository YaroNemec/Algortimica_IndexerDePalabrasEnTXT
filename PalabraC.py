import ListaSimplementeEnlazada
import hashlib

class Palabra:

    def __init__(self):
        self.Repeticiones = 0
        self.Lineas = ListaSimplementeEnlazada.Lista1Enlace()
        self.Letras = ""

    def Llave(self,m):#FunciónHash
        a = hashlib.md5(self.Letras.lower().encode())
        indice = int(a.hexdigest(),16)%m
        return indice
        
"""
list = Palabra()
lista = Palabra()
lista.Lineas.añadir(15)
lista.Lineas.añadir(25)
lista.Lineas.añadir(35)
list.Lineas.añadir(18)
list.Lineas.añadir(17)
list.Lineas.añadir(19)
print(lista.Lineas.Str())
"""