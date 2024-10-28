# Importa e inicia pacotes
import pygame
pygame.init()

# Gera tela principal
window = pygame.display.set_mode((1200, 600))
pygame.display.set_caption('Battlefighters ⚔️')

# Inicia estruturas de dados
game = True

# Loop principal
while game:
    # Trata eventos
    for event in pygame.event.get():
        # Verifica consequências
        if event.type == pygame.QUIT:
            game = False
    # Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor preta

    # Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# Finalização
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados