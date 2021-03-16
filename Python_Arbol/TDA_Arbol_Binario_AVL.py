from TDA_Cola_Dinamica import Cola, cola_vacia, arribo, atencion
from Archivo import leer

class nodoArbol(object):

    def __init__(self, info, nrr = None):
        self.izq = None
        self.der = None
        self.info = info
        self.nrr = nrr
        self.altura = 0

class nodoArbolHuffman(object):
    
    def __init__(self, info, valor):
        self.izq = None
        self.der = None
        self.info = info
        self.valor = valor

def altura(raiz):
    "Devuelve la altura de un nodo."
    if(raiz is None):
        return -1
    else:
        return raiz.altura


def actualizaraltura(raiz):
    "Actualiza la altura de un nodo."
    if(raiz is not None):
        alt_izq = altura(raiz.izq)
        alt_der = altura(raiz.der)
        raiz.altura = (alt_izq if alt_izq > alt_der else alt_der) + 1


def insertar_nodo(raiz, dato, nrr=None):
    "Agrega un elemento al arbol"
    if(raiz is None):
        raiz = nodoArbol(dato, nrr)
    else:
        if(raiz.info > dato):
            raiz.izq = insertar_nodo(raiz.izq, dato, nrr)
        else:
            raiz.der = insertar_nodo(raiz.der, dato, nrr)
    raiz = balancear(raiz)
    actualizaraltura(raiz)
    return raiz

def insertar_nodo_SW(raiz, dato, nrr=None):
    "Agrega un elemento al arbol"
    if(raiz is None):
        raiz = nodoArbol(dato, nrr)
    else:
        if(raiz.info.nombre > dato.nombre):
            raiz.izq = insertar_nodo_SW(raiz.izq, dato, nrr)
        else:
            raiz.der = insertar_nodo_SW(raiz.der, dato, nrr)
    raiz = balancear(raiz)
    actualizaraltura(raiz)
    return raiz

def insertar_nodo_codigo(raiz, dato, nrr=None):
    "Agrega un elemento al arbol"
    if(raiz is None):
        raiz = nodoArbol(dato, nrr)
    else:
        if(raiz.info.codigo > dato.codigo):
            raiz.izq = insertar_nodo_codigo(raiz.izq, dato, nrr)
        else:
            raiz.der = insertar_nodo_codigo(raiz.der, dato, nrr)
    raiz = balancear(raiz)
    actualizaraltura(raiz)
    return raiz

def insertar_nodo_mensajes(raiz,simbolo,frecuencia):
    if(raiz is None):
        raiz = nodoArbolHuffman(simbolo,frecuencia)
    else:
        if(raiz.info > simbolo):
            raiz.izq = insertar_nodo_mensajes(raiz.izq,simbolo,frecuencia)
        else:
            raiz.der = insertar_nodo_mensajes(raiz.der,simbolo,frecuencia)
    return raiz

    
def inorden(raiz):
    "Realiza un recorrido del arbol, mostrando la informacion"
    if(raiz is not None):
        inorden(raiz.izq)
        print(raiz.info)
        inorden(raiz.der)


def inorden_jedimaster(raiz, archivo):
    if raiz is not None:
        inorden_jedimaster(raiz.izq, archivo)
        jedi = leer(archivo, raiz.nrr)
        if jedi.rank.find('Jedi Master') > -1:
            print('Nombre:',jedi.nombre,'|Especie:',jedi.especie,'|Rank:',jedi.rank,'|Maestro:',jedi.maestro,'|Color del Sable:',jedi.color_sable)
        inorden_jedimaster(raiz.der, archivo)


def inorden_lightsaber(raiz, archivo):
    if raiz is not None:
        inorden_lightsaber(raiz.izq, archivo)
        jedi = leer(archivo, raiz.nrr)
        if jedi.color_sable.find('Verde') > -1:
            print('Nombre:',jedi.nombre,'|Especie:',jedi.especie,'|Rank:',jedi.rank,'|Maestro:',jedi.maestro,'|Color del Sable:',jedi.color_sable)
        inorden_lightsaber(raiz.der, archivo)


def inorden_especie(raiz, archivo):
    if raiz is not None:
        inorden_especie(raiz.izq, archivo)
        jedi = leer(archivo, raiz.nrr)
        if jedi.especie.find('Togruta') > -1 or jedi.especie.find('Cerean') > -1:
            print('Nombre:',jedi.nombre,'|Especie:',jedi.especie,'|Rank:',jedi.rank,'|Maestro:',jedi.maestro,'|Color del Sable:',jedi.color_sable)
        inorden_especie(raiz.der, archivo)


