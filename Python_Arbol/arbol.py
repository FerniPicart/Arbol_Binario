from TDA_Arbol_Binario import insertar_nodo, eliminar_nodo, insertar_nodo_huffman, nodoArbolHuffman, inorden, inorden_dioses, inorden_villano, postorden, preorden, por_nivel, por_nivel_nario, busqueda_valor, arbol_vacio, remplazar, pares_impares, contar_ocurrencias, insertar_nodo_morse, busqueda_nario, por_nivel_nario, Nodo_Greek, insertar_nario, insertar_nodo_nrr, busqueda_proximidad
from TDA_Arbol_Binario_AVL import insertar_nodo_mensajes, altura, actualizaraltura, superheroes_c, contar_supreheroes, bosque_s_v, contar_nodos, insertar_nodo, padre, busqueda, padre, hijo_der, hijo_izq, maximo_nodo, minimo_nodo, postorden_superheroes, cantidad_hojas, inorden_nombre_rank, busqueda_arbol, inorden_jedimaster, inorden_especie, inorden_ayguion, inorden_lightsaber, inorden_altura, inorden_peso, busqueda_proximidad_archivo_pokemon, busqueda_archivo_pokemon_num, inorden_pok, busqueda_proximidad_archivo_libro, busqueda_archivo_ISBN, busqueda_mayor_cant_pag
from random import randint
from Archivo import abrir, cerrar, leer, guardar, modificar

# 2 3 7 10 13 18 22 24

