# Importa e inicia pacotes
import pygame
pygame.init()

# Gera tela principal
width=1200
height=600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Battlefighters ⚔️')

# Inicia estruturas de dados
game = True
sound = True
frames=0
current_screen='tela carregamento'
clock = pygame.time.Clock()
FPS=60
countloadbar=0

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
        if countloadbar+300<900:
            pygame.draw.polygon(window, colorload2, verticesloadbar2)
        else:
            verticesloadbar2=[(300,510),(300,525),(900,525),(900,510)]
            colorload2=(15,255,3)
            pygame.draw.polygon(window, colorload2, verticesloadbar2)
        countloadbar+=3

        if countloadbar>=600:
            font = pygame.font.SysFont(None, 24)
            text = font.render('Concluído!', True, (255,255,255))
            textrect=text.get_rect()
            window.blit(text, (600-textrect[2]/2, 530))


    if current_screen == 'tela inicio':
        # Trata eventos
        for event in pygame.event.get():
            # Verifica consequências
            if event.type == pygame.QUIT:
                game = False

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

        # Cria botão do play e musica:
        # Cria círculo
        radiusplayb=50
        centerplayb=((width/2)-100,(height/2)+70)
        colorplayb=(214,217,54)
        pygame.draw.circle(window, colorplayb, centerplayb, radiusplayb)
        radiussetb=50
        centersetb=((width/2)+100,(height/2)+70)
        colorsetb=(214,217,54)
        pygame.draw.circle(window, colorsetb, centersetb, radiussetb) 
        
        # Importa Botões:
        Muteimage = pygame.image.load('images/BotaoMute.png')
        Volumeimage = pygame.image.load('images/Botaovolume.png')
        if sound==False:
            Soundimage=Muteimage
        else:
            Soundimage=Volumeimage
        # if CLICARBOTAODIREITO:
        #     if sound==False:
        #         sound=True
        #     else:
        #         sound=False
         
        Soundimagewidth = 100
        Soundimageheight = 100
        Soundimage = pygame.transform.scale(Soundimage, (Soundimagewidth, Soundimageheight))
        Soundimage_rect=Soundimage.get_rect()
        Soundimage_rect.center=(centersetb)
        window.blit(Soundimage, Soundimage_rect)

        Playimage = pygame.image.load('images/Botaoplay.png')
        Playimagewidth = 70
        Playimageheight = 70
        Playimage = pygame.transform.scale(Playimage, (Playimagewidth, Playimageheight))
        Playimage_rect=Playimage.get_rect()
        Playimage_rect.center=((width/2)-98,(height/2)+70)
        window.blit(Playimage, Playimage_rect)

        # confere se botão do volume foi apertado 

    # Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# Finalização
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
