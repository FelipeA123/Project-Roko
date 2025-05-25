import time
from abc import ABC, abstractmethod
from Mecanicas.Eficiencia import Eficiencia

# Variável global para controle de ativação das classes de ensino
CLASSES_ATIVAS = {
    "Doutorado": False,
    "Mestrado": False,
    "Faculdade": False,
    "Cursinho": False
}
class Skill(ABC):
    def __init__(self):
        self.nivel = 0
        self.desbloqueado = False
        self.nivel_necessario = None
        self.tempo_acumulado = 0
        self.tempo_desbloqueio = None

    def subir_nivel(self, eficiencia: Eficiencia):
        if self.tempo_desbloqueio is None:
            raise ValueError("tempo_desbloqueio não foi definido!")
        while self.tempo_acumulado < self.tempo_desbloqueio:
            time.sleep(1)
            self.tempo_acumulado += 1 * eficiencia
        self.tempo_acumulado = 0
        self.nivel += 1
        self.desbloquear()

    def desbloquear(self):
        if self.nivel >= self.nivel_necessario:
            self.desbloqueado = True
            self.efeito_especial()  # Chama o método abstrato

    @abstractmethod
    def efeito_especial(self):
        pass