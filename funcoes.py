from imports import *
import random

# Iniciando estruturas de dados
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Battlefighters ⚔️')
clock = pygame.time.Clock()
game = True

# Tela de carregamento
def tela_carregamento():

    # Define variáveis
    frames=0
    countloadbar=0
    current_screen='tela carregamento'
    game=True

    # Inicia Loop
    while current_screen=='tela carregamento' and game==True:        
        
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
        
        # Atualiza variáveis
        frames+=1
        countloadbar+=2

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
def tela_inicio():
    
    # Definindo variáveis
    current_screen='tela inicio'
    game=True
    sound=True
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
                        current_screen='personagens'
                        
        pygame.display.update()  # Mostra o novo frame para o jogador

    return current_screen,game

# Grade de Personagens
def personagens():

    # Definindo variáveis
    current_screen='personagens'
    game=True
    imagepers1=False
    imagepers2=False
    j1=False
    j2=False

    # Iniciando Loop
    while current_screen=='personagens':


        if SecScreen>0:
            Fullpicrect1.center=(150,300)
            Fullpicrect2.center=(1050,300)

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

        pygame.display.update()  # Mostra o novo frame para o jogador
    return current_screen,game,Fullpic1,Fullpic2,Fullpicrect1,Fullpicrect2,np1,np2,j1_pers,j2_pers