import pygame

width=1200
height=600

# Importa imagem de carregamento
Loadingimage = pygame.image.load('images/LogoTelaCarregamento.png')
Loadingimagewidth=width/2
Loadingimageheight=height*(2/3)
Loadingimage = pygame.transform.scale(Loadingimage, (Loadingimagewidth, Loadingimageheight))
Loadingimage_rect=Loadingimage.get_rect()
Loadingimage_rect.center=(width/2,height/2)


# Cria barra de carregamento
verticesloadbar1=[(width/4,510*(height/600)),(width/4,525*(height/600)),(3*(width/4),525*(height/600)),(3*(width/4),510*(height/600))]
colorload1=(255,255,255)
colorload2=(15,255,3)


# Fonte "concluído"
concfont = pygame.font.SysFont(None, 24)
conctext = concfont.render('Concluído!', True, (255,255,255))
conctextrect=conctext.get_rect()


# Gera imagem background
BGSSimage=pygame.image.load('images/BGtelainicial.png')
BGSSwidth=width
BGSSheight=height
BGSSimage = pygame.transform.scale(BGSSimage, (BGSSwidth, BGSSheight))
BGSSimage_rect=BGSSimage.get_rect()
BGSSimage_rect.center=((width/2),(height/2))


# Importa imagem de carregamento
Titleimage = pygame.image.load('images/BattlefightersArco.png')
Titleimagewidth=width/2
Titleimageheight=height/3
Titleimage = pygame.transform.scale(Titleimage, (Titleimagewidth, Titleimageheight))
Titleimage_rect=Titleimage.get_rect()
Titleimage_rect.center=(width/2,(height/2)-(height/4))


# Importa imagem de grade de personagens
Gradeimage=pygame.image.load('images/Gradepersonagens.png')
Gradeimagewidth=width*(2/3)
Gradeimageheight=height*(5/6)
Gradeimage = pygame.transform.scale(Gradeimage, (Gradeimagewidth, Gradeimageheight))
Gradeimage_rect=Gradeimage.get_rect()
Gradeimage_rect.center=((width/2),(height/2))


# Imagem Versus
Versus=pygame.image.load('images/Versus.png')
Versuswidth=300
Versusheight=200
Versusrect=Versus.get_rect()
Versusrect.center=(width/2,height/2)


plano_de_fundo_vitoria = pygame.image.load("images/plano_de_fundo_vitoria.jpeg")
plano_de_fundo_vitoria_width=width
plano_de_fundo_vitoria_height=height
plano_de_fundo_vitoria_image = pygame.transform.scale(plano_de_fundo_vitoria, (plano_de_fundo_vitoria_width, plano_de_fundo_vitoria_height))
plano_de_fundo_vitoria_rect=plano_de_fundo_vitoria_image.get_rect()
plano_de_fundo_vitoria_rect.center=((width/2),(height/2))