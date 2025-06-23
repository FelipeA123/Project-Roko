import os
import sys
import json
import time
from Mecanicas.Dinheiro import Dinheiro
from Progresso.Variaveis_Globais import CLASSES_ATIVAS
from Mecanicas.FazerRoko import FazerRoko
from Mecanicas.Eficiencia import Eficiencia

if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(sys.argv[0]))

CAMINHO_SAVE = os.path.join(BASE_DIR, "Progresso", "save.json")

class SalvarJogo:
    def __init__(self, dinheiro: Dinheiro, fazerroko: FazerRoko, eficiencia: Eficiencia):
        self.dinheiro = dinheiro
        self.fazerroko = fazerroko
        self.eficiencia = eficiencia
        self.SAVE_DIR = os.path.join(BASE_DIR, "Progresso")
        self.SAVE_PATH = os.path.join(self.SAVE_DIR, "save.json")

    def salvar(self):
        save_data = {
            "dinheiro": self.dinheiro.saldo,
            "classes_ativas": CLASSES_ATIVAS,
            "roko_criado": self.fazerroko.roko_criado,
            "progresso_roko" : self.fazerroko.progresso_roko,
            "eficiencia_itens": [item["ativo"] for item in self.eficiencia.itens]
            # Adicione outros dados do jogo aqui
        }
        os.makedirs(self.SAVE_DIR, exist_ok=True)  # Garante que a pasta existe
        with open(self.SAVE_PATH, "w") as f:
            json.dump(save_data, f)
        print("Progresso salvo!")

    def salvar_periodicamente(self, intervalo=60):
        while True:
            self.salvar()
            time.sleep(intervalo)
