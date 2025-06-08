import time
from Mecanicas.Skills import Skill
from Mecanicas.Dinheiro import Dinheiro
from Mecanicas.Skills import CLASSES_ATIVAS

class Cursinho(Skill):
    def __init__(self):
        super().__init__()
        self.nivel_necessario = 15
        self.tempo_desbloqueio = 10
    
    def ativar(self):
        self.ativo = True
        CLASSES_ATIVAS["Cursinho"] = True

    def desativar(self):
        self.ativo = False
        CLASSES_ATIVAS["Cursinho"] = False

    def efeito_especial(self):
        dinheiro = Dinheiro()
        dinheiro.adicao(200.0)
        print("Efeito especial do Cursinho ativado!")
        print("Você ganhará 1.0 de dinheiro a cada segundo enquanto o efeito estiver ativo.")
        segundos = 0
        ativo = True

        while True:
            if ativo:
                dinheiro.adicao(10.0)
                print(f"Dinheiro atual: {dinheiro.saldo}")
                segundos += 1
                if not CLASSES_ATIVAS["Faculdade"]:
                    if segundos >= 60:
                        if dinheiro.subtracao(50.0):
                            print("Taxa de 50 reais descontada para manter o Cursinho ativo.")
                            segundos = 0
                        else:
                            print("Saldo insuficiente para manter o Cursinho ativo. Aguardando saldo suficiente para reativar...")
                            ativo = False
                            segundos = 0
                else:
                    # Tenta descontar a taxa a cada segundo até conseguir
                    if dinheiro.subtracao(50.0):
                        print("Cursinho reativado!")
                        ativo = True
                    else:
                        print("Aguardando saldo suficiente para reativar o Cursinho...")
                time.sleep(1)