# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 09:55:55 2021
@author: nemec
"""
import time 

class Node:
    
    def __init__(self,value, siguiente):
        self.value = value
        self.siguiente = siguiente
        
    def value(self):
        return self.value
    
    def set_value(self, value):
        self.value = value
    
    def siguiente(self):
        return next
    
    def set_siguiente(self, nuevo):
        self.siguiente = nuevo
    
class Lista1Enlace:
    first = Node(None, None)
    last = Node(None, None)
    def __init__(self):
        pass
        
    def vacio(self):
        if self.first.value is None :
            return True
        else:
            return False
    
    def añadir(self, valor): #Añade un elemento al final
        nuevo = Node(valor, None)
        #print('Estamos en añadir queremos ingresar el valor ', valor)
        if self.first.value is None :#3
            self.first = nuevo
            self.last = self.first
           # print('Se agrego a nuevo')
        else:            #2n
            self.last.siguiente = nuevo
            self.last = nuevo
          #  print('Se agrego a cola')
            #eficiencia = 6 + 3n 
    def añadirOrdenado(self, valor): #Añade de forma ordenada un elemento
        nuevo = Node(valor, None)
        print('Estamos en añadir ordenado queremos ingresar el valor ', valor)
        if self.first.value is None :
            print('Se agrego a nuevo')
            self.first = nuevo
            self.last = self.first
            
        else:            
            if(valor < self.first.value):
                nuevo.siguiente = self.first 
                self.first = nuevo
                print('Se agrego al principio')
            elif(valor > self.last.value):
                self.last.siguiente = nuevo
                self.last = nuevo
                print('Se agrego a cola')
            else:
                puntero = self.first
                while(puntero.siguiente.value < valor):
                    puntero = puntero.siguiente
                print('Se agrego entre los nodos con valor',puntero.value , ' y ', puntero.siguiente.value )
                nuevo.siguiente = puntero.siguiente
                puntero.siguiente = nuevo
                     
    def eliminarUltimo(self):
        if self.first.value is None :
            print('La lista está vacia')
        else:            
            puntero = self.first
            while(puntero.siguiente != self.last):
                puntero = puntero.siguiente
            puntero.siguiente = None
            self.last = puntero
            print('Se eliminó el ultimo elemento')
    
    def eliminarConValor(self, valor):
        existe = True#1
        if self.first.value is None :#2
            print('La lista está vacia')
        else:            
            puntero = self.first#3
            print()
            print('Se eliminara el primer elemento que contenga el numero ', valor)
            if puntero.value == valor:#4
                self.first = self.first.siguiente
            else:
                while(puntero.siguiente.value != valor):#5n
                    puntero = puntero.siguiente#6n
                    if puntero.siguiente == None :#7n
                        existe = False
                        break
                
                if existe :#8n
                    puntero.siguiente = puntero.siguiente.siguiente#9n
                else:
                    print('No se encontró el valor')
                    
        #Eficiencia(n) = 4 + 6n
                    
    def Str(self):
        if self.first.value is None :
            mensaje = ('La lista esta vacia')
        else:
            puntero = self.first
            mensaje = ""
            while(puntero != None):
                mensaje += str(puntero.value) +  ', '
                puntero = puntero.siguiente
        return mensaje 

    def imprimir(self):
        if self.first.value is None :
            print('La lista esta vacia')
        else:
            puntero = self.first
            while(puntero != None):
                print('[', puntero.value, ']', end= ', ')
                puntero = puntero.siguiente
                
    def length(self):
        if self.first.value is not None:
            cantidad = 1
            puntero = self.first
            while(puntero != self.last):
                puntero = puntero.siguiente
                cantidad += 1
            return cantidad
        else:
            cantidad = 0
            return cantidad
            
                
    def ObtenerPorIndice(self, Indice):
        puntero = self.first
        if Indice >= 0 and Indice <= self.length():
            for i in range(1, Indice+1):
                puntero = puntero.siguiente
            return puntero
        else:
            return puntero
        
    def Intercambio(self, IND1, IND2):
        aux = self.ObtenerPorIndice(IND1).value
        self.ObtenerPorIndice(IND1).value = self.ObtenerPorIndice(IND2).value
        self.ObtenerPorIndice(IND2).value = aux
            
            
    def BubbleSort(self):
        m = 0
        n = 0
        cantidad = self.length()
        print("Son ", cantidad, " elementos")
        
        for m in range (1, cantidad):
            for n in range (0 , cantidad - m):
                if self.ObtenerPorIndice(n).value > self.ObtenerPorIndice(n + 1).value:
                    self.Intercambio(n , n + 1)
        
            
            
    def multiplicacion(self, a, b):
        resultado = 0
        for i in range (1, b +1 ):
            resultado += a
        return resultado
    
    def division (self, a, b):
        resultado = 0
        a = self.multiplicacion(a, 1000)
        while (a > b):
            resultado += 1
            a = a-b
            
        return resultado