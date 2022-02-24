#####################################################

#funcoes



import os
import pygame
from pygame import mixer


def obter_imagem(pasta,nomeImagem):
    Imagem=pygame.transform.scale2x(pygame.image.load(os.path.join(pasta,nomeImagem)))
    
    return Imagem


def config_musica(musica, volume):
    mixer.init() 
    mixer.music.load(musica) 
    mixer.music.set_volume(volume) 
    mixer.music.play()  


def config_fonte(nomeFonte, tamanho):
    pygame.font.init()
    pygame.font.SysFont(nomeFonte,tamanho)

def config_fps(fps):
    pygame.time.Clock().tick(fps)
    


def aparecer_tela(display,imagem,x,y):
    display.blit(imagem,(x,y))
    