def inorden_ayguion(raiz, archivo):
    if raiz is not None:
        inorden_ayguion(raiz.izq, archivo)
        jedi = leer(archivo, raiz.nrr)
        if jedi.nombre[0].find('A') > -1 or jedi.nombre.find('-') > -1:
            print('Nombre:',jedi.nombre,'|Especie:',jedi.especie,'|Rank:',jedi.rank,'|Maestro:',jedi.maestro,'|Color del Sable:',jedi.color_sable)
        inorden_ayguion(raiz.der, archivo)

def inorden_name(raiz, archivo, jedis):
    if(raiz is not None):
        inorden_name(raiz.izq, archivo, jedis)
        jedi = leer(archivo, raiz.nrr)
        jedis.append(jedi)
        inorden_name(raiz.der, archivo, jedis)

def inorden_nombre_rank(raiz, archivo):
    if raiz is not None:
        inorden_nombre_rank(raiz.izq, archivo)
        jedi = leer(archivo, raiz.nrr)
        if jedi.nombre:
            print(jedi.nombre,'-', jedi.rank)
        inorden_nombre_rank(raiz.der, archivo)


def inorden_altura(raiz, archivo):
    if raiz is not None:
        inorden_altura(raiz.izq, archivo)
        sw = leer(archivo, raiz.nrr)
        if sw.altura >= 1:
            print(sw.nombre,'-', sw.altura)
        inorden_altura(raiz.der, archivo)

def por_altura(raiz):
    if raiz is not None:
        por_altura(raiz.izq)
        if raiz.info.altura < 0.80:
            print(raiz.info.nombre,'-', raiz.info.altura)
        por_altura(raiz.der)

def inorden_peso(raiz, archivo):
    if raiz is not None:
        inorden_peso(raiz.izq, archivo)
        sw = leer(archivo, raiz.nrr)
        if sw.peso <= 75:
            print(raiz.info,'-', sw.peso)
        inorden_peso(raiz.der, archivo)

def inorden_pok(raiz, archivo):
    if(raiz is not None):
        inorden_pok(raiz.izq, archivo)
        pok = leer(archivo, raiz.nrr)
        if pok.num:
            print('nombre: ', pok.nombre, '|num:', pok.num,'|tipo:', pok.tipo, '|debilidad:',pok.debilidad)
        inorden_pok(raiz.der, archivo)

def postorden(raiz):
    "Recorrido de orden posterior, mostrando la informacion"
    if(raiz is not None):
        postorden(raiz.der)
        print(raiz.info)
        postorden(raiz.izq)

def postorden_superheroes(raiz):
    if(raiz is not None):
        postorden_superheroes(raiz.der)
        if raiz.valor == True:
            print(raiz.info)
        postorden_superheroes(raiz.izq)

def preorden(raiz):
    "Recorrido de orden previo, mostrando la informacion"
    if(raiz is not None):
        print(raiz.info)
        preorden(raiz.izq)
        preorden(raiz.der)

def por_nivel(raiz):
    "Muestra la informacion del arbol, por nivel"
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
    "Devuelve un puntero que apunta al nodo que tiene el elemnento buscado"
    if(raiz is not None):
        if(raiz.info == buscado):
            return raiz
        else:
            if(raiz.info > buscado):         
                return busqueda(raiz.izq, buscado)
            else:
                return busqueda(raiz.der, buscado)

def busqueda_nombre(raiz, buscado):
    "Devuelve un puntero que apunta al nodo que tiene el elemnento buscado"
    if(raiz is not None):
        if(raiz.info.nombre == buscado):
            return raiz.nrr
        else:
            if(raiz.info.nombre > buscado):         
                return busqueda_nombre(raiz.izq, buscado)
            else:
                return busqueda_nombre(raiz.der, buscado)

def busqueda_cod(raiz, buscado):
    "Devuelve un puntero que apunta al nodo que tiene el elemnento buscado"
    if(raiz is not None):
        if(raiz.info.codigo == buscado):
            return raiz
        else:
            if(raiz.info.codigo > buscado):         
                return busqueda_cod(raiz.izq, buscado)
            else:
                return busqueda_cod(raiz.der, buscado)

