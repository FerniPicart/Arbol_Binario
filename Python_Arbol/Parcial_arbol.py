from TDA_Arbol_Binario import insertar_nodo, eliminar_nodo, insertar_nodo_huffman, nodoArbolHuffman, inorden, inorden_dioses, inorden_villano, postorden, preorden, por_nivel, por_nivel_nario, busqueda_valor, arbol_vacio, remplazar, pares_impares, contar_ocurrencias, insertar_nodo_morse, busqueda_nario, por_nivel_nario, Nodo_Greek, insertar_nario, insertar_nodo_nrr, busqueda_proximidad
from TDA_Arbol_Binario_AVL import insertar_nodo_mensajes, altura, actualizaraltura, superheroes_c, contar_supreheroes, bosque_s_v, contar_nodos, insertar_nodo, padre, busqueda, padre, hijo_der, hijo_izq, maximo_nodo, minimo_nodo, postorden_superheroes, cantidad_hojas, inorden_nombre_rank, busqueda_arbol, inorden_jedimaster, inorden_especie, inorden_ayguion, inorden_lightsaber, inorden_altura, inorden_peso, busqueda_proximidad_archivo_pokemon, busqueda_archivo_pokemon_num, inorden_pok, busqueda_proximidad_archivo_libro, busqueda_archivo_ISBN, busqueda_mayor_cant_pag
from TDA_Arbol_Binario_AVL import insertar_nodo_SW, busqueda_arbol_SW, busqueda_nombre, busqueda_cod, por_altura, insertar_nodo_codigo
from random import randint
from Archivo import abrir, cerrar, leer, guardar, modificar


class Personaje():
    def __init__(self,nombre,edad,altura,codigo):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.codigo = codigo

lista = [['Darth Vader', 90, 1.85, 934], ['Kit Fisto',402, 2.04, 113], ['C-3PO',89, 0.67, 729],
         ['Yoda',1000, 0.9, 473], ['Boba Fett',260, 0.53, 784], ['Han Solo',45, 1.77, 839],
         ['Jabba el Hutt',65, 3.9, 531], ['Darth Maul',332, 1.78, 123]]

a_nombre = None
a_edad = None
a_codigo = None
for i in lista:
    dato = Personaje(i[0],i[1],i[2],i[3])
    a_nombre = insertar_nodo_SW(a_nombre,dato,i)
    a_edad = insertar_nodo_SW(a_edad,dato,i)
    a_codigo = insertar_nodo_codigo(a_codigo,dato,i)
print('Lista por nombre ascendente')
preorden(a_nombre)
print()
print('Lista por nombre descendente')
postorden(a_nombre)
input()

print('información de Yoda y Darth Vader')
bus = busqueda_arbol_SW(a_nombre,'Yoda')
print('Yoda')
print(bus)
print()
print('Darth Vader')
bus = busqueda_arbol_SW(a_nombre,'Darth Vader')
print(bus)
input()
# Indicar en que posición del archivo encuentra Kit Fisto y el personaje con código 123
pos = busqueda_nombre(a_nombre,'Kit Fisto')
print('Posicion en el arbol de Kit Fisto:',pos)
print()
print('Personaje con código 123:')
bus = busqueda_cod(a_codigo,123)
print(bus)
print()

print('personajes menores a 80 cm:')
por_altura(a_nombre)
print()

cant = contar_nodos(a_edad)
print('Cantidad de personajes dentro del arbol son:',cant)
print()
print('General Grievous esta en el árbol?')
esta = busqueda_arbol_SW(a_nombre,'General Grievous')   # No esta.
# esta = busqueda_arbol_SW(a_nombre,'Darth Vader')   # Si esta.
if esta == None:
    print('Respuesta: No esta en el arbol.')
else:
    print('Respuesta: Si esta en el arbol cargado')
input()
