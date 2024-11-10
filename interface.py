x=1
if x==1:
    # Importa e inicia pacotes
    import pygame
    import random
    pygame.init()


    # Gera tela principal
    width=1200
    height=600
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Battlefighters ⚔️')


    # Inicia estruturas de dados
    game = True
    sound = True
    sound2 = True
    j1=False
    j2=False
    frames=0
    current_screen='tela carregamento'
    clock = pygame.time.Clock()
    FPS=60
    countloadbar=0
    j1_wins=0
    j2_wins=0
    SecScreen=0


    # Importa imagens das ações dos personagens durante o jogo:
    dic_pos={}
    for i in range(20):
        DGwidth=width/16
        DGheight=height/4
        side = pygame.image.load(f'images/Personagenspartida/Perslado{i}.png')
        side = pygame.transform.scale(side, (DGwidth, DGheight))
       
        punch = pygame.image.load(f'images/Personagenspartida/Perssoco{i}.png')
        punch = pygame.transform.scale(side, (DGwidth, DGheight))
       
        kick = pygame.image.load(f'images/Personagenspartida/Perschute{i}.png')
        kick = pygame.transform.scale(side, (DGwidth, DGheight))
       
        dic_pos[i]=[side,punch,kick]


    # Importa imagem de carregamento
    Loadingimage = pygame.image.load('images/LogoTelaCarregamento.png').convert()
    Loadingimagewidth=width/2
    Loadingimageheight=height*(2/3)
    Loadingimage = pygame.transform.scale(Loadingimage, (Loadingimagewidth, Loadingimageheight))
    Loadingimage_rect=Loadingimage.get_rect()
    Loadingimage_rect.center=(width/2,height/2)


    # Cria barra de carregamento
    verticesloadbar1=[(width/4,510*(height/600)),(width/4,525*(height/600)),(3*(width/4),525*(height/600)),(3*(width/4),510*(height/600))]
    colorload1=(255,255,255)
    colorload2=(15,255,3)


    # Fonte "concluído"
    concfont = pygame.font.SysFont(None, 24)
    conctext = concfont.render('Concluído!', True, (255,255,255))
    conctextrect=conctext.get_rect()


    # Gera imagem background
    BGSSimage=pygame.image.load('images/BGtelainicial.png')
    BGSSwidth=width
    BGSSheight=height
    BGSSimage = pygame.transform.scale(BGSSimage, (BGSSwidth, BGSSheight))
    BGSSimage_rect=BGSSimage.get_rect()
    BGSSimage_rect.center=((width/2),(height/2))


    # Importa imagem de carregamento
    Titleimage = pygame.image.load('images/BattlefightersArco.png')
    Titleimagewidth=width/2
    Titleimageheight=height/3
    Titleimage = pygame.transform.scale(Titleimage, (Titleimagewidth, Titleimageheight))
    Titleimage_rect=Titleimage.get_rect()
    Titleimage_rect.center=(width/2,(height/2)-(height/4))


    # Importa Botões de mute e volume
    Muteimage = pygame.image.load('images/mudo.png')
    Volumeimage = pygame.image.load('images/som_ligado.png')


    # Cria botão do play e musica:
    Soundimagewidth = width/12
    Soundimageheight = height/6
    Volumeimage = pygame.transform.scale(Volumeimage, (Soundimagewidth, Soundimageheight))
    Muteimage = pygame.transform.scale(Muteimage, (Soundimagewidth, Soundimageheight))
    Soundimage_rect=Volumeimage.get_rect()
    Soundimage_rect.bottom = window.get_height()
    Soundimage_rect.left = 0


    volume_area=pygame.Rect(0, 5*(height/6), width/12, height/6)
    play_area=pygame.Rect(3*(width/8),(width/8),width/4,height/2)


    Playimage = pygame.image.load('images/botao_play.png')
    Playimagewidth = width/4
    Playimageheight = height/2
    Playimage = pygame.transform.scale(Playimage, (Playimagewidth, Playimageheight))
    Playimage_rect=Playimage.get_rect()
    Playimage_rect.center=((width/2),(height/2))


    # Importa imagem seta
    Arrowimage=pygame.image.load('images/Setavoltar.png')
    Arrowimagewidth=width/16
    Arrowimageheight=height/12
    Arrowimage = pygame.transform.scale(Arrowimage, (Arrowimagewidth, Arrowimageheight))
    Arrowimage_rect=Arrowimage.get_rect()
    Arrowimage_rect.top = 0
    Arrowimage_rect.left = 0
    arrow_area=pygame.Rect(0,0,(width/16),(height/12))


    # Importa imagem de grade de personagens
    Gradeimage=pygame.image.load('images/Gradepersonagens.png')
    Gradeimagewidth=width*(2/3)
    Gradeimageheight=height*(5/6)
    Gradeimage = pygame.transform.scale(Gradeimage, (Gradeimagewidth, Gradeimageheight))
    Gradeimage_rect=Gradeimage.get_rect()
    Gradeimage_rect.center=((width/2),(height/2))


    # Importa imagens de personagens
    Namelist=[]
    Facelist=[]
    face_area_list=[]
    Fullbody_list=[]
    Full_list1={}
    Full_list2={}
    list_characters=['Fred Tio','Alekinho','Baiano','NiGOATlas','Leo messi','J Viddy','Old Serra','Mr Fein','Fogaca','Marcio desoft','Pelicano','Dani Livros','Gabigol','Cauezada','Irmaozin','Ninja 1','Ninja 2','Ninja 3','Gagui','Juba']
    for characters in range(20):
        Characimage = pygame.image.load(f'images/Personagem{characters}.png')
        Fullbody = pygame.image.load(f'images/FullPerson{characters}.png')
        Namelist.append(list_characters[characters])
        Facelist.append(Characimage)
        Fullbody_list.append(Fullbody)


    # Importa imagens de mapas
    maps_list=['Deserto','Vulcão','Montanhas','Floresta','Favela','Aeroporto','Bahia Pirata']
    listahmapa=[470,470,470,470,470,470,470]
    dic_maps={}
    dic_mapsrect={}
    for counter in range(len(maps_list)):
        map=maps_list[counter]
        Mapimage=pygame.image.load(f'images/Mapa{counter}.jpg')
        Mapimagewidth=width
        Mapimageheight=height
        Mapimage = pygame.transform.scale(Mapimage, (Mapimagewidth, Mapimageheight))
        Mapimage_rect=Mapimage.get_rect()
        Mapimage_rect.center=((width/2),(height/2))
        trilha_sonora_mapas = pygame.mixer.Sound(f"trilhas_sonoras/trilhasonoramapa{counter}.mp3")
        dic_maps[map]=(Mapimage, trilha_sonora_mapas)
        dic_mapsrect[map]=Mapimage_rect


    # Nomes, faces e fotos do corpo todo
    Facewidth=width/10
    Faceheight=height/9
    list_facenrect=[]
    list_namenrect=[]
    counter=0
    for heightcount in range(4):
        for Gridcount in range(5):
            Name=Namelist[counter]
            Face=Facelist[counter]
            Full=Fullbody_list[counter]
            counter+=1
            Face = pygame.transform.scale(Face, (Facewidth, Faceheight))
            Face_rect=Face.get_rect()
            Face_rect.center=(((345*(width/1200))+(Gridcount*130)),((187.5*(width/1200))+(heightcount*75)))
            list_facenrect.append([Face,Face_rect])
            face_area=((-Facewidth/2)+((345*(width/1200)))+(Gridcount*130), ((-Faceheight/2)+(187.5*(width/1200))+(heightcount*75)), Facewidth, Faceheight)
            face_area_list.append(face_area)


            persnamefont = pygame.font.SysFont(None, 24)
            Name = persnamefont.render(f'{Name.upper()}', True, (255, 255, 255))
            Name_rect=Name.get_rect()
            Name_rect.center=(((345*(width/1200))+(Gridcount*130)),(-7.5+50+75+100+(heightcount*75)))
            list_namenrect.append([Name,Name_rect])


            Fullwidth=200
            Fullheight=300
            Full = pygame.transform.scale(Full, (Fullwidth, Fullheight))
            Full_rect1=Full.get_rect()
            Full_rect2=Full.get_rect()
            Full_rect1.center=(150,350)
            Full_list1[Full]=Full_rect1
            Full_rect2.center=(1050,350)
            Full_list2[Full]=Full_rect2


    # Carregar a música de fundo
    pygame.mixer.music.load("trilhas_sonoras/trilha_sonora_tela_inicial.mp3")  # Substitua pelo caminho do seu arquivo de música
    pygame.mixer.music.set_volume(0.1)  # Define o volume da música (0.0 a 1.0)
    song1variable=0
    test=0


    # Botão de confirmar
    Confirmb=pygame.image.load('images/Confirmb.png')
    Confirmedb=pygame.image.load('images/Confirmedb.png')
    Confirmbwidth=300
    Confirmbheight=200
    Confirmb1 = pygame.transform.scale(Confirmb, (Confirmbwidth, Confirmbheight))
    Confirmb2 = pygame.transform.scale(Confirmb, (Confirmbwidth, Confirmbheight))
    Confirmedb1 = pygame.transform.scale(Confirmedb, (Confirmbwidth, Confirmbheight))
    Confirmedb2 = pygame.transform.scale(Confirmedb, (Confirmbwidth, Confirmbheight))
    Confirmb1_rect=Confirmb1.get_rect()
    Confirmb2_rect=Confirmb2.get_rect()
    Confirmedb1_rect=Confirmedb1.get_rect()
    Confirmedb2_rect=Confirmedb2.get_rect()


    Confirmb1_rect.left=250
    Confirmb1_rect.top=425
    Confirmedb1_rect.left=250
    Confirmedb1_rect.top=425


    Confirmb2_rect.left=650
    Confirmb2_rect.top=425
    Confirmedb2_rect.left=650
    Confirmedb2_rect.top=425


    Confirmb1_area=pygame.Rect(250,450,300,200)
    Confirmb2_area=pygame.Rect(650,450,300,200)

    mapfont = pygame.font.SysFont(None, 128)
    maptext1 = mapfont.render('Mapa selecionado:', True, (255,255,255))
    text1rect=maptext1.get_rect()
    text1rect.center=(width/2,400)

    # Imagem Versus
    Versus=pygame.image.load('images/Versus.png')
    Versuswidth=300
    Versusheight=200
    Versusrect=Versus.get_rect()
    Versusrect.center=(width/2,height/2)


    # Criar contagem regressiva
    n3 = mapfont.render('3', True, (255,31,45))
    n2 = mapfont.render('2', True, (255,31,45))
    n1 = mapfont.render('1', True, (255,31,45))
    nstart = mapfont.render('Start!', True, (255,31,45))


    nrect=n1.get_rect()
    nsrect=nstart.get_rect()
    nrect.center=(width/2,125)
    nsrect.center=(width/2,125)


    # Cria botão de pausa
    Pauseb=pygame.image.load('images/Botaopausa.png')
    Pausebwidth=width/12
    Pausebheight=height/6
    Pauseb = pygame.transform.scale(Pauseb, (Pausebwidth, Pausebheight))
    Pauseb_rect=Pauseb.get_rect()
    Pauseb_rect.center=(width/2,Pausebheight/2)
    Pause_area=pygame.Rect(550,0,Pausebwidth,Pausebheight)


    # Cria botões da tela de pausa
    vjogo=pygame.image.load('images/Voltjogo.png')
    vjogowidth=width/4
    vjogoheight=height/4
    vjogo = pygame.transform.scale(vjogo, (vjogowidth, vjogoheight))
    vjogo_rect=vjogo.get_rect()
    vjogo_rect.center=(width/2,105)
    vjogo_area=pygame.Rect((width/2)-(vjogowidth/2),105-(vjogoheight/2),vjogowidth,vjogoheight)


    controles=pygame.image.load('images/Controlesb.png')
    controleswidth=width/4
    controlesheight=height/4
    controles = pygame.transform.scale(controles, (controleswidth, controlesheight))
    controles_rect=controles.get_rect()
    controles_rect.center=(width/2,285)
    controles_area=pygame.Rect((width/2)-(controleswidth/2),285-(controlesheight/2),controleswidth,controlesheight)


    # Tela final informações
    resfont=pygame.font.SysFont(None, 128)

    plano_de_fundo_vitoria = pygame.image.load("images/plano_de_fundo_vitoria.jpeg")
    plano_de_fundo_vitoria_width=width
    plano_de_fundo_vitoria_height=height
    plano_de_fundo_vitoria_image = pygame.transform.scale(plano_de_fundo_vitoria, (plano_de_fundo_vitoria_width, plano_de_fundo_vitoria_height))
    plano_de_fundo_vitoria_rect=plano_de_fundo_vitoria_image.get_rect()
    plano_de_fundo_vitoria_rect.center=((width/2),(height/2))

    Jogardenovo=pygame.image.load(f'images/Jogardenovo.png')
    Jogardenovowidth=300
    Jogardenovoheight=150
    Jogardenovo = pygame.transform.scale(Jogardenovo, (Jogardenovowidth, Jogardenovoheight))
    Jogardenovo_rect=Jogardenovo.get_rect()
    Jogardenovo_rect.center=((width/2),(105))
    Jogardenovoarea=pygame.Rect(450,30,300,150)


    Trocarpers=pygame.image.load(f'images/Trocarpers.png')
    Trocarperswidth=300
    Trocarpersheight=150
    Trocarpers = pygame.transform.scale(Trocarpers, (Trocarperswidth, Trocarpersheight))
    Trocarpers_rect=Trocarpers.get_rect()
    Trocarpers_rect.center=((width/2),(285))
    Trocarpersarea=pygame.Rect(450,210,300,150)

    Retmenu=pygame.image.load(f'images/Retmenu.png')
    Retmenuwidth=300
    Retmenuheight=150
    Retmenu = pygame.transform.scale(Retmenu, (Retmenuwidth, Retmenuheight))
    Retmenu_rect=Retmenu.get_rect()
    Retmenu_rect.center=((width/2),(465))
    Retmenu_area=pygame.Rect(450,390,300,150)

