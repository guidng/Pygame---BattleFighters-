from imports import *
import random

# Iniciando estruturas de dados
width=1200
height=600
sound=True
sound2=True
j1_wins=0
j2_wins=0
FPS=60
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Battlefighters ⚔️')
clock = pygame.time.Clock()
clock.tick(FPS)

# Tela de carregamento
def tela_carregamento():
    # Define variáveis
    frames=0
    countloadbar=0
    current_screen='tela carregamento'
    game=True
 
    # Inicia Loop
    while current_screen=='tela carregamento' and game==True:     
        clock.tick(FPS)

        # Atualiza variáveis
        countloadbar+=3
        frames+=1

        # Confere se carregamento está pronto
        if frames>360:
            current_screen = 'tela inicio'

        # Gera imagem de fundo
        window.fill((0, 0, 0))  # Preenche o fundo com a cor preta
        window.blit(Loadingimage, Loadingimage_rect)

        # Cria barra de carregamento
        pygame.draw.polygon(window, colorload1, verticesloadbar1)
        verticesloadbar2=[(width/4,510*(height/600)),(width/4,525*(height/600)),((width/4)+countloadbar,525*(height/600)),((width/4)+countloadbar,510*(height/600))]

        # Verifica se ultrapassa limite
        if countloadbar+(width/4)<3*(width/4):
            pygame.draw.polygon(window, colorload2, verticesloadbar2)
        else:
            verticesloadbar2=[((width/4),510*(height/600)),((width/4),525*(height/600)),(3*(width/4),525*(height/600)),(3*(width/4),510*(height/600))]
            pygame.draw.polygon(window, colorload2, verticesloadbar2)
        
        # Verifica se atinge limite
        if countloadbar>=width/2:
            window.blit(conctext, ((width/2)-conctextrect[2]/2, 530*(height/600)))
        
        # Atualiza tela
        pygame.display.update()  # Mostra o novo frame para o jogador

        # Trata eventos
        for event in pygame.event.get():
            # Verifica consequências
            if event.type == pygame.QUIT:
                game = False

    return current_screen,game


# Tela de início
def tela_inicio(sound):
    
    # Definindo variáveis
    current_screen='tela inicio'
    game=True
    song1variable=0

    # Inicia Loop
    while current_screen=='tela inicio' and game==True:
    
        # Da play na musica em loop
        if song1variable==0:
            pygame.mixer.music.play(-1,2)
        song1variable+=1

        # Gera imagem background e titulo
        window.blit(BGSSimage, BGSSimage_rect)
        window.blit(Titleimage, Titleimage_rect)

        # Verifica o estado atual do botão de mute
        if sound==False:
            Soundimage=Muteimage
        else:
            Soundimage=Volumeimage

        # Cria botão do play e musica:
        window.blit(Soundimage, Soundimage_rect)
        window.blit(Playimage, Playimage_rect)

        # Trata eventos
        for event in pygame.event.get():
            # Verifica consequências
            if event.type == pygame.QUIT:
                game = False
            # Verifica clique do mouse
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1: # Botão esquerdo
                    mouse_pos=event.pos
                    if volume_area.collidepoint(mouse_pos):
                        if sound==True:
                            sound=False
                            pygame.mixer.music.set_volume(0)  # Define o volume da música (0.0 a 1.0)
                        else:
                            sound=True
                            pygame.mixer.music.set_volume(0.1)  # Define o volume da música (0.0 a 1.0)

                    if play_area.collidepoint(mouse_pos):
                        current_screen='personagens'
                        
        pygame.display.update()  # Mostra o novo frame para o jogador

    return current_screen,game,Soundimage,sound


