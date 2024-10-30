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
frames=0
tela_atual='tela carregamento'
clock = pygame.time.Clock()
FPS=60
countloadbar=0

# Loop principal
while game:

    clock.tick(FPS)

    if tela_atual == 'tela carregamento':
        frames+=1
        # Trata eventos
        for event in pygame.event.get():
            # Verifica consequências
            if event.type == pygame.QUIT:
                game = False   
        if frames>300:
            tela_atual = 'tela inicio'

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
    
    if tela_atual == 'tela inicio':
        # Trata eventos
        for event in pygame.event.get():
            # Verifica consequências
            if event.type == pygame.QUIT:
                game = False

        # Gera imagem
        window.fill((135,206,250))  # Preenche o fundo com a cor azul




    # Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# Finalização
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados