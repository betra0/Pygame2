import pygame
#variables
#pantalla
ancho =1020
anchoingame= 700
alto = 800
limiteinterior =(ancho-anchoingame)//2
size = (ancho, alto)

tamaño = 17
#====meteoros====#
tamaño_meteoro = 30

rangomax_velmeteoro = 8
rangomin_velmeteoro = 5
#::::::::::::
cantidad_meteoros = 0
velocidadfondo = 1.2
frame = 60
#velocidad y rango jjuagdor
maxvel_jugador = 3
rangovel_jugador = 115
#::::::::

velocidadmisil = 15
velocidaddisparo = 14

#======activar/desactivar funciones======
colisionesmeteoros_bol = True
colisionesnaves_bol = True
#;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
#enemigos

#velocidad y rango naveenemy
maxvel_nave = 3.8
rangovel_nave = 200
#::
vidaenemy_crater = 4
vidaenemy_nave = 1
velocidad_disparo_enemigos=6
tamaño_bala_enemy = 6
tamaño_nave_enemy = 35
recarga_enemy = 50
 
retardo_reacion_bala = -10
retardo_reacion_nave = -9
#IA ENEMI
tiempo_mov_naveenemy = 300



# 
score = 0
timexscore = 0 
timexetapa = 0 

blanco = (255,255,255)
rojo = (255,0,0)
tiempo_recarga = 200


#==== Listas
cordenadasjugador = []
#grupos pygames


#los niveles se ejecutan atraves de este dicionario (clave: valor), 
#para cada nivel hay unas intruciones especificas
#de lo que se quiere hacer 
#(duracion,fpsinicial, cant_meteoros,cantidadnave1,none, trascision, estapa actual, cantidad escudo)
niveles={1:(25, 60,     15,         0 , 0,                      False, 1, 0),
         2:(10, 400,    0,        0, 0,                      True, 0, 0), # Trancision
         3:(700, 60,    0,        5, 0,                      False, 2, 0),
         4:(700, 60,    0,        10, 0,                      False, 2, 1),
         5:(35, 65,    0,        0, 0,                      True, 0, 0),   #Trancision
         6:(35, 65,    19,        0, 0,                    False, 3, 0),   
         7:(80, 65,    0,        13, 0,                    False, 3, 0),
         8:(5, 65,    0,        0, 0,                      False, 3, 1),
         9:(10, 65,    0,        0, 0,                    True, 0, 0),   #Trancision
         10:(100, 68,    0,        15, 0,                    False, 4, 0),
         11:(10, 72,    0,        0, 0,                    True, 0, 0), #Trancision
         12:(100, 73,    20,        0, 0,                    False, 5, 0)}
        

#=================Funciones =================

def agregar_coordenada(x, y):
    cordenadasjugador.append((x, y))
    revisar_cordenadas()

def revisar_cordenadas():
    while len(cordenadasjugador) > 20:
        cordenadasjugador.pop(0)
def reiniciar_cordenadas():
    cordenadasjugador.clear()