#####
#EJ 1
arbol = None
'''
print('Ej 1')
for i in range(10):
    arbol = insertar_nodo(arbol, randint(50,57))
print()
# A
#inorden(arbol)
#preorden(arbol)
#postorden(arbol)
por_nivel(arbol)
print()
# B
bus = int(input('Verifique si un numero está cargado: '))
busqueda(arbol, bus)
# C
print()
elim = randint(50,100)
print('Numero a eliminar: ' + str(elim))
eliminar_nodo(arbol,elim)
elim = randint(50,100)
print('Numero a eliminar: ' + str(elim))
eliminar_nodo(arbol,elim)
elim = randint(50,100)
print('Numero a eliminar: ' + str(elim))
eliminar_nodo(arbol,elim)
print()
print('ULTIMO ARBOL:')
inorden(arbol)
print()
# E
bus = int(input('A que nro contar las ocurrencias? : '))
cant = 0
cant = contar_ocurrencias(arbol,bus,cant)
print('El nro fue encontrado: '+ str(cant) + ' veces.')
print()
# F
par,impar = 0,0
par, impar = pares_impares(arbol,par,impar)
print('cantidad de nros pares: '+str(par))
print('cantidad de nros impares: '+str(impar))

# EJ 4
print()
print('Ejercicio 4')
hijo_der(arbol)
hijo_izq(arbol)
print()
'''
#####
#EJ 5
'''
print('Ejercicio 5:')
arbol = None

# A
# True = Heroe, False = Villano
arbol = insertar_nodo_huffman(arbol,'Iron Man',True)
arbol = insertar_nodo_huffman(arbol,'Thor',True)
arbol = insertar_nodo_huffman(arbol,'Loki',False)
arbol = insertar_nodo_huffman(arbol,'Ultrón',False)
arbol = insertar_nodo_huffman(arbol,'Hulk',True)
arbol = insertar_nodo_huffman(arbol,'Thanos',False)
arbol = insertar_nodo_huffman(arbol,'Capitán América',True)
arbol = insertar_nodo_huffman(arbol,'Doctor Strange',True)
# B
# Muestra todos los Villanos
print('Listado de villanos en orden alfabetico:')
inorden_villano(arbol)
print()
# C
# Solo Superheroes con la primera letra "C"
print('Superheroes que empiezan con C:')
superheroes_c(arbol)
# D
# Numero de superheroes en el arbol
input()
cont = 0
print('Hay '+ str(contar_supreheroes(arbol,cont)) + ' supreheroes en el arbol.')
# E
# Busqueda de nombre por proximidad
print()
busc = input('Busque un nombre de superheroe por proximidad: ')
busqueda_proximidad(arbol,busc)
input()
# F
# Muestra info de todos los Superheroes
print('Superheroes ordenados de manera descendente')
postorden_superheroes(arbol)
print()
# G
sup, vill = None, None
sup,vill = bosque_s_v(arbol,sup ,vill)
print('.................')
print('Bosque SuperHeroes alfabeticamente:')
inorden(sup)
cant = None
cant = contar_nodos(sup)
print('->Cantidad de nodos Heroes: ', cant)
print()
print('.................')
print('Bosque Villanos alfabeticamente:')
inorden(vill)
cant = None
cant = contar_nodos(vill)
print('->Cantidad de nodos Villanos: ', cant)
'''
#####
# Ejercicio 6
'''
print('Ejercicio 6')
print()
datos = [['Yoda','Desconocida','1800','Verde','Jedi Knight','Luke Skywalker'],
         ['Luke Skywalker','Humano','1450','Verde','Jedi Master','Obi-Wan Kenobi'],
         ['Sifo-Dyas','Cerean','1600','Verde','Jedi Knight','Conde Dooku'],
         ['Shaak Ti','Togruta','1800','Azul','Padawan','Zett Jukassa'],
         ['Aayla Secura','Twi’lek','1500','Azul','Jedi Master','Quinlan Vos'],
         ['Zett Jukassa','Cerean','1650','Azul','Padawan','Yoda'],
         ['Qui-Gon Jinn','Humano','','Verde','Jedi Master','Conde Dooku']]

class Jedi():
    def __init__(self,nombre,especie,año_nacimiento,color_sable,rank,maestro):
        self.nombre = nombre
        self.especie = especie
        self.año_nacimiento = año_nacimiento
        self.color_sable = color_sable
        self.rank = rank
        self.maestro = maestro

# A
arbol_nombre = None
arbol_rank = None
arbol_especie = None

# Cargo los datos en archivo
arch = abrir('jedis')
for i in datos:
    dato = Jedi(i[0],i[1],i[2],i[3],i[4],i[5])
    guardar(arch,dato)
cerrar(arch)
# Cargo los datos del archivo en los arboles
arch = abrir('jedis')
pos = 0
while pos < len(datos):
    jedi = leer(arch, pos)
    arbol_nombre = insertar_nodo_nrr(arbol_nombre, jedi.nombre, pos)
    arbol_rank = insertar_nodo_nrr(arbol_rank, jedi.rank, pos)
    arbol_especie = insertar_nodo_nrr(arbol_especie , jedi.especie, pos)
    pos += 1
cerrar(arch)

# B
# Barrido inorden por Nombre y Ranking
print('INORDEN POR NOMBRE Y RANKING')
arch = abrir('jedis')
inorden_nombre_rank(arbol_nombre, arch)
cerrar(arch)
input()

# C
# Barrido por nivel de Ranking y Especies
arch = abrir('jedis')
print('_ Por Nivel Ranking:')
por_nivel(arbol_rank)
input()
print('_Por Nivel Especies:')
por_nivel(arbol_especie)
input()

# D
# Muestro info de Luke Skywalker y Yoda
print('Informacion: Luke Skywalker')
print('NOMBRE, ESPECIE, RANKING,  MAESTRO, COLOR DE SABLE')
pos = busqueda_arbol(arbol_nombre, 'Luke Skywalker')
# Datos Luke Skywalker
if pos is not None:
    arch = abrir('jedis')
    jedi = leer(arch, pos.nrr)
    print('Nombre:',jedi.nombre,'|Especie:',jedi.especie,'|Rank:',jedi.rank,'|Maestro:',jedi.maestro,'|Color del Sable:',jedi.color_sable)
    cerrar(arch)
print()
# Datos Yoda
print('Info de Yoda')
print('NOMBRE, ESPECIE, RANKING,  MAESTRO, COLOR DE SABLE')
pos = busqueda_arbol(arbol_nombre, 'Yoda')
if pos is not None:
    arch = abrir('jedis')
    jedi = leer(arch, pos.nrr)
    print('Nombre:',jedi.nombre,'|Especie:',jedi.especie,'|Rank:',jedi.rank,'|Maestro:',jedi.maestro,'|Color del Sable:',jedi.color_sable)
    cerrar(arch)
input()

# E
# Informacion de JEDIS CON RANKING: "JEDI MASTER"
print('JEDIS CON RANKING: "JEDI MASTER"')
arch = abrir('jedis')
inorden_jedimaster(arbol_nombre, arch)
cerrar(arch)
input()

# F
print('JEDIS CON SABLE COLOR VERDE')
arch = abrir('jedis')
inorden_lightsaber(arbol_nombre, arch)
cerrar(arch)
input()

# h
print('JEDIS DE ESPECIE TOGRUTA O CEREAN')
arch = abrir('jedis')
inorden_especie(arbol_nombre, arch)
cerrar(arch)
input()

# i
print('JEDIS QUE COMIENZAN CON LA LETRA A Y CONTIENEN UN "-"')
arch = abrir('jedis')
inorden_ayguion(arbol_nombre, arch)
cerrar(arch)
input()
'''
#####
#Ejercicio 8
'''
print('Ejercicio 8')
arbol = None

for i in range(10):
    arbol = insertar_nodo(arbol,randint(0,100))

preorden(arbol)
max = maximo_nodo(arbol)
print('-Nodo Maximo: ' + str(max.info))
min = minimo_nodo(arbol)
print('-Nodo Minimo: ' + str(min.info))
'''
####
#Ejercicio 9
'''
print('Ejercicio 9')

tabla = [['A', 0.2], ['F', 0.17], ['1', 0.13], ['3', 0.21], ['0', 0.05], ['M', 0.09], ['T', 0.15]]
dic = {'A' : '00', '3': '01', '1' : '100', 'T': '110', 'F' : '111', '0': '1010', 'M' : '1011'}
def como_comparo(elemento):
    return elemento[1]
def como_comparo_nodo(elemento):
    return elemento.valor


tabla.sort(key=como_comparo)
bosque = []
for elemento in tabla:
    nodo = nodoArbolHuffman(elemento[0], elemento[1])
    bosque.append(nodo)
for elemento in bosque:
    print(elemento.info, elemento.valor)
print()
while(len(bosque) > 1):
    elemento1 = bosque.pop(0)
    elemento2 = bosque.pop(0)
    nodo = nodoArbolHuffman('', elemento1.valor + elemento2.valor)
    nodo.izq = elemento1
    nodo.der = elemento2
    bosque.append(nodo)
    bosque.sort(key=como_comparo_nodo)
por_nivel(bosque[0])

def decodificar(cadena, arbol_huff):
    cadena_deco = ''
    raiz_aux = arbol_huff
    pos = 0
    while(pos < len(cadena)):
        if(cadena[pos] == '0'):
            raiz_aux = raiz_aux.izq
        else:
            raiz_aux = raiz_aux.der
        pos += 1
        if(raiz_aux.izq is None):
            cadena_deco += raiz_aux.info
            raiz_aux = arbol_huff
        cadena_deco
    return cadena_deco

def codificar(cadena, dic):
    cadena_cod = ''
    for caracter in cadena:
        cadena_cod += dic[caracter]
    return cadena_cod
cadena = "AA31TF0AAMMMMMM0000"
from sys import getsizeof
cadena_cod = codificar(cadena, dic)
print(getsizeof(cadena_cod), getsizeof(b'00000110011011110100000'))
print('cadena decodificada')
cadena_deco = decodificar(cadena_cod, bosque[0])
print(cadena_deco)
'''
#####
# Ejercicio 11
'''
print('Ejercicio 11')
arbol = None
for i in range(10):
    aux = randint(1,12)
    arbol = insertar_nodo(arbol,aux)
    print(aux)
nodos = 0
# A
nodos = contar_nodos(arbol,nodos)
print('Cantidad de nodos del arbol: ', nodos)
# B y C
hojas = 0
print('-Nodos hojas:')
hojas = cantidad_hojas(arbol,hojas)
print()
print('Cantidad de Hojas del arbol: ', hojas)
# D
print()
bus = int(input('Conocer padre del nodo: '))
padre(arbol,bus)
# E
# alt = None
# alt = altura(arbol)
# print('La altura del arbol es de :', alt)
'''
#######
# Ejercicio 12
'''
arbol = None
print('-Ejercicio 12:')

for i in range(1,1024):
    arbol = insertar_nodo(arbol, i)

cantidad = [0]
contar_nodos(arbol, cantidad)
print('Cantidad de nodos:', cantidad[0])
print('Altura del arbol:', altura(arbol))
print()

bosque = []
cortar_por_nivel(arbol, bosque)
print('Cortando el arbol...')
print('Tamaño del bosque:', len(bosque))
print()

for arbol in bosque:
    print('Raiz del arbol:', arbol.info)
    cantidad = [0]
    #preorden(arbol)
    contar_nodos(arbol, cantidad)
    print('Cantidad de nodos del arbol:', cantidad[0])
    print()
'''
########
# Ejercicio 14
'''
print('Ejercicio 14')
arbol = None
alfa = ['','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0']
cod = ['','.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---',
        '.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..',
        '.----','..---','...--','....-','.....','-....','--...','---..','----.','-----']

for i in range(0,len(alfa)):
        arbol = insertar_nodo_huffman(arbol,alfa[i-1],cod[i-1])
inorden_dioses(arbol)

mensaje = ''
arbol = None
tabla = [[10000, ''],[5000, 'E'],[15000, 'T'],[2500, 'I'],[7500, 'A'],[12500, 'N'],[17500, 'M'],[1500, 'S'],[3500, 'U'],[6500, 'R'], [8500, 'W'],[11500, 'D'],[13500, 'K'],[16500, 'G'],[18500, 'O'],
        [1000, 'H'],[2000, 'V'],[3000, 'F'],[4000, ''],[6000, 'L'],[7000, ''],[8000, 'P'],[9000, 'J'],[11000, 'B'],[12000, 'X'],
        [13000, 'C'],[14000, 'Y'],[16000, 'Z'],[17000, 'Q'],[18000, ''],[19000, ''],[750, '5'],[1250, '4'],[2250,'3'],[4250, '2'],[9250, '1'], [10750, '6'],[15750, '7'],[17750, '8'],[18750, '9'],[19250, '0']]

#A Generar un árbol que contenga todo el alfabeto y los dígitos del 0 al 9.
#B Cuya raíz es vacía y, a partir de esta, la izquierda significa punto y la derecha guion, y se cargaran según su codificación morse.

for letra in tabla:
    arbol = insertar_nodo_morse(arbol, letra)

def decodificar_morse(raiz, cadena):
    cadena_deco = ''
    raiz_aux = raiz
    pos = 0
    while(pos < len(cadena)):
        if(cadena[pos] == '.'):
            #print('Dato izq: ',raiz_aux.izq.info)
            raiz_aux = raiz_aux.izq
        else:
            #print('Dato der: ',raiz_aux.der.info)
            raiz_aux = raiz_aux.der
        pos += 1
    if (raiz_aux is not None):
        cadena_deco += raiz_aux.info[1]
    raiz_aux = raiz
    return cadena_deco
def descifrar_morse(msj, mensaje):
    for palabra in msj.split('/'):
        x = ''
        #print('Palabra:', palabra)
        for letra in palabra.split(' '):
            #print(letra)
            x += decodificar_morse(arbol, letra)
        mensaje += x
        mensaje += ' '
    return mensaje
#D Descifrar los siguientes mensajes.
msj1 = '.--. .- ... . / .-.. --- / --.- ..- . / .--. .- ... . / -- .- .- -. .- / .--. .-. --- -- . - .- -- . / .- .-.. --. --- / --.- ..- . / ... . --. ..- .. .-. / ... .. . -. -.. --- / ..- ... - . -.. / -. --- / ..- -. / ... --- .-.. -.. .- -.. --- / .--. . .-. ..-. . -.-. - --- / ... .. -. --- / ..- -. / -... ..- . -. / .... --- -- -... .-. . .-.-.'
msj2 = '-. --- ... --- - .-. --- ... / ... --- -- --- ... / .-.. --- ... / -- .- .-.. -.. .. - --- ... / --. ..- .- .-. -.. .. .- -. . ... / -.. . / .-.. .- / --. .- .-.. .- -..- .. .- .-.-.'
msj3 = '-.-- --- / ... --- .-.. --- / .- -.-. - ..- --- / -.-. --- -- --- / ... .. / . -. / ...- . .-. -.. .- -.. / .-.. --- / ... ..- .--. .. . .-. .- / - --- -.. --- .-.-.'
msj4 = '-.-. .... .. -.-. --- ... / . ... - --- -.-- / .-.. .-.. . ...- .- -. -.. --- / .-.. .- / ..-. .. . ... - .- / .... .- -.-. .. .- / ..- ... - . -.. . ... .-.-.'
msj5 = '.--. --- -.. .-. .. .- / .... .- -.-. . .-. / . ... - --- / - --- -.. --- / . .-.. / -.. .. .- .-.-.'
print('Mensaje 1 (Dr. Abraham Erskine): ',descifrar_morse(msj1, mensaje))
print()
print('Mensaje 2 (Rocket Raccoon): ',descifrar_morse(msj2, mensaje))
print()
print('Mensaje 3 (Natasha Romanoff): ',descifrar_morse(msj3, mensaje))
print()
print('Mensaje 4 (Tony Stark): ',descifrar_morse(msj4, mensaje))
print()
print('Mensaje 5 (Steve Rogers): ',descifrar_morse(msj5, mensaje))
print()
'''
#####
# Ejercicio 15

