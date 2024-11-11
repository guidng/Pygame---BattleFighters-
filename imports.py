# Importa e inicia pacotes
import pygame

# Gera tela principal
width=1200
height=600

# Inicia estruturas de dados
sound = True
sound2 = True
j1=False
j2=False
frames=0
current_screen='tela carregamento'
FPS=60
countloadbar=0
j1_wins=0
j2_wins=0
SecScreen=0


# Importa imagens das ações dos personagens durante o jogo:
dic_pos={}
for i in range(20):
    DGwidth=width/16
    DGheight=height/4
    side = pygame.image.load(f'images/Personagenspartida/Perslado{i}.png')
    side = pygame.transform.scale(side, (DGwidth, DGheight))
    
    punch = pygame.image.load(f'images/Personagenspartida/Perssoco{i}.png')
    punch = pygame.transform.scale(side, (DGwidth, DGheight))
    
    kick = pygame.image.load(f'images/Personagenspartida/Perschute{i}.png')
    kick = pygame.transform.scale(side, (DGwidth, DGheight))
    
    dic_pos[i]=[side,punch,kick]


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


# Importa Botões de mute e volume
Muteimage = pygame.image.load('images/mudo.png')
Volumeimage = pygame.image.load('images/som_ligado.png')


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


Playimage = pygame.image.load('images/botao_play.png')
Playimagewidth = width/4
Playimageheight = height/2
Playimage = pygame.transform.scale(Playimage, (Playimagewidth, Playimageheight))
Playimage_rect=Playimage.get_rect()
Playimage_rect.center=((width/2),(height/2))


# Importa imagem seta
Arrowimage=pygame.image.load('images/Setavoltar.png')
Arrowimagewidth=width/16
Arrowimageheight=height/12
Arrowimage = pygame.transform.scale(Arrowimage, (Arrowimagewidth, Arrowimageheight))
Arrowimage_rect=Arrowimage.get_rect()
Arrowimage_rect.top = 0
Arrowimage_rect.left = 0
arrow_area=pygame.Rect(0,0,(width/16),(height/12))


# Importa imagem de grade de personagens
Gradeimage=pygame.image.load('images/Gradepersonagens.png')
Gradeimagewidth=width*(2/3)
Gradeimageheight=height*(5/6)
Gradeimage = pygame.transform.scale(Gradeimage, (Gradeimagewidth, Gradeimageheight))
Gradeimage_rect=Gradeimage.get_rect()
Gradeimage_rect.center=((width/2),(height/2))


# Importa imagens de personagens
Namelist=[]
Facelist=[]
face_area_list=[]
Fullbody_list=[]
Full_list1={}
Full_list2={}
list_characters=['Fred Tio','Alekinho','Baiano','NiGOATlas','Leo Messi','J Viddy','Old Serra','Mr Fein','Fogaca','Marcio desoft','Pelicano','Dani Livros','Gabigol','Cauezada','Irmaozin','Ninja 1','Ninja 2','Ninja 3','Gagui','Juba']
for characters in range(20):
    Characimage = pygame.image.load(f'images/Personagem{characters}.png')
    Fullbody = pygame.image.load(f'images/FullPerson{characters}.png')
    Namelist.append(list_characters[characters])
    Facelist.append(Characimage)
    Fullbody_list.append(Fullbody)


# Importa imagens de mapas
maps_list=['Deserto','Vulcão','Montanhas','Floresta','Favela','Aeroporto','Baía Pirata','Circo']
listahmapa=[470,470,470,470,470,470,470,470]
dic_maps={}
dic_mapsrect={}
for counter in range(len(maps_list)):
    map=maps_list[counter]
    Mapimage=pygame.image.load(f'images/Mapa{counter}.jpg')
    Mapimagewidth=width
    Mapimageheight=height
    Mapimage = pygame.transform.scale(Mapimage, (Mapimagewidth, Mapimageheight))
    Mapimage_rect=Mapimage.get_rect()
    Mapimage_rect.center=((width/2),(height/2))
    trilha_sonora_mapas = pygame.mixer.Sound(f"trilhas_sonoras/trilhasonoramapa{counter}.mp3")
    dic_maps[map]=(Mapimage, trilha_sonora_mapas)
    dic_mapsrect[map]=Mapimage_rect


# Nomes, faces e fotos do corpo todo
Facewidth=width/10
Faceheight=height/9
list_facenrect=[]
list_namenrect=[]
counter=0
for heightcount in range(4):
    for Gridcount in range(5):
        Name=Namelist[counter]
        Face=Facelist[counter]
        Full=Fullbody_list[counter]
        counter+=1
        Face = pygame.transform.scale(Face, (Facewidth, Faceheight))
        Face_rect=Face.get_rect()
        Face_rect.center=(((345*(width/1200))+(Gridcount*130)),((187.5*(width/1200))+(heightcount*75)))
        list_facenrect.append([Face,Face_rect])
        face_area=((-Facewidth/2)+((345*(width/1200)))+(Gridcount*130), ((-Faceheight/2)+(187.5*(width/1200))+(heightcount*75)), Facewidth, Faceheight)
        face_area_list.append(face_area)


        persnamefont = pygame.font.SysFont(None, 24)
        Name = persnamefont.render(f'{Name.upper()}', True, (255, 255, 255))
        Name_rect=Name.get_rect()
        Name_rect.center=(((345*(width/1200))+(Gridcount*130)),(-7.5+50+75+100+(heightcount*75)))
        list_namenrect.append([Name,Name_rect])


        Fullwidth=200
        Fullheight=300
        Full = pygame.transform.scale(Full, (Fullwidth, Fullheight))
        Full_rect1=Full.get_rect()
        Full_rect2=Full.get_rect()
        Full_rect1.center=(150,350)
        Full_list1[Full]=Full_rect1
        Full_rect2.center=(1050,350)
        Full_list2[Full]=Full_rect2


