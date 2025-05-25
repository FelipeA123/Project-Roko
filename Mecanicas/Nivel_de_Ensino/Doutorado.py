import time
from Mecanicas.Skills import Skill
from Mecanicas.Dinheiro import Dinheiro

class Doutorado(Skill):
    def __init__(self):
        super().__init__()
        self.nivel_necessario = 20
        self.tempo_desbloqueio = 80

    def efeito_especial(self):
        dinheiro = Dinheiro()
        dinheiro.adicao(1000.0)
        print("Efeito especial do Doutorado ativado!")
        print("Você ganhará 1.0 de dinheiro a cada segundo enquanto o efeito estiver ativo.")
        segundos = 0
        ativo = True

        while True:
            if ativo:
                dinheiro.adicao(100.0)
                print(f"Dinheiro atual: {dinheiro.saldo}")
                segundos += 1
                if segundos >= 60:
                    if dinheiro.subtracao(2000.0):
                        print("Taxa de 2000 reais descontada para manter o Doutorado ativo.")
                        segundos = 0
                    else:
                        print("Saldo insuficiente para manter o Doutorado ativo. Aguardando saldo suficiente para reativar...")
                        ativo = False
                        segundos = 0
            else:
                # Tenta descontar a taxa a cada segundo até conseguir
                if dinheiro.subtracao(2050.0):
                    print("Doutorado reativado!")
                    ativo = True
                else:
                    print("Aguardando saldo suficiente para reativar o Doutorado...")
            time.sleep(1)