print('Ejercicio 15')
arbol = None

class Personaje():
    def __init__(self,nombre,altura,peso):
        self.nombre = nombre
        self.altura = altura
        self.peso = peso

datos = [['Darth Vader', 1.85, 93.4], ['Chewbacca', 2.04, 113.0], ['C-3PO', 1.67, 72.9],
         ['Yoda', 0.9, 47.3], ['Boba Fett', 1.83, 78.4], ['Han Solo', 1.77, 83.9],
         ['Jabba el Hutt', 3.9, 531.2], ['Darth Maul', 1.78, 74.1]]

arch = abrir('starwars')
for dato in datos:
    x = Personaje(dato[0], dato[1], dato[2])
    guardar(arch, x)

# A
# inserta nombres en arbol
pos = 0
while pos < len(datos):
    personaje = leer(arch, pos)
    arbol = insertar_nodo_nrr(arbol, personaje.nombre,pos)
    print(personaje.nombre, 'añadido en la posicion:', pos)
    pos += 1
cerrar(arch)
# Muestro el arbol completo POR NIVEL
input()
print('Arbol de personajes:')
por_nivel(arbol)
input()

# B
# Cargar , eliminar o modificar personaje
print('1) Alta')
print('2) Baja')
print('3) Modificacion')
print('4) Salir')
control = input('Seleccione una opcion (1/2/3/4): ')
print()
mod = False

