import time
import threading
from Mecanicas.Skills import Skill
from Mecanicas.Dinheiro import Dinheiro
from Mecanicas.Eficiencia import Eficiencia

from Progresso.Variaveis_Globais import CLASSES_ATIVAS

class Mestrado(Skill):
    def __init__(self):
        super().__init__()
        self.nivel_necessario = 20
        self.tempo_desbloqueio = 40

    def efeito_especial(self):
        CLASSES_ATIVAS["Doutorado"] = True
        print("Doutrado debloqueado, você pode trabalhar como consultor.")

    def subir_nivel(self, eficiencia):
        super().subir_nivel(eficiencia)
        print("Você mal consegue acompanhar, mas após muito esforço você progride.")

    def ganhar_dinheiro(self, dinheiro: Dinheiro, eficiencia: Eficiencia):
        print("Indo para o trabalho")
        segundos = 0.0
        while segundos < 10:
            time.sleep(1)
            segundos += eficiencia.eficiencia
        dinheiro.adicao(5000.0)
        print ("Você foi pago em R$ 5000, o project manager um dia irá entender sua timeline!")