import pygame
from PPlay.keyboard import *
from PPlay.collision import *
from PPlay.mouse import *
from PPlay.sprite import *
from PPlay.window import *
from PPlay.gameobject import *
from PPlay.gameimage import *
import random

# Importa suas funções de "tela" de forma explícita
from biblioteca.menu import gamemenu
from biblioteca.loopjogo import loopjogo
from biblioteca.ranking import ranking

# --- 1. CONFIGURAÇÃO INICIAL (SETUP) ---

pygame.init() # É uma boa prática iniciar o pygame

# Criação do teclado e mouse
mouse = Mouse()
teclado = Keyboard()

# Janela
janela_largura = 1920
janela_altura = 1080
janela = Window(janela_largura, janela_altura)
janela.set_title('VULCANO')

# Carrega as imagens de fundo que serão passadas para as funções
gm1 = GameImage('VULCANO/ARTES/jogar1.png')
menu_img = GameImage('VULCANO/ARTES/menu.png') # Renomeado de 'menu' para 'menu_img'

# --- 2. GERENCIADOR DE ESTADOS ---

# Variáveis que controlam qual tela está ativa
MENU = True
RANKING = False
PLAY = False

# --- 3. LOOP PRINCIPAL DO JOGO ---
# Este é o ÚNICO 'while True' do seu projeto.
while True:
    
    # Limpa a tela (prepara para desenhar o novo frame)
    janela.set_background_color([0,0,0])

    # Decide qual função de "tela" deve ser executada
    
    if MENU:
        # Roda UM frame da lógica do menu
        # Esta função desenha o menu e checa os cliques
        PLAY, MENU, RANKING = gamemenu(janela, mouse, menu_img, teclado, PLAY, MENU, RANKING)
    
    elif PLAY:
        # Roda UM frame da lógica do jogo
        # Esta função roda física, colisão, desenho do jogo, etc.
        PLAY, MENU, RANKING = loopjogo(janela, mouse, gm1, teclado, PLAY, MENU, RANKING)
    
    elif RANKING:
        # Roda UM frame da lógica do ranking
        # Esta função desenha o ranking e checa se o jogador quer voltar
        PLAY, MENU, RANKING = ranking(janela, teclado, PLAY, MENU, RANKING)


    janela.update()