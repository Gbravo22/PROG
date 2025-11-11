# Em: biblioteca/plataforma.py

import pygame
from PPlay.sprite import Sprite

class Plataforma(Sprite):
    
    def __init__(self, imagem_path, x_centro, y_pos, largura, altura):
        #
        # ... seu código __init__ (está correto) ...
        #
        super().__init__(imagem_path)
        self.width = largura
        self.height = altura
        try:
            self.image = pygame.transform.scale(self.image, (largura, altura))
        except Exception as e:
            print(f"Erro ao redimensionar plataforma: {e}")
        self.x = x_centro - (self.width / 2)
        self.y = y_pos

    # --- ADICIONE ESTE MÉTODO ---
    def desenhar(self, camera):
        # Calcula a posição Y da tela temporariamente
        screen_y = self.y - camera.y
        
        # Define a posição de TELA e desenha
        self.set_position(self.x, screen_y)
        self.draw()
