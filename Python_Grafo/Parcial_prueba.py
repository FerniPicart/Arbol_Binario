from TDA_Grafo import Grafo, barrido_grafo, buscar_vertice_aero, dijkstra_distancia
from TDA_Grafo import insertar_vertice_aeropuerto, insertar_arista_viaje, prim_red, eliminar_arista_red
from TDA_Grafo import dijkstra_duracion, dijkstra_costo, adyacentes, existe_paso_aero, barrido_profundidad_aero
from TDA_Grafo import buscar_vertice_red, insertar_arista_red, insertar_vertice_red, barrido_amplitud_red
from TDA_Grafo import marcar_no_visitado, barrido_profundidad_red, dijkstra_red, prim_arq, prim_nat
from TDA_Grafo import insertar_vertice_antena, barrido_grafo_antena, buscar_vertice_id, insertar_arista_antena, dijkstra_distancia_antena, buscar_vertice_ubicacion, prim_antena, kruskal_antena, existe_paso_antena
from TDA_Pila_Din import desapilar, pila_vacia
from random import randint, choice, shuffle
from datetime import time



grafo = Grafo(False)

class Antena():
    def __init__(self,ubicacion,id,latitud,longitud,MBs):
        self.ubicacion = ubicacion
        self.id = id
        self.latitud = latitud
        self.longitud = longitud
        self.MBs = MBs

lista = [['Arg','TGK-783',randint(1,100),randint(1,100),randint(1000000,10000000)],
        ['Uru','KRS-108',randint(1,100),randint(1,100),randint(1000000,10000000)],
        ['Bra','LSK-347',randint(1,100),randint(1,100),randint(1000000,10000000)],
        ['Par','PPP-030',randint(1,100),randint(1,100),randint(1000000,10000000)],
        ['Bol','FAS-420',randint(1,100),randint(1,100),randint(1000000,10000000)],
        ['Mex','REY-175',randint(1,100),randint(1,100),randint(1000000,10000000)]]
# B
# Carga de Vertices
for i in lista:
    dato = Antena(i[0],i[1],i[2],i[3],i[4])
    insertar_vertice_antena(grafo,dato)
# Carga de Aristas
ori = buscar_vertice_ubicacion(grafo,'Arg')
des = buscar_vertice_ubicacion(grafo,'Uru')
insertar_arista_antena(grafo,13,ori,des)

des = buscar_vertice_ubicacion(grafo,'Par')
insertar_arista_antena(grafo,13,ori,des)

des = buscar_vertice_ubicacion(grafo,'Bol')
insertar_arista_antena(grafo,20,ori,des)

ori = buscar_vertice_ubicacion(grafo,'Uru')
des = buscar_vertice_ubicacion(grafo,'Bol')
insertar_arista_antena(grafo,13,ori,des)

des = buscar_vertice_ubicacion(grafo,'Mex')
insertar_arista_antena(grafo,13,ori,des)

ori = buscar_vertice_ubicacion(grafo,'Mex')
des = buscar_vertice_ubicacion(grafo,'Bra')
insertar_arista_antena(grafo,13,ori,des)

ori = buscar_vertice_ubicacion(grafo,'Bra')
des = buscar_vertice_ubicacion(grafo,'Par')
insertar_arista_antena(grafo,13,ori,des)

#barrido_grafo_antena(grafo)

# C
tam = grafo.tamanio
print('El tamaño del grafo es :',tam)

# D
# Camino mas corto
ori = buscar_vertice_ubicacion(grafo,'Arg')
des = buscar_vertice_ubicacion(grafo,'Mex')
camino = dijkstra_distancia_antena(grafo, 'Arg', 'Mex')
fin = 'Mex'
distancia = None
while not pila_vacia(camino):
    dato = desapilar(camino)
    if distancia is None and fin == dato[1][0].info.ubicacion:
        distancia = dato[0]

print('Distancia desde',ori.info.ubicacion,'hasta',des.info.ubicacion,'es :',distancia)
print()
# E
# Bosque de expansion minimo (PRIM)
print('Bosque de expansion minimo: ')
bosque = []
bosque = prim_antena(grafo)
for i in range(0,len(bosque),2):
    print(bosque[i], '|',bosque[i+1])
print()

# F
# Busqueda de ID
bus = buscar_vertice_id(grafo,'TGK-783')
if bus != None:
    print('Se ha encontrado el ID "TGK-783":')
    print('-------------------------------')
    print('- Ubicacion:',bus.info.ubicacion,'             -\n- ID:',bus.info.id,'                -\n- Latitud y Longitud:',bus.info.latitud,',',bus.info.longitud,'-\n- Vel. MBs:',bus.info.MBs,'          -')
    print('-------------------------------')

print('Bosque de expansion minima: ')
bosque = []
bosque = kruskal_antena(grafo)
for i in range(0,len(bosque),2):
    print(bosque[i], '|',bosque[i+1])
print()
# Existe paso
marcar_no_visitado(grafo)
ori = buscar_vertice_ubicacion(grafo,'Uru')
des = buscar_vertice_ubicacion(grafo,'Mex')
var = existe_paso_antena(grafo,ori,des)
if var:
    print('Existe paso')