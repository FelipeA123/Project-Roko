import sys
import pygame

class Logger:
    def __init__(self, x=10, y=400, max_mensagens=6, cor_texto=(255, 255, 255), fonte_nome='Arial', fonte_tamanho=16):
        pygame.font.init()
        self.x = x
        self.y = y
        self.max_mensagens = max_mensagens
        self.cor_texto = cor_texto
        self.fonte = pygame.font.SysFont(fonte_nome, fonte_tamanho)
        self.mensagens = []

    def write(self, texto):
        if texto.strip() != "":
            self.mensagens.append(texto.strip())
            if len(self.mensagens) > self.max_mensagens:
                self.mensagens.pop(0)
            sys.__stdout__.write(texto)  # Mantém print no console


    def desenhar(self, superficie):
        for i, msg in enumerate(self.mensagens):
            texto_surf = self.fonte.render(msg, True, self.cor_texto)
            superficie.blit(texto_surf, (self.x, self.y + i * 20))
