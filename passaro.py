import pygame

from funcoes import *


class Passaro:

    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.velocidade=0
        self.altura=self.y
        self.tempo=0
        self.angulo=0
        
    def pular(self):
        self.velocidade=-10.5
        
        self.tempo=0
        self.altura=self.y
    
    def deslocar(self):
        self.tempo = self.tempo + 1
        
        deslocamento=1.2*(self.tempo**2)+self.velocidade*self.tempo
        

        if deslocamento >16:
            deslocamento=16
        elif deslocamento <0: 
            deslocamento=deslocamento-2

        self.y=self.y+deslocamento
          

    
    def aparecer_tela(self,display,imagem):
        display.blit(imagem,(self.x,self.y))




