import time
from Mecanicas.Skills import Skill
from Mecanicas.Dinheiro import Dinheiro
from Mecanicas.Skills import CLASSES_ATIVAS
class Mestrado(Skill):
    def __init__(self):
        super().__init__()
        self.nivel_necessario = 20
        self.tempo_desbloqueio = 40

    def ativar(self):
        self.ativo = True
        CLASSES_ATIVAS["Mestrado"] = True

    def desativar(self):
        self.ativo = False
        CLASSES_ATIVAS["Mestrado"] = False

    def efeito_especial(self):
        dinheiro = Dinheiro()
        dinheiro.adicao(1000.0)
        print("Efeito especial do Mestrado ativado!")
        print("Você ganhará 1.0 de dinheiro a cada segundo enquanto o efeito estiver ativo.")
        segundos = 0
        ativo = True

        while True:
            if ativo:
                dinheiro.adicao(50.0)
                print(f"Dinheiro atual: {dinheiro.saldo}")
                segundos += 1
                if not CLASSES_ATIVAS["Doutorado"]:
                # cobrar taxa do mestrado
                    if segundos >= 60:
                        if dinheiro.subtracao(1000.0):
                            print("Taxa de 1000 reais descontada para manter o Mestrado ativo.")
                            segundos = 0
                        else:
                            print("Saldo insuficiente para manter o Mestrado ativo. Aguardando saldo suficiente para reativar...")
                            ativo = False
                            segundos = 0
                else:
                    # Tenta descontar a taxa a cada segundo até conseguir
                    if dinheiro.subtracao(1050.0):
                        print("Mestrado reativado!")
                        ativo = True
                    else:
                        print("Aguardando saldo suficiente para reativar o Mestrado...")
                time.sleep(1)