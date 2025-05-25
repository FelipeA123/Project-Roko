import time
from Skills import CLASSES_ATIVAS
from Skills import Skill
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
        self.fator_ensino = 0.0
        self.roko_criado = False

    def criar_AI(self, eficiencia: Eficiencia):
        if self.nivel is None:
            raise ValueError("tempo_desbloqueio não foi definido!")
        while self.progresso_roko < self.nivel:
            time.sleep(1)
            self.cortar_nivel()
            self.progresso_roko += 1 * eficiencia
        self.roko_criado = True

    def cortar_nivel(self):
        for classe in ORDEM_COMPARACAO:
            if CLASSES_ATIVAS[classe]:
                self.fator_ensino = CORTE_NIVEL_ENSINO[classe]
                self.nivel = self.nivel * self.fator_ensino
                break
            self.progresso += 0.0


