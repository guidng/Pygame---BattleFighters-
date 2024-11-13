import pygame

width=1200
height=600

# Importa Botões de mute e volume
Muteimage = pygame.image.load('images/botoes/mudo.png')
Volumeimage = pygame.image.load('images/botoes/som_ligado.png')


# Cria botão do play e musica:
Soundimagewidth = width/12
Soundimageheight = height/6
Volumeimage = pygame.transform.scale(Volumeimage, (Soundimagewidth, Soundimageheight))
Muteimage = pygame.transform.scale(Muteimage, (Soundimagewidth, Soundimageheight))
Soundimage_rect=Volumeimage.get_rect()
Soundimage_rect.bottom = height
Soundimage_rect.left = 0


volume_area=pygame.Rect(0, 5*(height/6), width/12, height/6)
play_area=pygame.Rect(3*(width/8),(width/8),width/4,height/2)


Playimage = pygame.image.load('images/botoes/botao_play.png')
Playimagewidth = width/4
Playimageheight = height/2
Playimage = pygame.transform.scale(Playimage, (Playimagewidth, Playimageheight))
Playimage_rect=Playimage.get_rect()
Playimage_rect.center=((width/2),(height/2))


# Importa imagem seta
Arrowimage=pygame.image.load('images/botoes/Setavoltar.png')
Arrowimagewidth=width/16
Arrowimageheight=height/12
Arrowimage = pygame.transform.scale(Arrowimage, (Arrowimagewidth, Arrowimageheight))
Arrowimage_rect=Arrowimage.get_rect()
Arrowimage_rect.top = 0
Arrowimage_rect.left = 0
arrow_area=pygame.Rect(0,0,(width/16),(height/12))


# Botão de confirmar
Confirmb=pygame.image.load('images/botoes/Confirmb.png')
Confirmedb=pygame.image.load('images/botoes/Confirmedb.png')
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


# Cria botão de pausa
Pauseb=pygame.image.load('images/botoes/Botaopausa.png')
Pausebwidth=width/12
Pausebheight=height/6
Pauseb = pygame.transform.scale(Pauseb, (Pausebwidth, Pausebheight))
Pauseb_rect=Pauseb.get_rect()
Pauseb_rect.center=(width/2,Pausebheight/2)
Pause_area=pygame.Rect(550,0,Pausebwidth,Pausebheight)


# Cria botões da tela de pausa
vjogo=pygame.image.load('images/botoes/Voltjogo.png')
vjogowidth=width/4
vjogoheight=height/4
vjogo = pygame.transform.scale(vjogo, (vjogowidth, vjogoheight))
vjogo_rect=vjogo.get_rect()
vjogo_rect.center=(width/2,105)
vjogo_area=pygame.Rect((width/2)-(vjogowidth/2),105-(vjogoheight/2),vjogowidth,vjogoheight)


controles=pygame.image.load('images/botoes/Controlesb.png')
controleswidth=width/4
controlesheight=height/4
controles = pygame.transform.scale(controles, (controleswidth, controlesheight))
controles_rect=controles.get_rect()
controles_rect.center=(width/2,285)
controles_area=pygame.Rect((width/2)-(controleswidth/2),285-(controlesheight/2),controleswidth,controlesheight)


# Tela final informações
resfont=pygame.font.SysFont(None, 128)

# Jogar de novo
Jogardenovo=pygame.image.load(f'images/botoes/Jogardenovo.png')
Jogardenovowidth=300
Jogardenovoheight=150
Jogardenovo = pygame.transform.scale(Jogardenovo, (Jogardenovowidth, Jogardenovoheight))
Jogardenovo_rect=Jogardenovo.get_rect()
Jogardenovo_rect.center=((width/2),(105))
Jogardenovoarea=pygame.Rect(450,30,300,150)


# Trocar personagem
Trocarpers=pygame.image.load(f'images/botoes/Trocarpers.png')
Trocarperswidth=300
Trocarpersheight=150
Trocarpers = pygame.transform.scale(Trocarpers, (Trocarperswidth, Trocarpersheight))
Trocarpers_rect=Trocarpers.get_rect()
Trocarpers_rect.center=((width/2),(285))
Trocarpersarea=pygame.Rect(450,210,300,150)


# Retornar ao menu
Retmenu=pygame.image.load(f'images/botoes/Retmenu.png')
Retmenuwidth=300
Retmenuheight=150
Retmenu = pygame.transform.scale(Retmenu, (Retmenuwidth, Retmenuheight))
Retmenu_rect=Retmenu.get_rect()
Retmenu_rect.center=((width/2),(465))
Retmenu_area=pygame.Rect(450,390,300,150)