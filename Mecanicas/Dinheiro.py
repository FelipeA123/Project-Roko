import json
import os
import sys

if getattr(sys, 'frozen', False):
    BASE_DIR = sys._MEIPASS
else:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
class Dinheiro():
    def __init__(self):
        self.saldo = 0.0
        self.quantia_dinheiro = 0.0
        self.carregar_saldo()

    def carregar_saldo(self):
        caminho = os.path.join(BASE_DIR, "Progresso", "save.json")
        if os.path.exists(caminho):
            with open(caminho, "r") as f:
                try:
                    dados = json.load(f)
                    self.saldo = dados.get("dinheiro", 0.0)
                except Exception:
                    self.saldo = 0.0


    def adicao(self, valor: float):
        if valor > 0:
            self.saldo += valor
            return True
        return False
        
    def subtracao(self, valor: float):
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
            return True
        return False