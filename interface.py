# Iniciando jogo
import pygame
pygame.init()
current_screen='tela carregamento'

# Importando outras janelas
from imports import *
from funcoes import *

game=True
clock = pygame.time.Clock()
FPS=60
clock.tick(FPS)

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
        frames,current_screen,game,current_map,current_map_image,current_map_rect,atual_TS,mapnumber = tela_mapas()

    # Troca tela
    if current_screen=='prepartida':
        current_screen,game = prepartida(current_map_image,current_map_rect,Fullpicrect1,Fullpicrect2,Fullpic1,Fullpic2)

    # Troca tela
    if current_screen=='partida':
        current_screen,game,hp1,hp2,song2variable,SecScreen,counting = partida(mapnumber,current_map_image,current_map_rect,np1,np2)

    # Troca tela
    if current_screen=='Jogo pausado':
        current_screen,game = jogo_pausado(current_map_image,current_map_rect,atual_TS)

    # Troca tela
    if current_screen=='controles':
        current_screen,game = controles(current_map_image,current_map_rect)

    # Troca tela
    if current_screen=='Fim de jogo':
        current_screen,game,jw,jwin,j1_wins,j2_wins=fimdejogo(current_map_image,current_map_rect,hp1,hp2,j1_pers,j2_pers,Fullpic1,Fullpic2)

    # Troca tela
    if current_screen=='Opções pós jogo':
        current_screen,game=opcoespj(current_map,current_map_rect,atual_TS)
        
    pygame.display.update()  # Mostra o novo frame para o jogador

# Finalização
pygame.quit()  # Função do PyGame que  finaliza os recursos utilizados