def alta_sw(arbol):
    arch = abrir('starwars')
    nom = input('Ingrese un nombre: ')
    alt = float(input('Ingrese su altura: '))
    peso = float(input('Ingrese su peso: '))
    dato = Personaje(nom,alt, peso)
    insertar_nodo_nrr(arbol, dato.nombre, pos)
    guardar(arch, dato)
    cerrar(arch)
    datos.append([nom, alt, peso])

def baja_sw(arbol):
    arch = abrir('starwars')
    buscado = input('Ingrese nombre del personaje a dar de baja: ')
    arbol, x = eliminar_nodo(arbol, buscado)
    print('Se ha eliminado:', x)
    cerrar(arch)

def modif_sw(arbol):
    arch = abrir('starwars')
    busc = input('Ingrese nombre del personaje a modificar: ')
    val = busqueda_arbol(arbol, busc)
    if val is not None:
        print('1) Nombre')
        print('2) Altura')
        print('3) Peso')
        mod = input('Elija campo a modificar: ')
        sw = leer(arch, pos)
        if mod == '1':
            nom = input('Ingrese el nuevo nombre: ')
            dato = Personaje(nom, sw.altura, sw.peso)
            modificar(arch, pos, dato)
            sw = leer(arch, pos)
            arbol = insertar_nodo_nrr(arbol, sw.nombre, pos)
        elif mod == '2':
            alt = float(input('Ingrese la nueva altura: '))
            dato = Personaje(sw.nombre, alt, sw.peso)
            modificar(arch, pos, dato)
            sw = leer(arch, pos)
            arbol = insertar_nodo_nrr(arbol, sw.nombre, pos)
        elif mod == '3':
            peso = float(input('Ingrese el nuevo peso: '))
            dato = Personaje(sw.nombre, sw.altura, peso)
            modificar(arch, pos, dato)
            sw = leer(arch, pos)
            arbol = insertar_nodo_nrr(arbol, sw.nombre, pos)
        else:
            print('ERROR')
    else:
        print('El personaje no existe')
    cerrar(arch)


if control == '1':
    print('Op 1:')
    alta_sw(arbol)
    mod = True
elif control == '2':
    print('Op 2:')
    baja_sw(arbol)
    mod = True
elif control == '3':
    print('Op 3:')
    modif_sw(arbol)
    mod = True
elif control == '4':
    print('Op 4.')
else:
    print('ERROR')
print()

# C
arch = abrir('starwars')

# Informacion de Yoda
for i in range(len(datos)):
    pos = leer(arch, i)
    if pos.nombre == 'Yoda':
        print('Informacion de Yoda:')
        print('Nombre:', pos.nombre)
        print('Altura:', pos.altura)
        print('Peso:', pos.peso)
print()

# Informacion de Boba Fett
for i in range(len(datos)):
    pos = leer(arch,i)
    if pos.nombre == 'Boba Fett':
        print('Informacion de Boba Fett:')
        print('Nombre:', pos.nombre)
        print('Altura:', pos.altura)
        print('Peso:', pos.peso)

cerrar(arch)
input()

# D
# Lista ordenada de personajes + 1m altura
print('Personajes que miden mas de 1 metro')
arch = abrir('starwars')
inorden_altura(arbol, arch)
cerrar(arch)
print()

# E
# Los que pesan menos de 75kg
print('Personajes que pesan menos de 75kg')
arch = abrir('starwars')
inorden_peso(arbol, arch)
cerrar(arch)
input()

