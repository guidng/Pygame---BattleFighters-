import pygame

width=1200
height=600

power_list=['Pistola','Escudo','Gigante','Supervelocidade']
dic_power={}
for counter in range(len(power_list)):
    power=power_list[counter]
    powerimage=pygame.image.load(f'images/poderes/poder{counter}.png')
    powerimagewidth=width/24
    powerimageheight=height/12
    powerimage = pygame.transform.scale(powerimage, (powerimagewidth, powerimageheight))
    powerimage_rect=powerimage.get_rect()
    powerimage_rect.center=((width/2),(height/2))
    dic_power[power]=powerimage