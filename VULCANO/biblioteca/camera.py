# Em: biblioteca/camera.py

class Camera:
    def __init__(self, janela):
        self.janela = janela
        self.y = 0 
        self.scroll_limit = janela.height * 0.33

    def atualizar(self, jogador):
        # Este método está CORRETO
        if jogador.no_chao:
            if (jogador.y - self.scroll_limit) < self.y:
                self.y = jogador.y - self.scroll_limit


