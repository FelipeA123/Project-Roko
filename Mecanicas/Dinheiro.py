import json
import os

class Dinheiro():
    def __init__(self):
        self.saldo = 0.0
        self.quantia_dinheiro = 0.0
        self.carregar_saldo()

    def carregar_saldo(self):
        caminho = os.path.join("Progresso", "save.json")
        if os.path.exists(caminho):
            with open(caminho, "r") as f:
                try:
                    dados = json.load(f)
                    self.saldo = dados.get("dinheiro", 0.0)
                except Exception:
                    self.saldo = 0.0

    def adicao(self, valor: float):
        if valor <= 0:
            print("A quantia digitada deve ser maior que zero.\n")
            return False
        else:
            self.saldo += valor
            return True
        
    def subtracao(self, valor:float):
        if valor <= 0:
            print("A quantia digitada deve ser maior que zero.\n")
            return False
        elif self.saldo >= valor:
            self.saldo -= valor
            return True
        else:
            print("Saldo insuficiente. Continue trabalhando para aumentar seu saldo.\n")
            return False