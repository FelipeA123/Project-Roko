import json
import time
from Mecanicas.Dinheiro import Dinheiro
from Mecanicas.Skills import CLASSES_ATIVAS
from Mecanicas.FazerRoko import FazerRoko

class SalvarJogo:
    def __init__(self, dinheiro: Dinheiro, fazerroko: FazerRoko):
        self.dinheiro = dinheiro
        self.fazerroko = fazerroko

    def salvar(self):
        save_data = {
            "dinheiro": self.dinheiro.saldo,
            "classes_ativas": CLASSES_ATIVAS,
            "roko_criado": self.fazerroko.roko_criado,
            "progresso_roko" : self.fazerroko.progresso_roko
            # Adicione outros dados do jogo aqui
        }
        with open("Progresso/save.json", "w") as f:
            json.dump(save_data, f)
        print("Progresso salvo!")

    def salvar_periodicamente(self, intervalo=60):
        while True:
            self.salvar()
            time.sleep(intervalo)
