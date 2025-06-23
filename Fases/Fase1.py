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
        self.SalvarJogo = SalvarJogo(self.Dinheiro, self.fazerroko, self.Eficiencia)
        global CLASSES_ATIVAS

        from Progresso.Variaveis_Globais import EFICIENCIA_ITENS

        if EFICIENCIA_ITENS is not None:
            for ativo, item in zip(EFICIENCIA_ITENS, self.Eficiencia.itens):
                item["ativo"] = ativo
            self.Eficiencia.atualizar_eficiencia()

         # Flags de bloqueio para cada ação
        self.cooldowns = [0] * 12  # Um para cada botão
        self.tempo_acao = [2, 2, 2, 2, 2, 2, 10, 10, 10, 10, 11, 0]  # Tempo de bloqueio em segundos (ajuste conforme necessário)


    def rodar_jogo(self):
        pygame.init()
        largura_original, altura_original = 1000, 1000
        info = pygame.display.Info()
        largura_tela, altura_tela = info.current_w, info.current_h
        tela = pygame.display.set_mode((largura_tela, altura_tela), pygame.FULLSCREEN)
        superficie_base = pygame.Surface((largura_original, altura_original))
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
            Botao(625, 475, 200, 50, "Abrir loja de eficiencia", desbloqueado = True),

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

            superficie_base.fill(CINZA_ESCURO)

            # --- Desenhar botão "X" no canto superior direito ---
            x_size = 40
            x_margin = 10
            x_rect = pygame.Rect(
                largura_original - x_size - x_margin,
                x_margin,
                x_size,
                x_size
            )
            pygame.draw.rect(superficie_base, (200, 0, 0), x_rect)
            fonte_x = pygame.font.SysFont('Arial', 32, bold=True)
            texto_x = fonte_x.render("X", True, (255, 255, 255))
            texto_x_rect = texto_x.get_rect(center=x_rect.center)
            superficie_base.blit(texto_x, texto_x_rect)

             
            # Pegue a posição do mouse na tela cheia
            pos_mouse_tela = pygame.mouse.get_pos()
            # Converta para a escala da superficie_base
            pos_mouse = (
                int(pos_mouse_tela[0] * largura_original / largura_tela),
                int(pos_mouse_tela[1] * altura_original / altura_tela)
            )

            # Atualiza estados dos botões conforme bloqueio
            for i, botao in enumerate(botoes):
                botao.desbloqueado = not self.cooldowns[i]    
                botao.atualizar(pos_mouse)
                botao.desenhar(superficie_base)

            botoes[1].atualizar_estado(CLASSES_ATIVAS["Cursinho"])
            botoes[6].atualizar_estado(CLASSES_ATIVAS["Cursinho"])
            botoes[11].atualizar_estado(CLASSES_ATIVAS["Cursinho"])

            botoes[2].atualizar_estado(CLASSES_ATIVAS["Faculdade"])
            botoes[7].atualizar_estado(CLASSES_ATIVAS["Faculdade"])

            botoes[3].atualizar_estado(CLASSES_ATIVAS["Mestrado"])
            botoes[8].atualizar_estado(CLASSES_ATIVAS["Mestrado"])

            botoes[4].atualizar_estado(CLASSES_ATIVAS["Doutorado"])
            botoes[9].atualizar_estado(CLASSES_ATIVAS["Doutorado"])

            mensagens[0].definir_valor(lambda: f"{self.Dinheiro.saldo:.2f}")
            mensagens[1].definir_valor(lambda: f"{self.fazerroko.progresso_percentual():.2f}%")
            mensagens[2].definir_valor(lambda: f"{self.Eficiencia.eficiencia:.2f}x")

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    rodando = False
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    # Verifica se clicou no "X"
                    if x_rect.collidepoint(pos_mouse):
                        rodando = False
                    # Verifica se clicou em algum botão
                    for i, botao in enumerate(botoes):
                        if botao.verificar_clique(pos_mouse) and botao.desbloqueado:
                            self.cooldowns[i] = True
                            if i == 10:
                                # Loja de eficiência deve rodar na thread principal!
                                self.executar_acao(i)
                            else:
                                threading.Thread(target=self.executar_acao, args=(i,)).start()

            log.desenhar(superficie_base)
            for mensagem in mensagens:
                mensagem.desenhar(superficie_base)
            
            pygame.display.flip()

            # Redimensiona a superficie_base para a tela cheia mantendo proporção
            superficie_redimensionada = pygame.transform.smoothscale(superficie_base, (largura_tela, altura_tela))
            tela.blit(superficie_redimensionada, (0, 0))
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
            self.abrir_loja_eficiencia(pygame.display.get_surface())
        elif i == 11:
            self.fazerroko.criar_AI(self.Eficiencia)
        self.cooldowns[i] = False  # Desbloqueia o botão ao terminar

    def abrir_loja_eficiencia(self, tela):
        rodando_loja = True
        fonte = pygame.font.SysFont('Arial', 28)
        x_size = 40
        x_margin = 10
        largura, altura = tela.get_size()
        clock = pygame.time.Clock()
        while rodando_loja:
            tela.fill((40, 40, 40))
            # Botão X para fechar
            x_rect = pygame.Rect(largura - x_size - x_margin, x_margin, x_size, x_size)
            pygame.draw.rect(tela, (200, 0, 0), x_rect)
            texto_x = fonte.render("X", True, (255, 255, 255))
            tela.blit(texto_x, texto_x.get_rect(center=x_rect.center))

            # Título
            titulo = fonte.render("Loja de Eficiência", True, (255, 255, 255))
            tela.blit(titulo, (largura // 2 - titulo.get_width() // 2, 30))

            # Lista de itens
            item_rects = []
            for idx, item in enumerate(self.Eficiencia.itens):
                y = 100 + idx * 45
                cor = (100, 200, 100) if not item["ativo"] else (150, 150, 150)
                item_rect = pygame.Rect(80, y, 700, 40)
                pygame.draw.rect(tela, cor, item_rect, border_radius=8)
                texto = f'{item["nome"]} | R$ {item["custo"]:.2f} | +{item["modificador"]} eficiência'
                if item["ativo"]:
                    texto += " (Comprado)"
                txt = fonte.render(texto, True, (0, 0, 0))
                tela.blit(txt, (90, y + 5))
                item_rects.append(item_rect)

            # Saldo
            saldo_txt = fonte.render(f"Saldo: R$ {self.Dinheiro.saldo:.2f}", True, (255, 255, 0))
            tela.blit(saldo_txt, (80, altura - 60))

            pygame.display.flip()
            clock.tick(60)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if x_rect.collidepoint(pos):
                        rodando_loja = False
                    for idx, item in enumerate(self.Eficiencia.itens):
                        if not item["ativo"] and item_rects[idx].collidepoint(pos):
                            comprou = self.Eficiencia.comprar_item(item["nome"], self.Dinheiro)
                            if comprou:
                                self.SalvarJogo.salvar()   

    def finalizar_jogo(self, tela):
        fonte = pygame.font.SysFont('Arial', 28)
        texto = fonte.render("O Basilistico foi criado. Todas as pessoas do planeta, exceto Felipe Aoun, Marcos Freitas e Gabriela Nunes, foram julgadas pelo mestre.", True, (255, 0, 0))
        subtitulo = fonte.render("Fim de jogo.", True, (255, 255, 255))

        largura, altura = tela.get_size()
        texto_rect = texto.get_rect(center=(largura//2, altura//2 - 20))
        subtitulo_rect = subtitulo.get_rect(center=(largura//2, altura//2 + 30))

        tela.blit(texto, texto_rect)
        tela.blit(subtitulo, subtitulo_rect)
        pygame.display.flip()

    # Espera 5 segundos antes de fechar o jogo
        pygame.time.wait(5000)
        try:
            self.SalvarJogo.salvar()
        except Exception as e:
            print(f"Erro ao salvar progresso: {e}")
        tela.fill((0, 0, 0))  # Tela preta
        pygame.display.flip()
        pygame.time.wait(1000)
        pygame.quit()
        sys.exit()

