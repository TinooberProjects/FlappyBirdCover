import pygame
import random

from funcoes import *

class Cano:
    def __init__(self,x,distancia,velocidade):
        self.x=x
        self.altura=0
        self.pos_topo=0
        self.pos_base=0
        self.CANO_TOPO=pygame.transform.flip(obter_imagem("imgs","pipe.png"),False,True)
        self.CANO_BASE=obter_imagem("imgs","pipe.png")
        self.sensor=False
        self.distancia=distancia
        self.velocidade=velocidade
        self.definir_altura()
    
    def definir_altura(self):
        self.altura=random.randrange(50,450)
        self.pos_topo=self.altura - self.CANO_TOPO.get_height()
        self.pos_base=self.altura +self.distancia
    
    def deslocar(self):
        self.x=self.x - self.velocidade

    def aparecer_tubos(self,display):
        display.blit(self.CANO_TOPO,(self.x,self.pos_topo))
        display.blit(self.CANO_BASE,(self.x,self.pos_base))
       

