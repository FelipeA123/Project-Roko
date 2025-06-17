import time
import threading
from Mecanicas.Skills import Skill
from Mecanicas.Dinheiro import Dinheiro
from Mecanicas.Eficiencia import Eficiencia

from Progresso.Variaveis_Globais import CLASSES_ATIVAS

class Faculdade(Skill):

    def __init__(self):
        super().__init__()
        self.nivel_necessario = 20
        self.tempo_desbloqueio = 20

    def efeito_especial(self):
        CLASSES_ATIVAS["Mestrado"] = True
        print("Mestrado desbloqueado, você pode trabalhar como programador.")

    def subir_nivel(self, eficiencia):
        super().subir_nivel(eficiencia)
        print("Você estuda diligentemente, gerando bons resultados.")

    def ganhar_dinheiro(self, dinheiro: Dinheiro, eficiencia: Eficiencia):
        print("Indo para o estágio...")
        segundos = 0.0
        while segundos < 10:
            time.sleep(1)
            segundos += eficiencia.eficiencia
        dinheiro.adicao(250.0)
        print ("Você foi pago em R$ 250, buscar café nunca foi tão valioso!")