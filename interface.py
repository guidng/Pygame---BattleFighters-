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

# Importa imagens do jogo:
dic_pos={}
for i in range(20):
    DGwidth=50
    DGheight=75
    side = pygame.image.load(f'images/Personagenspartida/Perslado{i}.png')
    side = pygame.transform.scale(side, (DGwidth, DGheight))
    
    punch = pygame.image.load(f'images/Personagenspartida/Perssoco{i}.png')
    punch = pygame.transform.scale(side, (DGwidth, DGheight))
    
    kick = pygame.image.load(f'images/Personagenspartida/Perschute{i}.png')
    kick = pygame.transform.scale(side, (DGwidth, DGheight))
    
    dic_pos[i]=[side,punch,kick]


# Importa imagens de personagens
Namelist=[]
Facelist=[]
area_list=[]
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
maps_list=['Deserto','Vulcão','Montanhas','Estádio','Floresta','Favela']
dic_maps={}
dic_mapsrect={}
for counter in range(len(maps_list)):
    map=maps_list[counter]
    BGSSimage=pygame.image.load(f'images/Mapa{counter}.jpg')
    BGSSwidth=1200
    BGSSheight=600
    BGSSimage = pygame.transform.scale(BGSSimage, (BGSSwidth, BGSSheight))
    BGSSimage_rect=BGSSimage.get_rect()
    BGSSimage_rect.center=((width/2),(height/2))
    trilha_sonora_mapas = pygame.mixer.Sound(f"trilhas_sonoras/trilhasonoramapa{counter}.mp3")
    dic_maps[map]=(BGSSimage, trilha_sonora_mapas)
    dic_mapsrect[map]=BGSSimage_rect

# Carregar a música de fundo
pygame.mixer.music.load("trilhas_sonoras/trilha_sonora_tela_inicial.mp3")  # Substitua pelo caminho do seu arquivo de música
pygame.mixer.music.set_volume(0.1)  # Define o volume da música (0.0 a 1.0) 
song1variable=0