# Grade de Personagens
def personagens():

    # Definindo variáveis
    current_screen='personagens'
    game=True
    imagepers1=False
    imagepers2=False
    j1=False
    j2=False
    Fullpic1=0
    Fullpic2=0
    Fullpicrect1=0
    Fullpicrect2=0
    np1=0
    np2=0
    j1_pers=0
    j2_pers=0

    # Iniciando Loop
    while current_screen=='personagens' and game==True:

        # Teste pra ver qual rect usar
        if SecScreen>0:
            Fullpicrect1.center=(150,300)
            Fullpicrect2.center=(1050,300)

        # Plota background, grade, personagens, confirmar e seta
        window.blit(BGSSimage, BGSSimage_rect)
        window.blit(Gradeimage, Gradeimage_rect)
        window.blit(Arrowimage, Arrowimage_rect)
       
        # Mostra imagens das caras e nomes dos personagens 
        for counter in range(20):
            Face=list_facenrect[counter][0]
            Face_rect=list_facenrect[counter][1]
            Name=list_namenrect[counter][0]
            Name_rect=list_namenrect[counter][1]

            window.blit(Face, Face_rect)
            window.blit(Name, Name_rect)

        # Verifica se jogadores estão prontos
        if j1==False:
            window.blit(Confirmb1, Confirmb1_rect)
        else:
            window.blit(Confirmedb1, Confirmedb1_rect)
        if j2==False:
            window.blit(Confirmb2, Confirmb2_rect)
        else:
            window.blit(Confirmedb2, Confirmedb2_rect)

        if imagepers1==True:
            window.blit(Fullpic1, Fullpicrect1)

        if imagepers2==True:
            window.blit(Fullpic2, Fullpicrect2)

        # Trata eventos
        for event in pygame.event.get():
            # Verifica consequências
            if event.type == pygame.QUIT:
                game = False
            # Verifica clique do mouse
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1: #Botão esquerdo
                    mouse_pos=event.pos
                    for countarea in range(len(face_area_list)): # Tamanho da lista de areas ocupadas por imagens de face
                        face_area=pygame.Rect(face_area_list[countarea]) # Area da face atual
                        if face_area.collidepoint(mouse_pos): # Se colidir com a area do clique
                            for num in dic_pos.keys(): # Chute, soco e lado
                                diccount=0 # Contagem do dicionario
                                for Fullpic,Fullpicrect in Full_list1.items(): #Foto e rect da foto (corpo todo)
                                    if num==countarea: # Se o número da foto toda bater 
                                        if diccount==countarea: # Se o número do personagem bater
                                            if j1==False: # Se o j1 ainda não confirmou
                                                # Define imagens do j1
                                                imagepers1=True
                                                Fullpic1=Fullpic
                                                Fullpicrect1=Fullpicrect
                                                j1_pers=list_characters[diccount]
                                                np1=num
                                        diccount+=1 #Atualiza variável
                                
                                diccount=0 # Redefine variável
                                for Fullpic,Fullpicrect in Full_list2.items(): #Mesma linha de pensamento da primeira
                                    if num==countarea:
                                        if diccount==countarea:
                                            if j1==True and j2==False:
                                                imagepers2=True
                                                Fullpic2=Fullpic
                                                Fullpicrect2=Fullpicrect
                                                j2_pers=list_characters[diccount]
                                                np2=num
                                        diccount+=1
                    if arrow_area.collidepoint(mouse_pos):
                        current_screen='tela inicio'

                    # Botão Confirma
                    if Confirmb1_area.collidepoint(mouse_pos):
                        if imagepers1==True:
                            if j1==False:
                                j1=True
                            else:
                                j1=False
                    if Confirmb2_area.collidepoint(mouse_pos):
                        if imagepers2==True:
                            if j2==False and j1==True:
                                j2=True

        # Vê se ambos estão prontos
        if j1 and j2:
            current_screen='tela mapas'

        pygame.display.update()  # Mostra o novo frame para o jogador
    
    return current_screen,game,Fullpic1,Fullpic2,Fullpicrect1,Fullpicrect2,np1,np2,j1_pers,j2_pers


# Mapa
def tela_mapas():
    
    # Definindo variáveis
    frames=0
    counter=0
    song2variable=0
    current_screen='tela mapas'
    game=True

    # Criando loop
    while current_screen=='tela mapas' and game==True:
        clock.tick(FPS)            
        
        # Sorteia mapa
        mapnumber=random.randint(0,len(maps_list)-1)

        # Conta tempo
        if frames>300:
            current_screen='prepartida'

        # Conferindo mapa do sorteio
        for map,(image, trilha_sonora_mapas) in dic_maps.items():
            for map1,rect in dic_mapsrect.items():
                if map==map1:
                    if counter==mapnumber:
                        current_map=map
                        current_map_image=image
                        current_map_rect=rect
                        window.blit(image, rect)
                        maptext2= mapfont.render(f'{map}', True, (255,255,255))
                        text2rect=maptext2.get_rect()
                        text2rect.center=(width/2,500)
                        window.blit(maptext1, text1rect)
                        window.blit(maptext2, text2rect)
                        pygame.mixer.music.set_volume(0) # Zerar volume da música de intro
                        trilha_sonora_mapas.set_volume(0.1) # Aumentar volume da música de batalha
                        if song2variable==0:
                            trilha_sonora_mapas.play(-1)  # Toca a música da batalha em loop
                            atual_TS=trilha_sonora_mapas
                        song2variable += 1
                    counter+=1

        # Atualiza variáveis
        frames+=1

        # Trata eventos
        for event in pygame.event.get():
            # Verifica consequências
            if event.type == pygame.QUIT:
                game = False

        pygame.display.update()  # Mostra o novo frame para o jogador

    return frames,current_screen,game,current_map,current_map_image,current_map_rect,atual_TS,mapnumber


