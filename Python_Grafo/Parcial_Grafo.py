from TDA_Grafo import Grafo, barrido_grafo, buscar_vertice_aero, dijkstra_distancia
from TDA_Grafo import insertar_vertice_aeropuerto, insertar_arista_viaje, prim_red, eliminar_arista_red
from TDA_Grafo import dijkstra_duracion, dijkstra_costo, adyacentes, existe_paso_aero, barrido_profundidad_aero
from TDA_Grafo import buscar_vertice_red, insertar_arista_red, insertar_vertice_red, barrido_amplitud_red
from TDA_Grafo import marcar_no_visitado, barrido_profundidad_red, dijkstra_red, prim_arq, prim_nat
from TDA_Grafo import insertar_arista_puesto, insertar_vertice_puesto, buscar_vertice_puesto, dijkstra_costo, dijkstra_tiempo, kruskal_puesto
from TDA_Pila_Din import desapilar, pila_vacia
from random import randint, choice, shuffle
from datetime import time

grafo = Grafo(False)

class Puesto():
    def __init__(self,nombre,direccion):
        self.nombre = nombre
        self.direccion = direccion

    
    def __str__(self):
        return 'Nombre' + self.nombre + '| Direccion: ' + self.direccion

class Viaje():
    def __init__(self, costo, tiempo):
        self.costo = costo
        self.tiempo = tiempo

    def __str__(self):
        return 'Costo:',self.costo,'| Tiempo:',self.tiempo

# vertices
dato = Puesto('Hospital', 'dir1')
insertar_vertice_puesto(grafo, dato)
dato = Puesto('zona2', 'dir2')
insertar_vertice_puesto(grafo, dato)
dato = Puesto('zona3', 'dir3')
insertar_vertice_puesto(grafo, dato)
dato = Puesto('Isla del Puerto', 'dir4')
insertar_vertice_puesto(grafo, dato)
dato = Puesto('zona5', 'dir5')
insertar_vertice_puesto(grafo, dato)


# aristas
ori = buscar_vertice_puesto(grafo, 'Hospital')
des = buscar_vertice_puesto(grafo, 'zona2')
dato = Viaje(randint(10,200),randint(5,60))
insertar_arista_puesto(grafo, dato, ori, des)

des = buscar_vertice_puesto(grafo, 'zona3')
dato = Viaje(randint(10, 200),randint(5, 60))
insertar_arista_puesto(grafo, dato, ori, des)

des = buscar_vertice_puesto(grafo, 'zona5')
dato = Viaje(randint(10, 200),randint(5, 60))
insertar_arista_puesto(grafo, dato, ori, des)

ori = buscar_vertice_puesto(grafo, 'zona2')
des = buscar_vertice_puesto(grafo, 'Isla del Puerto')
dato = Viaje(randint(10, 200),randint(5, 60))
insertar_arista_puesto(grafo, dato, ori, des)

ori = buscar_vertice_puesto(grafo, 'Isla del Puerto')
des = buscar_vertice_puesto(grafo, 'zona5')
dato = Viaje(randint(10, 200),randint(5, 60))
insertar_arista_puesto(grafo, dato, ori, des)

des = buscar_vertice_puesto(grafo, 'zona3')
dato = Viaje(randint(10, 200),randint(5, 60))
insertar_arista_puesto(grafo, dato, ori, des)

des = buscar_vertice_puesto(grafo, 'zona5')
dato = Viaje(randint(10, 200),randint(5, 60))
insertar_arista_puesto(grafo, dato, ori, des)


# barrido_grafo(grafo)


ori = buscar_vertice_puesto(grafo,'Hospital')
des = buscar_vertice_puesto(grafo,'Isla del Puerto')
pila = dijkstra_costo(grafo, 'Hospital', 'Isla del Puerto')
fin = 'Isla del Puerto'
precio = None
print('Camino desde Hospital hasya Isla del Puerto:')
while not pila_vacia(pila):
    dato = desapilar(pila)
    if precio is None and fin == dato[1][0].info.nombre:
        precio = dato[0]
    if fin == dato[1][0].info.nombre:
        print(dato[1][0].info.nombre)
        fin = dato[1][1]
print('Desde',ori.info.nombre,'hasta',des.info.nombre,'El pasaje tiene un costo de $',precio)
input()

marcar_no_visitado(grafo)
ori = buscar_vertice_puesto(grafo,'Hospital')
des = buscar_vertice_puesto(grafo,'Isla del Puerto')
pila = dijkstra_tiempo(grafo,'Hospital','Isla del Puerto')
fin = 'Isla del Puerto'
duracion = None
while not pila_vacia(pila):
    dato = desapilar(pila)
    if duracion is None and fin == dato[1][0].info.nombre:
        duracion = dato[0]
    if fin == dato[1][0].info.nombre:
        print(dato[1][0].info.nombre)
        fin = dato[1][1]
print('Tiempo yendo desde:',ori.info.nombre,'hasta',des.info.nombre,'es de:',duracion)
input()

print('Bosque de expansion minima: ')
bosque = []
bosque = kruskal_puesto(grafo)
for i in range(0,len(bosque),2):
    print(bosque[i], '|',bosque[i+1])