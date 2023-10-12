import pygame 
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, 
            K_ESCAPE, KEYDOWN, QUIT, K_w, K_s, K_d, K_a, K_SPACE)

from clases import(jugador, crater, misil, disparo, nave_enemy, disparo_enemy)

import random
import time as timer
import os
import win32gui


def gameon():
    exit = False
    pygame.init()
    pygame.mixer.init()
    from var import(ancho, alto, size, tamaño, cantidad_meteoros, velocidadfondo, score, 
    timexscore, blanco, rojo, frame, tiempo_recarga, limiteinterior, colisionesmeteoros_bol,
    timexetapa, colisionesnaves_bol,
    niveles,
    agregar_coordenada, revisar_cordenadas, reiniciar_cordenadas)

    ventana = pygame.display.set_mode(size)
    pygame.display.set_caption("Detectar Minimizar")
    time = pygame.time.Clock()
    #======textos
    pausafont = pygame.font.Font(None, 80)
    scorefont = pygame.font.Font(None, 30)

    #=======rutas=======#
    rutasprites = os.path.join("sprites")
    rutamultimedia = os.path.join("multimedia")

    #===============cargar explosion============
    explosion_images = [pygame.image.load(os.path.join(rutasprites, f"explosion{i+1}.png")) for i in range(11)]
    for i in range(len(explosion_images)):
        explosion_images[i] = pygame.transform.scale(explosion_images[i], (100, 100))  # Cambia el tamaño aquí
    explosion_frame = 0  # Índice del fotograma actual de la explosión
    #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    #====Fondos====#
    fondo = pygame.image.load(os.path.join(rutasprites, "fondo.png")).convert()


    def antesdesalir(comenzar, run, exit):
        #============Render TXT
        salirtxt = scorefont.render(f" Presione Esc para salir ", True, blanco)
        txt5ancho, txt5alto = salirtxt.get_size()
        pausatxt = pausafont.render("Pausa", True, blanco)
        txt1ancho, txt1alto = pausatxt.get_size()
        #============Pausa Gui============
        while True:
            for eventos in pygame.event.get():
                if eventos.type == QUIT:
                        run = False
                        exit = True
                        break
                elif eventos.type == KEYDOWN:
                        if eventos.key == K_ESCAPE:
                            run = False
                            exit = True
                            break

                elif eventos.type == pygame.MOUSEBUTTONDOWN:
                    if eventos.button == 1:  # Botón izquierdo del mouse
                        comenzar = True
                        break
            if comenzar == True:
                break     
            if run == False:
                break         
            ventana.blit(fondo, (0, posyfondo1))
            ventana.blit(fondo, (0, posyfondo2))
            all.draw(ventana)
            ventana.blit(pausatxt, ((ancho - txt1ancho) // 2, (alto - txt1alto) // 2 ))
            ventana.blit(salirtxt, ((ancho - txt5ancho) // 2, (alto - txt5alto) // 1.8 ))
            pygame.display.flip()
            time.tick(35)
        return comenzar, run, exit       
    def spawnmeteoros(contadorenemi, encender):
        
        if contadorenemi >= 15:
           if cantidad_meteoros > len(asteroides):
                enemigo = crater()
                asteroides.add(enemigo)
                all.add(enemigo)
                all_enemys.add(enemigo)
                contadorenemi = 0

        return contadorenemi
    def pausagame(comenzar, run, exit):
        #============Render TXT============================
        pausatxt = pausafont.render("Pausa", True, blanco)
        txt1ancho, txt1alto = pausatxt.get_size()
        subpausatxt = scorefont.render(f" Presione clic izquierdo para continuar ", True, blanco)
        txt3ancho, txt3alto = subpausatxt.get_size()
        subpausa2txt = scorefont.render(f" Esc para salir ", True, blanco)
        txt4ancho, txt4alto = subpausa2txt.get_size()
        #=================================================================
        
        if comenzar==False:
            pygame.mixer.music.pause()
            while True:
                for eventos in pygame.event.get():
                    if eventos.type == QUIT:
                            run = False
                            exit = True
                            break
                    elif eventos.type == KEYDOWN:
                        if eventos.key == K_ESCAPE:
                            comenzar, run, exit = antesdesalir(comenzar, run, exit)
                        if eventos.key == K_SPACE:
                            comenzar = True
                            break

                    elif eventos.type == pygame.MOUSEBUTTONDOWN:
                        if eventos.button == 1:  # Botón izquierdo del mouse
                             comenzar = True
                             break
                if comenzar == True:
                    pygame.mixer.music.unpause()
                    break     
                if run == False:
                    break         
                
                ventana.blit(fondo, (0, posyfondo1))
                ventana.blit(fondo, (0, posyfondo2))
                pygame.draw.line(ventana, blanco, (limiteinterior, alto), (limiteinterior, 0), 2)
                pygame.draw.line(ventana, blanco, (ancho-limiteinterior, alto), (ancho-limiteinterior, 0), 2)
                all.draw(ventana)
                ventana.blit(pausatxt, ((ancho - txt1ancho) // 2, (alto - txt1alto) // 2 ))
                ventana.blit(subpausatxt, ((ancho - txt3ancho) // 2, (alto - txt3alto) // 1.8 ))
                ventana.blit(subpausa2txt, ((ancho - txt4ancho) // 2, (alto - txt4alto) // 1.68 ))
                pygame.display.flip()
                time.tick(35)
        return comenzar, run, exit
    def gameover(posyfondo1, posyfondo2, score = 0, exit = False):
        #============Render TXT=====
        gameovertxt = pausafont.render("Game Over", True, rojo)
        txt1ancho, txt1alto = gameovertxt.get_size()

        scoretxt = scorefont.render(f"score: {score}", True, blanco)
        txt2ancho, txt2alto = scoretxt.get_size()

        #===================================================
        finexplosion = False
        explosion_frame = 0
        contadorfin = 40
        frameover = 35
        efex_explocion1.play()
        exit2 = False
        
        while True:
            for eventos in pygame.event.get():
                if eventos.type == QUIT:
                        exit2 = True
                        break
            if exit2:
                exit = True
                break
            posyfondo1 += velocidadfondo
            posyfondo2 += velocidadfondo
             # Reinicia las posiciones de los fondos cuando salen de la ventana
            if posyfondo1 > alto:
                posyfondo1 = posyfondo2 - alto -224

            if posyfondo2 > alto:
                posyfondo2 = posyfondo1 - alto -224
            asteroides.update()
            #=============dibujado de pantalla =============
            ventana.blit(fondo, (0, posyfondo1))
            ventana.blit(fondo, (0, posyfondo2))
            pygame.draw.line(ventana, blanco, (limiteinterior, alto), (limiteinterior, 0), 2)
            pygame.draw.line(ventana, blanco, (ancho-limiteinterior, alto), (ancho-limiteinterior, 0), 2)
            xss, yss = jugador1.rect.center
            asteroides.draw(ventana)
            
            finexplosion, explosion_frame =explosion(xss, yss, finexplosion, explosion_frame)
            if finexplosion == True:
                pygame.mixer.music.pause()
                contadorfin -= 1
                frameover -= 0.5

                ventana.blit(gameovertxt, ((ancho - txt1ancho) // 2, (alto - txt1alto) // 2 ))
                ventana.blit(scoretxt, ((ancho - txt2ancho) // 2, (alto +100) // 2 ))

            #============================================================
            pygame.display.flip()
            time.tick(frameover)
            
            if contadorfin ==0:
                timer.sleep(0.5)
                break
        return exit
    def trancision(frame, proxfps, posyfondo1, posyfondo2, duracionevento, score):
        
        # Declaracion de variables===
        
        inicio = False
        run = True
        exit = False
        acendente = True
        decreciente = False
        maximo = False
        fintrancision = False
        fps = 0
        frame = round(frame)
        n, newproxfps, n, n, n, n, n, n, proxnivel_real =niveles[nivel+1]
        velocidadfondo_mov = velocidadfondo

        #:::::::::
        while True:
            
            #============Render TXT============================
            scoretxt = scorefont.render(f"score: {score}", True, blanco)
            txt2ancho, txt2alto = scoretxt.get_size()
    
            fpstxt = scorefont.render(f"FPS: {fps}", True, blanco)
            txt3ancho, txt3alto = fpstxt.get_size()

            proxeetapatxt = pausafont.render(f"Etapa: {proxnivel_real}", True, blanco)
            txt4ancho, txt4alto = proxeetapatxt.get_size()

            
        #::::::::::::::::::::::::::::::::::::::::::::::::
            if acendente:
                if proxfps:
                    
                    diferencia = proxfps - frame
                    print("hola", proxfps, frame, "diferencia", diferencia)
                    
                    if diferencia >1:
                            frame +=1
                      
                          
                    elif diferencia <= 1:
                        frame += 0.50
                        print("hols")
                
                print("mov no", velocidadfondo_mov)

                if velocidadfondo_mov <4:
                    velocidadfondo_mov += 0.01
                    print("mov alc", velocidadfondo_mov)

            elif maximo:
                duracionevento -= 0.01
                if -1 < duracionevento < 1:
                    decreciente = True
                    maximo = False
                    print("fin maximo")
                print(duracionevento)
            elif decreciente: 
                    if velocidadfondo_mov > 2:
                        velocidadfondo_mov -= 0.005
                    print("mov no", velocidadfondo_mov)

                    diferencia = frame - newproxfps 
                    print("ultimo proceso", newproxfps, frame, "diferencia", diferencia)
                    
                    if diferencia >3:
                        if diferencia >4:
                            if diferencia > 6:
                                if diferencia >9:
                                    if diferencia >20:
                                        if diferencia >50:
                                            frame -= 1
                                        else:
                                            frame -= 0.50
                                    else:
                                        frame -= 0.25
                                else:
                                    frame -= 0.25
                            else:
                                frame -= 0.25
                        else:
                            frame -= 0.125
                    elif diferencia <= 3:
                        frame = newproxfps
                        decreciente= False
                        fintrancision = True          
            if frame == proxfps and acendente:
                acendente = False
                maximo = True
                print("inicio maximo")

            if fintrancision:
                break
             
            for eventos in pygame.event.get():
                if eventos.type == QUIT:
                        run = False
                        exit = True
                        break
                elif eventos.type == KEYDOWN:
                    if eventos.key == K_ESCAPE:
                        nada, run, exit = pausagame(False, run, exit)
                        break
            if run == False:
                break
            posyfondo1 += velocidadfondo_mov
            posyfondo2 += velocidadfondo_mov
            # Reinicia las posiciones de los fondos cuando salen de la ventana
            if posyfondo1 > alto:
                posyfondo1 = posyfondo2 - alto -224
            if posyfondo2 > alto:
                posyfondo2 = posyfondo1 - alto -224
            jugador1.centrar()
            asteroides.update()
            misil1.update()
            municion.update()
            naves_enemys.update()
            municion_enemy.update()
            #==========================zona de dibujo=================
            ventana.blit(fondo, (0, posyfondo1))
            ventana.blit(fondo, (0, posyfondo2))
            pygame.draw.line(ventana, blanco, (limiteinterior, alto), (limiteinterior, 0), 2)
            pygame.draw.line(ventana, blanco, (ancho-limiteinterior, alto), (ancho-limiteinterior, 0), 2)
            ventana.blit(scoretxt, ((ancho - txt2ancho-50) , (alto - txt2alto)))
            ventana.blit(fpstxt, ((40) , (alto - txt3alto)))
            ventana.blit(proxeetapatxt, ((ancho - txt4ancho) // 2, (alto - txt4alto) // 2 ))
            all.draw(ventana)
            
            pygame.display.flip()
            #==========================calcular FPS
            if inicio:
                try:       
                    fin = timer.time()
                    retardo = fin - inicio  
                    fps = 1 // retardo
                except ZeroDivisionError:
                    pass
            inicio = timer.time()

            time.tick(frame)
        


        return posyfondo1, posyfondo2, run, exit
                            
    def antes_de_empezar(comenzar, run, exit):
        #============Render TXT============================
        pausatxt = pausafont.render("Play", True, blanco)
        txt1ancho, txt1alto = pausatxt.get_size()
        subpausatxt = scorefont.render(f" Presione clic izquierdo para comenzar ", True, blanco)
        txt3ancho, txt3alto = subpausatxt.get_size()
        subpausa2txt = scorefont.render(f" Esc para salir ", True, blanco)
        txt4ancho, txt4alto = subpausa2txt.get_size()
        #=================================================================
        if comenzar==False:
            while True:
                for eventos in pygame.event.get():
                    if eventos.type == QUIT:
                            run = False
                            exit = True
                            break
                    elif eventos.type == KEYDOWN:
                        if eventos.key == K_ESCAPE:
                            comenzar, run, exit = antesdesalir(comenzar, run, exit)
                        if eventos.key == K_SPACE:
                            comenzar = True
                            break

                    elif eventos.type == pygame.MOUSEBUTTONDOWN:
                        if eventos.button == 1:  # Botón izquierdo del mouse
                             comenzar = True
                             break
                if comenzar == True:
                    pygame.mixer.music.play(-1)
                    break     
                if run == False:
                    break         
                 
                ventana.blit(fondo, (0, posyfondo1))
                ventana.blit(fondo, (0, posyfondo2))
                pygame.draw.line(ventana, blanco, (limiteinterior, alto), (limiteinterior, 0), 2)
                pygame.draw.line(ventana, blanco, (ancho-limiteinterior, alto), (ancho-limiteinterior, 0), 2)
                all.draw(ventana)
                #ventana.blit(pausatxt, ((ancho - txt1ancho) // 2, (alto - txt1alto) // 2 ))
                ventana.blit(subpausatxt, ((ancho - txt3ancho) // 2, (alto - txt3alto) // 1.8 ))
                ventana.blit(subpausa2txt, ((ancho - txt4ancho) // 2, (alto - txt4alto) // 1.68 ))
                pygame.display.flip()
                time.tick(35)
        
        return comenzar, run, exit
    def eventospygame(run, exit, pausa, actmisil=False, actdisparo=False, con_bloq_windows = 0):
        #=================EVENTOSPYGAME==========================
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                    run = False
                    exit = True
            elif eventos.type == pygame.ACTIVEEVENT:
            # Verificar si la ventana perdió el enfoque
                if eventos.gain == 0:
                    con_bloq_windows +=1
                elif eventos.gain == 1:
                    con_bloq_windows = 0
                    
            elif eventos.type == KEYDOWN:
                if eventos.key == K_ESCAPE:
                    pausa = False
                if eventos.key == K_SPACE:
                    actmisil = True
            elif eventos.type == pygame.MOUSEBUTTONDOWN:
                if eventos.button == 1:  # Botón izquierdo del mouse
                     actdisparo = True
                elif eventos.button == 3:  # Botón izquierdo del mouse
                     actmisil = True

        if con_bloq_windows >= 2:
            pausa = False
        return run, exit, pausa, actmisil, actdisparo, con_bloq_windows
        #=======================FIN==========================#
    def dificil(frame, cantidadenemigos, score):
        frame += 0.05
        if cantidadenemigos >0:
            for m in range(0,20):
                compare= m*35
                if score == compare:
                    cantidadenemigos += 1

        
        return frame, cantidadenemigos
    def explosion(x,y, finexplosion, explosion_frame):
        if finexplosion == False:
                ventana.blit(explosion_images[explosion_frame], (x-50, y-50))
                explosion_frame = (explosion_frame + 1) % len(explosion_images)
                if explosion_frame == 10:
                    finexplosion= True
        return finexplosion, explosion_frame
    def agregarmunicion():
        bala2 = disparo_enemy()
        all.add(bala2)
        municion_enemy.add(bala2)
        print("agregado municion")
    def spawnnave1(maxnave, contadornave1):
        if maxnave > contadornave1:
            for i in range(1):
                nave1 = nave_enemy()
                all.add(nave1)
                naves_enemys.add(nave1)
                all_enemys.add(nave1)
                contadornave1 += 1
        return contadornave1
                  



    # Posiciones iniciales de los fondos
    posyfondo1 = 0
    posyfondo2 = -alto-224
    # ===Musica =========
    musica1mp3 = os.path.join(rutamultimedia, "musicamain.mp3")
    efectoexplocion1mp3 = os.path.join(rutamultimedia, "explosion1.mp3")
    efectoexplocion2mp3 = os.path.join(rutamultimedia, "explosion2.mp3")
    pygame.mixer.music.load(musica1mp3)
    pygame.mixer.music.set_volume(0.1)
    
    efex_explocion1 = pygame.mixer.Sound(efectoexplocion2mp3)
    efex_explocion2 = pygame.mixer.Sound(efectoexplocion1mp3)
    efex_explocion1.set_volume(0.05)
    efex_explocion2.set_volume(0.1)
    
    #=====================
    #Grupos Pygame==
    all = pygame.sprite.Group()
    asteroides = pygame.sprite.Group()
    municion = pygame.sprite.Group()
    municion_enemy = pygame.sprite.Group()
    naves_enemys = pygame.sprite.Group()
    all_enemys = pygame.sprite.Group()
    
    #===Iniciasion de Objetos PYGAME==
    jugador1 = jugador()
    misil1 = misil()
    
    
    for i in range(6):
        bala1 = disparo()
        all.add(bala1)
        municion.add(bala1)

    for i in range(3):
        bala2 = disparo_enemy()
        all.add(bala2)
        municion_enemy.add(bala2)

    all.add(jugador1)
    all.add(misil1)
    

    #=====================
    reiniciar_cordenadas()
    contadorenemi = 0
    comenzar = False
    
    run = True
    pausa = True
    fps = 0
    inicio = False
    finexplosion = True
    actmisil = False
    actdisparo = False
    bumx, bumy =0, 0
    cooldown_misil = 0
    # declaracion variables niveles
    nivel = 0
    max_tiempoxetapa = 3
    cantidad_meteoros = 0
    isnave1 = 0
    contadornave1 = 0
    procesocambionivel = False
    modonaves = False
    proxfps = None
    istrancision = False
    con_bloq_windows = 0
    #=========================================<<<<<<<<<GAME Bucle|>>>>>>>>>=====================================#
    while run:

        #===pausa===
        comenzar, run, exit = antes_de_empezar(comenzar, run, exit)
        if pausa == False:
            pausa, run, exit = pausagame(pausa, run, exit)
            con_bloq_windows = 0

        #==========================Sistema de niveles================================
        if istrancision == True:
            posyfondo1, posyfondo2, run, exit =trancision(frame, proxfps, posyfondo1,
                            posyfondo2, max_tiempoxetapa, score)
            nivel += 1
            procesocambionivel = True
            timexetapa = 0
            contadornave1 = 0
            modonaves = False
            #asegurase que la explosion no aparesca en la transicion
            finexplosion = True
            explosion_frame = 0
            print("nivel:", nivel)
            
        if proxfps:
            if proxfps > frame:
                frame += 1
            elif proxfps < frame:
                frame -= 0.25
        if modonaves and len(naves_enemys) < 1 and contadornave1 > 0:
            print("no hay mas naves")
            modonaves = False
            nivel += 1
            procesocambionivel = True
            timexetapa = 0
            print("nivel:", nivel)
            contadornave1 = 0
          
        if timexetapa == max_tiempoxetapa:
            nivel += 1
            procesocambionivel = True
            timexetapa = 0
            contadornave1 = 0
            modonaves = False
            print("nivel:", nivel)
            #print("=====================")
            pass

        if nivel > 0 and procesocambionivel == True:
            procesocambionivel= False
            try:
                #(duracion, fps inicial, meteoros, cant_meteoros, cantidadnave1, agregarnave1, cantidad nave2,  agregarnave2)
                max_tiempoxetapa, proxfps, cantidad_meteoros, isnave1, nada, nada, nada, istrancision, nada =niveles[nivel]
                if isnave1 > 0:
                    modonaves = True
            except KeyError:
                print("Error: No hay mas niveles ")
                pass 
    #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: 

        #=================EVENTOSPYGAME==========================
        run, exit, pausa, actmisil, actdisparo, con_bloq_windows= eventospygame(run, exit, pausa, actmisil,
            actdisparo, con_bloq_windows)
        
        if actmisil:     #lanzar Misil
            xh, yh = jugador1.rect.center
            if misil1.activarmisil(xh, yh) =="activado":
                pass
            actmisil = False
        if actdisparo:   #Realizar diparos
            for bala1 in municion:
                xh, yh = jugador1.rect.center
                if bala1.activardisparo(xh, yh) == True:
                    break
            actdisparo = False
        #================================  
       
        # Actualiza las posiciones de los fondos
        posyfondo1 += velocidadfondo
        posyfondo2 += velocidadfondo
         # Reinicia las posiciones de los fondos cuando salen de la ventana
        if posyfondo1 > alto:
            posyfondo1 = posyfondo2 - alto -224
        if posyfondo2 > alto:
            posyfondo2 = posyfondo1 - alto -224
        #=============eventos======#
        if cantidad_meteoros > 0:
            contadorenemi = spawnmeteoros(contadorenemi, True)
        else:
            for meteoros in asteroides:
                meteoros.activate = False

        if isnave1 > 0:
            contadornave1 = spawnnave1(isnave1, contadornave1)
            
        xb, yb= jugador1.rect.center
        agregar_coordenada(xb, yb)
        # = Enemigo pueden dispara 
        for nave1 in naves_enemys:
            disparar, xc, yc = nave1.disparar()
            if disparar == True:
                haymunicion =0
                for bala2 in municion_enemy:
                    if bala2.activardisparo(xc, yc) == True:
                        haymunicion+=1
                        break
                if haymunicion == 0:
                    agregarmunicion()

        #=============Render Textos==============
        scoretxt = scorefont.render(f"score: {score}", True, blanco)
        txt2ancho, txt2alto = scoretxt.get_size()

        fpstxt = scorefont.render(f"FPS: {fps}", True, blanco)
        txt3ancho, txt3alto = fpstxt.get_size()
        if cooldown_misil < 100:
            cooldowntxt = scorefont.render(f"Recarga: {cooldown_misil}%", True, (255-cooldown_misil,255-tiempo_recarga + cooldown_misil,0))
        else:
            cooldowntxt = scorefont.render(f"Cargado", True, (0,200,0))
        txt4ancho, txt4alto = cooldowntxt.get_size()
        #=============Update===========#
        asteroides.update()
        jugador1.update()
        misil1.update()
        municion.update()
        naves_enemys.update()
        municion_enemy.update()
        #==========interaciones con entorno / colisiones===========#
        if pygame.sprite.spritecollideany(jugador1, asteroides, pygame.sprite.collide_mask) and colisionesmeteoros_bol:
            run = False
        colisionadoenemigo = pygame.sprite.spritecollideany(misil1, asteroides)
        if colisionadoenemigo:  #============ Colisiones misil y meteoritos=====
            efex_explocion2.play()
            bumx, bumy = colisionadoenemigo.rect.center
            asteroides.remove(colisionadoenemigo)
            all.remove(colisionadoenemigo)
            finexplosion = False
            explosion_frame = 0
            colisionadoenemigo.kill()
            misil1.desarmarmisil()
        for bala in municion:     #colisiones con balas contra meteoros y naves enemigas
        

            enemigo = pygame.sprite.spritecollideany(bala, all_enemys)
            if enemigo:
                bala.desarmardisparo()
                if enemigo.disminuirvida() == True:
                    efex_explocion2.play()
                    bumx, bumy = enemigo.rect.center
                    finexplosion = False
                    explosion_frame = 0
                    enemigo.kill()
        #colisiones balas enemigas VS Jugador
        if pygame.sprite.spritecollideany(jugador1, municion_enemy, pygame.sprite.collide_mask) and colisionesnaves_bol:
            run = False
        #colisiones balasVS Balas enemigas 
        for bala in municion:
            enemigo = pygame.sprite.spritecollideany(bala, municion_enemy)
            if enemigo:
                bala.desarmardisparo()
                enemigo.desarmardisparo()
                

                pass
        #======score
        if timexscore >= 20:
            timexetapa +=1
            score += 1
            frame, cantidad_meteoros = dificil(frame, cantidad_meteoros, score) 
            #print(cantidadenemigos)
            timexscore = 0
        cooldown_misil = 100 - ((misil1.cooldown * 100) // tiempo_recarga)

        #===========Zona de dibujo=============#
        ventana.blit(fondo, (0, posyfondo1))
        ventana.blit(fondo, (0, posyfondo2))
        pygame.draw.line(ventana, blanco, (limiteinterior, alto), (limiteinterior, 0), 2)
        pygame.draw.line(ventana, blanco, (ancho-limiteinterior, alto),
                          (ancho-limiteinterior, 0), 2)
        all.draw(ventana)
        finexplosion, explosion_frame =explosion(bumx, bumy, finexplosion, explosion_frame)
        ventana.blit(scoretxt, ((ancho - txt2ancho-50) , (alto - txt2alto)))
        ventana.blit(fpstxt, ((40) , (alto - txt3alto)))
        ventana.blit(cooldowntxt, ((ancho  -txt4ancho)//2 , (alto - txt4alto)))
        #===========================================================================
        #========== Actualizar  pantalla========#
        pygame.display.flip()
        #=======contadores========#
        timexscore += 1
        contadorenemi += 1
        #print(len(asteroides))
        #==========
        if inicio:
            try:       
                fin = timer.time()
                retardo = fin - inicio  
                fps = 1 // retardo
            except ZeroDivisionError:
                pass
        inicio = timer.time()
        time.tick(frame)

    print("score:", score)
    exit = gameover(posyfondo1,posyfondo2, score, exit=exit)
    pygame.quit()
    return exit

