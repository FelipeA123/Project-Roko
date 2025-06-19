import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import pygame
from pygame.locals import *
from Mecanicas.Skills import *
from Mecanicas.Dinheiro import *
from Mecanicas.Eficiencia import *
from Mecanicas.FazerRoko import *
from Mecanicas.Nivel_de_Ensino.VideoYoutube import *
from Mecanicas.Nivel_de_Ensino.Cursinho import *
from Mecanicas.Nivel_de_Ensino.Faculdade import *
from Mecanicas.Nivel_de_Ensino.Mestrado import *
from Mecanicas.Nivel_de_Ensino.Doutorado import *

class Fase2:
    def __init__(self):
        self.dinheiro = Dinheiro()
        self.eficiencia = Eficiencia()
        self.video_yt = VideoYoutube()
        self.cursinho = Cursinho()
        self.faculdade = Faculdade()
        self.mestrado = Mestrado()
        self.doutorado = Doutorado()
        # Ativação inicial pode ser feita aqui se desejar

    def subir_nivel(self):
        # Usa o método subir_nivel da classe Skill
        self.cursinho.subir_nivel(self.eficiencia)

    def ativar_video_yt(self):
        self.video_yt.efeito_especial()

    def ativar_cursinho(self):
        self.cursinho.efeito_especial()

    def ativar_faculdade(self):
        self.faculdade.efeito_especial()

    def ativar_mestrado(self):
        self.mestrado.efeito_especial()

    def ativar_doutorado(self):
        self.doutorado.efeito_especial()

    def ganhar_dinheiro(self):
        self.cursinho.ganhar_dinheiro(self.dinheiro, self.eficiencia)

def rodar_jogo():
    pygame.init()
    largura, altura = 900, 700
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Cursinho Clicker - Fase 2")

    branco = (255, 255, 255)
    preto = (0, 0, 0)
    azul = (0, 0, 255)
    verde = (0, 200, 0)
    vermelho = (200, 0, 0)
    cinza = (100, 100, 100)
    amarelo = (200, 200, 0)
    roxo = (150, 0, 150)

    fonte = pygame.font.Font(None, 36)

    # Define os botões (x, y, largura, altura)
    botoes = [
        {"nome": "Subir de Nivel", "rect": pygame.Rect(50, 100, 250, 60), "cor": azul},
        {"nome": "Video de YouTube", "rect": pygame.Rect(50, 200, 250, 60), "cor": amarelo},
        {"nome": "Cursinho", "rect": pygame.Rect(50, 300, 250, 60), "cor": verde},
        {"nome": "Faculdade", "rect": pygame.Rect(50, 400, 250, 60), "cor": cinza},
        {"nome": "Mestrado", "rect": pygame.Rect(50, 500, 250, 60), "cor": roxo},
        {"nome": "Doutorado", "rect": pygame.Rect(50, 600, 250, 60), "cor": vermelho},
        {"nome": "Ganhar Dinheiro", "rect": pygame.Rect(350, 300, 250, 60), "cor": azul},
    ]

    jogo = Fase2()

    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                rodando = False
            elif evento.type == MOUSEBUTTONDOWN:
                pos = evento.pos
                if botoes[0]["rect"].collidepoint(pos):
                    jogo.subir_nivel()
                elif botoes[1]["rect"].collidepoint(pos):
                    jogo.ativar_video_yt()
                elif botoes[2]["rect"].collidepoint(pos):
                    jogo.ativar_cursinho()
                elif botoes[3]["rect"].collidepoint(pos):
                    jogo.ativar_faculdade()
                elif botoes[4]["rect"].collidepoint(pos):
                    jogo.ativar_mestrado()
                elif botoes[5]["rect"].collidepoint(pos):
                    jogo.ativar_doutorado()
                elif botoes[6]["rect"].collidepoint(pos):
                    jogo.ganhar_dinheiro()

        tela.fill(branco)

        # Desenha os botões
        for botao in botoes:
            pygame.draw.rect(tela, botao["cor"], botao["rect"])
            texto = fonte.render(botao["nome"], True, branco)
            tela.blit(texto, (botao["rect"].x + 20, botao["rect"].y + 15))

        # Exibe saldo e nível do cursinho
        texto_saldo = fonte.render(f"Saldo: R$ {jogo.dinheiro.saldo:.2f}", True, preto)
        tela.blit(texto_saldo, (650, 50))
        texto_nivel_cursinho = fonte.render(f"Nível do Cursinho: {jogo.cursinho.nivel}", True, preto)
        tela.blit(texto_nivel_cursinho, (650, 100))

        pygame.display.flip()

    pygame.quit()
