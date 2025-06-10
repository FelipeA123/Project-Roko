from Mecanicas.Skills import Skill
from Mecanicas.Dinheiro import Dinheiro
import time

from Progresso.Variaveis_Globais import CLASSES_ATIVAS

class VideoYoutube(Skill):
    def __init__(self):
        super().__init__()
        self.nivel_necessario = 5
        self.tempo_desbloqueio = 5

    def efeito_especial(self):
        CLASSES_ATIVAS["Cursinho"] = True
        print("Cursinho desbloqueado, você pode fazer teste de usabilidade para ganhar dinheiro.")

    def subir_nivel(self, eficiencia):
        super().subir_nivel(eficiencia)
        print("Você aprende como printar Hello World, incrível!")

    def ganhar_dinheiro(self, dinheiro: Dinheiro):
        print("Pedindo dinheiro pros pais...")
        segundos = 1
        while segundos < 5:
            time.sleep(1)
            segundos += 1
        dinheiro.adicao(10.0)
        print ("Após muita humilhação eles te dão 10 reais!")        