# Loop principal
while game:

    clock.tick(FPS)
   
    # Troca tela
    if current_screen == 'tela carregamento':
        frames+=1
        # Trata eventos
        for event in pygame.event.get():
            # Verifica consequências
            if event.type == pygame.QUIT:
                game = False  
        if frames>300:
            current_screen = 'tela inicio'


        # Gera imagem
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
        countloadbar+=3


        # Verifica se atinge limite
        if countloadbar>=width/2:
            window.blit(conctext, ((width/2)-conctextrect[2]/2, 530*(height/600)))

    # Troca tela
    if current_screen == 'tela inicio':
       
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
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    mouse_pos=event.pos
                    if volume_area.collidepoint(mouse_pos):
                        if sound==True:
                            sound=False
                            pygame.mixer.music.set_volume(0)  # Define o volume da música (0.0 a 1.0)
                        else:
                            sound=True
                            pygame.mixer.music.set_volume(0.1)  # Define o volume da música (0.0 a 1.0)


                    if play_area.collidepoint(mouse_pos):
                        imagepers1=False
                        imagepers2=False
                        current_screen='personagens'

    # Troca tela
    if current_screen=='personagens':
        song2variable=0
        if SecScreen>0:
            Fullpicrect1.center=(150,300)
            Fullpicrect2.center=(1050,300)
        frames=0






        # Plota background, grade, personagens, confirmar e seta
        window.blit(BGSSimage, BGSSimage_rect)
        window.blit(Gradeimage, Gradeimage_rect)
        window.blit(Arrowimage, Arrowimage_rect)
       
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

        # Sorteia mapa
        mapnumber=random.randint(0,len(maps_list)-1)


        # Trata eventos
        for event in pygame.event.get():
            # Verifica consequências
            if event.type == pygame.QUIT:
                game = False
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    mouse_pos=event.pos
                    if arrow_area.collidepoint(mouse_pos):
                        current_screen='tela inicio'
                    for countarea in range(len(face_area_list)):
                        face_area=pygame.Rect(face_area_list[countarea])
                        if face_area.collidepoint(mouse_pos):
                            for num,list in dic_pos.items():
                                diccount=0
                                for Fullpic,Fullpicrect in Full_list1.items():
                                    if num==countarea:
                                        if diccount==countarea:
                                            if j1==False:
                                                imagepers1=True
                                                Fullpic1=Fullpic
                                                Fullpicrect1=Fullpicrect
                                                j1_pers=list_characters[diccount]
                                                np1=num
                                        diccount+=1
                                diccount=0
                                for Fullpic,Fullpicrect in Full_list2.items():
                                    if num==countarea:
                                        if diccount==countarea:
                                            if j1==True and j2==False:
                                                imagepers2=True
                                                Fullpic2=Fullpic
                                                Fullpicrect2=Fullpicrect
                                                j2_pers=list_characters[diccount]
                                                np2=num
                                        diccount+=1


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




        if j1 and j2:
            current_screen='tela mapas'
   
    # Troca tela
    if current_screen=='tela mapas':
        frames+=1
        if frames>300:
            current_screen='prepartida'
        j1=False
        j2=False
        counter=0


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


        # Trata eventos
        for event in pygame.event.get():
            # Verifica consequências
            if event.type == pygame.QUIT:
                game = False
   
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


        frames+=1


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