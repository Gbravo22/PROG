# Em: biblioteca/loopjogo.py

import pygame 
import random 
from PPlay.keyboard import *
from PPlay.collision import *
from PPlay.mouse import *
from PPlay.sprite import *
from PPlay.window import *
from PPlay.gameobject import *
from PPlay.gameimage import *
from biblioteca.personagem import Personagem
from biblioteca.lava import lava
from biblioteca.camera import Camera
from biblioteca.plataforma import Plataforma

def loopjogo(janela, mouse, gm1, teclado, PLAY, MENU, RANKING):
    
    camera = Camera(janela)
    camera.scroll_limit_tela = janela.height * 0.33 

    largura_plat = 424
    altura_plat = 87
    pos_y_plataforma = janela.height / 2 + 150 
    
    plataforma_inicial = Plataforma(
        imagem_path='VULCANO/ARTES/plataforma1.png',
        x_centro=janela.width / 2,
        y_pos=pos_y_plataforma,
        largura=largura_plat,
        altura=altura_plat
    )
    
    altura_jogador = 80
    largura_jogador = 60
    pos_x_jogador = janela.width / 2
    pos_y_jogador = plataforma_inicial.y
    
    jogador = Personagem(
        xinicial=pos_x_jogador,
        yinicial=pos_y_jogador,
        altura=altura_jogador,
        largura=largura_jogador
    )
    jogador.no_chao = True 
    
    obstaculo = lava(jogador, janela)
    lista_plataformas = [plataforma_inicial]
    
    ultima_y = plataforma_inicial.y 
    min_gap_vertical = 80
    max_gap_vertical = 150

    for _ in range(15):
        novo_x_centro = random.randint(largura_plat // 2, janela.width - (largura_plat // 2))
        gap_vertical = random.randint(min_gap_vertical, max_gap_vertical)
        novo_y = ultima_y - gap_vertical
        nova_plat = Plataforma(
            imagem_path='VULCANO/ARTES/plataforma1.png',
            x_centro=novo_x_centro,
            y_pos=novo_y,
            largura=largura_plat,
            altura=altura_plat
        )
        lista_plataformas.append(nova_plat)
        ultima_y = novo_y
        
    while PLAY:
        
        if teclado.key_pressed("ESC"):
            PLAY = False
            MENU = True
            RANKING = False
            return PLAY, MENU, RANKING
            
        jogador.no_chao = False 
        margem_de_colisao = 15 

        for p in lista_plataformas:
            colidiu = True
            if ( (jogador.x + jogador.width) < p.x or
                  jogador.x > (p.x + p.width) or
                  (jogador.y + jogador.height) < p.y or
                  jogador.y > (p.y + p.height) ):
                colidiu = False
            
            if colidiu:
                if (jogador.velocidade_y >= 0) and abs((jogador.y + jogador.height) - p.y) < margem_de_colisao:
                    jogador.y = p.y - jogador.height 
                    jogador.velocidade_y = 0      
                    jogador.no_chao = True        
                    break 
                if (jogador.velocidade_y < 0) and abs(jogador.y - (p.y + p.height)) < margem_de_colisao:
                    jogador.y = p.y + p.height
                    jogador.velocidade_y = 0 
                    break 
                    
        # Ordem: Jogador primeiro, Câmera depois
        jogador.atualizar(janela, teclado)
        obstaculo.atualizar()
        camera.atualizar(jogador) # (NÃO passa a 'janela' aqui)

        # Lógica de Game Over (Usa camera.y atualizado)
        pe_jogador_na_tela_y = (jogador.y - camera.y) + jogador.height
        
        if pe_jogador_na_tela_y > obstaculo.y:
            PLAY = False
            MENU = True
            RANKING = False
            return PLAY, MENU, RANKING 
            
        # Desenho
        janela.set_background_color([0, 0, 0])
        gm1.draw() 
        
        for p in lista_plataformas:
            p.desenhar(camera) 
            
        jogador.desenhar(camera)
        obstaculo.desenhar()
        
        janela.update()
        
    return PLAY, MENU, RANKING