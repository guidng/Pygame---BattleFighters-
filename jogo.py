# Iniciando jogo
import pygame
pygame.init()
pygame.joystick.init()
# configurações dos controles 
joysticks = []
for i in range(pygame.joystick.get_count()):
    joystick = pygame.joystick.Joystick(i)
    joystick.init()
    joysticks.append(joystick)
acoes =['pulo', 'ANALOGesquerda', 'soco', 'chute']
calibracao = {} 
if pygame.joystick.get_count()>0:
    for n in range(pygame.joystick.get_count()):
        calibracao[f'player{n}'] = {}
    for player, controles in calibracao.items():
        for acao in acoes:
            print(f"{player} - Pressione o botão ou mova o eixo para '{acao}'...")

            mapeado = False
            while not mapeado:
                for event in pygame.event.get():
                    # Botões
                    if event.type == pygame.JOYBUTTONDOWN and event.instance_id == list(calibracao.keys()).index(player):
                        controles[acao] = ("botao", event.button)
                        print(f"{acao} mapeado para botão {event.button}")
                        mapeado = True
                    elif event.type == pygame.JOYAXISMOTION and acao == 'ANALOGesquerda' and event.instance_id == list(calibracao.keys()).index(player):
                        if abs(event.value) > 0.5:  # Evita leituras não intencionais de eixos neutros
                            controles[acao] = ("eixo", event.axis, event.value)
                            print(f"{acao} mapeado para eixo {event.axis} com direção {'positiva' if event.value > 0 else 'negativa'}")
                            mapeado = True

            pygame.time.delay(2000)
    print(calibracao)
current_screen='tela carregamento'


# Importando outras janelas
from imports import *
from funcoes import *

game=True
sound2=True
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
        current_screen,game,Soundimage,sound = tela_inicio(sound)

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
        current_screen,game,hp1,hp2,song2variable,SecScreen,counting = partida(mapnumber,current_map_image,current_map_rect,np1,np2,calibracao)

    # Troca tela
    if current_screen=='Jogo pausado':
        current_screen,game,sound2 = jogo_pausado(current_map_image,current_map_rect,atual_TS,sound2)

    # Troca tela
    if current_screen=='controles':
        current_screen,game,sound2 = fcontroles(current_map_image,current_map_rect,sound2)

    # Troca tela
    if current_screen=='Fim de jogo':
        current_screen,game,jw,jwin,j1_wins,j2_wins=fimdejogo(current_map_image,current_map_rect,hp1,hp2,j1_pers,j2_pers,Fullpic1,Fullpic2,j1_wins,j2_wins)

    # Troca tela
    if current_screen=='Opções pós jogo':
        current_screen,game=opcoespj(current_map,current_map_image,atual_TS,jw,j1_wins,j2_wins)
        
    pygame.display.update()  # Mostra o novo frame para o jogador

# Finalização
pygame.quit()  # Função do PyGame que  finaliza os recursos utilizados