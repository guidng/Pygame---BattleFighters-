from imports import *

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

        # Roda eventos
        for event in pygame.event.get():
            # Verifica consequências
            if event.type == pygame.QUIT:
                game = False

    return current_screen,game