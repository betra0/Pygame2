import pygame
#variables
#pantalla
ancho =1020
anchoingame= 700
alto = 800
limiteinterior =(ancho-anchoingame)//2
size = (ancho, alto)

tamaño = 17
cantidadenemigos_meteoros = 0
velocidadfondo = 2
frame = 35

velocidadmisil = 15
velocidaddisparo = 20

#======activar/desactivar funciones======
colisionesmeteoros_bol = True
colisionesnaves_bol = True
#;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
#enemigos
vidaenemy_crater = 5
vidaenemy_nave = 1
velocidad_disparo_enemigos=8
tamaño_bala_enemy = 6
tamaño_nave_enemy = 35
recarga_enemy = 39

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

#(duracion,fpsinicial, cant_meteoros,cantidadnave1,agregarnave1,cantidadnave2,agregarnave2)
niveles={1:(1000, 42,   0,      4 , 0,   0, 0,                   False, 1),
         2:(1000, 40,    0,        7, 0,   0, 0,                   False, 0),
         3:(1000, 40,    0,        15, 0,   0, 0,                   False, 2),
         4:(10, 400,    0,        15, 0,   0, 0,                   False, 0),
         5:(80, 40,    0,        15, 0,   0, 0,                   False, 3),
         6:(100, 38,    0,        15, 0,   0, 0,                   False, 0),
         7:(10, 35,    0,        15, 0,   0, 0,                   False, 0 ),}
        

#=================Funciones =================

def agregar_coordenada(x, y):
    cordenadasjugador.append((x, y))
    revisar_cordenadas()

def revisar_cordenadas():
    while len(cordenadasjugador) > 20:
        cordenadasjugador.pop(0)
def reiniciar_cordenadas():
    cordenadasjugador.clear()




