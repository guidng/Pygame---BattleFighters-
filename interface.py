# Iniciando jogo
import pygame
import random
pygame.init()
current_screen='tela carregamento'

# Importando outras janelas
from imports import *
from funcoes import *

# Loop principal
while game:

    clock.tick(FPS)
   
    # Troca tela
    if current_screen == 'tela carregamento':
        current_screen,game = tela_carregamento() 

    # Troca tela
    if current_screen == 'tela inicio':
        current_screen,game = tela_inicio()

    # Troca tela
    if current_screen=='personagens':
        current_screen,game,Fullpic1,Fullpic2,Fullpicrect1,Fullpicrect2,np1,np2,j1_pers,j2_pers = personagens()
   
    # Troca tela
    if current_screen=='tela mapas':
        frames,current_screen,game,current_map,current_map_image,current_map_rect,atual_TS,mapnumber=tela_mapas()

    # Troca tela
    if current_screen=='prepartida':
        # Parâmetros para inversão de imagem funcionar
        last_keyj1='d'
        last_keyj2='LEFT'

        # Verifica altura:
        hmapa=listahmapa[mapnumber]


        # Cria variáveis
        song2variable=0
        SecScreen=1
        MStest=0
        counting=0
        hp1=100
        hp2=100
        Px1_pos=100
        Px2_pos=1100
        Py1_pos=hmapa
        Py2_pos=hmapa
   
        Kickj1=0
        Kickj2=0
        Punchj1=0
        Punchj2=0

        # Plota imagens
        window.blit(current_map_image,current_map_rect)
        Fullpicrect1.center=(300,300)
        Fullpicrect2.center=(900,300)
        window.blit(Fullpic1, Fullpicrect1)
        window.blit(Fullpic2, Fullpicrect2)
        window.blit(Versus,Versusrect)


        # Contagem regressiva
        if frames>300 and frames<360:
            window.blit(n3, nrect)


        if frames>=360 and frames<420:
            window.blit(n2, nrect)


        if frames>=420 and frames<480:
            window.blit(n1, nrect)


        if frames>=480 and frames<540:
            window.blit(nstart, nsrect)


        if frames>=540:
            current_screen='partida'
            atual_pos1=0
            atual_pos2=0
       
        time=120*60
        timeMS=30*60
        lim=0
        pulo1=False
        pulo2=False
        desce1=False
        desce2=False
        counterj1=0
        counterj2=0
        estab1=False
        estab2=False

        # Trata eventos
        for event in pygame.event.get():
            # Verifica consequências
            if event.type == pygame.QUIT:
                game = False

    # Troca tela
    if current_screen=='partida':

        # Vê posição atual
        if Punchj2>0:
            Punchj2-=1
            atual_pos2=1
        elif Kickj2>0:
            Kickj2-=1
            atual_pos2=2
        else:
            atual_pos2=0

        if Punchj1>0:
            Punchj1-=1
            atual_pos1=1
        elif Kickj1>0:
            Kickj1-=1
            atual_pos1=2
        else:
            atual_pos1=0

        # Cria variáveis e plota fundo
        frames=0
        limit=0
        window.blit(current_map_image,current_map_rect)

        if MStest==1 and lim==0:
            Px1_pos=100
            Px2_pos=1100
            Py1_pos=hmapa
            Py2_pos=hmapa
            lim=1
            last_keyj1='d'
            last_keyj2='LEFT'

        # Plota imagens
        window.blit(Pauseb, Pauseb_rect)

        if atual_pos1==0:    
            mov1 = pygame.image.load(f'images/Personagenspartida/Perslado{np1}.png')
            mov1 = pygame.transform.scale(mov1, (DGwidth, DGheight))
        elif atual_pos1==1:
            mov1 = pygame.image.load(f'images/Personagenspartida/Perssoco{np1}.png')
            mov1 = pygame.transform.scale(mov1, (DGwidth, DGheight))
        else:
            mov1 = pygame.image.load(f'images/Personagenspartida/Perschute{np1}.png')
            mov1 = pygame.transform.scale(mov1, (DGwidth, DGheight))


        if atual_pos2==0:    
            mov2 = pygame.image.load(f'images/Personagenspartida/Perslado{np2}.png')
            mov2 = pygame.transform.scale(mov2, (DGwidth, DGheight))
        elif atual_pos2==1:
            mov2 = pygame.image.load(f'images/Personagenspartida/Perssoco{np2}.png')
            mov2 = pygame.transform.scale(mov2, (DGwidth, DGheight))
        else:
            mov2 = pygame.image.load(f'images/Personagenspartida/Perschute{np2}.png')
            mov2 = pygame.transform.scale(mov2, (DGwidth, DGheight))

        # Inverte imagem se preciso
        if last_keyj1=='a':
            mov1=pygame.transform.flip(mov1, True, False)
        if last_keyj2=='LEFT':
            mov2 = pygame.transform.flip(mov2, True, False)

        rect1=mov1.get_rect()
        rect2=mov2.get_rect()


        rect1.center=(Px1_pos,Py1_pos)
        rect2.center=(Px2_pos,Py2_pos)

        p1_area=pygame.Rect(Px1_pos-(DGwidth/2),Py1_pos+(DGheight/2),DGwidth,DGheight)
        p2_area=pygame.Rect(Px2_pos-(DGwidth/2),Py2_pos+(DGheight/2),DGwidth,DGheight)

        window.blit(mov1,rect1)
        window.blit(mov2,rect2)


        # Cria barras de hp
        verticesp1=[(25,25),(25,50),((25+(hp1*3)),50),((40+(hp1*3)),25)]
        pygame.draw.polygon(window, colorload2, verticesp1)
        verticesp2=[(1175,25),(11755,50),((1175-(hp2*3)),50),((1160-(hp2*3)),25)]
        pygame.draw.polygon(window, colorload2, verticesp2)

        hpfont=pygame.font.SysFont(None,36)
        texthp1=hpfont.render(f'{hp1}',True,(255,255,255))
        texthp2=hpfont.render(f'{hp2}',True,(255,255,255))
        texthp1_rect=texthp1.get_rect()
        texthp2_rect=texthp2.get_rect()
        texthp1_rect.left=26
        texthp1_rect.bottom=49
        texthp2_rect.right=width-26
        texthp2_rect.bottom=49
        window.blit(texthp1,texthp1_rect)
        window.blit(texthp2,texthp2_rect)

        # Atualiza tempo
        time-=1
        time/=60
        minutes=int(time//60)
        sec=int(time%60)
        time*=60


        # Cria cronometro
        timetextfont = pygame.font.SysFont(None, 64)
        if sec<10:
            timetext = timetextfont.render(f'{minutes}:0{sec}', True, (255,255,255))
        else:
            timetext = timetextfont.render(f'{minutes}:{sec}', True, (255,255,255))          
        timerect=timetext.get_rect()
        timerect.center=(width/2,125)


        # Impede personagem de sair do mapa
        if Px1_pos<0:
            Px1_pos=width
        if Px1_pos>width:
            Px1_pos=0


        if Px2_pos<0:
            Px2_pos=width
        if Px2_pos>width:
            Px2_pos=0

        seconds=time/60


        # Verifica pulo
        if pulo1==True:
            Py1_pos-=8
        if Py1_pos<=hmapa-100:
            estab1=True
            pulo1=False
        if estab1==True:
            counterj1+=1
        if counterj1>=5:
            counterj1=0
            estab1=False
            desce1=True
        if desce1==True:
            Py1_pos+=12
        if Py1_pos>=hmapa:
            desce1=False

        if pulo2==True:
            Py2_pos-=8
        if Py2_pos<=hmapa-100:
            estab2=True
            pulo2=False
        if estab2==True:
            counterj2+=1
        if counterj2>=5:
            counterj2=0
            estab2=False
            desce2=True
        if desce2==True:
            Py2_pos+=12
        if Py2_pos>=hmapa:
            desce2=False


        # Contagem Regressiva
        if MStest==0:
            if seconds>=3 and seconds<4:
                window.blit(n3, nrect)


            elif seconds>=2 and seconds<=3:
                window.blit(n2, nrect)


            elif seconds>0 and seconds<2:
                window.blit(n1, nrect)


            else:
                window.blit(timetext,timerect)
        else:
            # Nova contagem
            newtimetext = resfont.render(f'{(timeMS//60)}', True, (255,31,31))          
            newtimerect=newtimetext.get_rect()
            newtimerect.center=(width/2,(height/4)+15)
            window.blit(newtimetext,newtimerect)


            # Detecta momento do jogo
            if timeMS>(29*60):
                timetext = resfont.render('Morte Súbita!', True, (255,31,31))          
                timerect=timetext.get_rect()
                timerect.center=(width/2,height/2)
                window.blit(timetext,timerect)
            

            timeMS-=1

        if timeMS<=0:
            current_screen='Fim de jogo'

        # Confere se jogo acabou
        if hp1<=0 or hp2<=0:
            current_screen='Fim de jogo'
        if time<=1:
            MStest=1


        # Trata eventos
        for event in pygame.event.get():
            # Verifica consequências
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos=event.pos
                    if Pause_area.collidepoint(mouse_pos):
                        current_screen='Jogo pausado'
            if event.type ==pygame.KEYDOWN:
                if event.key == pygame.K_v:
                    if Punchj1==0:
                        Punchj1=30
                        if p1_area.colliderect(p2_area):
                            hp2-=2
                if event.key == pygame.K_b:
                    if Kickj1==0:
                        Kickj1=30
                        if p1_area.colliderect(p2_area):
                            hp2-=2
                if event.key == pygame.K_k:
                    if Punchj2==0:
                        Punchj2=30
                        if p2_area.colliderect(p1_area):
                            hp1-=2
                if event.key == pygame.K_l:
                    if Kickj2==0:
                        Kickj2=30
                        if p2_area.colliderect(p1_area):
                            hp1-=2
                if event.key == pygame.K_w:
                    pulo1=True
                if event.key == pygame.K_UP:
                    pulo2=True




        # Movimentação personagens
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            Px1_pos -= 6
            last_keyj1='a'
        if keys[pygame.K_d]:
            Px1_pos += 6
            last_keyj1='d'
        if keys[pygame.K_LEFT]:
            Px2_pos -= 6
            last_keyj2='LEFT'
        if keys[pygame.K_RIGHT]:
            Px2_pos += 6
            last_keyj2='RIGHT'
   
    # Troca tela
    if current_screen=='Jogo pausado':
        if sound2 == True:
            Sound2image=Volumeimage
        else:
            Sound2image=Muteimage


        window.blit(current_map_image,current_map_rect)
        window.blit(vjogo,vjogo_rect)
        window.blit(Retmenu,Retmenu_rect)
        window.blit(controles,controles_rect)
        window.blit(Sound2image,Soundimage_rect)


        # Trata eventos
        for event in pygame.event.get():
            # Verifica consequências
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos=event.pos
                    if controles_area.collidepoint(mouse_pos):
                        current_screen='controles'
                    if vjogo_area.collidepoint(mouse_pos):
                        current_screen='partida'
                    if Retmenu_area.collidepoint(mouse_pos):
                        current_screen='tela inicio'
                        pygame.mixer.music.set_volume(0.1)
                        atual_TS.stop()
                    if volume_area.collidepoint(mouse_pos):
                        if sound2==True:
                            sound2=False
                        else:
                            sound2=True
        if sound2==True:
            trilha_sonora_mapas.set_volume(0.1)
        else:
            trilha_sonora_mapas.set_volume(0)
   
    # Troca tela
    if current_screen=='controles':
        if sound2 == True:
            Sound2image=Volumeimage
        else:
            Sound2image=Muteimage


        window.blit(current_map_image,current_map_rect)
        window.blit(Arrowimage, Arrowimage_rect)
        window.blit(Sound2image,Soundimage_rect)


        for event in pygame.event.get():
            # Verifica consequências
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    mouse_pos=event.pos
                    if arrow_area.collidepoint(mouse_pos):
                        current_screen='Jogo pausado'
                    if volume_area.collidepoint(mouse_pos):
                        if sound2==True:
                            sound2=False
                        else:
                            sound2=True


        if sound2==True:
            trilha_sonora_mapas.set_volume(0.1)
        else:
            trilha_sonora_mapas.set_volume(0)

    # Troca tela
    if current_screen=='Fim de jogo':
        frames+=1
        window.blit(current_map_image,current_map_rect)
        if limit==0:
            if hp2<hp1:
                res = resfont.render(f'{j1_pers} wins!', True, (255,255,255))
                resrect=res.get_rect()
                resrect.center=(width/2,height/2)
                jw=Fullpic1
                jwin=j1_pers
                j1_wins+=1


            elif hp1<hp2:
                res = resfont.render(f'{j2_pers} wins!', True, (255,255,255))
                resrect=res.get_rect()
                resrect.center=(width/2,height/2)
                jw=Fullpic2
                jwin=j2_pers
                j2_wins+=1
           
            elif hp1==hp2:
                camp=random.randint(1,2)
                if camp==1:
                    res = resfont.render(f'{j1_pers} wins!', True, (255,255,255))
                    resrect=res.get_rect()
                    resrect.center=(width/2,height/2)
                    jw=Fullpic1
                    jwin=j1_pers
                    j1_wins+=1
                else:
                    res = resfont.render(f'{j2_pers} wins!', True, (255,255,255))
                    resrect=res.get_rect()
                    resrect.center=(width/2,height/2)
                    jw=Fullpic2
                    jwin=j2_pers
                    j2_wins+=1




        limit+=1


        window.blit(res,resrect)
       
        if frames>240:
            current_screen='Opções pós jogo'


        # Trata eventos
        for event in pygame.event.get():
            # Verifica consequências
            if event.type == pygame.QUIT:
                game = False

    # Troca tela
    if current_screen=='Opções pós jogo':
        imagepers1=False
        imagepers2=False
        window.blit(plano_de_fundo_vitoria_image, plano_de_fundo_vitoria_rect )


        if frames>300:
            frames=0
            current_screen='personagens'
        jw=pygame.transform.scale(jw,(400,666))
        jwrect=jw.get_rect()
        jwrect.center=(200,300)
        window.blit(jw,jwrect)
        current_map_image=pygame.transform.scale(current_map_image,(300,200))
        current_map_rect=current_map_image.get_rect()
        current_map_rect.center=(1000,150)
        window.blit(current_map_image,current_map_rect)
        mapfont2 = pygame.font.SysFont(None, 48)
        maptext = mapfont2.render(f'{current_map}', True, (255,255,255))
        maptextrect=maptext.get_rect()
        maptextrect.center=(1000,250)
        window.blit(maptext, maptextrect)


        window.blit(Jogardenovo,Jogardenovo_rect)
        window.blit(Trocarpers,Trocarpers_rect)
        window.blit(Retmenu,Retmenu_rect)


        pwinfont = pygame.font.SysFont(None, 60)
        P1wins = pwinfont.render(f'Player 1: {j1_wins} W', True, (255,255,255))
        P1winsrect=P1wins.get_rect()
        P1winsrect.center=(1000,375)
        window.blit(P1wins, P1winsrect)


        P2wins = pwinfont.render(f'Player 2: {j2_wins} W', True, (255,255,255))
        P2winsrect=P1wins.get_rect()
        P2winsrect.center=(1000,475)
        window.blit(P2wins, P2winsrect)
       
        # Trata eventos
        for event in pygame.event.get():
            # Verifica consequências
            if event.type == pygame.QUIT:
                game = False
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    mouse_pos=event.pos
                    if Retmenu_area.collidepoint(mouse_pos):
                        current_screen='tela inicio'
                        pygame.mixer.music.set_volume(0.1)
                        atual_TS.stop()
                    if Trocarpersarea.collidepoint(mouse_pos):
                        current_screen='personagens'
                        pygame.mixer.music.set_volume(0.1)
                        atual_TS.stop()
                    if Jogardenovoarea.collidepoint(mouse_pos):
                        current_screen='tela mapas'
                        atual_TS.stop()

    pygame.display.update()  # Mostra o novo frame para o jogador

# Finalização
pygame.quit()  # Função do PyGame que  finaliza os recursos utilizados