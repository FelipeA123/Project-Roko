import pygame

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZA_CLARO = (200, 200, 200)
CINZA_ESCURO = (120, 120, 120)

class Botao:
    def __init__(self, x, y, largura, altura, texto, desbloqueado):
        self.fonte = pygame.font.SysFont('Arial', 16, bold=True)
        self.rect = pygame.Rect(x, y, largura, altura)
        self.texto = texto
        self.sublinhado = False
        self.atualizar_estado(desbloqueado)

    def atualizar_estado(self, desbloqueado):
        self.desbloqueado = desbloqueado
        self.cor_texto = BRANCO if desbloqueado else CINZA_CLARO
        self.cor_borda = BRANCO if desbloqueado else CINZA_CLARO
        self.texto_surf = self.fonte.render(self.texto, True, self.cor_texto)
        self.texto_rect = self.texto_surf.get_rect(center=self.rect.center)

    def desenhar(self, superficie):
        pygame.draw.rect(superficie, CINZA_ESCURO, self.rect, border_radius=4)
        pygame.draw.rect(superficie, self.cor_borda, self.rect, 2, border_radius=4)
        superficie.blit(self.texto_surf, self.texto_rect)
        if self.sublinhado and self.desbloqueado:
            pygame.draw.line(
                superficie, BRANCO,
                (self.texto_rect.left, self.texto_rect.bottom + 2),
                (self.texto_rect.right, self.texto_rect.bottom + 2),
                1
            )

    def verificar_clique(self, pos_mouse):
        return self.desbloqueado and self.rect.collidepoint(pos_mouse)

    def atualizar(self, pos_mouse):
        self.sublinhado = self.rect.collidepoint(pos_mouse)
