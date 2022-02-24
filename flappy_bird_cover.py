#importando as bibliotecas
# from sqlite3 import Time
# from threading import Timer
import time
import pygame # biblioteca de jogos

import os #garante que eu consiga ter acesso a arquivos

import random #geração de números randômicos

from pygame import mixer #controle de música

from funcoes import *

from tela import *

from cano import *



from chao import *
from passaro import *

#Programa principal

def main():
    jogo=Tela(500,800)
    fundo=obter_imagem("imgs","bg.png")
    img_passaro=obter_imagem("imgs","bird1.png")
    chao=obter_imagem("imgs","base.png")
    imgCano=obter_imagem("imgs","pipe.png")
    chao_jogo=Chao(700,1)
    passaro=Passaro(230,100)
    jogar=0
    canos=[Cano(500 ,150,1)]   
    
    sensor=True
    
    fpsJogo=config_fps(30) 
    config_musica("song.mp3",0.3)
    
    
    game_over = False
    while game_over==False:
        #fps
        fpsJogo
        

        #interação com o usuário
        for evento in pygame.event.get():
            #Para o usuário fechar a aplicação 
            if evento.type == pygame.QUIT:
                game_over=True
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key==pygame.K_SPACE:
                    jogar=jogar+1
                    passaro.pular() 
                    if jogar % 10 == 0:
                        canos.append(Cano(500 ,150,1))
                        jogar=0
        

        aparecer_tela(jogo.display,fundo,0,0)
        
        
        
        passaro.aparecer_tela(jogo.display,img_passaro)
        passaro.deslocar()

        

        for cano in canos:
            cano.aparecer_tubos(jogo.display)
            
            cano.deslocar()

        chao_jogo.aparecer_tela(jogo.display,chao)    
        chao_jogo.deslocar()    
        pygame.display.update()
         
        
       

#iniciando o programa
if __name__ == '__main__':
    main()

