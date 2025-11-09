class Camera:
    def __init__(self, janela):
        self.janela = janela
        self.y = 0  # O deslocamento vertical da câmera.
        # Define a "linha" que o jogador deve cruzar para a câmera subir.
        self.scroll_limit = janela.height / 2
    def atualizar(self, jogador):
        if (jogador.y - self.scroll_limit) <self.y:
            self.y = jogador.y - self.scroll_limit
    def desenhar(self, objeto):
        objeto.set_position(objeto.x, objeto.y - self.y)
        objeto.draw()
    def desenhar_lista(self, lista_objetos):
        for objeto in lista_objetos:
            self.desenhar(objeto)


