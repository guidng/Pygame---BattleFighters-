import pygame

width=1200
height=600

# Importa imagens de mapas
maps_list=['Deserto','Vulcão','Montanhas','Floresta','Favela','Aeroporto','Baía Pirata','Circo','Bar']
listahmapa=[470,470,470,470,470,470,470,470,470]
dic_maps={}
dic_mapsrect={}
for counter in range(len(maps_list)):
    map=maps_list[counter]
    Mapimage=pygame.image.load(f'images/mapas/Mapa{counter}.jpg')
    Mapimagewidth=width
    Mapimageheight=height
    Mapimage = pygame.transform.scale(Mapimage, (Mapimagewidth, Mapimageheight))
    Mapimage_rect=Mapimage.get_rect()
    Mapimage_rect.center=((width/2),(height/2))
    trilha_sonora_mapas = pygame.mixer.Sound(f"trilhas_sonoras/trilhasonoramapa{counter}.mp3")
    dic_maps[map]=(Mapimage, trilha_sonora_mapas)
    dic_mapsrect[map]=Mapimage_rect


# Carregar a música de fundo
pygame.mixer.music.load("trilhas_sonoras/trilha_sonora_tela_inicial.mp3")  # Substitua pelo caminho do seu arquivo de música
pygame.mixer.music.set_volume(0.1)  # Define o volume da música (0.0 a 1.0)
song1variable=0
test=0


# Criar contagem regressiva
mapfont = pygame.font.SysFont(None, 128)
maptext1 = mapfont.render('Mapa selecionado:', True, (255,255,255))
text1rect=maptext1.get_rect()
text1rect.center=(width/2,400)

n3 = mapfont.render('3', True, (255,31,45))
n2 = mapfont.render('2', True, (255,31,45))
n1 = mapfont.render('1', True, (255,31,45))
nstart = mapfont.render('Start!', True, (255,31,45))


nrect=n1.get_rect()
nsrect=nstart.get_rect()
nrect.center=(width/2,125)
nsrect.center=(width/2,125)