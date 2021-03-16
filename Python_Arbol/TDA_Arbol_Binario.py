from Archivo import leer
from TDA_Cola_Dinamica import arribo, atencion, cola_vacia, Cola

class nodoArbol(object):
    def __init__(self, info, nrr=None):
        self.izq = None
        self.der = None
        self.info = info
        self.nrr = nrr

class nodoArbolHuffman(object): 
    def __init__(self, info, valor):
        self.izq = None
        self.der = None
        self.info = info
        self.valor = valor

class nodoArbolGreek(object):  
    def __init__(self, info, madre, descipcion=None):
        self.izq = None
        self.der = None
        self.info = info
        self.madre = madre
        self.descripcion = descipcion

class nodoArbolMarvel(object):
    def __init__(self, nombre, heroe):
        self.izq = None
        self.der = None
        self.nombre = nombre
        self.heroe = heroe

class Nodo_Greek():
    def __init__(self, info, madre, descipcion=None):
        self.izq = None
        self.der = None
        self.info = info
        self.madre = madre
        self.descripcion = descipcion


def insertar_nodo(raiz, dato):
    if(raiz is None):
        raiz = nodoArbol(dato)
    else:
        if(raiz.info > dato):
            raiz.izq = insertar_nodo(raiz.izq, dato)
        else:
            raiz.der = insertar_nodo(raiz.der, dato)
    return raiz

def insertar_nodo_nrr(raiz, dato, nrr=None):
    if(raiz is None):
        raiz = nodoArbol(dato, nrr)
    else:
        if(raiz.info > dato):
            raiz.izq = insertar_nodo_nrr(raiz.izq, dato, nrr)
        else:
            raiz.der = insertar_nodo_nrr(raiz.der, dato, nrr)
    return raiz

def insertar_nodo_huffman(raiz, dato, derrotado):
    if(raiz is None):
        raiz = nodoArbolHuffman(dato,derrotado)
    else:
        if(raiz.info > dato):
            raiz.izq = insertar_nodo_huffman(raiz.izq, dato, derrotado)
        else:
            raiz.der = insertar_nodo_huffman(raiz.der, dato, derrotado)
    return raiz

def insertar_nodo_morse(raiz, dato):
    if(raiz is None):
        raiz = nodoArbol(dato)
    else:
        if(raiz.info[0] > dato[0]):
            raiz.izq = insertar_nodo_morse(raiz.izq, dato)
        else:
            raiz.der = insertar_nodo_morse(raiz.der, dato)
    return raiz

def inorden(raiz):
    if(raiz is not None):
        inorden(raiz.izq)
        print(raiz.info)
        inorden(raiz.der)

def inorden_dioses(raiz):
    if(raiz is not None):
        inorden_dioses(raiz.izq)
        print(raiz.info , raiz.valor)
        inorden_dioses(raiz.der)

def inorden_villano(raiz):
    if raiz != None:
        inorden_villano(raiz.izq)
        if raiz.valor == False:
            print('Villano: ' + raiz.info)
        inorden_villano(raiz.der)

def inorden_altura(raiz, archivo):
    if(raiz is not None):
        inorden_altura(raiz.izq, archivo)
        personaje = leer(archivo, raiz.nrr)
        if(personaje.altura > 1.00):
            print(raiz.info, personaje.altura)
        inorden_altura(raiz.der, archivo)

def inorden_peso(raiz, archivo):
    if(raiz is not None):
        inorden_peso(raiz.izq, archivo)
        personaje = leer(archivo, raiz.nrr)
        if(personaje.peso < 75):
            print(raiz.info, personaje.peso)
        inorden_peso(raiz.der, archivo)


def postorden(raiz):
    if(raiz is not None):
        inorden(raiz.der)
        print(raiz.info)
        inorden(raiz.izq)

def preorden(raiz):
    if(raiz is not None):
        print(raiz.info)
        preorden(raiz.izq)
        preorden(raiz.der)

def por_nivel(raiz):
    cola = Cola()
    arribo(cola, raiz)
    while(not cola_vacia(cola)):
        nodo = atencion(cola)
        print(nodo.info)
        if(nodo.izq is not None):
            arribo(cola, nodo.izq)
        if(nodo.der is not None):
            arribo(cola, nodo.der)


