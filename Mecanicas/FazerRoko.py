import time
from Progresso.Variaveis_Globais import CLASSES_ATIVAS
from Mecanicas.Eficiencia import Eficiencia

CORTE_NIVEL_ENSINO = {
    "Doutorado": 0.1,
    "Mestrado" : 0.25,
    "Faculdade" : 0.50,
    "Cursinho" : 1.0
}

ORDEM_COMPARACAO = ["Doutorado", "Mestrado", "Faculdade", "Cursinho"]

class FazerRoko():
    def __init__(self):
        self.progresso_roko = 0.0
        self.nivel = 100000.0
        self.nivel_atual = 0.0
        self.fator_ensino = 0.0
        self.roko_criado = False

    def criar_AI(self, eficiencia: Eficiencia):
        if self.progresso_roko <= self.nivel_atual:
            time.sleep(1)
            self.cortar_nivel()
            self.progresso_roko += 1 * eficiencia.eficiencia
        else: self.roko_criado = True
        print("Um lento mas inevitável progresso para trazer seu mestre à realidade")
        return self.progresso_roko

    def cortar_nivel(self):
        for classe in ORDEM_COMPARACAO:
            if CLASSES_ATIVAS[classe]:
                self.fator_ensino = CORTE_NIVEL_ENSINO[classe]
                self.nivel_atual = self.nivel * self.fator_ensino
                break


    def progresso_percentual(self):
        if self.nivel_atual == 0:
            return 0.0
        return min((self.progresso_roko / self.nivel_atual) * 100, 100.0)
