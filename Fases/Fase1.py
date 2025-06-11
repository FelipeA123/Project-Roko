import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import pygame
from pygame.locals import *

from Display.Botao import Botao, BRANCO, CINZA_CLARO, CINZA_ESCURO, PRETO
from Display.Log import Logger
from Display.MensagemPermanente import MensagemPermanente

from Progresso.Variaveis_Globais import CLASSES_ATIVAS

from Mecanicas.Dinheiro import Dinheiro
from Mecanicas.Eficiencia import Eficiencia
from Mecanicas.FazerRoko import FazerRoko
from Mecanicas.Nivel_de_Ensino.VideoYoutube import VideoYoutube
from Mecanicas.Nivel_de_Ensino.Cursinho import Cursinho

from Progresso.Progresso_jogo import SalvarJogo

class Fase1():
    def __init__(self):
        self.Dinheiro = Dinheiro()
        self.Eficiencia = Eficiencia()
        self.fazerroko = FazerRoko()
        self.VideoYoutube = VideoYoutube()
        self.cursinho = Cursinho()
        self.SalvarJogo = SalvarJogo(self.Dinheiro, self.fazerroko)
        global CLASSES_ATIVAS

    def rodar_jogo(self):
        pygame.init()
        largura, altura = 1000, 1000
        tela = pygame.display.set_mode((largura, altura))
        pygame.display.set_caption("Roko's Basilisk")

        log = Logger()
        sys.stdout = log

        botoes = [
            Botao(25, 100, 200, 50, "Assistir Tutorial", desbloqueado = True),
            Botao(626, 100, 200, 50, "Pedir dinheiro", desbloqueado = True),
            Botao(25, 175, 200, 50, "Ir a aula", desbloqueado = CLASSES_ATIVAS["Cursinho"]),
            Botao(625, 175, 200, 50, "Teste de usabilidade", desbloqueado = CLASSES_ATIVAS["Cursinho"]),
            Botao(275, 100, 300, 100, "Criar AI", desbloqueado = CLASSES_ATIVAS["Cursinho"])
        ]

        mensagens = [
            MensagemPermanente(25, 25, "Saldo: R$ "),
            MensagemPermanente(300, 25, "Progresso Roko: "),
            MensagemPermanente(625, 25, "Eficiência: ")
        ]

        rodando = True
        while rodando:
            tela.fill(CINZA_ESCURO)
            


            botoes[2].atualizar_estado(CLASSES_ATIVAS["Cursinho"])
            botoes[3].atualizar_estado(CLASSES_ATIVAS["Cursinho"])
            botoes[4].atualizar_estado(CLASSES_ATIVAS["Cursinho"])

            mensagens[0].definir_valor(lambda: f"{self.Dinheiro.saldo:.2f}")
            mensagens[1].definir_valor(lambda: f"{self.fazerroko.progresso_percentual():.2f}%")
            mensagens[2].definir_valor(lambda: f"{self.Eficiencia.eficiencia:.2f}x")

 
            pos_mouse = pygame.mouse.get_pos()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    rodando = False
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if botoes[0].verificar_clique(pos_mouse):
                        self.VideoYoutube.subir_nivel(self.Eficiencia)
                    if botoes[1].verificar_clique(pos_mouse):
                        self.VideoYoutube.ganhar_dinheiro(self.Dinheiro)
                    if botoes[2].verificar_clique(pos_mouse):
                        self.cursinho.subir_nivel(self.Eficiencia)
                    if botoes[3].verificar_clique(pos_mouse):
                        self.cursinho.ganhar_dinheiro(self.Dinheiro, self.Eficiencia)
                    if botoes[4].verificar_clique(pos_mouse):
                        self.fazerroko.criar_AI(self.Eficiencia)

            for botao in botoes:
                botao.atualizar(pos_mouse)
                botao.desenhar(tela)

            log.desenhar(tela)
            for mensagem in mensagens:
                mensagem.desenhar(tela)

            
            pygame.display.flip()
        
        self.SalvarJogo.salvar()
        pygame.quit()
        sys.exit()
