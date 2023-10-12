from typing import Any
import pygame
from var import*
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, 
            K_ESCAPE, KEYDOWN, QUIT, K_w, K_s, K_d, K_a,)
import random
import os
import math

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

            self.posx, self.posy = self.rect.center

        def update(self):
            xmaus, ymaus= pygame.mouse.get_pos()
            corx, cory = self.rect.center

            distanciax = xmaus - corx
            distanciay = ymaus - cory
            
            modulo = (distanciax**2 + distanciay**2)**0.5
            
            try:
                vectorx = distanciax / modulo
                vectory = distanciay / modulo
            except ZeroDivisionError:
                vectorx, vectory = 0, 0
           
            velmaximo =5
            altomax = 130
            
            porcentajedistancia = modulo*100/altomax
            velocidad = porcentajedistancia*velmaximo/100

            self.posx += vectorx*velocidad
            self.posy += vectory*velocidad

            self.rect.center = round(self.posx), round(self.posy)

            if self.posx < 10 + limiteinterior:
                self.posx = 10 + limiteinterior 
            
            elif self.posx > ancho-limiteinterior -10:
                self.posx = ancho-limiteinterior -10





        def centrar(self):
            
            x, y= (ancho//2, alto//1.5)

            corx, cory = self.rect.center

            distanciax = x - corx
            if distanciax <0:
                 distanciax = distanciax*-1
            
            distanciay = y - cory
            if distanciay <0:
                 distanciay = distanciay*-1
           
            velmaximo =4
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


            if y > cory:
                self.rect.y += velocidady
            if y < cory:
                self.rect.y -= velocidady

            if x > corx:
                self.rect.x += velocidadx
            if x < corx:
                self.rect.x -= velocidadx  

            if self.rect.centerx < 10 + limiteinterior:
                self.rect.centerx = 10 + limiteinterior 
            
            elif self.rect.centerx > ancho-limiteinterior -10:
                self.rect.centerx = ancho-limiteinterior -10   

            self.posx, self.posy = self.rect.center          

class crater(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.tamaño = tamaño +13 + random.randint(0,5)
            self.image = pygame.image.load(os.path.join(rutasprites, "asteroide.png"))
            self.image = pygame.transform.scale(self.image, (self.tamaño, self.tamaño))
            self.mask = pygame.mask.from_surface(self.image)
            self.rect = self.image.get_rect()
            self.vida = vidaenemy_crater
            self.activate = True

            x = random.randint(tamaño+limiteinterior, ancho-limiteinterior-tamaño//2)
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

            if self.rect.y > alto: #   cuando lo meteoros salen de la camara
                self.vida = vidaenemy_crater
                x = random.randint(tamaño+limiteinterior, ancho-limiteinterior-tamaño//2)
                y = random.randint(-30, 0-tamaño//2)
                self.rect.center = (x, y)
                if self.activate == False:
                    self.kill()
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
            self.original_image = pygame.image.load(os.path.join(rutasprites, "unnamed2.png"))
            self.original_image = pygame.transform.scale(self.original_image, (self.tamaño, self.tamaño))
            self.image = self.original_image.copy()
            self.rect = self.image.get_rect()
            self.rect.center = (ancho//2,-400) 
            self.vida = vidaenemy_nave
            self.activate = False 
            self.speed = velocidaddisparo
            self.contador = 0
            self.maxcontador = random.randint(recarga_enemy-5, recarga_enemy+5)
            self.contadordisparar = random.randint(0,self.maxcontador)
            # self.x y self.y son las ubicaciones RELATIVAS(NO exactas) del Jugador
            self.x = None
            self.y = None
            self.IA = True
            self.primera_pocision = False
            #=== INIT ROTATE
            self.angle = 0
        def update(self):

            if self.IA:
                self.contador += 1
                if self.x == None or self.y == None:
                    self.y = random.randint(10, 300)
                    self.x = random.randint(20+limiteinterior, ancho -20-limiteinterior)
                if len(cordenadasjugador) >= retardo_reacion_nave*-1:

                    xf, yf = cordenadasjugador[retardo_reacion_nave]
                    predistanciax = xf - self.x
                    predistanciay = yf - self.y
                    if predistanciax <0:
                        predistanciax = predistanciax*-1
                    if predistanciay <0:
                        predistanciay = predistanciay*-1

                    if predistanciax < 90 :
                        self.contador = 300
                      
                    #==========Movimiento enemigo====================
                    if self.contador >= 300: 
                        self.contador = 0
                        x, y = cordenadasjugador[retardo_reacion_nave]
                        self.y = random.randint(10, 300)
                        bitramdom = random.randint(1,2)
                        try:
                            if bitramdom == 1:
                                self.x = random.randint(x+40, ancho-20-limiteinterior)
                        except ValueError:
                            self.x = random.randint(20+ limiteinterior, x-40)
                        try:
                            if bitramdom == 2:
                                self.x = random.randint(20+limiteinterior, x-40)
                        except ValueError:
                            self.x = random.randint(x+40, ancho-20-limiteinterior)
                
                #para no generar error en Los primeros Frames
                if self.x == None or self.y == None:
                    self.y = random.randint(10, 300)
                    self.x = random.randint(20+limiteinterior, ancho -20-limiteinterior)

                x, y = self.x, self.y

            else: #Cuando LA IA esta desactivada
                x, y = (ancho//2), 300
            #=========Sistema de movimiento a um punto dado========
            corx, cory = self.rect.center
            distanciax = x - corx
            if distanciax <0:
                 distanciax = distanciax*-1
            distanciay = y - cory
            if distanciay <0:
                 distanciay = distanciay*-1
            velmaximo =4
            altomax = 300
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
            #etapa final movimientos
            if y > cory:
                self.rect.y += velocidady
            if y < cory:
                self.rect.y -= velocidady
            if x > corx:
                self.rect.x += velocidadx
            if x < corx:
                self.rect.x -= velocidadx 
            #::::::::::::::::FIN SISTEMA MOVIMOIENTOS::::::::::::::::::::::
            if len(cordenadasjugador) >= -retardo_reacion_nave:
                    xf, yf = cordenadasjugador[retardo_reacion_nave]
                    x, y = self.rect.center
                    dx = x -xf
                    dy = yf -y
                    self.angle = math.degrees(math.atan2(dy, dx))

            
        
            self.image = pygame.transform.rotate(self.original_image, self.angle + 90)

            # Actualiza el rectángulo de la imagen
            self.rect = self.image.get_rect(center=self.rect.center)

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

        def disminuirvida(self):
            self.vida -= 1
            if self.vida <= 0:
                retorno = True
            else: retorno = False
            return retorno

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
             
            


