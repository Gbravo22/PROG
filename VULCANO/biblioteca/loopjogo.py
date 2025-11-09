from PPlay.keyboard import *
from PPlay.collision import *
from PPlay.mouse import *
from PPlay.sprite import *
from PPlay.window import *
from PPlay.gameobject import *
from PPlay.gameimage import * 
from biblioteca.personagem import *
from biblioteca.lava import *
from biblioteca.camera import *


janela = Window(1920, 1080)
jogador = Personagem(janela.width/2, janela.height/2, janela.height/11, janela.width/12)
obstaculo = lava(jogador, janela)

plataforma = Sprite('VULCANO/ARTES/plataforma1.png')
nova_largura = 424
nova_altura = 87
plataforma.image = pygame.transform.scale(plataforma.image, (nova_largura, nova_altura))
plataforma.width = nova_largura
plataforma.height = nova_altura
plataforma.x = janela.width/2 - plataforma.width/2
plataforma.y = janela.height/2 + jogador.height/2 - 5

def loopjogo(janela, mouse, gm1, teclado, PLAY, MENU, RANKING):
    while True:
        if teclado.key_pressed("ESC"):
            PLAY = False
            MENU = True
            return PLAY, MENU, RANKING
        jogador.atualizar(janela, teclado)
        janela.set_background_color([255,255,255])
        gm1.draw()
        plataforma.draw()
        jogador.desenhar()
        obstaculo.atualizar()
        obstaculo.desenhar()
        janela.update()