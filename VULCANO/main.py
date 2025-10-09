from PPlay.keyboard import *
from PPlay.collision import *
from PPlay.mouse import *
from PPlay.sprite import *
from PPlay.window import *
from PPlay.gameobject import *
from PPlay.gameimage import *
from biblioteca.menu import*
import random
#criacao do teclado e mouse
mouse = Mouse()
teclado = Keyboard()
#janela
janela_largura = 1920
janela_altura = 1080
janela = Window(janela_largura,janela_altura)
janela.set_title('VULCANO')
janela.set_background_color([0,0,0])
#criacao do menu
menu = GameImage('VULCANO/ARTES/menu.png')
#criacao das variaveis booleanas
MENU = True
RANKING = False
PLAY = False
while True:
    if MENU:
        PLAY, MENU, RANKING = gamemenu(janela, mouse, teclado, menu , PLAY, MENU, RANKING)
    #if PLAY:
        #PLAY, MENU, RANKING =
    janela.update()