# Pré partida
def prepartida(current_map_image,current_map_rect,Fullpicrect1,Fullpicrect2,Fullpic1,Fullpic2):

    # Definindo variáveis
    game=True
    current_screen='prepartida'
    frames=0

    # Criando loop
    while current_screen=='prepartida' and game==True:
        clock.tick(FPS)

        # Plota imagens
        window.blit(current_map_image,current_map_rect)
        Fullpicrect1.center=(300,300)
        Fullpicrect2.center=(900,300)
        window.blit(Fullpic1, Fullpicrect1)
        window.blit(Fullpic2, Fullpicrect2)
        window.blit(Versus,Versusrect)

        # Contagem regressiva
        if frames>=0 and frames<60:
            window.blit(n3, nrect)

        if frames>=60 and frames<120:
            window.blit(n2, nrect)

        if frames>=120 and frames<180:
            window.blit(n1, nrect)

        if frames>=180 and frames<240:
            window.blit(nstart, nsrect)

        if frames>=240:
            current_screen='partida'
        
        # Trata eventos
        for event in pygame.event.get():
            # Verifica consequências
            if event.type == pygame.QUIT:
                game = False

        frames+=1

        pygame.display.update()  # Mostra o novo frame para o jogador

    return current_screen,game


# Partida
def partida(mapnumber,current_map_image,current_map_rect,np1,np2):
    
    # Parâmetros para inversão de imagem funcionar
    last_keyj1='d'
    last_keyj2='LEFT'

    # Verifica altura:
    hmapa=listahmapa[mapnumber]

    # Variáveis de poder
    escudo1=False
    velocidade1=False
    superpulo1=False
    gigante1=False
    pistola1=False
    escudo2=False
    velocidade2=False
    superpulo2=False
    gigante2=False
    pistola2=False

    # Cria variáveis
    song2variable=0
    SecScreen=1
    counting=0
    MStest=0
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
    atual_pos1=0
    atual_pos2=0
    atual_pos1=0
    atual_pos2=0       
    time=90*60
    timeMS=31*60
    lim=0
    pulo1=False
    pulo2=False
    desce1=False
    desce2=False
    counterj1=0
    counterj2=0
    estab1=False
    estab2=False
    timepower=0

    current_screen='partida'
    game=True

    while current_screen=='partida' and game==True:
        
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

        # Plota fundo
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
            mov1 = pygame.image.load(f'images/Personagenspartida/lado/Perslado{np1}.png')
        elif atual_pos1==1:
            mov1 = pygame.image.load(f'images/Personagenspartida/soco/Perssoco{np1}.png')
        else:
            mov1 = pygame.image.load(f'images/Personagenspartida/chute/Perschute{np1}.png')
        
        if gigante1==False:
            mov1 = pygame.transform.scale(mov1, (DGwidth, DGheight))
        else:
            mov1 = pygame.transform.scale(mov1, (2*DGwidth, 3*DGheight))

        if atual_pos2==0:    
            mov2 = pygame.image.load(f'images/Personagenspartida/lado/Perslado{np2}.png')
        elif atual_pos2==1:
            mov2 = pygame.image.load(f'images/Personagenspartida/soco/Perssoco{np2}.png')
        else:
            mov2 = pygame.image.load(f'images/Personagenspartida/chute/Perschute{np2}.png')

        if gigante2==False:
            mov2 = pygame.transform.scale(mov2, (DGwidth, DGheight))
        else:
            mov2 = pygame.transform.scale(mov2, (2*DGwidth, 3*DGheight))

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

        if superpulo1==False:
            if Py1_pos<=hmapa-100:
                estab1=True
                pulo1=False
        else:
            if Py1_pos<=hmapa-200:
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

        if superpulo2==False:
            if Py2_pos<=hmapa-100:
                estab2=True
                pulo2=False
        else:
            if Py2_pos<=hmapa-200:
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

        if timeMS<1:
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
                            if escudo2==False:
                                hp2-=2
                if event.key == pygame.K_b:
                    if Kickj1==0:
                        Kickj1=30
                        if p1_area.colliderect(p2_area):
                            if escudo2==False:
                                hp2-=2
                if event.key == pygame.K_k:
                    if Punchj2==0:
                        Punchj2=30
                        if p2_area.colliderect(p1_area):
                            if escudo1==False:
                                hp1-=2
                if event.key == pygame.K_l:
                    if Kickj2==0:
                        Kickj2=30
                        if p2_area.colliderect(p1_area):
                            if escudo1==False:    
                                hp1-=2
                if event.key == pygame.K_w:
                    pulo1=True
                if event.key == pygame.K_UP:
                    pulo2=True




        # Movimentação personagens
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            if velocidade1==False:
                Px1_pos -= 6
            else:
                Px1_pos -= 12
            last_keyj1='a'
        if keys[pygame.K_d]:
            if velocidade1==False:
                Px1_pos += 6
            else:
                Px1_pos += 12
            last_keyj1='d'
        if keys[pygame.K_LEFT]:
            if velocidade2==False:
                Px2_pos -= 6
            else:
                Px2_pos -= 12 
            last_keyj2='LEFT'
        if keys[pygame.K_RIGHT]:
            if velocidade2==False:
                Px2_pos += 6
            else:
                Px2_pos += 12
            last_keyj2='RIGHT'
        
        if (time+15)%30==0:
            power=random.randint(0,len(power_list)-1)
            atualpower=power_list[power]
            atualpowerimage=dic_power[atualpower]
            timepower=5*60
        
        if timepower>0:
            atualpowerimage_rect=atualpowerimage.get_rect()
            atualpowerwidth=random.randint(1,1200)
            atualpowerheight=(height-hmapa)+(((timepower*2)/height)*hmapa)
            atualpowerimage_rect.center=(atualpowerwidth,atualpowerheight)
            atualpowerarea=(atualpowerwidth-(powerimagewidth/2),atualpowerheight-(powerimageheight/2),powerimagewidth,powerimageheight)
            window.blit(atualpowerimage,atualpowerimage_rect)
            
            if p1_area.colliderect(atualpowerarea):
                timepower=0
                if atualpower=='Escudo':
                    escudo1=True
                if atualpower=='Supervelocidade':
                    velocidade1=True
                if atualpower=='Superpulo':
                    superpulo1=True
                if atualpower=='Gigante':
                    gigante1=True
                if atualpower=='Pistola':
                    pistola1=True
                timeusepower=15*60
            
            elif p2_area.colliderect(atualpowerarea):
                timepower=0
                if atualpower=='Escudo':
                    escudo2=True
                if atualpower=='Supervelocidade':
                    velocidade2=True
                if atualpower=='Superpulo':
                    superpulo2=True
                if atualpower=='Gigante':
                    gigante2=True
                if atualpower=='Pistola':
                    pistola2=True
                timeusepower=15*60
            
                
            timepower-=1
        else:
            atualpowerarea=(0,0,0,0)
        
        if timeusepower>0:
            timeusepower-=1

        else:
            escudo1=False
            velocidade1=False
            superpulo1=False
            gigante1=False
            pistola1=False
            escudo2=False
            velocidade2=False
            superpulo2=False
            gigante2=False
            pistola2=False            

        pygame.display.update()  # Mostra o novo frame para o jogador
    
    return current_screen,game,hp1,hp2,song2variable,SecScreen,counting


