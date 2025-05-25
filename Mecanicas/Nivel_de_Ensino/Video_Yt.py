import time
from Mecanicas.Skills import Skill
from Mecanicas.Dinheiro import Dinheiro

class VideoYoutube(Skill):
    def __init__(self):
        super().__init__()
        self.nivel_necessario = 10
        self.tempo_desbloqueio = 5

    def efeito_especial(self):
        dinheiro = Dinheiro()
        dinheiro.adicao(100.0)
        print("Efeito especial do Cursinho ativado!")
        print("Você ganhará 1.0 de dinheiro a cada segundo enquanto o efeito estiver ativo.")

        # Exemplo de loop infinito para ganhar dinheiro a cada segundo
        while True:
            dinheiro.adicao(1.0)
            print(f"Dinheiro atual: {dinheiro.saldo}")
            time.sleep(1)