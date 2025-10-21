from PPlay.keyboard import *
from PPlay.sprite import *
from PPlay.animation import *

class lava:
    def __init__(self, personagem, janela):
        #definindo a animacaao lava
        self.lava = Animation("VULCANO/ARTES/lava.png", 2)
        self.lava.width = janela.width 
        self.lava.height = janela.height

        self.lava.image = pygame.transform.scale(self.lava.image, (self.lava.width*2, self.lava.height))

        self.lava.set_total_duration(800)
        self.lava.velocidade = 100

        self.atual = self.lava
        self.lava.y = janela.height - janela.height/10
    def atualizar (self):
        self.lava.update()

    def desenhar (self):

        self.lava.draw()