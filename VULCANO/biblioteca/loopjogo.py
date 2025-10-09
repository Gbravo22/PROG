from PPlay.keyboard import *
from PPlay.collision import *
from PPlay.mouse import *
from PPlay.sprite import *
from PPlay.window import *
from PPlay.gameobject import *
from PPlay.gameimage import *
def loopjogo(janela, mouse, teclado, menu, PLAY, MENU, RANKING):
    while True:
        if teclado.key_pressed("ESC"):
            PLAY = False
            MENU = True
        return PLAY, MENU, RANKING
    janela.updade()