test=0
# Loop principal
while game:

    clock.tick(FPS)
    
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

        # Importa imagem de carregamento
        Loadingimage = pygame.image.load('images/LogoTelaCarregamento.png').convert()
        Loadingimagewidth=600
        Loadingimageheight=400
        Loadingimage = pygame.transform.scale(Loadingimage, (Loadingimagewidth, Loadingimageheight))
        Loadingimage_rect=Loadingimage.get_rect()
        Loadingimage_rect.center=(width/2,height/2)
        window.blit(Loadingimage, Loadingimage_rect)

        # Cria barra de carregamento
        verticesloadbar1=[(300,510),(300,525),(900,525),(900,510)]
        colorload1=(255,255,255)
        pygame.draw.polygon(window, colorload1, verticesloadbar1)
        verticesloadbar2=[(300,510),(300,525),(300+countloadbar,525),(300+countloadbar,510)]
        colorload2=(15,255,3)

        # Verifica se ultrapassa limite
        if countloadbar+300<900:
            pygame.draw.polygon(window, colorload2, verticesloadbar2)
        else:
            verticesloadbar2=[(300,510),(300,525),(900,525),(900,510)]
            colorload2=(15,255,3)
            pygame.draw.polygon(window, colorload2, verticesloadbar2)
        countloadbar+=3

        # Verifica se atinge limite
        if countloadbar>=600:
            font = pygame.font.SysFont(None, 24)
            text = font.render('Concluído!', True, (255,255,255))
            textrect=text.get_rect()
            window.blit(text, (600-textrect[2]/2, 530))


    # Troca tela
    if current_screen == 'tela inicio':
        
        # Da play na musica em loop
        if song1variable==0:
            pygame.mixer.music.play(-1,2)
        song1variable+=1

        # Gera imagem
        BGSSimage=pygame.image.load('images/BGtelainicial.png')
        BGSSwidth=1200
        BGSSheight=600
        BGSSimage = pygame.transform.scale(BGSSimage, (BGSSwidth, BGSSheight))
        BGSSimage_rect=BGSSimage.get_rect()
        BGSSimage_rect.center=((width/2),(height/2))
        window.blit(BGSSimage, BGSSimage_rect)

        # Importa imagem de carregamento
        Arcimage = pygame.image.load('images/BattlefightersArco.png')
        Arcimagewidth=600
        Arcimageheight=200
        Arcimage = pygame.transform.scale(Arcimage, (Arcimagewidth, Arcimageheight))
        Arcimage_rect=Arcimage.get_rect()
        Arcimage_rect.center=(width/2,(height/2)-150)
        window.blit(Arcimage, Arcimage_rect)

        
        
        # Importa Botões:
        Muteimage = pygame.image.load('images/mudo.png')
        Volumeimage = pygame.image.load('images/som_ligado.png')
        if sound==False:
            Soundimage=Muteimage
        else:
            Soundimage=Volumeimage
        
        # Cria botão do play e musica:

        Soundimagewidth = 100
        Soundimageheight = 100
        Soundimage = pygame.transform.scale(Soundimage, (Soundimagewidth, Soundimageheight))
        Soundimage_rect=Soundimage.get_rect()
        Soundimage_rect.bottom = window.get_height()
        Soundimage_rect.left = 0
        window.blit(Soundimage, Soundimage_rect)

        Playimage = pygame.image.load('images/botao_play.png')
        Playimagewidth = 300
        Playimageheight = 300
        Playimage = pygame.transform.scale(Playimage, (Playimagewidth, Playimageheight))
        Playimage_rect=Playimage.get_rect()
        Playimage_rect.center=((width/2),(height/2))
        window.blit(Playimage, Playimage_rect)

        # Trata eventos
        for event in pygame.event.get():
            # Verifica consequências
            if event.type == pygame.QUIT:
                game = False
            volume_area=pygame.Rect(0, height-100, 100, 100)
            play_area=pygame.Rect(450,150,300,300)

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
                        current_screen='modo de jogo'


    # Troca tela 
    if current_screen=='modo de jogo':
        window.blit(BGSSimage, BGSSimage_rect)
        
        # Importa imagens
        Arrowimage=pygame.image.load('images/Setavoltar.png')
        Arrowimagewidth=75
        Arrowimageheight=50
        Arrowimage = pygame.transform.scale(Arrowimage, (Arrowimagewidth, Arrowimageheight))
        Arrowimage_rect=Arrowimage.get_rect()
        Arrowimage_rect.top = 0
        Arrowimage_rect.left = 0
        window.blit(Arrowimage, Arrowimage_rect)

        x1image=pygame.image.load('images/1v1.png')
        x1imagewidth=250
        x1imageheight=250
        x1image = pygame.transform.scale(x1image, (x1imagewidth, x1imageheight))
        x1image_rect=x1image.get_rect()
        x1image_rect.center=((width/2)-150,(height/2))
        window.blit(x1image, x1image_rect)

        Arcadeimage=pygame.image.load('images/Arcade.png')
        Arcadeimagewidth=250
        Arcadeimageheight=250
        Arcadeimage = pygame.transform.scale(Arcadeimage, (Arcadeimagewidth, Arcadeimageheight))
        Arcadeimage_rect=Arcadeimage.get_rect()
        Arcadeimage_rect.center=((width/2)+150,(height/2))
        window.blit(Arcadeimage, Arcadeimage_rect)
    
        # Define areas
        x1_area=pygame.Rect(((width/2))-(x1imagewidth/2)-150,(height/2)-(x1imageheight/2),200,200)
        Arcade_area=pygame.Rect(((width/2))-(Arcadeimagewidth/2)+150,(height/2)-(Arcadeimageheight/2),200,200)
        arrow_area=pygame.Rect(0,0,75,50)

        for event in pygame.event.get():
            # Verifica consequências
            if event.type == pygame.QUIT:
                game = False
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    mouse_pos=event.pos
                    if arrow_area.collidepoint(mouse_pos):
                        current_screen='tela inicio'
                    if x1_area.collidepoint(mouse_pos):
                        current_screen='personagens'
                        currentmode='1v1'
                    if Arcade_area.collidepoint(mouse_pos):
                        current_screen='personagens'
                        currentmode='arcade'

        # Cria variáveis de imagem
        imagepers1=False
        imagepers2=False

    # Troca tela
    if current_screen=='personagens':
        gagui=0
        if SecScreen>0:
            second1.center=(150,300)
            second2.center=(1050,300)
        frames=0

        # Plota Bg
        window.blit(BGSSimage, BGSSimage_rect)

        # Importa imagens
        Gradeimage=pygame.image.load('images/Gradepersonagens.png')
        Gradeimagewidth=800
        Gradeimageheight=500
        Gradeimage = pygame.transform.scale(Gradeimage, (Gradeimagewidth, Gradeimageheight))
        Gradeimage_rect=Gradeimage.get_rect()
        Gradeimage_rect.center=((width/2),(height/2))
        window.blit(Gradeimage, Gradeimage_rect)
        window.blit(Arrowimage, Arrowimage_rect)

        # Nomes, faces e fotos do corpo todo
        counter=0
        for heightcount in range(4):
            for Gridcount in range(5):
                Name=Namelist[counter]
                Face=Facelist[counter]
                Full=Fullbody_list[counter]
                counter+=1
                Facewidth=120
                Faceheight=75
                Face = pygame.transform.scale(Face, (Facewidth, Faceheight))
                Face_rect=Face.get_rect()
                Face_rect.center=((200+60+85+(Gridcount*130)),(50+37.5+100+(heightcount*75)))
                window.blit(Face, Face_rect)
                current_area=((-Facewidth/2)+200+60+85+(Gridcount*130), ((-Faceheight/2)+50+37.5+100+(heightcount*75)), Facewidth, Faceheight)
                if len(area_list)<20:
                    area_list.append(current_area)

                font = pygame.font.SysFont(None, 24)
                Name = font.render(f'{Name.upper()}', True, (255, 255, 255))
                Name_rect=Name.get_rect()
                Name_rect.center=((200+85+60+(Gridcount*130)),(-7.5+50+75+100+(heightcount*75)))
                window.blit(Name, Name_rect)

                Fullwidth=300
                Fullheight=500
                Full = pygame.transform.scale(Full, (Fullwidth, Fullheight))
                Full_rect1=Full.get_rect()
                Full_rect2=Full.get_rect()
                Full_rect1.center=(125,300)
                Full_list1[Full]=Full_rect1
                Full_rect2.center=(1075,300)
                Full_list2[Full]=Full_rect2

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
        
        if j1==False:
            window.blit(Confirmb1, Confirmb1_rect)
        else:
            window.blit(Confirmedb1, Confirmedb1_rect)
        if j2==False:
            window.blit(Confirmb2, Confirmb2_rect)
        else:
            window.blit(Confirmedb2, Confirmedb2_rect)

        if imagepers1==True:
            window.blit(first1, second1)

        if imagepers2==True:
            window.blit(first2, second2)

        Confirmb1_area=pygame.Rect(250,450,300,200)
        Confirmb2_area=pygame.Rect(650,450,300,200)

        number=random.randint(0,5)
        #number=3

        for event in pygame.event.get():
            # Verifica consequências
            if event.type == pygame.QUIT:
                game = False
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    mouse_pos=event.pos
                    if arrow_area.collidepoint(mouse_pos):
                        current_screen='modo de jogo'
                    for countarea in range(len(area_list)):
                        current_area=pygame.Rect(area_list[countarea])
                        if current_area.collidepoint(mouse_pos):
                            for num,list in dic_pos.items():
                                diccount=0
                                for firs,secon in Full_list1.items():
                                    if num==countarea:
                                        if diccount==countarea:
                                            if j1==False:
                                                imagepers1=True
                                                first1=firs
                                                second1=secon
                                                j1_pers=list_characters[diccount]
                                                list_p1pos=list
                                        diccount+=1
                                diccount=0
                                for firs,secon in Full_list2.items():
                                    if num==countarea:
                                        if diccount==countarea:
                                            if j1==True and j2==False:
                                                imagepers2=True
                                                first2=firs
                                                second2=secon
                                                j2_pers=list_characters[diccount]
                                                list_p2pos=list
                                        diccount+=1

                    if Confirmb1_area.collidepoint(mouse_pos):
                        if j1==False:
                            j1=True
                        else:
                            j1=False
                    if Confirmb2_area.collidepoint(mouse_pos):
                        if j2==False and j1==True:
                            j2=True
        if j1 and j2:
            current_screen='tela mapas'
    
    if current_screen=='tela mapas':
        frames+=1
        if frames>300:
            current_screen='prepartida'
        j1=False
        j2=False
        counter=0
        for map,(image, trilha_sonora_mapas) in dic_maps.items():
            for map1,rect in dic_mapsrect.items():
                if map==map1:
                    if counter==number:
                        current_map=map
                        current_map_image=image
                        current_map_rect=rect
                        window.blit(image, rect)
                        font = pygame.font.SysFont(None, 128)
                        text1 = font.render('Mapa selecionado:', True, (255,255,255))
                        text2= font.render(f'{map}', True, (255,255,255))
                        text1rect=text1.get_rect()
                        text2rect=text2.get_rect()
                        text1rect.center=(width/2,400)
                        text2rect.center=(width/2,500)
                        window.blit(text1, text1rect)
                        window.blit(text2, text2rect)
                        pygame.mixer.music.stop()  # Para a música anterior
                        trilha_sonora_mapas.set_volume(0.1) # Aumentar volume da música de batalha
                        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)  # Ajuste conforme necessário
                        if gagui==0:
                            trilha_sonora_mapas.play(-1)  # Toca a música da batalha em loop
                        gagui += 1 

                    counter+=1

        window.blit(Arrowimage, Arrowimage_rect)

        for event in pygame.event.get():
            # Verifica consequências
            if event.type == pygame.QUIT:
                game = False
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    mouse_pos=event.pos
                    if arrow_area.collidepoint(mouse_pos):
                        current_screen='personagens'
    
    pygame.display.update()  # Mostra o novo frame para o jogador
 
    if current_screen=='prepartida':
        gagui=0
        SecScreen=1
        counting=0
        hp1=100
        hp2=100
        Px1_pos=100
        Px2_pos=1100

        if number==3:
            Py1_pos=470
            Py2_pos=470
        
        frames+=1
        seconds=0
        window.blit(current_map_image,current_map_rect)
        second1.center=(300,300)
        second2.center=(900,300)
        window.blit(first1, second1)
        window.blit(first2, second2)
        Versus=pygame.image.load('images/Versus.png')
        Versuswidth=300
        Versusheight=200
        Versusrect=Versus.get_rect()
        Versusrect.center=(width/2,height/2)
        window.blit(Versus,Versusrect)
        if frames>300 and frames<360:
            n3 = font.render('3', True, (255,31,45))
            n3rect=n3.get_rect()
            n3rect.center=(width/2,100)
            window.blit(n3, n3rect)
        if frames>=360 and frames<420:
            n2 = font.render('2', True, (255,31,45))
            n2rect=n2.get_rect()
            n2rect.center=(width/2,100)
            window.blit(n2, n2rect)
        if frames>=420 and frames<480:
            n1 = font.render('1', True, (255,31,45))
            n1rect=n1.get_rect()
            n1rect.center=(width/2,100)
            window.blit(n1, n1rect)
        if frames>=480 and frames<540:
            nstart = font.render('Start!', True, (255,31,45))
            nstartrect=nstart.get_rect()
            nstartrect.center=(width/2,100)
            window.blit(nstart, nstartrect)
        if frames>=540:
            current_screen='partida'
            atual_pos=0
        for event in pygame.event.get():
            # Verifica consequências
            if event.type == pygame.QUIT:
                game = False

    if current_screen=='partida':
        frames=0
        limit=0
        window.blit(current_map_image,current_map_rect)
        if hp1==0 or hp2==0:
            current_screen='Fim de jogo'
        if seconds>120:
            current_screen='Fim de jogo'
        seconds+=1/60

        mov1=list_p1pos[atual_pos]
        mov2=list_p2pos[atual_pos]

        rect1=mov1.get_rect()
        rect2=mov2.get_rect()

        rect1.center=(Px1_pos,Py1_pos)
        rect2.center=(Px2_pos,Py2_pos)

        window.blit(mov1,rect1)
        window.blit(mov2,rect2)

        for event in pygame.event.get():
            # Verifica consequências
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    Px1_pos-=1
                if event.key == pygame.K_d:
                    Px1_pos+=1

    if current_screen=='Fim de jogo':
        frames+=1
        window.blit(current_map_image,current_map_rect)
        hp1=0
        if limit==0:
            if hp2>hp1:
                res = font.render(f'{j2_pers} wins!', True, (255,255,255))
                resrect=res.get_rect()
                resrect.center=(width/2,height/2)
                jw=first2
                jwin=j2_pers
                j2_wins+=1

            elif hp1>hp2:
                res = font.render(f'{j1_pers} wins!', True, (255,255,255))
                resrect=res.get_rect()
                resrect.center=(width/2,height/2)
                jw=first1
                jwin=j1_pers
                j1_wins+=1
            
            elif hp1==hp2:
                camp=random.randint(1,2)
                if camp==1:
                    res = font.render(f'{j1_pers} wins!', True, (255,255,255))
                    resrect=res.get_rect()
                    resrect.center=(width/2,height/2)
                    jw=first1
                    jwin=j1_pers
                    j1_wins+=1
                else:
                    res = font.render(f'{j2_pers} wins!', True, (255,255,255))
                    resrect=res.get_rect()
                    resrect.center=(width/2,height/2)
                    jw=first2
                    jwin=j2_pers
                    j2_wins+=1


        limit+=1

        window.blit(res,resrect)
        
        if frames>240:
            current_screen='Opções pós jogo'

        for event in pygame.event.get():
            # Verifica consequências
            if event.type == pygame.QUIT:
                game = False

    if current_screen=='Opções pós jogo':
        imagepers1=False
        imagepers2=False

        window.fill((0,0,0))
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
        font = pygame.font.SysFont(None, 48)
        maptext = font.render(f'{current_map}', True, (255,255,255))
        maptextrect=maptext.get_rect()
        maptextrect.center=(1000,250)
        window.blit(maptext, maptextrect)

        Jogardenovo=pygame.image.load(f'images/Jogardenovo.png')
        Jogardenovowidth=300
        Jogardenovoheight=150
        Jogardenovo = pygame.transform.scale(Jogardenovo, (Jogardenovowidth, Jogardenovoheight))
        Jogardenovo_rect=Jogardenovo.get_rect()
        Jogardenovo_rect.center=((width/2),(105))
        Jogardenovoarea=pygame.Rect(450,30,300,150)
        window.blit(Jogardenovo,Jogardenovo_rect)
    
        Trocarpers=pygame.image.load(f'images/Trocarpers.png')
        Trocarperswidth=300
        Trocarpersheight=150
        Trocarpers = pygame.transform.scale(Trocarpers, (Trocarperswidth, Trocarpersheight))
        Trocarpers_rect=Trocarpers.get_rect()
        Trocarpers_rect.center=((width/2),(285))
        Trocarpersarea=pygame.Rect(450,210,300,150)
        window.blit(Trocarpers,Trocarpers_rect)

        Retmenu=pygame.image.load(f'images/Retmenu.png')
        Retmenuwidth=300
        Retmenuheight=150
        Retmenu = pygame.transform.scale(Retmenu, (Retmenuwidth, Retmenuheight))
        Retmenu_rect=Retmenu.get_rect()
        Retmenu_rect.center=((width/2),(465))
        Retmenuarea=pygame.Rect(450,390,300,150)
        window.blit(Retmenu,Retmenu_rect)

        font = pygame.font.SysFont(None, 60)
        P1wins = font.render(f'Player 1: {j1_wins} W', True, (255,255,255))
        P1winsrect=P1wins.get_rect()
        P1winsrect.center=(1000,375)
        window.blit(P1wins, P1winsrect)

        P2wins = font.render(f'Player 2: {j2_wins} W', True, (255,255,255))
        P2winsrect=P1wins.get_rect()
        P2winsrect.center=(1000,475)
        window.blit(P2wins, P2winsrect)
        
        for event in pygame.event.get():
            # Verifica consequências
            if event.type == pygame.QUIT:
                game = False
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    mouse_pos=event.pos
                    if Retmenuarea.collidepoint(mouse_pos):
                        current_screen='tela inicio'
                    if Trocarpersarea.collidepoint(mouse_pos):
                        current_screen='personagens'
                    if Jogardenovoarea.collidepoint(mouse_pos):
                        current_screen='tela mapas'


# Finalização
pygame.quit()  # Função do PyGame que  finaliza os recursos utilizados