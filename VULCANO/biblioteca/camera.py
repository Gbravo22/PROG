# Em: biblioteca/camera.py

class Camera:
    def __init__(self, janela):
        self.janela = janela
        self.y = 0 
        self.scroll_limit_tela = janela.height * 0.33

    def atualizar(self, jogador):
        """
        Lógica HÍBRIDA INSTANTÂNEA (A prova de explosão):
        NÃO usa delta_time(), por isso não pode "explodir".
        """
        
        target_y = jogador.y - self.scroll_limit_tela
        
        if target_y < 0:
            # Se o jogador está "alto", a câmera
            # INSTANTANEAMENTE vai para a posição correta.
            self.y = target_y
        else:
            # Se o jogador está na "base", a câmera
            # INSTANTANEAMENTE trava no topo.
            self.y = 0