# Carregar a música de fundo
pygame.mixer.music.load("trilhas_sonoras/trilha_sonora_tela_inicial.mp3")  # Substitua pelo caminho do seu arquivo de música
pygame.mixer.music.set_volume(0.1)  # Define o volume da música (0.0 a 1.0)
song1variable=0
test=0


# Botão de confirmar
Confirmb=pygame.image.load('images/Confirmb.png')
Confirmedb=pygame.image.load('images/Confirmedb.png')
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

mapfont = pygame.font.SysFont(None, 128)
maptext1 = mapfont.render('Mapa selecionado:', True, (255,255,255))
text1rect=maptext1.get_rect()
text1rect.center=(width/2,400)

# Imagem Versus
Versus=pygame.image.load('images/Versus.png')
Versuswidth=300
Versusheight=200
Versusrect=Versus.get_rect()
Versusrect.center=(width/2,height/2)


# Criar contagem regressiva
n3 = mapfont.render('3', True, (255,31,45))
n2 = mapfont.render('2', True, (255,31,45))
n1 = mapfont.render('1', True, (255,31,45))
nstart = mapfont.render('Start!', True, (255,31,45))


nrect=n1.get_rect()
nsrect=nstart.get_rect()
nrect.center=(width/2,125)
nsrect.center=(width/2,125)


# Cria botão de pausa
Pauseb=pygame.image.load('images/Botaopausa.png')
Pausebwidth=width/12
Pausebheight=height/6
Pauseb = pygame.transform.scale(Pauseb, (Pausebwidth, Pausebheight))
Pauseb_rect=Pauseb.get_rect()
Pauseb_rect.center=(width/2,Pausebheight/2)
Pause_area=pygame.Rect(550,0,Pausebwidth,Pausebheight)


# Cria botões da tela de pausa
vjogo=pygame.image.load('images/Voltjogo.png')
vjogowidth=width/4
vjogoheight=height/4
vjogo = pygame.transform.scale(vjogo, (vjogowidth, vjogoheight))
vjogo_rect=vjogo.get_rect()
vjogo_rect.center=(width/2,105)
vjogo_area=pygame.Rect((width/2)-(vjogowidth/2),105-(vjogoheight/2),vjogowidth,vjogoheight)


controles=pygame.image.load('images/Controlesb.png')
controleswidth=width/4
controlesheight=height/4
controles = pygame.transform.scale(controles, (controleswidth, controlesheight))
controles_rect=controles.get_rect()
controles_rect.center=(width/2,285)
controles_area=pygame.Rect((width/2)-(controleswidth/2),285-(controlesheight/2),controleswidth,controlesheight)


# Tela final informações
resfont=pygame.font.SysFont(None, 128)

plano_de_fundo_vitoria = pygame.image.load("images/plano_de_fundo_vitoria.jpeg")
plano_de_fundo_vitoria_width=width
plano_de_fundo_vitoria_height=height
plano_de_fundo_vitoria_image = pygame.transform.scale(plano_de_fundo_vitoria, (plano_de_fundo_vitoria_width, plano_de_fundo_vitoria_height))
plano_de_fundo_vitoria_rect=plano_de_fundo_vitoria_image.get_rect()
plano_de_fundo_vitoria_rect.center=((width/2),(height/2))

Jogardenovo=pygame.image.load(f'images/Jogardenovo.png')
Jogardenovowidth=300
Jogardenovoheight=150
Jogardenovo = pygame.transform.scale(Jogardenovo, (Jogardenovowidth, Jogardenovoheight))
Jogardenovo_rect=Jogardenovo.get_rect()
Jogardenovo_rect.center=((width/2),(105))
Jogardenovoarea=pygame.Rect(450,30,300,150)


Trocarpers=pygame.image.load(f'images/Trocarpers.png')
Trocarperswidth=300
Trocarpersheight=150
Trocarpers = pygame.transform.scale(Trocarpers, (Trocarperswidth, Trocarpersheight))
Trocarpers_rect=Trocarpers.get_rect()
Trocarpers_rect.center=((width/2),(285))
Trocarpersarea=pygame.Rect(450,210,300,150)

Retmenu=pygame.image.load(f'images/Retmenu.png')
Retmenuwidth=300
Retmenuheight=150
Retmenu = pygame.transform.scale(Retmenu, (Retmenuwidth, Retmenuheight))
Retmenu_rect=Retmenu.get_rect()
Retmenu_rect.center=((width/2),(465))
Retmenu_area=pygame.Rect(450,390,300,150)
