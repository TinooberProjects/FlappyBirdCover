


import os
import pygame

from cano import *

class Tela:
    '''Tela do Jogo'''    
    
    def __init__(self,largura,altura):
        self.altura=altura
        self.largura=largura
        self.display= pygame.display.set_mode((self.largura,self.altura))


