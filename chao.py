import pygame

from funcoes import *
class Chao:

    def __init__(self,altura,velocidade):
        self.altura=altura
        self.pos_inicial=0
        self.largura=obter_imagem("imgs","base.png").get_width()
        self.pos_final=self.largura
        self.velocidade=velocidade
    
    def deslocar(self):
        self.pos_inicial=self.pos_inicial-self.velocidade
        self.pos_final=self.pos_final-self.velocidade
        
        if self.pos_inicial +self.largura<0:
            self.pos_inicial=self.pos_final+self.largura
        
        if self.pos_final +self.largura<0:
            self.pos_final=self.pos_inicial+self.largura

    def aparecer_tela(self,display,imagem):
        display.blit(imagem,(self.pos_inicial,self.altura))
        display.blit(imagem,(self.pos_final,self.altura))


