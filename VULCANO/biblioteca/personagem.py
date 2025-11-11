# Importa o pygame (necessário, pois a PPlay roda sobre ele)
import pygame 
from PPlay.animation import *
from PPlay.window import *
from PPlay.sprite import *
from PPlay.keyboard import *
class Personagem:
    def __init__(self, xinicial, yinicial, altura, largura):

        # --- ANIMAÇÕES ---
        self.anim_parado = Animation("VULCANO/ARTES/parado.png", 2)
        self.anim_esquerda = Animation ("VULCANO/ARTES/esquerda.png", 4)
        self.anim_direita = Animation ("VULCANO/ARTES/direita.png", 4)

        # Tamanho do personagem (de UM frame)
        self.width = largura
        self.height = altura

        # --- REDIMENSIONAMENTO CORRETO ---
        
        # 1. Define o tamanho de UM frame para a PPlay
        self.anim_direita.height = self.anim_esquerda.height = self.anim_parado.height = self.height
        self.anim_direita.width = self.anim_esquerda.width = self.anim_parado.width = self.width

        # 2. Redimensiona o ARQUIVO DE IMAGEM (spritesheet)
        #    Isso é ESSENCIAL e deve ser adicionado de volta
        try:
            self.anim_parado.image = pygame.transform.scale(self.anim_parado.image, (self.width * 2, self.height)) # 2 frames
            self.anim_esquerda.image = pygame.transform.scale(self.anim_esquerda.image, (self.width * 4, self.height)) # 4 frames
            self.anim_direita.image = pygame.transform.scale(self.anim_direita.image, (self.width * 4, self.height)) # 4 frames
        except Exception as e:
            print(f"Erro ao redimensionar imagens do Personagem: {e}")
        # --- FIM DA CORREÇÃO ---

        # --- DURAÇÃO DAS ANIMAÇÕES ---
        self.anim_parado.set_total_duration(1000)
        self.anim_direita.set_total_duration(500)
        self.anim_esquerda.set_total_duration(500)

        # ... (resto do seu __init__ e da sua classe) ...
        self.agora = self.anim_parado
        self.x = xinicial - self.width/2
        self.y = yinicial - self.height # Ajustado para yinicial ser o "pé"
        
        # Física...
        self.velocidade_horizontal = 200
        self.velocidade_y = 0
        self.gravidade_forca = 1200
        self.forca_pulo = -700
        self.no_chao = False

    def atualizar(self, janela, teclado):
        # --- 1. LÓGICA DE PULO ---
        # Checa o pulo PRIMEIRO
        if (teclado.key_pressed("SPACE") or teclado.key_pressed("W")) and self.no_chao:
            self.velocidade_y = self.forca_pulo
            self.no_chao = False # Ao pular, ele não está mais no chão

        # --- 2. LÓGICA DA GRAVIDADE (A CORREÇÃO) ---
        # SÓ aplica gravidade se NÃO estiver no chão
        if not self.no_chao:
            # Está no ar: aplica gravidade
            self.velocidade_y += self.gravidade_forca * janela.delta_time()
        elif self.velocidade_y > 0:
            # Está no chão: zera a velocidade Y para parar o acúmulo
            self.velocidade_y = 0 
            
        # --- 3. MOVIMENTO (FÍSICA) ---
        # Move o personagem no eixo Y (seja pulando ou caindo)
        self.y += self.velocidade_y * janela.delta_time()

        # --- 4. INPUT HORIZONTAL E ANIMAÇÃO ---
        if teclado.key_pressed("A") or teclado.key_pressed("LEFT"):
            self.agora = self.anim_esquerda
            if self.x > 0: 
                self.x -= self.velocidade_horizontal * janela.delta_time()
                
        elif teclado.key_pressed("D") or teclado.key_pressed("RIGHT"):
            self.agora = self.anim_direita
            if self.x < janela.width - self.width:
                self.x += self.velocidade_horizontal * janela.delta_time()
        else:
            # Só mostra animação 'parado' se estiver no chão
            if self.no_chao:
                self.agora = self.anim_parado

        # Atualiza o frame da animação atual
        self.agora.update()

    def desenhar(self, camera):
        """
        Define a posição de TELA (Mundo - Câmera) e desenha.
        """
        # A posição Y na tela é a posição Y no mundo, menos o deslocamento da câmera
        screen_y = self.y - camera.y
        
        self.agora.set_position(self.x, screen_y)
        self.agora.draw()