def busqueda_proximidad(raiz, buscado):
    2
    if(raiz is not None):
        if(raiz.info[0:len(buscado)] == buscado):
            print(raiz.info)
        busqueda_proximidad(raiz.izq, buscado)
        busqueda_proximidad(raiz.der, buscado)

def busqueda_proximidad_archivo_libro(raiz, buscado, archivo):
    '''Busca en archivo el TITULO de un libro'''
    if(raiz is not None):
        if(raiz.info[0:len(buscado)] == buscado):
            libro = leer(archivo, raiz.nrr)
            print('Libro: ',libro.titulo,'|Autor:',libro.autor,'|ISBN:',libro.ISBN,'|PAG:', libro.cant_pag)
        busqueda_proximidad_archivo_libro(raiz.izq, buscado, archivo)
        busqueda_proximidad_archivo_libro(raiz.der, buscado, archivo)

def busqueda_archivo_ISBN(raiz, ISBN, archivo):
    '''Busca en archivo el cod ISBN de un libro'''
    if(raiz is not None):
        libro = leer(archivo, raiz.nrr)
        if(libro.ISBN == ISBN):
            print('Libro: ',libro.titulo,'|Autor:',libro.autor,'|ISBN:',libro.ISBN,'|PAG:', libro.cant_pag)
        busqueda_archivo_ISBN(raiz.izq, ISBN, archivo)
        busqueda_archivo_ISBN(raiz.der, ISBN, archivo)

def busqueda_mayor_cant_pag(raiz, cant, archivo):
    if(raiz is not None):
        libro = leer(archivo, raiz.nrr)
        if(int(libro.cant_pag) > cant):
            print('Libro: ',libro.titulo,'|Autor:',libro.autor,'|ISBN:',libro.ISBN,'|PAG:', libro.cant_pag)
        busqueda_mayor_cant_pag(raiz.izq, cant, archivo)
        busqueda_mayor_cant_pag(raiz.der, cant, archivo)


def busqueda_proximidad_archivo_pokemon(raiz, buscado, archivo):
    if(raiz is not None):
        if(raiz.info[0:len(buscado)] == buscado):
            pokemon = leer(archivo, raiz.nrr)
            print('nombre: ', pokemon.nombre, '|num:', pokemon.num,'|tipo:', pokemon.tipo, '|debilidad:',pokemon.debilidad)
        busqueda_proximidad_archivo_pokemon(raiz.izq, buscado, archivo)
        busqueda_proximidad_archivo_pokemon(raiz.der, buscado, archivo)

def busqueda_archivo_pokemon_num(raiz, numero, archivo):
    if(raiz is not None):
        pokemon = leer(archivo, raiz.nrr)
        if(pokemon.num == numero):
            print('nombre: ', pokemon.nombre, '|num:', pokemon.num,'|tipo:', pokemon.tipo, '|debilidad:',pokemon.debilidad)
        busqueda_archivo_pokemon_num(raiz.izq, numero, archivo)
        busqueda_archivo_pokemon_num(raiz.der, numero, archivo)

def busqueda_arbol(raiz, buscado):
    '''Busca y devuelve un elemento en el arbol'''
    if raiz is not None:
        if raiz.info == buscado:
            return raiz
        else:
            if buscado < raiz.info:
                return busqueda_arbol(raiz.izq, buscado)
            else:
                return busqueda_arbol(raiz.der, buscado)

def busqueda_arbol_SW(raiz, buscado):
    '''Busca y devuelve un elemento en el arbol'''
    if raiz is not None:
        if raiz.info.nombre == buscado:
            return raiz
        else:
            if buscado < raiz.info.nombre:
                return busqueda_arbol_SW(raiz.izq, buscado)
            else:
                return busqueda_arbol_SW(raiz.der, buscado)


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


def cantidad_hojas(raiz, cont=0):
    '''Devuelve la cantidad de hojas de un arbol'''
    if raiz is not None:
        if (raiz.izq is None) and (raiz.der is None):
            cont += 1
            print(raiz.info, 'es un nodo hoja')
        cont = cantidad_hojas(raiz.izq, cont)
        cont = cantidad_hojas(raiz.der, cont)
    return cont

def bosque_s_v(arbol, arbol_superheroes, arbol_villanos):
    if arbol is not None:
        arbol_superheroes, arbol_villanos = bosque_s_v(arbol.izq, arbol_superheroes, arbol_villanos)
        if arbol.valor is True:
            arbol_superheroes = insertar_nodo(arbol_superheroes, arbol.info)
        else:
            arbol_villanos = insertar_nodo(arbol_villanos, arbol.info)
        arbol_superheroes, arbol_villanos = bosque_s_v(arbol.der, arbol_superheroes, arbol_villanos)
    return arbol_superheroes, arbol_villanos