# Menu de pausa
def jogo_pausado(current_map_image,current_map_rect,atual_TS,sound2):
    current_screen='Jogo pausado'
    game=True
    while current_screen=='Jogo pausado' and game==True:
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
            atual_TS.set_volume(0.1)
        else:
            atual_TS.set_volume(0)

        pygame.display.update()  # Mostra o novo frame para o jogador

    return current_screen,game,sound2


# Menu de controles
def fcontroles(current_map_image,current_map_rect,sound2):
    
    current_screen='controles'
    game=True
    while current_screen=='controles' and game==True:
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

        pygame.display.update()  # Mostra o novo frame para o jogador

    return current_screen,game,sound2


def fimdejogo(current_map_image,current_map_rect,hp1,hp2,j1_pers,j2_pers,Fullpic1,Fullpic2,j1_wins,j2_wins):
    current_screen='Fim de jogo'
    game=True
    frames=0
    clock.tick(FPS)
    limit=0
    while current_screen=='Fim de jogo' and game==True:
        clock.tick(FPS)
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

        pygame.display.update()  # Mostra o novo frame para o jogador

    return current_screen,game,jw,jwin,j1_wins,j2_wins


def opcoespj(current_map,current_map_image,atual_TS,jw,j1_wins,j2_wins):
    current_screen='Opções pós jogo'
    game=True
    while current_screen=='Opções pós jogo' and game==True:

        window.blit(plano_de_fundo_vitoria_image, plano_de_fundo_vitoria_rect )

        jw=pygame.transform.scale(jw,(300,500))
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

    return current_screen,game