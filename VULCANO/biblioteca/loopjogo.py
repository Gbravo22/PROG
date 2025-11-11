# Este é o arquivo: biblioteca/loopjogo.py
import pygame 
import random # <-- IMPORTANTE: Adicione esta linha
from PPlay.keyboard import *
from PPlay.collision import *
from PPlay.mouse import *
from PPlay.sprite import *
from PPlay.window import *
from PPlay.gameobject import *
from PPlay.gameimage import *
# --- Imports das suas classes ---
from biblioteca.personagem import Personagem
from biblioteca.lava import lava
from biblioteca.camera import Camera
from biblioteca.plataforma import Plataforma

def loopjogo(janela, mouse, gm1, teclado, PLAY, MENU, RANKING):
    """
    Esta função é chamada pelo main.py CADA VEZ que o jogador
    clica em "Jogar".
    """

    # --- 1. SETUP INICIAL DO JOGO ---
    
    # Câmera
    camera = Camera(janela)
    camera.scroll_limit = janela.height * 0.33 # Câmera mais suave

    # --- Posição Inicial ---
    
    # 1. Criar a Plataforma 
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
    
    # 2. Criar o Jogador 
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
    
    jogador.no_chao = True # Começa no chão
    
    # Lava (Obstáculo)
    obstaculo = lava(jogador, janela)
    
    # Crie uma LISTA de plataformas
    lista_plataformas = [plataforma_inicial]
    
    # --- 1.5 GERAÇÃO DAS 15 PLATAFORMAS ---
    
    # Pega o Y da última plataforma
    ultima_y = plataforma_inicial.y 

    # Define o espaçamento vertical (ajuste conforme seu pulo)
    min_gap_vertical = 80
    max_gap_vertical = 150

    for _ in range(15): # Loop para criar 15 plataformas
        
        # Calcula a nova posição X (aleatória)
        # (Garante que a plataforma não saia da tela)
        novo_x_centro = random.randint(largura_plat // 2, janela.width - (largura_plat // 2))
        
        # Calcula a nova posição Y (sempre acima da anterior)
        gap_vertical = random.randint(min_gap_vertical, max_gap_vertical)
        novo_y = ultima_y - gap_vertical

        # Cria a nova plataforma
        nova_plat = Plataforma(
            imagem_path='VULCANO/ARTES/plataforma1.png',
            x_centro=novo_x_centro,
            y_pos=novo_y,
            largura=largura_plat,
            altura=altura_plat
        )
        
        # Adiciona a plataforma na lista
        lista_plataformas.append(nova_plat)
        
        # Atualiza a altura da "última" plataforma para o próximo loop
        ultima_y = novo_y
        
    # --- FIM DA GERAÇÃO ---
    # --- 2. O LOOP DO JOGO EM SI ---
    while PLAY:
        # --- 3. INPUT (Controles) ---
        if teclado.key_pressed("ESC"):
            PLAY = False
            MENU = True
            RANKING = False
            return PLAY, MENU, RANKING
        # --- 4. COLISÕES --- 
        jogador.no_chao = False # Assume que está no ar
        margem_de_colisao = 15 # pixels

        for p in lista_plataformas:
            
            # --- AABB Check (Manual) ---
            # Checa se os retângulos estão se sobrepondo no "mundo"
            colidiu = True
            if ( (jogador.x + jogador.width) < p.x or
                  jogador.x > (p.x + p.width) or
                  (jogador.y + jogador.height) < p.y or # Pé acima do topo
                  jogador.y > (p.y + p.height) ):       # Cabeça abaixo da base
                colidiu = False
            # --- Fim do AABB Check ---
            
            if colidiu:
                
                # --- LÓGICA DE "POUSAR" (CORRIGIDA) ---
                # Se o jogador está caindo (v_y > 0) OU PARADO (v_y == 0)
                # E o "pé" está perto do "topo" da plataforma
                
                if (jogador.velocidade_y >= 0) and abs((jogador.y + jogador.height) - p.y) < margem_de_colisao:
                    
                    jogador.y = p.y - jogador.height # Corrige a posição
                    jogador.velocidade_y = 0      # Para a queda
                    jogador.no_chao = True        # Permite pular
                    break # Encontrou o chão, para o loop

                # --- LÓGICA DE "BATER A CABEÇA" ---
                # Se o jogador estava subindo (v_y < 0)
                # E a "cabeça" está perto da "base" da plataforma

                if (jogador.velocidade_y < 0) and abs(jogador.y - (p.y + p.height)) < margem_de_colisao:
                    
                    # Empurra o jogador para baixo da plataforma
                    jogador.y = p.y + p.height
                    # Para a subida e faz ele começar a cair
                    jogador.velocidade_y = 0 
                    break # Bateu a cabeça, para o loop        
        # --- 5. LÓGICA (Atualizações) ---
        # (Agora é chamado DEPOIS da colisão)
        jogador.atualizar(janela, teclado)
        obstaculo.atualizar()
        # --- 6. ATUALIZAÇÃO DA CÂMERA ---
        camera.atualizar(jogador)
        # --- 7. DESENHO (Renderização) ---
        janela.set_background_color([0, 0, 0])
        gm1.draw() # Fundo (fixo)
        
        # --- CORREÇÃO NO DESENHO ---
        
        # 3. Desenha as PLATAFORMAS
        for p in lista_plataformas:
            # Chama o método .desenhar() da PRÓPRIA plataforma
            p.desenhar(camera) 
            
        # 4. Desenha o JOGADOR
        # (Este já estava correto)
        jogador.desenhar(camera)
        
        # 5. Desenha a LAVA (fixa)
        obstaculo.desenhar()
        
        # 6. Atualiza a tela
        janela.update()
    return PLAY, MENU, RANKING