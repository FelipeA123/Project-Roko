import time
import threading
from Mecanicas.Skills import Skill
from Mecanicas.Dinheiro import Dinheiro
from Mecanicas.Eficiencia import Eficiencia

from Progresso.Variaveis_Globais import CLASSES_ATIVAS

class Doutorado(Skill):
    def __init__(self):
        super().__init__()
        self.nivel_necessario = 20
        self.tempo_desbloqueio = 80

    def efeito_especial(self):
        CLASSES_ATIVAS["Doutorado"] = True
        print("Você chegou no limite da sua jornada como estudante, agora seu progresso é por conta própria")

    def subir_nivel(self, eficiencia):
        super().subir_nivel(eficiencia)
        print("Você pesquisa por conta própria, sem muito retorno")

    def ganhar_dinheiro(self, dinheiro: Dinheiro, eficiencia: Eficiencia):
        print("Iniciando consultoria...")
        segundos = 0.0
        while segundos < 10:
            time.sleep(1)
            segundos += eficiencia.eficiencia
        dinheiro.adicao(50000.0)
        print ("Após otimizar holisticamente processos internos, aglutinando setores, você é pago em R$ 50.000, incrível!")