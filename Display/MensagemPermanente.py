import pygame

class MensagemPermanente:
    def __init__(self, x, y, label, cor=(255, 255, 255), fonte=None):
        self.x = x
        self.y = y
        self.label = label  # Ex: "Saldo: "
        self.cor = cor
        self.valor_funcao = lambda: "N/A"  # Função que retorna o valor
        self.fonte = fonte or pygame.font.SysFont("arial", 24)

    def definir_valor(self, func):
        """Define uma função que retorna o valor a ser exibido dinamicamente."""
        self.valor_funcao = func

    def desenhar(self, tela):
        """Desenha o texto formatado no local especificado."""
        texto = f"{self.label}{self.valor_funcao()}"
        superficie = self.fonte.render(texto, True, self.cor)
        tela.blit(superficie, (self.x, self.y))
