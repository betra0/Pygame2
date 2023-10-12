import pygame
#variables
#pantalla
ancho =700
alto = 800
size = (ancho, alto)
tamaño = 17
cantidadenemigos = 10
velocidadfondo = 2
frame = 35

velocidadmisil = 15
velocidaddisparo = 20

#enemigos
vidaenemy = 6
velocidad_disparo_enemigos=7
tamaño_bala_enemy = 6
tamaño_nave_enemy = 15
recarga_enemy = 46

retardo_reacion_bala = -3
retardo_reacion_nave = -9

# 
score = 0
timegame= 0  

blanco =(255,255,255)
rojo = (255,0,0)
tiempo_recarga = 200

#==== Listas
cordenadasjugador = []
#grupos pygames



#=================Funciones =================

def agregar_coordenada(x, y):
    cordenadasjugador.append((x, y))
    revisar_cordenadas()

def revisar_cordenadas():
    while len(cordenadasjugador) > 20:
        cordenadasjugador.pop(0)
def reiniciar_cordenadas():
    cordenadasjugador.clear()