def busqueda(raiz, buscado):
    """Busca un nombre dentro del arbol"""
    if(raiz is not None):
        print(raiz.info)
        if(raiz.info == buscado):
            return raiz
        else:
            if(raiz.info > buscado):         
                return busqueda(raiz.izq, buscado)
            else:
                return busqueda(raiz.der, buscado)

def busqueda_nario(raiz, buscado, pos):
    if(raiz is not None):
        if(raiz.info == buscado):
            pos.append(raiz)
            return
        busqueda_nario(raiz.izq, buscado, pos)
        busqueda_nario(raiz.der, buscado, pos)

def busqueda_valor(raiz, buscado, pos):
    if(raiz is not None):
        if(raiz.valor == buscado):
            pos.append(raiz.info)
            return
        busqueda_valor(raiz.izq, buscado, pos)
        busqueda_valor(raiz.der, buscado, pos)

def busqueda_proximidad(raiz, buscado):
    if(raiz is not None):
        if(raiz.info[0:len(buscado)] == buscado):
            print(raiz.info)
        busqueda_proximidad(raiz.izq, buscado)
        busqueda_proximidad(raiz.der, buscado)

def arbol_vacio(raiz):
    return raiz is None

def remplazar(raiz):
    """Determina el nodo que remplazará al que se elimina."""
    aux = None
    if(raiz.der is None):
        aux = raiz
        raiz = raiz.izq
    else:
        raiz.der, aux = remplazar(raiz.der)
    return raiz, aux

def eliminar_nodo(raiz, clave):
    x = None
    if(raiz is not None):
        if(clave < raiz.info):
            raiz.izq, x = eliminar_nodo(raiz.izq, clave)
        elif(clave > raiz.info):
            raiz.der, x = eliminar_nodo(raiz.der, clave)
        else:
            x = raiz.info
            if(raiz.izq is None):
                raiz = raiz.der
            elif(raiz.der is None):
                raiz = raiz.izq
            else:
                raiz.izq, aux = remplazar(raiz.izq)
                raiz.info = aux.info
    return raiz, x

def insertar_nario(padre, hijo):
    if(padre.izq is None):
        #print('insertar hijo de', padre.info)
        padre.izq = hijo
    else:
        aux = padre.izq
        while(aux.der is not None):
            aux = aux.der
        #print('insertar hno de', aux.info)
        aux.der = hijo

def por_nivel_nario(raiz):
    cola = Cola()
    arribo(cola, raiz)
    while(not cola_vacia(cola)):
        nodo = atencion(cola)
        print(nodo.info)
        if(nodo.izq is not None):
            arribo(cola, nodo.izq)
        hno = nodo.der
        while(hno is not None):
            print(hno.info)
            if(hno.izq is not None):
                arribo(cola, hno.izq)
            hno = hno.der

def pares_impares(raiz, cp, ci):
    if(raiz is not None):
        if(raiz.info % 2 == 0):
            cp += 1
        else:
            ci += 1
        cp, ci = pares_impares(raiz.izq, cp, ci)
        cp, ci = pares_impares(raiz.der, cp, ci)
    return cp, ci

# cantp, canti = contar(arbol, cantp, canti)
# print(cantp, canti)


def contar_ocurrencias(raiz, buscado, cant):
    if(raiz is not None):
        if(raiz.info == buscado):
            cant += 1
            cant = contar_ocurrencias(raiz.der, buscado, cant)
        elif buscado < raiz.info:
            cant = contar_ocurrencias(raiz.izq, buscado, cant)
        else:
            cant = contar_ocurrencias(raiz.der, buscado, cant)
    return cant



# cant = 0
# bus = 7
# pos = busqueda(arbol, bus)
# if(pos is not None):
#     print('asdas', contar_repetidos(pos, bus, cant))
# else:
#     print(0)
'''
arbol = None

arbol = insertar_nodo(arbol, 5)
arbol = insertar_nodo(arbol, 3)
arbol = insertar_nodo(arbol, 4)
arbol = insertar_nodo(arbol, 7)
arbol = insertar_nodo(arbol, 9)
arbol = insertar_nodo(arbol, 0)
arbol = insertar_nodo(arbol, 1)
arbol = insertar_nodo(arbol, 6)

arbol, dato = eliminar_nodo(arbol, 5)
preorden(arbol)
'''