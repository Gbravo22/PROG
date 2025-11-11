# Em: biblioteca/lava.py
import pygame 
from PPlay.keyboard import *
from PPlay.sprite import *
from PPlay.animation import *

class lava:
    def __init__(self, personagem, janela):
        self.sprite_lava = Animation("VULCANO/ARTES/lava.png", 2)
        
        self.sprite_lava.width = janela.width
        self.sprite_lava.height = 100 # Altura da barra de lava

        # Redimensiona a imagem (spritesheet)
        try:
            self.sprite_lava.image = pygame.transform.scale(
                self.sprite_lava.image, 
                (self.sprite_lava.width * 2, self.sprite_lava.height) # 2 frames
            )
        except Exception as e:
            print(f"Erro ao redimensionar imagem da Lava: {e}")

        self.sprite_lava.set_total_duration(800)
        
        self.x = 0
        # Esta é a posição FIXA NA TELA (embaixo)
        self.y = janela.height - self.sprite_lava.height 

    def atualizar(self):
        self.sprite_lava.update()

    def desenhar(self): 
        # 2. Desenhe a lava na posição de TELA (self.y)
        #    Ignorando totalmente a câmera.
        self.sprite_lava.set_position(self.x, self.y)
        self.sprite_lava.draw()