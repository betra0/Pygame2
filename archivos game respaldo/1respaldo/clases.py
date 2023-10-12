from typing import Any
import pygame
from var import*
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, 
            K_ESCAPE, KEYDOWN, QUIT, K_w, K_s, K_d, K_a,)
import random
import os

#=======rutas=======#
rutasprites = os.path.join("sprites")

class jugador(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.tamaño = tamaño +33
            self.image = pygame.image.load(os.path.join(rutasprites, "rocket.png"))
            self.image = pygame.transform.scale(self.image, (self.tamaño, self.tamaño))
            self.rect = self.image.get_rect()
            self.rect.center = (ancho//2, alto//1.5)
        def update(self):
            x, y= pygame.mouse.get_pos()

            corx, cory = self.rect.center

            distanciax = x - corx
            if distanciax <0:
                 distanciax = distanciax*-1
            
            distanciay = y - cory
            if distanciay <0:
                 distanciay = distanciay*-1
           
            velmaximo =10
            altomax = 400
            

            porcentajedistanciay = distanciay*100/altomax
            velocidady = porcentajedistanciay*velmaximo/100
            velocidady += 1
            if 1 > velocidady > 0:
                velocidady = 1

            porcentajedistanciax = distanciax*100/altomax
            velocidadx = porcentajedistanciax*velmaximo/100
            velocidadx += 1
            if 1 > velocidadx > 0:
                velocidadx = 1

            #print(porcentajedistanciax, porcentajedistanciay)
            #print("velocidad",velocidadx, velocidady)

            if y > cory:
                self.rect.y += velocidady
            if y < cory:
                self.rect.y -= velocidady

            if x > corx:
                self.rect.x += velocidadx
            if x < corx:
                self.rect.x -= velocidadx                
              
class crater(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.tamaño = tamaño +13 + random.randint(0,5)
            self.image = pygame.image.load(os.path.join(rutasprites, "asteroide.png"))
            self.image = pygame.transform.scale(self.image, (self.tamaño, self.tamaño))
            self.mask = pygame.mask.from_surface(self.image)
            self.rect = self.image.get_rect()
            self.vida = vidaenemy

            x = random.randint(tamaño, ancho-tamaño//2)
            y = random.randint(-30, 0-tamaño//2)
            self.rect.center = (x, y)
            
            self.speed = random.randint(tamaño//2, tamaño-7)
            self.speedx = 0
            if random.randint(0, 8) == 3:
                 self.speedx = random.randint(1, 1)
                 xs, ys = self.rect.center
                 if xs >= ancho//2:
                      self.speedx *= -1

        def update(self):
            self.rect.x += self.speedx
            self.rect.y += self.speed
            if self.rect.y > alto:
                self.vida = vidaenemy
                x = random.randint(tamaño, ancho-tamaño//2)
                y = random.randint(-30, 0-tamaño//2)
                self.rect.center = (x, y)
                self.speed = random.randint(tamaño//2, tamaño-5)
                if random.randint(0, 6) == 3:
                    self.speedx = random.randint(1, 1)
                    xs, ys = self.rect.center
                    if xs >= ancho//2:
                         self.speedx *= -1
                else: 
                     self.speedx = 0
        def disminuirvida(self):
            self.vida -= 1
            if self.vida <= 0:
                retorno = True
            else: retorno = False
            return retorno

class misil(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.tamaño = 10
            self.image = pygame.image.load(os.path.join(rutasprites, "misil.png"))
            self.image = pygame.transform.scale(self.image, (self.tamaño, self.tamaño*3))
            self.rect = self.image.get_rect()
            self.rect.center= (-200,1000)
            self.speed = velocidadmisil
            self.activate = False
            self.cooldown =29

        def update(self):
            if self.activate == True:
                self.rect.y -= self.speed

            if self.rect.y < -10:
                self.activate = False
                self.rect.center= (-200,1000)
                print("misil desactivado")
            if self.activate == False and self.cooldown>0:
                self.cooldown -= 1

        def activarmisil(self, x, y):
            if self.cooldown == 0:
                self.activate = True
                self.rect.center = (x, y)
                self.cooldown = tiempo_recarga
                activado = "activado"
            else: 
                 activado = "none"
            return activado
        def desarmarmisil(self):
            self.activate = False
            self.rect.center= (-200,1000)
            print("misil desactivado")

class disparo(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.tamaño = 3
            self.image = pygame.Surface((self.tamaño, self.tamaño*3))
            self.image.fill((255,100,0))
            self.rect = self.image.get_rect()
            self.rect.center = (-ancho,alto+100)  
            self.activate = False 
            self.speed = velocidaddisparo

        def update(self):
            if self.activate == True:
                self.rect.y -= velocidaddisparo
            if self.rect.y < -self.tamaño*3:
                self.activate = False
                self.rect.center= (-ancho,alto+100)



        def activardisparo(self, x, y):
            if self.activate == False:
                self.activate = True
                self.rect.center = (x, y)
                retorno = True
            else:
                retorno = False
            return retorno
        def desarmardisparo(self):
            self.activate = False
            self.rect.center= (-ancho,alto+100)

class nave_enemy(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.tamaño = tamaño_nave_enemy 
            self.image = pygame.Surface((self.tamaño, self.tamaño))
            self.image.fill((0,255,0))
            self.rect = self.image.get_rect()
            self.rect.center = (200,200)  
            self.activate = False 
            self.speed = velocidaddisparo
            self.contador = 0

            self.maxcontador = random.randint(recarga_enemy-5, recarga_enemy+5)
            self.contadordisparar = random.randint(0,self.maxcontador)

            self.x = None
            self.y = None
            self.IA = True
        def update(self):
            if self.IA:
                self.contador += 1
                if len(cordenadasjugador) >= retardo_reacion_nave*-1:

                    xf, yf = cordenadasjugador[retardo_reacion_nave]
                    #cortx, corty = self.rect.center
                    predistanciax = xf - self.x
                    predistanciay = yf - self.y
                    if predistanciax <0:
                        predistanciax = predistanciax*-1
                    if predistanciay <0:
                        predistanciay = predistanciay*-1

                    #print(predistanciax)
                    if predistanciax < 39:
                        self.contador = 300
                        print("========================================")
                    #===Movimiento enemigo
                    if self.contador >= 300: 
                        self.contador = 0
                        x, y = cordenadasjugador[retardo_reacion_nave]
                        self.y = random.randint(10, 300)
                        bitramdom = random.randint(1,2)
                        try:
                            if bitramdom == 1:
                                self.x = random.randint(x+40, ancho-20)
                        except ValueError:
                            self.x = random.randint(20, x-40)
                        try:
                            if bitramdom == 2:
                                self.x = random.randint(20, x-40)
                        except ValueError:
                            self.x = random.randint(x+40, ancho-20)
                #print(self.contador)

                if self.x == None or self.y == None:
                    self.y = random.randint(10, 300)
                    self.x = random.randint(20, ancho -20)

                x, y = self.x, self.y
            else:
                x, y = (ancho//2), 200

            corx, cory = self.rect.center

            distanciax = x - corx
            if distanciax <0:
                 distanciax = distanciax*-1
            
            distanciay = y - cory
            if distanciay <0:
                 distanciay = distanciay*-1
           
            velmaximo =4
            altomax = 300
            anchomax = 400

            porcentajedistanciay = distanciay*100/altomax
            velocidady = porcentajedistanciay*velmaximo/100
            velocidady += 1
            if 1 > velocidady > 0:
                velocidady = 1

            porcentajedistanciax = distanciax*100/altomax
            velocidadx = porcentajedistanciax*velmaximo/100
            velocidadx += 1
            if 1 > velocidadx > 0:
                velocidadx = 1

            #print(porcentajedistanciax, porcentajedistanciay)
            #print("velocidad",velocidadx, velocidady)

            if y > cory:
                self.rect.y += velocidady
            if y < cory:
                self.rect.y -= velocidady

            if x > corx:
                self.rect.x += velocidadx
            if x < corx:
                self.rect.x -= velocidadx 

            if self.rect.y < 0:
                self.rect.y = 0
            
            if self.rect.x < 0:
                self.rect.x = 0
            
            pass
        def disparar(self):
            self.contadordisparar +=1
            if self.contadordisparar >= self.maxcontador:
                self.contadordisparar = 0
                x, y = self.rect.center
                disparar = True
            else:
                disparar = False
                x, y = False, False
            
            return disparar, x, y

class disparo_enemy(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.tamaño = tamaño_bala_enemy
            self.image = pygame.Surface((self.tamaño, self.tamaño))
            self.image.fill((210,159,0))
            self.rect = self.image.get_rect()
            self.rect.center = (-ancho,alto+100)  
            self.activate = False 
            self.speed = velocidad_disparo_enemigos
            self.direciony = 0
            self.direcionx = 0
            self.posx, self.posy = self.rect.center

        def update(self):
            if self.activate == True:
                self.posy += self.direciony*self.speed
                self.posx += self.direcionx*self.speed
            
                if self.posy > alto+self.tamaño and self.activate== True:
                    self.desarmardisparo()
                
                if self.posy < 0 and self.activate== True:
                    self.desarmardisparo()
                    
                if self.posx < 0 and self.activate== True:
                    print("desarmed")
                    self.desarmardisparo()
                if self.posx > ancho+self.tamaño and self.activate== True:
                    print("desarme3d")
                    self.desarmardisparo()
            
            self.rect.center = (round(self.posx)), (round(self.posy))

            
        def direcionbala(self, x, y):
  
            xf, yf = cordenadasjugador[retardo_reacion_bala]

            dx = xf - x
            dy = yf - y
            moduloD =(dx**2+dy**2)**0.5

            if moduloD > 0:
                self.direcionx = (dx/moduloD)
                self.direciony = (dy/moduloD)
            else:
                self.direcionx = 0
                self.direciony = 0




        def activardisparo(self, x, y):
            if self.activate == False and len(cordenadasjugador) >= retardo_reacion_bala*-1:
                self.activate = True
                self.posx, self.posy = (x, y)
                self.rect.center = (round(self.posx)), (round(self.posy))
                self.direcionbala(x, y)
                retorno = True
            else:
                retorno = False
            return retorno
        def desarmardisparo(self):
            self.activate = False
            self.posx, self.posy =(-ancho,alto+100) 
            self.rect.center = (round(self.posx)), (round(self.posy))               
             
            