def eliminar_nodo(raiz, clave):
    "Elimina un elemento del arbol y lo devuelve si lo envuentra"
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
    raiz = balancear(raiz)
    actualizaraltura(raiz)
    return raiz, x


def padre(raiz, buscado):
    if(raiz is not None):
        if((raiz.der is not None and raiz.der.info == buscado) or (raiz.izq is not None and raiz.izq.info == buscado)):
            print('El padre del buscado es', raiz.info)
        else:
            padre(raiz.izq, buscado)
            padre(raiz.der, buscado)

def hijo_der(arbol):
    if(arbol.der is None):
        print(arbol.der)
    else:
        print('Hijo derecho:', arbol.der.info)

def hijo_izq(arbol):
    if(arbol.izq is None):
        print(arbol.izq)
    else:
        print('Hijo izquierdo:', arbol.izq.info)

def rotar_simple(raiz, control):
    "Realiza una rotación simple de nodos a la derecha o a la izquierda."
    if control:
        aux = raiz.izq
        raiz.izq = aux.der
        aux.der = raiz
    else:
        aux = raiz.der
        raiz.der = aux.izq
        aux.izq = raiz
    actualizaraltura(raiz)
    actualizaraltura(aux)
    raiz = aux
    return raiz

def rotar_doble(raiz, control):
    "Realiza una rotación doble de nodos a la derecha o a la izquierda."
    if control:
        raiz.izq = rotar_simple(raiz.izq, False)
        raiz = rotar_simple(raiz, True)
    else:
        raiz.der = rotar_simple(raiz.der, True)
        raiz = rotar_simple(raiz, False)
    return raiz

def superheroes_c(raiz):
    'Busca superheroes que su nombre comience con C'
    if raiz is not None:
        superheroes_c(raiz.izq)
        if raiz.valor is True and raiz.info[0][0] == 'C':
            print(raiz.info)
        superheroes_c(raiz.der)

def balancear(raiz):
    "Determina que rotación hay que hacer para balancear el árbol."
    if(raiz is not None):
        if(altura(raiz.izq)-altura(raiz.der) == 2):
            if(altura(raiz.izq.izq) >= altura(raiz.izq.der)):
                raiz = rotar_simple(raiz, True)
            else:
                raiz = rotar_doble(raiz, True)
        elif(altura(raiz.der)-altura(raiz.izq) == 2):
            if(altura(raiz.der.der) >= altura(raiz.der.izq)):
                raiz = rotar_simple(raiz, False)
            else:
                raiz = rotar_doble(raiz, False)
    return raiz

def cortar_por_nivel(raiz, bosque):
    cola = Cola()
    arribo(cola, raiz)
    while(not cola_vacia(cola)):
        nodo = atencion(cola)
        if(altura(nodo) == 7 ):
            bosque.append(nodo.izq)
            bosque.append(nodo.der)
        if(nodo.izq is not None):
            arribo(cola, nodo.izq)
        if(nodo.der is not None):
            arribo(cola, nodo.der)

def contar_a(raiz, cantidad):
    if(raiz is not None):
        contar_a(raiz.izq, cantidad)
        contar_a(raiz.der, cantidad)
        cantidad[0] += 1

def contar_nodos(raiz, cont=0):
    'Devuelve la cantidad de nodos de un arbol'
    if raiz is not None:
        cont = contar_nodos(raiz.izq, cont)
        cont += 1
        cont = contar_nodos(raiz.der, cont)
    return cont

def contar_supreheroes(raiz, cont=0):
    'Devuelve la cantidad de SuperHeroes de un arbol'
    if raiz is not None:
        cont = contar_supreheroes(raiz.izq, cont)
        if raiz.valor == True:
            cont += 1
        cont = contar_supreheroes(raiz.der, cont)
    return cont

def minimo_nodo(raiz):
    'Obtiene el nodo minimo de un arbol'
    if raiz.izq is not None:
        raiz = minimo_nodo(raiz.izq)
    return raiz

def maximo_nodo(raiz):
    'Obtiene el nodo maximo de un arbol'
    if raiz.der is not None:
        raiz = maximo_nodo(raiz.der)
    return raiz