import json
import time
from Mecanicas.dinheiro import Dinheiro
from Mecanicas.Skills import CLASSES_ATIVAS

class SalvarJogo:
    def __init__(self, dinheiro: Dinheiro):
        self.dinheiro = dinheiro

    def salvar(self):
        save_data = {
            "dinheiro": self.dinheiro.saldo,
            "classes_ativas": CLASSES_ATIVAS
            # Adicione outros dados do jogo aqui
        }
        with open("Progresso/save.json", "w") as f:
            json.dump(save_data, f)
        print("Progresso salvo!")

    def salvar_periodicamente(self, intervalo=60):
        while True:
            self.salvar()
            time.sleep(intervalo)
