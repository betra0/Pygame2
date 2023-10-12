import pygame 
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, 
            K_ESCAPE, KEYDOWN, QUIT, K_w, K_s, K_d, K_a, K_SPACE)

from clases import(jugador, crater, misil, disparo, nave_enemy, disparo_enemy, escudo)


import time as timer
import os

def gameon():
    
    exit = False
    pygame.init()
    pygame.mixer.init()
    from var import(ancho, alto, size, tamaño, cantidad_meteoros, velocidadfondo, score, 
    timexscore, blanco, rojo, frame, tiempo_recarga, limiteinterior, colisionesmeteoros_bol,
    timexetapa, colisionesnaves_bol,
    niveles,
    agregar_coordenada, revisar_cordenadas, reiniciar_cordenadas)
    #=============DEFINIR GLOBAL VARIABLES Modulo game========
    # Posiciones iniciales de los fondos
    posyfondo1 = 0
    posyfondo2 = -alto-224
    #======================================
    ventana = pygame.display.set_mode(size)
    pygame.display.set_caption("PY GAME")
    time = pygame.time.Clock()
    #======textos
    pausafont = pygame.font.Font(None, 80)
    scorefont = pygame.font.Font(None, 30)

    #=======rutas=======#
    rutasprites = os.path.join("sprites")
    rutamultimedia = os.path.join("multimedia")

    #===============#caragar imagen escudos disponibles=========
    escudoimage = pygame.image.load(os.path.join(rutasprites, "escudo.png"))
    escudoimage = pygame.transform.scale(escudoimage, (50, 50))


    #===============cargar explosion============
    explosion_chica_images = []
    explosion_images = [pygame.image.load(os.path.join(rutasprites, f"explosion{i+1}.png")) for i in range(11)]

    for i in range(len(explosion_images)):
        imagen_escalada = pygame.transform.scale(explosion_images[i], (30, 30))
        explosion_chica_images.append(imagen_escalada)

    for i in range(len(explosion_images)):
        explosion_images[i] = pygame.transform.scale(explosion_images[i], (100, 100))
    explosion_frame = 0  # Índice del fotograma actual de la explosión
    explosion_chica_frame = 0
    #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    #====Fondos====#
    fondo = pygame.image.load(os.path.join(rutasprites, "fondo.png")).convert()

    def explosion_chica(x,y, finexplosion_chica, explosion_chica_frame):
        #se encarga de generar una explosion frame por frame 
        #en el x e y proporcionados
        if finexplosion_chica == False:
                ventana.blit(explosion_chica_images[explosion_chica_frame], (x-15, y-5))
                explosion_chica_frame = (explosion_chica_frame + 1) % len(explosion_chica_images)
                if explosion_chica_frame == 10:
                    finexplosion_chica= True
        return finexplosion_chica, explosion_chica_frame
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
        contadorfin = 50
        fpsover = 60
        efex_explocion1.play()
        exit2 = False
        
        while True:
            #revisar eventos 
            for eventos in pygame.event.get():
                if eventos.type == QUIT:
                        exit2 = True
                        break
            #revisar si se preciono clic en exit mientras estava activa la trancision
            if exit2:
                exit = True
                break
            #movimiento del fondo 
            posyfondo1 += velocidadfondo
            posyfondo2 += velocidadfondo
             # Reinicia las posiciones de los fondos cuando salen de la ventana
            if posyfondo1 > alto:
                posyfondo1 = posyfondo2 - alto -224

            if posyfondo2 > alto:
                posyfondo2 = posyfondo1 - alto -224
            #actualizar cordenada de los objetos
            asteroides.update()
            #=============dibujado de pantalla =============
            ventana.blit(fondo, (0, posyfondo1))
            ventana.blit(fondo, (0, posyfondo2))
            pygame.draw.line(ventana, blanco, (limiteinterior, alto), (limiteinterior, 0), 2)
            pygame.draw.line(ventana, blanco, (ancho-limiteinterior, alto), (ancho-limiteinterior, 0), 2)
            asteroides.draw(ventana)
            xss, yss = jugador1.rect.center
            #dibujar cada frame de la explosion
            finexplosion, explosion_frame =explosion(xss, yss, finexplosion, explosion_frame)

            if finexplosion == True:
                print("fin explosion")
                pygame.mixer.music.pause()
                contadorfin -= 1
                fpsover -= 1
            
                ventana.blit(gameovertxt, ((ancho - txt1ancho) // 2, (alto - txt1alto) // 2 ))
                ventana.blit(scoretxt, ((ancho - txt2ancho) // 2, (alto +100) // 2 ))

            #============================================================
            pygame.display.flip()
            time.tick(fpsover)
            
            if contadorfin ==0:
                print("prefin")
                timer.sleep(0.3)
                print("fin")
                break
        return exit
    def trancision(frame, posyfondo1, posyfondo2, score):
        #===
        proxfps = 200
        duracionevento = 4

        # Declaracion de variables===
        inicio = False
        run = True
        exit = False
        acendente = True
        decreciente = False
        maximo = False
        fps = 0
        frame = round(frame)
        n, newproxfps, n, n, n, n, proxnivel_real, n =niveles[nivel+1]
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
            #========Proceso de suvida de frame y fondo========
            if acendente:
                if proxfps:
                    diferencia = proxfps - frame
                    #print("Subiendo VEl", proxfps, frame, "diferencia", diferencia)                  
                    if diferencia >1:
                        diferencia = 1
                    frame +=diferencia
                if velocidadfondo_mov <19:
                    velocidadfondo_mov += 0.06
                    #print("mov alc", velocidadfondo_mov)
                else:
                    if frame == proxfps :
                        acendente = False
                        maximo = True
                        print("== inicio maximo ==")

            elif maximo:
                duracionevento -= 0.01
                if -1 < duracionevento < 1:
                    decreciente = True
                    maximo = False
                    #print("fin maximo")
                #print(duracionevento)
            
            elif decreciente: 
                    if velocidadfondo_mov > 2:
                        velocidadfondo_mov -= 0.05
                    #print("mov fondo decenso", velocidadfondo_mov)

                    diferencia = frame - newproxfps 
                    #print("ultimo proceso", newproxfps, frame, "diferencia", diferencia)
                    
                    if diferencia >1:
                        diferencia = 1

                    frame -= diferencia
                       
                    if frame == newproxfps and velocidadfondo_mov < 10:
                        break          
            
            #:::::::::::::::::FIN:::::::::::::::::::::::
            #====EVENTOS IN GAME===
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
            #::::::::::::::::::::::::
            xb, yb= jugador1.rect.center
            agregar_coordenada(xb, yb)
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
            escudos.update()
            #==========================zona de dibujo=================
            ventana.blit(fondo, (0, posyfondo1))
            ventana.blit(fondo, (0, posyfondo2))
            pygame.draw.line(ventana, blanco, (limiteinterior, alto), (limiteinterior, 0), 2)
            pygame.draw.line(ventana, blanco, (ancho-limiteinterior, alto), (ancho-limiteinterior, 0), 2)
            if len(escudos_activos) > 0:
                drawescudos(escudos_activos)
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
                            
    def antes_de_empezar(run = True, exit = False):
        #============Render TXT============================
        pausatxt = pausafont.render("Play", True, blanco)
        txt1ancho, txt1alto = pausatxt.get_size()
        subpausatxt = scorefont.render(f" Presione clic izquierdo para comenzar ", True, blanco)
        txt3ancho, txt3alto = subpausatxt.get_size()
        subpausa2txt = scorefont.render(f" Esc para salir ", True, blanco)
        txt4ancho, txt4alto = subpausa2txt.get_size()
        #=================================================================
        comenzar = False
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
        
        return run, exit
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
    def dificil(cantidadenemigos,):
        
        if cantidadenemigos >0:
            cantidadenemigos += 1

        return  cantidadenemigos
    def explosion(x,y, finexplosion, explosion_frame):
        #se encarga de generar una explosion frame por frame 
        #en el x e y proporcionados
        if finexplosion == False:
                ventana.blit(explosion_images[explosion_frame], (x-50, y-50))
                explosion_frame = (explosion_frame + 1) % len(explosion_images)
                if explosion_frame == 10:
                    finexplosion= True
        return finexplosion, explosion_frame
    def agregarmunicion():
        #se encarga de crear municion cuando las naves enemigas se quedas sin municion 
        bala2 = disparo_enemy()
        all.add(bala2)
        municion_enemy.add(bala2)
    def spawnnave1(maxnave, contadornave1):
        if maxnave > contadornave1:
            for i in range(1):
                nave1 = nave_enemy()
                all.add(nave1)
                naves_enemys.add(nave1)
                all_enemys.add(nave1)
                contadornave1 += 1
        return contadornave1
    def spawnescudo(maxescudo, contadorescudo):
        if maxescudo > contadorescudo:
            escudo1 = escudo()
            all.add(escudo1)    
            escudos.add(escudo1)
            escudos_inactivos.add(escudo1)
            contadorescudo += 1
        return contadorescudo
    def drawescudos(escudos_activos):
        vida = escudos_activos.sprites()[0].vida
        for i in range(vida):
            ventana.blit(escudoimage, (limiteinterior-60, alto-90-50*i))

    # ===Musica =========
    musica1mp3 = os.path.join(rutamultimedia, "musicamain.mp3")
    efectoexplocion1mp3 = os.path.join(rutamultimedia, "explosion1.mp3")
    efectoexplocion2mp3 = os.path.join(rutamultimedia, "explosion2.mp3")
    efectodisparo1 = os.path.join(rutamultimedia, "8bitgun.mp3")

    pygame.mixer.music.load(musica1mp3)
    pygame.mixer.music.set_volume(0.1)
    
    efex_explocion1 = pygame.mixer.Sound(efectoexplocion2mp3)
    efex_explocion2 = pygame.mixer.Sound(efectoexplocion1mp3)
    efex_disparo1 =  pygame.mixer.Sound(efectodisparo1)
    efex_disparo1.set_volume(0.3)
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
    escudos = pygame.sprite.Group()
    escudos_activos = pygame.sprite.Group()
    escudos_inactivos = pygame.sprite.Group()
    
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
    run = True
    pausa = True
    fps = 0
    inicio = False
    # ==== explosiones
    finexplosion = True
    finexplosion_chica = True
    bumx, bumy =0, 0
    bumx2, bumy2 =0, 0
    #==========
    actmisil = False
    actdisparo = False
    
    cooldown_misil = 0
    # declaracion variables niveles
    nivel = 0
    max_tiempoxetapa = 3
    cantidad_meteoros = 0
    isnave1 = 0
    isescudo = 0
    contadornave1 = 0
    contadorescudo = 0
    procesocambionivel = False
    modonaves = False
    proxfps = None
    istrancision = False
    con_bloq_windows = 0
    time_dificultad = 0
    #PANTALLA DE INICIO
    run, exit = antes_de_empezar()
    #=========================================<<<<<<<<<GAME Bucle|>>>>>>>>>=====================================#
    while run:
  
        #===pausa===
        if pausa == False:
            pausa, run, exit = pausagame(pausa, run, exit)
            con_bloq_windows = 0

        #==========================Sistema de niveles================================
        if istrancision == True:
            cantidad_meteoros = 0
            isnave1 = 0

            posyfondo1, posyfondo2, run, exit =trancision(frame, posyfondo1,
                            posyfondo2, score)

            procesocambionivel = True
            #asegurase que la explosion no aparesca en la transicion
            finexplosion = True
            explosion_frame = 0
            finexplosion_chica = True
            explosion_chica_frame = 0
        #____proceso para adecuar FPS__
        if proxfps:
            if proxfps > frame:
                frame += 1
            elif proxfps < frame:
                frame -= 0.25
        #::::: FIN ::::::

        if modonaves and len(naves_enemys) < 1 and contadornave1 > 0:
            print("no hay mas naves")
            procesocambionivel = True

        if timexetapa == max_tiempoxetapa:
            procesocambionivel = True


        if procesocambionivel == True:
            nivel += 1
            timexetapa = 0
            contadornave1 = 0
            contadorescudo = 0
            modonaves = False 
            print("nivel:", nivel)
            procesocambionivel= False
            try:
                #(duracion, fps inicial, meteoros, cant_meteoros, cantidadnave1, agregarnave1, cantidad nave2,  agregarnave2)
                max_tiempoxetapa, proxfps, cantidad_meteoros, isnave1,  na, istrancision, na, isescudo =niveles[nivel]
                if isnave1 > 0:
                    modonaves = True
                if isescudo < 1 and len(escudos_inactivos) > 0:
                    for escudo1 in escudos_inactivos:
                        escudo1.kill()
            except KeyError:
                print("Error: No hay mas niveles ")
                pass 
    #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: 

        #=================EVENTOSPYGAME==========================
        # se encaraga de manejar los eventos dentro y fuera de la pantalla 
        # y eventos del teclado o maus
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
                    efex_disparo1.play()
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
            #SE ENCARGA DE ELIMINAR A LOS METEOROS CUANDO FINALIZA SU ETAPA
            for meteoros in asteroides:
                meteoros.activate = False

        if isnave1 > 0:
            contadornave1 = spawnnave1(isnave1, contadornave1)
        if isescudo >0:
            contadorescudo = spawnescudo(isescudo, contadorescudo)
            pass
            
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

        if len(escudos_activos) >= 2:
            escudos_activos.sprites()[1].kill()
            escudos_activos.sprites()[0].aumentarvida()
            pass

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
        #se encarga de actualizar la posicion de los objetos
        # llama al metodo update de todos los objetos
        asteroides.update()
        jugador1.update()
        misil1.update()
        municion.update()
        naves_enemys.update()
        municion_enemy.update()
        escudos.update()
        
        #====================interaciones con entorno / colisiones================#
        colisionadoenemigo = pygame.sprite.spritecollideany(misil1, asteroides)
        if colisionadoenemigo:  #============ Colisiones misil y meteoritos=====
            efex_explocion2.play()
            
            bumx, bumy = colisionadoenemigo.rect.center
            finexplosion = False
            explosion_frame = 0

            asteroides.remove(colisionadoenemigo)
            all.remove(colisionadoenemigo)
            colisionadoenemigo.kill()
            misil1.desarmarmisil()
        for bala in municion:     #colisiones con balas contra meteoros y naves enemigas y escudos
            enemigo = pygame.sprite.spritecollideany(bala, all_enemys)
            if enemigo:
                
                if enemigo.disminuirvida() == True:
                    bala.desarmardisparo()
                    if cantidad_meteoros == 0:
                        score += 20
                    efex_explocion2.play()
                    bumx, bumy = enemigo.rect.center
                    finexplosion = False
                    explosion_frame = 0
                    enemigo.kill()
                else:
                    
                    print("hola")
                    bumx2, bumy2 = bala.rect.center
                    finexplosion_chica = False
                    explosion_chica_frame = 0
                    bala.desarmardisparo()

            if len(escudos_inactivos) > 0 :
                escudo1 = pygame.sprite.spritecollideany(bala, escudos_inactivos, pygame.sprite.collide_mask)
                if escudo1:
                    bala.desarmardisparo()
                    if escudo1.disminuirvida():
                        escudos_inactivos.remove(escudo1)
                        escudos_activos.add(escudo1)
        #colisiones balas enemigas VS Jugador
        if len(escudos_activos) > 0 :
            for escudo1 in escudos_activos:
                enemigo = pygame.sprite.spritecollideany(escudo1, municion_enemy, pygame.sprite.collide_mask)
                if enemigo:
                    enemigo.desarmardisparo()
                    escudo1.disminuirvida(1)
                enemigo = pygame.sprite.spritecollideany(escudo1, asteroides, pygame.sprite.collide_mask)
                if enemigo:
                    efex_explocion2.play()
                    bumx, bumy = enemigo.rect.center
                    finexplosion = False
                    explosion_frame = 0
                    enemigo.kill()
                    escudo1.disminuirvida(3)           
        else:
            if pygame.sprite.spritecollideany(jugador1, municion_enemy, pygame.sprite.collide_mask) and colisionesnaves_bol:
                run = False
            if pygame.sprite.spritecollideany(jugador1, asteroides, pygame.sprite.collide_mask) and colisionesmeteoros_bol:
                run = False
        if len(escudos_inactivos) > 0 :
                escudo1 = pygame.sprite.spritecollideany(jugador1, escudos_inactivos, pygame.sprite.collide_mask)
                if escudo1:
                    if escudo1.disminuirvida():
                        escudos_inactivos.remove(escudo1)
                        escudos_activos.add(escudo1)            
        #colisiones balasVS Balas enemigas 
        for bala in municion:
            enemigo = pygame.sprite.spritecollideany(bala, municion_enemy)
            if enemigo:
                bumx2, bumy2 = bala.rect.center
                finexplosion_chica = False
                explosion_chica_frame = 0

                bala.desarmardisparo()
                enemigo.desarmardisparo()   
        
        #::::::::::::::::::::::::::::::::::::FIN COLISIONES ::::::::::::::::::::::::::FIN COLISIONES::::::::::::::::::::
        #======dificultad

        if timexscore == 20:
            timexscore = 0
            time_dificultad += 1
            timexetapa +=0.5
            frame += 0.05
            if cantidad_meteoros > 0:
                score += 2
            if time_dificultad >= 11:
                cantidad_meteoros = dificil(cantidad_meteoros)
                time_dificultad = 0
                print(cantidad_meteoros)

        cooldown_misil = 100 - ((misil1.cooldown * 100) // tiempo_recarga)
        

        #===========Zona de dibujo=============#
        ventana.blit(fondo, (0, posyfondo1))
        ventana.blit(fondo, (0, posyfondo2))
        pygame.draw.line(ventana, blanco, (limiteinterior, alto), (limiteinterior, 0), 2)
        pygame.draw.line(ventana, blanco, (ancho-limiteinterior, alto),
                          (ancho-limiteinterior, 0), 2)
        all.draw(ventana)
        if len(escudos_activos) > 0:
            drawescudos(escudos_activos)
        finexplosion, explosion_frame =explosion(bumx, bumy, finexplosion, explosion_frame)

        finexplosion_chica, explosion_chica_frame =explosion_chica(
                bumx2, bumy2, finexplosion_chica, explosion_chica_frame)
        ventana.blit(scoretxt, ((ancho - txt2ancho-50) , (alto - txt2alto)))
        ventana.blit(fpstxt, ((40) , (alto - txt3alto)))
        ventana.blit(cooldowntxt, ((ancho  -txt4ancho)//2 , (alto - txt4alto)))
        #===========================================================================
        #========== Actualizar  pantalla========#
        pygame.display.flip()
        #=======contadores========#
        timexscore += 1
        contadorenemi += 1
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

