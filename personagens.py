import pygame

width=1200
height=600

# Importa imagens das ações dos personagens durante o jogo:
dic_pos={}
for i in range(20):
    DGwidth=width/16
    DGheight=height/4
    side = pygame.image.load(f'images/Personagenspartida/lado/Perslado{i}.png')
    side = pygame.transform.scale(side, (DGwidth, DGheight))
    
    punch = pygame.image.load(f'images/Personagenspartida/soco/Perssoco{i}.png')
    punch = pygame.transform.scale(side, (DGwidth, DGheight))
    
    kick = pygame.image.load(f'images/Personagenspartida/chute/Perschute{i}.png')
    kick = pygame.transform.scale(side, (DGwidth, DGheight))
    
    dic_pos[i]=[side,punch,kick]

# Importa imagens de personagens
Namelist=[]
Facelist=[]
face_area_list=[]
Fullbody_list=[]
Full_list1={}
Full_list2={}
list_characters=['Fred Tio','Alekinho','Baiano','NiGOATlas','Leo Messi','J Viddy','Old Serra','Mr Fein','Fogaca','Marcio desoft','Pelicano','Dani Livros','TheNatDes','Cauezada','Irmaozin','Ninja 1','Ninja 2','Ninja 3','Gagui','Juba']
for characters in range(20):
    Characimage = pygame.image.load(f'images/personagensface/Personagem{characters}.png')
    Fullbody = pygame.image.load(f'images/personagensfp/FullPerson{characters}.png')
    Namelist.append(list_characters[characters])
    Facelist.append(Characimage)
    Fullbody_list.append(Fullbody)

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