from PPlay.window import *
from PPlay.sprite import *
from PPlay.animation import *
from PPlay.keyboard import *


class Personagem:
    def __init__(self, xinicial, yinicial, altura, largura):

        #definindo os quesitos da animacao
        self.anim_parado = Animation("VULCANO/ARTES/parado.png", 2)
        self.anim_esquerda = Animation ("VULCANO/ARTES/esquerda.png", 4)
        self.anim_direita = Animation ("VULCANO/ARTES/direita.png", 4)

        self.width = largura - 40
        self.height = altura - 40

        #redimensionando o personagem
        self.anim_direita.height = self.anim_esquerda.height = self.anim_parado.height = self.height
        self.anim_direita.width = self.anim_esquerda.width = self.anim_parado.width = self.width
        self.anim_direita.image = pygame.transform.scale(self.anim_direita.image, (self.width*4, self.height))
        self.anim_esquerda.image = pygame.transform.scale(self.anim_esquerda.image, (self.width*4, self.height))
        self.anim_parado.image = pygame.transform.scale(self.anim_parado.image, (self.width*2, self.height))

        #tempo de cada animacao em milisegundos
        self.anim_parado.set_total_duration(1000)
        self.anim_direita.set_total_duration(500)
        self.anim_esquerda.set_total_duration(500)

        #frame a ser impresso na tela
        self.agora = self.anim_parado

        #posicao inicial
        self.x = xinicial - self.width/2
        self.y = yinicial - self.height/2
        self.velocidade = 200

    def atualizar(self, janela, teclado):
        #mecanica da animacao
        if teclado.key_pressed("A") or teclado.key_pressed("LEFT"):
            self.agora = self.anim_esquerda
            if self.x >= 0:
                self.x -=  self.velocidade * janela.delta_time()
        elif teclado.key_pressed("D") or teclado.key_pressed("RIGHT"):
            self.agora = self.anim_direita
            if self.width + self.x <= janela.width:
                self.x += self.velocidade * janela.delta_time()
        else:
            self.agora = self.anim_parado

        #definindo onde o personagem ficara
        self.agora.set_position(self.x , self.y)
        self.agora.update()
    def desenhar (self):
        self.agora.draw() 