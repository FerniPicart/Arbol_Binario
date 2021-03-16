from TDA_Grafo import Grafo, barrido_grafo, buscar_vertice_aero, dijkstra_distancia
from TDA_Grafo import insertar_vertice_aeropuerto, insertar_arista_viaje, prim_red, eliminar_arista_red
from TDA_Grafo import dijkstra_duracion, dijkstra_costo, adyacentes, existe_paso_aero, barrido_profundidad_aero
from TDA_Grafo import buscar_vertice_red, insertar_arista_red, insertar_vertice_red, barrido_amplitud_red
from TDA_Grafo import marcar_no_visitado, barrido_profundidad_red, dijkstra_red, prim_arq, prim_nat
from TDA_Pila_Din import desapilar, pila_vacia
from random import randint, choice, shuffle
from datetime import time

####
# Ejercicio 1
'''
print('Ejercicio 1:')
# A
class Aeropuerto(object):
    def __init__(self,nombre,longitud,latitud,cant_pistas):
        self.nombre = nombre
        self.longitud = longitud
        self.latitud = latitud
        self.cant_pistas = cant_pistas

    def __str__(self):
        return 'Aeropuerto: '+ self.nombre+ ' | Longitud= '+ str(self.longitud)+ ' y Latitud= '+ str(self.latitud)+ ' | Cant pistas: '+ str(self.cant_pistas)
# B
class Vuelo():
    def __init__(self,empresa,hora_salida,hora_arribo,costo_pasaje,distancia):
        self.empresa = empresa
        self.hora_salida = hora_salida
        self.hora_arribo = hora_arribo
        self.costo_pasaje = costo_pasaje
        self.duracion = (hora_arribo - hora_salida)
        self.distancia = distancia

grafo = Grafo(False)
# D
aero = ['Argentina','China','Brasil','Tailandia','Grecia','Alemania','Francia','Estados Unidos','Japón','Jamaica']
print(len(aero))

for i in range(len(aero)):
    dato = Aeropuerto(aero[i], randint(1,100), randint(1,100), randint(1,10))
    insertar_vertice_aeropuerto(grafo,dato)

dato = Vuelo('vuelo',22,24,2000,randint(2000,10000))
insertar_arista_viaje(grafo,dato,buscar_vertice_aero(grafo,'China'),buscar_vertice_aero(grafo,'Tailandia'))
dato = Vuelo('vuelo',10,24,1000,randint(2000,10000))
insertar_arista_viaje(grafo,dato,buscar_vertice_aero(grafo,'Tailandia'),buscar_vertice_aero(grafo,'Alemania'))
dato = Vuelo('vuelo',1,16,1000,randint(2000,10000))
insertar_arista_viaje(grafo,dato,buscar_vertice_aero(grafo,'Francia'),buscar_vertice_aero(grafo,'China'))
dato = Vuelo('vuelo',15,18,1000,randint(2000,10000))
insertar_arista_viaje(grafo,dato,buscar_vertice_aero(grafo,'Argentina'),buscar_vertice_aero(grafo,'Grecia'))
dato = Vuelo('vuelo',10,14,1000,randint(2000,10000))
insertar_arista_viaje(grafo,dato,buscar_vertice_aero(grafo,'Alemania'),buscar_vertice_aero(grafo,'China'))
dato = Vuelo('vuelo',0,24,1000,randint(2000,10000))
insertar_arista_viaje(grafo,dato,buscar_vertice_aero(grafo,'Argentina'),buscar_vertice_aero(grafo,'China'))
dato = Vuelo('vuelo',5,20,1000,randint(2000,10000))
insertar_arista_viaje(grafo,dato,buscar_vertice_aero(grafo,'Argentina'),buscar_vertice_aero(grafo,'Francia'))
dato = Vuelo('vuelo',10,18,1000,randint(2000,10000))
insertar_arista_viaje(grafo,dato,buscar_vertice_aero(grafo,'Francia'),buscar_vertice_aero(grafo,'Grecia'))
dato = Vuelo('vuelo',15,18,1000,randint(2000,10000))
insertar_arista_viaje(grafo,dato,buscar_vertice_aero(grafo,'Grecia'),buscar_vertice_aero(grafo,'Brasil'))

# E caminos mas cortos: 
# dijkstra

# Por distancia
camino_mas_corto = dijkstra_distancia(grafo, 'Argentina', 'Tailandia')
fin = 'Tailandia'
distancia = None
while not pila_vacia(camino_mas_corto):
    dato = desapilar(camino_mas_corto)
    if distancia is None and fin == dato[1][0].info.nombre:
        distancia = dato[0]
    if fin == dato[1][0].info.nombre:
        print(dato[1][0].info.nombre)
        fin = dato[1][1]
print('Distancia mas corta: ' + str(distancia) + 'km')
print()

# Por duración
camino = dijkstra_duracion(grafo,'Argentina','Tailandia')
fin = 'Tailandia'
duracion = None
while not pila_vacia(camino):
    x = desapilar(camino)
    if duracion == None and fin == x[1][0].info.nombre:
        duracion = x[0]
    if fin == x[1][0].info.nombre:
        print(x[1][0].info.nombre)
        fin = x[1][1]
print('Duracion viaje de Argentina hasta Tailandia:', duracion,'hs.')
print()

# Por costo de viajes
camino = dijkstra_costo(grafo,'Argentina','Tailandia')
fin = 'Tailandia'
costo = None
while not pila_vacia(camino):
    x = desapilar(camino)
    if costo == None and fin == x[1][0].info.nombre:
        costo = x[0]
    if fin == x[1][0].info.nombre:
        print(x[1][0].info.nombre)
        fin = x[1][1]
print('Costo del viaje:',costo)


# aeropuertos que se pueden arribar desde Grecia
# forma directa:
print()
ori = buscar_vertice_aero(grafo,'Grecia')
if ori != None:
    print('---Viajes directos desde Grecia---')
    adyacentes(ori)
# forma indirecta:
marcar_no_visitado(grafo)
print()
if ori != None:
    i = 0
    print('...Viajes indirectos desde Grecia...')
    for i in range(len(aero)):
        des = buscar_vertice_aero(grafo,aero[i])
        if des != ori:
            bus = existe_paso_aero(grafo,ori,des)
            print(bus)


#ori = buscar_vertice_aero(grafo,'Grecia')
#des = buscar_vertice_aero(grafo,'Brasil')
#bus = existe_paso_aero(grafo,ori,des)
#print(bus)
'''
#####
# Ejercicio 2
'''
print('Ejercicio 2')
class Objeto():
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
    
    def __str__(self):
        return '| Nombre: '+ self.nombre + ' |Tipo: ' + self.tipo

grafo = Grafo(False)

pc = ['Ubuntu','Mint','Fedora','Manjaro','Parrot']
notebook = ['Debian','Red Hat','Arch']
servidor = ['Guarani','MongoDB']
router = ['Router 1','Router 2','Router 3']
switch = ['Switch 1','Switch 2']
impresora = ['Impresora']

#Carga los vertices del grafo
#A
for i in range (len(pc)):
    dato = Objeto(pc[i], 'PC')
    insertar_vertice_red(grafo, dato)

for i in range (len(notebook)):
    dato = Objeto(notebook[i], 'Notebook')
    insertar_vertice_red(grafo, dato)

for i in range (len(servidor)):
    dato = Objeto(servidor[i], 'Servidor')
    insertar_vertice_red(grafo, dato)

for i in range (len(router)):
    dato = Objeto(router[i], 'Router')
    insertar_vertice_red(grafo, dato)

for i in range (len(switch)):
    dato = Objeto(switch[i], 'Switch')
    insertar_vertice_red(grafo, dato)

for i in range (len(impresora)):
    dato = Objeto(impresora[i], 'Impresora')
    insertar_vertice_red(grafo, dato)

#Carga las aristas del Grafo
ori = buscar_vertice_red(grafo,'Switch 1')
des = buscar_vertice_red(grafo, 'Debian')
dato = 17
insertar_arista_red(grafo,dato,ori,des)

ori = buscar_vertice_red(grafo,'Switch 1')
des = buscar_vertice_red(grafo, 'Ubuntu')
dato = 18
insertar_arista_red(grafo,dato,ori,des)

ori = buscar_vertice_red(grafo,'Switch 1')
des = buscar_vertice_red(grafo, 'Impresora')
dato = 22
insertar_arista_red(grafo,dato,ori,des)

ori = buscar_vertice_red(grafo,'Switch 1')
des = buscar_vertice_red(grafo, 'Mint')
dato = 80
insertar_arista_red(grafo,dato,ori,des)

ori = buscar_vertice_red(grafo,'Switch 1')
des = buscar_vertice_red(grafo, 'Router 1')
dato = 29
insertar_arista_red(grafo,dato,ori,des)

ori = buscar_vertice_red(grafo,'Router 1')
des = buscar_vertice_red(grafo, 'Router 2')
dato = 37
insertar_arista_red(grafo,dato,ori,des)

ori = buscar_vertice_red(grafo,'Router 1')
des = buscar_vertice_red(grafo, 'Router 3')
dato = 43
insertar_arista_red(grafo,dato,ori,des)

ori = buscar_vertice_red(grafo,'Router 2')
des = buscar_vertice_red(grafo, 'Red Hat')
dato = 25
insertar_arista_red(grafo,dato,ori,des)

ori = buscar_vertice_red(grafo,'Router 2')
des = buscar_vertice_red(grafo, 'Guarani')
dato = 29
insertar_arista_red(grafo,dato,ori,des)

ori = buscar_vertice_red(grafo,'Router 2')
des = buscar_vertice_red(grafo, 'Router 3')
dato = 50
insertar_arista_red(grafo,dato,ori,des)

ori = buscar_vertice_red(grafo,'Router 3')
des = buscar_vertice_red(grafo, 'Switch 2')
dato = 61
insertar_arista_red(grafo,dato,ori,des)

ori = buscar_vertice_red(grafo,'Switch 2')
des = buscar_vertice_red(grafo, 'Fedora')
dato = 3
insertar_arista_red(grafo,dato,ori,des)

ori = buscar_vertice_red(grafo,'Switch 2')
des = buscar_vertice_red(grafo, 'Arch')
dato = 56
insertar_arista_red(grafo,dato,ori,des)

ori = buscar_vertice_red(grafo,'Switch 2')
des = buscar_vertice_red(grafo, 'MongoDB')
dato = 5
insertar_arista_red(grafo,dato,ori,des)

ori = buscar_vertice_red(grafo,'Switch 2')
des = buscar_vertice_red(grafo, 'Parrot')
dato = 12
insertar_arista_red(grafo,dato,ori,des)

ori = buscar_vertice_red(grafo,'Switch 2')
des = buscar_vertice_red(grafo, 'Manjaro')
dato = 40
insertar_arista_red(grafo,dato,ori,des)

# Barridos en Amplitud y en Profundidad
#B
bus = buscar_vertice_red(grafo,'Red Hat')
print('Barrido en profundidad Red Hat')
#barrido_profundidad_red(grafo, bus)
print()
marcar_no_visitado(grafo)
print('Barrido en amplitud Red Hat')
#barrido_amplitud_red(grafo, bus)
print()
marcar_no_visitado(grafo)

bus = buscar_vertice_red(grafo,'Debian')
print('Barrido en profundidad Debian')
#barrido_profundidad_red(grafo, bus)
print()
marcar_no_visitado(grafo)
print('Barrido en amplitud Debian')
#barrido_amplitud_red(grafo, bus)
print()
marcar_no_visitado(grafo)

bus = buscar_vertice_red(grafo,'Arch')
print('Barrido en profundidad Arch')
#barrido_profundidad_red(grafo, bus)
print()
marcar_no_visitado(grafo)
print('Barrido en amplitud Arch')
barrido_amplitud_red(grafo, bus)
print()
marcar_no_visitado(grafo)

#C
distanciaMenor = ['Manjaro','Red Hat', 'Fedora']
for i in range(0,len(distanciaMenor)):
    ori = distanciaMenor[i]
    distancia = None
    fin = 'Impresora'
    camino_mas_corto = dijkstra_red(grafo,ori,'Impresora')
    while not pila_vacia(camino_mas_corto):
        dato = desapilar(camino_mas_corto)
        if distancia is None and fin == dato[1][0].info.nombre:
            distancia = dato[0]
    print('El camino mas corto desde',ori,'hasta impresora es:',distancia)


#C
distanciaMenor = ['Manjaro','Red Hat', 'Fedora']
for i in range(0,len(distanciaMenor)):
    ori = distanciaMenor[i]
    distancia = None
    fin = 'Impresora'
    camino_mas_corto = dijkstra_red(g,ori,'Impresora')
    while not pila_vacia(camino_mas_corto):
        dato = desapilar(camino_mas_corto)
        if distancia is None and fin == dato[1][0].info.nombre:
            distancia = dato[0]
    print('El camino mas corto desde',ori,'hasta impresora es: ',distancia)


#D
bosque = prim_red(g)

print('Arbol de expansion minima:')
for i in range(0,len(bosque),2):
    print(bosque[i], '|',bosque[i+1])
print()

#E
menor = 200
for i in range(0,len(pc)):
    ori = pc[i]
    distancia = None
    fin = 'Guarani'
    camino_mas_corto = dijkstra_red(g,ori,'Guarani')
    while not pila_vacia(camino_mas_corto):
        dato = desapilar(camino_mas_corto)
        if distancia is None and fin == dato[1][0].info.nombre:
            distancia = dato[0]
    if distancia < menor:
        menor_nombre = ori
        menor = distancia

print(menor_nombre,'es el camino mas corto hasta el servidor guarani con un peso de', menor)

#F
s1 = ['Debian','Ubuntu','Impresora','Mint']
menor = 218
for i in range(0,len(s1)):
    ori = s1[i]
    distancia = None
    fin = 'MongoDB'
    camino_mas_corto = dijkstra_red(g,ori,'MongoDB')
    while not pila_vacia(camino_mas_corto):
        dato = desapilar(camino_mas_corto)
        if distancia is None and fin == dato[1][0].info.nombre:
            distancia = dato[0]
    if distancia < menor:
        menor_nombre = ori
        menor = distancia
print(menor_nombre,'es el camino mas corto hasta el servidor MongoDB con un peso de', menor)

#G
"Eliminamos las aristas de impresora a sw1"
ori = buscar_vertice_red(g, 'Switch 1')
eliminar_arista_red(g, ori, 'Impresora')
ori = buscar_vertice_red(g, 'Impresora')
eliminar_arista_red(g, ori, 'Switch 1')

"Insertamos las aristas de impresora a router 2"
ori = buscar_vertice_red(g, 'Impresora')
des = buscar_vertice_red(g, 'Router 2')
insertar_arista_red(g, 22, ori, des)

'''
#####
#Ejercicio 3
'''
print('Ejercicio 3:')
nombre = ['M1','M2','M3','M4','M5','M6','M7']
tipo = ['Natural','Arquitectonica']
pais = ['México','Italia','Brasil','Argentina','Rusia','España','China']

class Maravilla():
    def __init__(self,nombre,pais,tipo):
        self.nombre = nombre
        self.pais = pais
        self.tipo = tipo
    
    def __str__(self):
        return self.nombre , '| Pais:', self.pais,'| Tipo de maravilla:', self.tipo

grafo = Grafo(False)
#A
shuffle(pais)
for i in range(len(nombre)):
    dato = Maravilla(nombre[i],pais[i],choice(tipo))
    insertar_vertice_red(grafo,dato)


# B
# Carga de aristas

ori = buscar_vertice_red(grafo,'M1')
des = buscar_vertice_red(grafo,'M2')
insertar_arista_red(grafo,randint(1,30),ori,des)
des = buscar_vertice_red(grafo,'M3')
insertar_arista_red(grafo,randint(1,30),ori,des)
des = buscar_vertice_red(grafo,'M4')
insertar_arista_red(grafo,randint(1,30),ori,des)
des = buscar_vertice_red(grafo,'M5')
insertar_arista_red(grafo,randint(1,30),ori,des)
des = buscar_vertice_red(grafo,'M6')
insertar_arista_red(grafo,randint(1,30),ori,des)
des = buscar_vertice_red(grafo,'M7')
insertar_arista_red(grafo,randint(1,30),ori,des)

ori = buscar_vertice_red(grafo,'M2')
des = buscar_vertice_red(grafo,'M3')
insertar_arista_red(grafo,randint(1,30),ori,des)
des = buscar_vertice_red(grafo,'M4')
insertar_arista_red(grafo,randint(1,30),ori,des)
des = buscar_vertice_red(grafo,'M5')
insertar_arista_red(grafo,randint(1,30),ori,des)
des = buscar_vertice_red(grafo,'M6')
insertar_arista_red(grafo,randint(1,30),ori,des)
des = buscar_vertice_red(grafo,'M7')
insertar_arista_red(grafo,randint(1,30),ori,des)

ori = buscar_vertice_red(grafo,'M3')
des = buscar_vertice_red(grafo,'M4')
insertar_arista_red(grafo,randint(1,30),ori,des)
des = buscar_vertice_red(grafo,'M5')
insertar_arista_red(grafo,randint(1,30),ori,des)
des = buscar_vertice_red(grafo,'M6')
insertar_arista_red(grafo,randint(1,30),ori,des)
des = buscar_vertice_red(grafo,'M7')
insertar_arista_red(grafo,randint(1,30),ori,des)

ori = buscar_vertice_red(grafo,'M4')
des = buscar_vertice_red(grafo,'M5')
insertar_arista_red(grafo,randint(1,30),ori,des)
des = buscar_vertice_red(grafo,'M6')
insertar_arista_red(grafo,randint(1,30),ori,des)
des = buscar_vertice_red(grafo,'M7')
insertar_arista_red(grafo,randint(1,30),ori,des)

ori = buscar_vertice_red(grafo,'M5')
des = buscar_vertice_red(grafo,'M6')
insertar_arista_red(grafo,randint(1,30),ori,des)
des = buscar_vertice_red(grafo,'M7')
insertar_arista_red(grafo,randint(1,30),ori,des)

ori = buscar_vertice_red(grafo,'M6')
des = buscar_vertice_red(grafo,'M7')
insertar_arista_red(grafo,randint(1,30),ori,des)

ar = prim_arq(grafo)
print()
print('Arbol de expansion minima:')
print(ar)

print()
ar = prim_nat(grafo)
print('otro arbol.')
print(ar)


#barrido_grafo(grafo)
'''