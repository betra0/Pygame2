
import pygame

ancho= 600
alto = 400

y= 100

cory = 300


distanciay = y - cory
if distanciay <0:
     distanciay = distanciay*-1


velmaximo =10

porcentajedistanciay = distanciay*100/alto
velocidady = porcentajedistanciay*velmaximo/100

print(porcentajedistanciay)
print(velocidady)

    
"""
#VELOCIDAD MAUS

            velocidad1 = 2
            velocidad2 = 3
            velocidad3 = 3.5
            velocidad4 = 4
            velocidad5 = 6
            velocidad6 = 7
            velocidad7 = 9

            if y > cory:
                if distanciay >= 50:
                    if distanciay >= 80:
                         if distanciay >= 150:
                             if distanciay >= 300:
                                 self.rect.y += velocidad7
                             else:
                                self.rect.y += velocidad6
                         else:
                            self.rect.y += velocidad5
                         pass
                    else:
                         self.rect.y += velocidad4  
                elif distanciay < 50:
                     if distanciay < 25:
                        if distanciay < 12:
                            if distanciay <=1:
                                pass
                            else:
                             self.rect.y += velocidad1
                        else:
                            self.rect.y += velocidad2
                     else:
                        self.rect.y += velocidad3
            
            if y < cory:
                if distanciay >= 50:
                    if distanciay >= 80:
                         if distanciay >= 150:
                             if distanciay >= 300:
                                 self.rect.y -= velocidad7
                             else:
                                self.rect.y -= velocidad6
                         else:
                            self.rect.y -= velocidad5
                         pass
                    else:
                         self.rect.y -= velocidad4  
                elif distanciay < 50:
                     if distanciay < 25:
                        if distanciay < 12:
                            if distanciay <=1:
                                pass
                            else:
                             self.rect.y -= velocidad1
                        else:
                            self.rect.y -= velocidad2
                     else:
                        self.rect.y -= velocidad3

            if x > corx:
                if distanciax >= 50:
                    if distanciax >= 80:
                         if distanciax >= 150:
                             if distanciax >= 300:
                                 self.rect.x += velocidad7
                             else:
                                self.rect.x += velocidad6
                         else:
                            self.rect.x += velocidad5
                         pass
                    else:
                         self.rect.x += velocidad4  
                elif distanciax < 50:
                     if distanciax < 25:
                        if distanciax < 12:
                            if distanciax <=1:
                                pass
                            else:
                             self.rect.x += velocidad1
                        else:
                            self.rect.x += velocidad2
                     else:
                        self.rect.x += velocidad3
            
            if x < corx:
                if distanciax >= 50:
                    if distanciax >= 80:
                         if distanciax >= 150:
                             if distanciax >= 300:
                                 self.rect.x -= velocidad7
                             else:
                                self.rect.x -= velocidad6
                         else:
                            self.rect.x -= velocidad5
                         pass
                    else:
                         self.rect.x -= velocidad4  
                elif distanciax < 50:
                     if distanciax < 25:
                        if distanciax < 12:
                            if distanciax <=1:
                                pass
                            else:
                             self.rect.x -= velocidad1
                        else:
                            self.rect.x -= velocidad2
                     else:
                        self.rect.x -= velocidad3

"""