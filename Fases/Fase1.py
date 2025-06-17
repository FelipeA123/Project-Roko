import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import pygame
import threading
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
from Mecanicas.Nivel_de_Ensino.Faculdade import Faculdade
from Mecanicas.Nivel_de_Ensino.Mestrado import Mestrado
from Mecanicas.Nivel_de_Ensino.Doutorado import Doutorado
from Progresso.Progresso_jogo import SalvarJogo

class Fase1():
    def __init__(self):
        self.Dinheiro = Dinheiro()
        self.Eficiencia = Eficiencia()
        self.fazerroko = FazerRoko()
        self.VideoYoutube = VideoYoutube()
        self.Cursinho = Cursinho()
        self.Faculdade = Faculdade()
        self.Mestrado = Mestrado()
        self.Doutorado = Doutorado()
        self.SalvarJogo = SalvarJogo(self.Dinheiro, self.fazerroko)
        global CLASSES_ATIVAS

         # Flags de bloqueio para cada ação
        self.cooldowns = [0] * 11  # Um para cada botão
        self.tempo_acao = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0]  # Tempo de bloqueio em segundos (ajuste conforme necessário)


    def rodar_jogo(self):
        pygame.init()
        largura, altura = 1000, 1000
        tela = pygame.display.set_mode((largura, altura))
        pygame.display.set_caption("Roko's Basilisk")

        log = Logger()
        sys.stdout = log

        botoes = [
            Botao(25, 100, 200, 50, "Assistir Tutorial", desbloqueado = True),
            Botao(25, 175, 200, 50, "Ir a aula", desbloqueado = CLASSES_ATIVAS["Cursinho"]),
            Botao(25, 250, 200, 50, "Ir a faculdade", desbloqueado = CLASSES_ATIVAS["Faculdade"]),
            Botao(25, 325, 200, 50, "Programa de mestrado", desbloqueado = CLASSES_ATIVAS["Mestrado"]),
            Botao(25, 400, 200, 50, "Pesquisar sozinho", desbloqueado = CLASSES_ATIVAS["Doutorado"]),

            Botao(626, 100, 200, 50, "Pedir dinheiro", desbloqueado = True),
            Botao(625, 175, 200, 50, "Teste de usabilidade", desbloqueado = CLASSES_ATIVAS["Cursinho"]),
            Botao(625, 250, 200, 50, "Estágio", desbloqueado = CLASSES_ATIVAS["Faculdade"]),
            Botao(625, 325, 200, 50, "Trabalho de dev", desbloqueado = CLASSES_ATIVAS["Mestrado"]),
            Botao(625, 400, 200, 50, "Consultoria", desbloqueado = CLASSES_ATIVAS["Doutorado"]),

            Botao(275, 100, 300, 100, "Criar AI", desbloqueado = CLASSES_ATIVAS["Cursinho"])
        ]

        mensagens = [
            MensagemPermanente(25, 25, "Saldo: R$ "),
            MensagemPermanente(300, 25, "Progresso Roko: "),
            MensagemPermanente(625, 25, "Eficiência: ")
        ]

        rodando = True
        while rodando:
            if self.fazerroko.roko_criado:
                self.finalizar_jogo(tela)

            tela.fill(CINZA_ESCURO)
            
            # Atualiza estados dos botões conforme bloqueio
            for i, botao in enumerate(botoes):
                botao.desbloqueado = not self.cooldowns[i]

            botoes[1].atualizar_estado(CLASSES_ATIVAS["Cursinho"])
            botoes[6].atualizar_estado(CLASSES_ATIVAS["Cursinho"])
            botoes[10].atualizar_estado(CLASSES_ATIVAS["Cursinho"])

            botoes[2].atualizar_estado(CLASSES_ATIVAS["Faculdade"])
            botoes[7].atualizar_estado(CLASSES_ATIVAS["Faculdade"])

            botoes[3].atualizar_estado(CLASSES_ATIVAS["Mestrado"])
            botoes[8].atualizar_estado(CLASSES_ATIVAS["Mestrado"])

            botoes[4].atualizar_estado(CLASSES_ATIVAS["Doutorado"])
            botoes[9].atualizar_estado(CLASSES_ATIVAS["Doutorado"])

            mensagens[0].definir_valor(lambda: f"{self.Dinheiro.saldo:.2f}")
            mensagens[1].definir_valor(lambda: f"{self.fazerroko.progresso_percentual():.2f}%")
            mensagens[2].definir_valor(lambda: f"{self.Eficiencia.eficiencia:.2f}x")

 
            pos_mouse = pygame.mouse.get_pos()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    rodando = False
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    for i, botao in enumerate(botoes):
                        if botao.verificar_clique(pos_mouse) and botao.desbloqueado:
                            self.cooldowns[i] = True  # Bloqueia o botão
                            # Inicia a ação em uma thread
                            threading.Thread(target=self.executar_acao, args=(i,)).start()



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

    def executar_acao(self, i):

        # Executa a ação correspondente ao botão i e desbloqueia ao terminar
        if i == 0:
            self.VideoYoutube.subir_nivel(self.Eficiencia)
        elif i == 1:
            self.Cursinho.subir_nivel(self.Eficiencia)
        elif i == 2:
            self.Faculdade.subir_nivel(self.Eficiencia)
        elif i == 3:
            self.Mestrado.subir_nivel(self.Eficiencia)
        elif i == 4:
            self.Doutorado.subir_nivel(self.Eficiencia)
        elif i == 5:
            self.VideoYoutube.ganhar_dinheiro(self.Dinheiro)
        elif i == 6:
            self.Cursinho.ganhar_dinheiro(self.Dinheiro, self.Eficiencia)
        elif i == 7:
            self.Faculdade.ganhar_dinheiro(self.Dinheiro, self.Eficiencia)
        elif i == 8:
            self.Mestrado.ganhar_dinheiro(self.Dinheiro, self.Eficiencia)
        elif i == 9:
            self.Doutorado.ganhar_dinheiro(self.Dinheiro, self.Eficiencia)
        elif i == 10:
            self.fazerroko.criar_AI(self.Eficiencia)
        self.cooldowns[i] = False  # Desbloqueia o botão ao terminar
        

    def finalizar_jogo(self, tela):
        tela.fill((0, 0, 0))  # Tela preta
        fonte = pygame.font.SysFont('Arial', 32)
        texto = fonte.render("O Basilisco foi criado. Você foi julgado.", True, (255, 0, 0))
        subtitulo = fonte.render("Fim de jogo.", True, (255, 255, 255))

        largura, altura = tela.get_size()
        texto_rect = texto.get_rect(center=(largura//2, altura//2 - 20))
        subtitulo_rect = subtitulo.get_rect(center=(largura//2, altura//2 + 30))

        tela.blit(texto, texto_rect)
        tela.blit(subtitulo, subtitulo_rect)
        pygame.display.flip()

    # Espera 5 segundos antes de fechar o jogo
        pygame.time.wait(5000)
        self.SalvarJogo.salvar()
        pygame.quit()
        sys.exit()

