import time
from abc import ABC, abstractmethod
from Mecanicas.eficiencia import Eficiencia

class Skill(ABC):
    def __init__(self):
        self.nivel = 0
        self.desbloquado = False
        self.nivel_necessario = None
        self.tempo_acumulado = 0
        self.tempo_desbloqueio = None

    def subir_nivel(self, eficiencia):
        while self.tempo_acumulado < self.tempo_desbloqueio:
            time.sleep(1)
            self.tempo_acumulado += 1 * eficiencia
        self.tempo_acumulado = 0.0
        self.nivel += 1
        self.desbloquear()

    def desbloquear(self):
        if self.nivel >= self.nivel_necessario:
            self.desbloquado = True
    

class Video_Youtube(Skill):
    def __init__(self):
        super().__init__()
        self.nivel_necessario = 10
        self.tempo_desbloqueio = 5

class Cursinho(Skill):
    def __init__(self):
        super().__init__()
        self.nivel_necessario = 15
        self.tempo_desbloqueio = 10

class Faculdade(Skill):
    def __init__(self):
        super().__init__()
        self.nivel_necessario = 20
        self.tempo_desbloqueio = 20

class Mestrado(Skill):
    def __init__(self):
        super().__init__()
        self.nivel_necessario = 20
        self.tempo_desbloqueio = 40

class Doutorado(Skill):
    def __init__(self):
        super().__init__()
        self.nivel_necessario = 20
        self.tempo_desbloqueio = 80