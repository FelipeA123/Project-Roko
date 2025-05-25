import time
from Mecanicas.Skills import Skill
from Mecanicas.Dinheiro import Dinheiro
from Mecanicas.Skills import CLASSES_ATIVAS
class Faculdade(Skill):
    def __init__(self):
        super().__init__()
        self.nivel_necessario = 20
        self.tempo_desbloqueio = 20
    
    def ativar(self):
        self.ativo = True
        CLASSES_ATIVAS["Faculdade"] = True

    def desativar(self):
        self.ativo = False
        CLASSES_ATIVAS["Faculdade"] = False

    def efeito_especial(self):
        dinheiro = Dinheiro()
        dinheiro.adicao(500.0)
        print("Efeito especial da Faculdade ativado!")
        print("Você ganhará 1.0 de dinheiro a cada segundo enquanto o efeito estiver ativo.")
        segundos = 0
        ativo = True

        while True:
            if ativo:
                dinheiro.adicao(10.0)
                print(f"Dinheiro atual: {dinheiro.saldo}")
                segundos += 1
                if not CLASSES_ATIVAS["Mestrado"]:
                    if segundos >= 60:
                        if dinheiro.subtracao(350.0):
                            print("Taxa de 350 reais descontada para manter a Faculdade ativa.")
                            segundos = 0
                        else:
                            print("Saldo insuficiente para manter a Faculdade ativo. Aguardando saldo suficiente para reativar...")
                            ativo = False
                            segundos = 0
                else:
                    # Tenta descontar a taxa a cada segundo até conseguir
                    if dinheiro.subtracao(375.0):
                        print("Faculdade reativada!")
                        ativo = True
                    else:
                        print("Aguardando saldo suficiente para reativar a Faculdade...")
                time.sleep(1)