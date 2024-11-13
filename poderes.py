import pygame

width=1200
height=600

power_list=['Escudo','Gigante','Supervelocidade','Superpulo','Superforça']
dic_power={}
for counter in range(len(power_list)):
    power=power_list[counter]
    powerimage=pygame.image.load(f'images/poderes/poder{counter}.png')
    powerimagewidth=width/24
    powerimageheight=height/12
    powerimage = pygame.transform.scale(powerimage, (powerimagewidth, powerimageheight))
    dic_power[power]=powerimage