if mod == True:
    print('FINAL: Arbol modificado:')
    por_nivel(arbol)
    print()
'''
#####
# Ejercicio 16
'''
def como_comparo(elemento):
    return elemento[1]

def como_comparo_nodo(elemento):
    return elemento.valor

print('Ejercicio 16')

tabla = []

archivo = open('valores.txt')

linea = archivo.readline()

print('archivo')
while linea:
    linea = linea.replace('\n', '')
    tabla.append(linea.split(';'))
    linea = archivo.readline()

dic = {}

tabla.sort(key=como_comparo)

bosque = []

for elemento in tabla:
    nodo = nodoArbolHuffman(elemento[0], elemento[1])
    bosque.append(nodo)

# for elemento in bosque:
#     print(elemento.info, elemento.valor)
# print()

while(len(bosque) > 1):
    elemento1 = bosque.pop(0)
    elemento2 = bosque.pop(0)
    nodo = nodoArbolHuffman('', elemento1.valor+elemento2.valor)
    nodo.izq = elemento1
    nodo.der = elemento2
    bosque.append(nodo)
    bosque.sort(key=como_comparo_nodo)


#por_nivel(bosque[0])

def generar_tabla(raiz, dic, cadena=''):
    if(raiz is not None):
        if(raiz.izq is None):
            dic[raiz.info] = cadena
            #print(raiz.info, cadena)
        else:
            cadena += '0'
            generar_tabla(raiz.izq, dic, cadena)
            cadena = cadena[0:-1]
            cadena += '1'
            generar_tabla(raiz.der, dic, cadena)


generar_tabla(bosque[0],dic)
print(dic)

def decodificar(cadena, arbol_huff):
    cadena_deco = ''
    raiz_aux = arbol_huff
    pos = 0
    while(pos < len(cadena)):
        if(cadena[pos] == '0'):
            raiz_aux = raiz_aux.izq
        else:
            raiz_aux = raiz_aux.der
        pos += 1
        if(raiz_aux.izq is None):
            cadena_deco += raiz_aux.info
            raiz_aux = arbol_huff
        cadena_deco
    return cadena_deco


def codificar(cadena, dic):
    cadena_cod = ''
    for caracter in cadena.split('-'):
        cadena_cod += dic[caracter]
    return cadena_cod

cadena = "Nublado-Baja-1-5-7"
cadena_cod = codificar(cadena, dic)
print(cadena_cod)
print('cadena decodificada')
cadena_deco = decodificar(cadena_cod, bosque[0])
print(cadena_deco)

#####
# Ejercicio 17
'''
print('Ejercicio 17')

class Pokemon():
    def __init__(self,nombre,num,tipo,debilidad):
        self.nombre = nombre
        self.num = num
        self.tipo= tipo
        self.debilidad = debilidad

a_nombres = None
a_numeros = None
a_tipos = None

datos = [['Bulbasaur', 1, 'planta/veneno', 'fuego/psiquico'],
         ['Charmander', 4, 'fuego', 'agua/tierra'],
         ['Charizard', 6, 'fuego/volador', 'agua/electrico'], 
         ['Squirtle', 7, 'agua', 'planta/electrico'], 
         ['Butterfree', 12, 'bicho/volador', 'fuego/electrico/hielo'], 
         ['Pidgeotto', 17, 'normal/volador', 'hielo/roca'], 
         ['Rattata', 19, 'normal', 'lucha'], 
         ['Weedle', 13, 'bicho/veneno', 'fuego/psiquico/volador'], 
         ['Pikachu', 25, 'electrico', 'tierra'], 
         ['Raichu', 26, 'electrico', 'tierra'], 
         ['Meowth', 52, 'normal', 'lucha'],
         ['Growlithe', 58, 'fuego', 'agua/roca'], 
         ['Tentacool', 72, 'agua/veneno', 'psiquico/electrico'], 
         ['Weepinbell', 70, 'planta/veneno', 'fuego/volador/hielo']]

# carga de datos
archivo = abrir('pokemon')

for i in datos:
    dato = Pokemon(i[0],i[1],i[2],i[3])
    guardar(archivo,dato)
# A
pos = 0
while pos < len(datos):
    x = leer(archivo,pos)
    a_nombres = insertar_nodo_nrr(a_nombres,x.nombre,pos)
    a_numeros = insertar_nodo_nrr(a_numeros,x.num,pos)
    a_tipos = insertar_nodo_nrr(a_tipos,x.tipo,pos)
    pos += 1
cerrar(archivo)
# B
# Busqueda datos pokemon por numero
archivo = abrir('pokemon')
bus = input(str('Busqueda pokemon por NUMERO: '))
busqueda_archivo_pokemon_num(a_numeros,int(bus),archivo)
print()
bus = input('pokemon a buscar por NOMBRE: ')
busqueda_proximidad_archivo_pokemon(a_nombres,bus,archivo)
print()
# C
bus = input('pokemon a buscar por TIPO: ')
busqueda_proximidad_archivo_pokemon(a_tipos,bus,archivo)

cerrar(archivo)

archivo = abrir('pokemon')
print()
print('Listado en orden por NUMERO:')
inorden_pok(a_numeros,archivo)
input()
print('Listado en orden por NOMBRE')
inorden_pok(a_nombres,archivo)
cerrar(archivo)
'''
#####
# Ejercicio 19
'''
print('Ejercicio 19')
a_titulo = None
a_ISBN = None
a_autor = None

class Libro():
    def __init__(self,titulo,ISBN,autor,editorial,cant_pag):
        self.titulo = titulo
        self.ISBN = ISBN
        self.autor = autor
        self.editorial = editorial
        self.cant_pag = cant_pag

lista = [['Mineria de datos', 1234, 'Tanenbaum', 'Santillán', 256],
         ['Algoritmos I', 4567, 'Connolly', 'Acantilado', 380],
         ['Algoritmos II', 8910, 'Rowling', 'Santillán',450],
         ['Los 100', 1112, 'Riordan', 'Acantilado', 360],
         ['Bases de datos', 1314, 'Morgan Kass', 'Santillán', 880],
         ['Algoritmos y estructuras de datos', 9789504967453, 'Tanenbaum', 'Acantilado', 950]]

arch = abrir('libros')
# C
for i in lista:
    dato = Libro(i[0],i[1],i[2],i[3],i[4])
    guardar(arch,dato)

pos = 0
while pos < len(lista):
    x = leer(arch,pos)
    a_titulo = insertar_nodo_nrr(a_titulo,x.titulo,pos)
    a_ISBN = insertar_nodo_nrr(a_ISBN,x.ISBN,pos)
    a_autor = insertar_nodo_nrr(a_autor,x.autor,pos)
    pos += 1

cerrar(arch)
arch = abrir('libros')
# D
busqueda_archivo_ISBN(a_ISBN,1234,arch)
print()
busqueda_proximidad_archivo_libro(a_autor,'Tan',arch)
print()
busqueda_proximidad_archivo_libro(a_titulo,'Alg',arch)
print()
print('- Libros de Tanenbaum:')
#busqueda_proximidad_archivo_libro(a_autor,'Tanenbaum',arch)
print('- Libros de Connolly:')
#busqueda_proximidad_archivo_libro(a_autor,'Connolly',arch)
print('- Libros de Rowling:')
#busqueda_proximidad_archivo_libro(a_autor,'Rowling',arch)
print('- Libros de Riordan:')
#busqueda_proximidad_archivo_libro(a_autor,'Riordan',arch)
print('- Libros de Morgan Kass:')
busqueda_proximidad_archivo_libro(a_autor,'Morgan Kass',arch)
input()

busqueda_proximidad_archivo_libro(a_titulo,'Bases de datos',arch)
busqueda_proximidad_archivo_libro(a_titulo,'Mineria de datos',arch)
busqueda_proximidad_archivo_libro(a_titulo,'Algoritmos',arch)
print()
print('Libros de mas de 873 Paginas:')
busqueda_mayor_cant_pag(a_titulo, 873, arch)
print()
print('Libro con ISBN = 9789504967453:')
busqueda_archivo_ISBN(a_ISBN,9789504967453,arch)
print()
print('Libro los 100:')
busqueda_proximidad_archivo_libro(a_titulo,'Los 100',arch)
'''
#####
# Ejercicio 20
'''
tabla = []
archivo = open('valores')
linea = archivo.readline()
while linea:
    linea = linea.replace('\n', '')
    tabla.append(linea.split(';'))
    linea = archivo.readline()
dic = {}
def como_comparo(elemento):
    return elemento[1]
def como_comparo_nodo(elemento):
    return elemento.valor
tabla.sort(key=como_comparo)
bosque = []
for elemento in tabla:
    nodo = nodoArbolHuffman(elemento[0], elemento[1])
    bosque.append(nodo)
# for elemento in bosque:
#     print(elemento.info, elemento.valor)
# print()
while(len(bosque) > 1):
    elemento1 = bosque.pop(0)
    elemento2 = bosque.pop(0)
    nodo = nodoArbolHuffman('', elemento1.valor+elemento2.valor)
    nodo.izq = elemento1
    nodo.der = elemento2
    bosque.append(nodo)
    bosque.sort(key=como_comparo_nodo)
#por_nivel(bosque[0])
def generar_tabla(raiz, dic, cadena=''):
    if(raiz is not None):
        if(raiz.izq is None):
            dic[raiz.info] = cadena
            #print(raiz.info, cadena)
        else:
            cadena += '0'
            generar_tabla(raiz.izq, dic, cadena)
            cadena = cadena[0:-1]
            cadena += '1'
            generar_tabla(raiz.der, dic, cadena)
generar_tabla(bosque[0],dic)
def decodificar(cadena, arbol_huff):
    cadena_deco = ''
    raiz_aux = arbol_huff
    pos = 0
    while(pos < len(cadena)):
        if(cadena[pos] == '0'):
            raiz_aux = raiz_aux.izq
        else:
            raiz_aux = raiz_aux.der
        pos += 1
        if(raiz_aux.izq is None):
            cadena_deco += raiz_aux.info
            raiz_aux = arbol_huff
        cadena_deco
    return cadena_deco
def codificar(cadena, dic):
    cadena_cod = ''
    for caracter in cadena.split('-'):
        cadena_cod += dic[caracter]
    return cadena_cod
cadena = "Nublado-Baja-1-5-7"
print('Mensaje a codificar:', cadena)
print()
cadena_cod = codificar(cadena, dic)
print('Cadena codificada')
print(cadena_cod)
print()
print('Cadena decodificada')
cadena_deco = decodificar(cadena_cod, bosque[0])
print(cadena_deco)
'''
#####
# Ejercicio 21
'''
print('Ejercicio 21')
print()

arbol = None

archivo = open('Greek_Gods.txt')

linea = archivo.readline()

while linea:        
    linea = linea.replace('\n', '')
    dios = linea.split(';')
    nodo = Nodo_Greek(dios[0], dios[2])
    #print('insertar', dios[0])
    if(arbol is None):
        arbol = nodo
    else:
        pos = []
        busqueda_nario(arbol, dios[1], pos)
        #print('resultado de busqueda', pos[0].info)
        insertar_nario(pos[0], nodo)

    linea = archivo.readline()

archivo.close()

print('ARBOL DIOSES')
por_nivel_nario(arbol)
print()

#pos = []
#busqueda_nario(arbol, 'zeus', pos)

#hijo = pos[0].izq

#while hijo is not None:
#    print(hijo.info)
#    hijo = hijo.der

bosque = []
hijo = arbol.izq

while hijo is not None:
    aux = hijo.der
    hijo.der = None
    bosque.append(hijo)
    hijo = aux

print('cantidad de arboles del bosque', len(bosque))
for arbol in bosque:
    print('raiz ----------->', arbol.info)
    inorden(arbol)
    print()
'''

'''
PARCIAL 

arbol = insertar_nodo_huffman(arbol,'Ceto',None)
arbol = insertar_nodo_huffman(arbol,'Tifon','Zeus')
arbol = insertar_nodo_huffman(arbol,'Ladon','Heracles')
arbol = insertar_nodo_huffman(arbol,'Talos','Medea')

inorden_dioses(arbol)
print()
pos = busqueda(arbol,'Talos')
print()
print(pos.info , pos.valor)
print()
lista = []
busqueda_valor(arbol,'Heracles',lista)
print(lista)
print()
sinDerrotas = []
busqueda_valor(arbol,None,sinDerrotas)
print(sinDerrotas)
print()
'''