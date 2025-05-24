import Dinheiro as Dinheiro

class Eficiencia():
    def __init__(self):
        self.eficiencia = 1.0
        self.itens = [
            {"nome": "cafe_aguado", "ativo": False, "custo": 5.0, "modificador": 0.1},
            {"nome": "cafe_gourmet", "ativo": False, "custo": 50.0, "modificador": 0.2},
            {"nome": "cafe_quantico", "ativo": False, "custo": 200.0, "modificador": 0.3},

            {"nome": "poster_elon_musk", "ativo": False, "custo": 10.0, "modificador": 0.1},
            {"nome": "poster_steve_jobs", "ativo": False, "custo": 30.0, "modificador": 0.2},
            {"nome": "poster_linus_torvalds", "ativo": False, "custo": 100.0, "modificador": 0.3},

            {"nome": "teclado_mecanico", "ativo": False, "custo": 50.0, "modificador": 0.1},
            {"nome": "teclado_gamer", "ativo": False, "custo": 200.0, "modificador": 0.2},
            {"nome": "teclado_ergonomico", "ativo": False, "custo": 300.0, "modificador": 0.3},

            {"nome": "monitor_led", "ativo": False, "custo": 300.0, "modificador": 0.2},
            {"nome": "monitor_curvado", "ativo": False, "custo": 1000.0, "modificador": 0.4},
            {"nome": "monitor_oculus_rift", "ativo": False, "custo": 2000.0, "modificador": 0.6},

            {"nome": "cadeira_escritorio", "ativo": False, "custo": 300.0, "modificador": 0.2},
            {"nome": "cadeira_gamer", "ativo": False, "custo": 1000.0, "modificador": 0.4},
            {"nome": "cadeira_bola_de_exercicio", "ativo": False, "custo": 2000.0, "modificador": 0.6},

            {"nome": "computador_dos_pais", "ativo": False, "custo": 800.0, "modificador": 0.3},
            {"nome": "computador_gamer", "ativo": False, "custo": 3000.0, "modificador": 0.6},
            {"nome": "computador_da_NASA", "ativo": False, "custo": 8000.0, "modificador": 0.9},

            {"nome": "meias_programador", "ativo": False, "custo": 50.0, "modificador": 0.3},
            {"nome": "patinho_debugger", "ativo": False, "custo": 20.0, "modificador": 0.3},
            {"nome": "caneca_programador", "ativo": False, "custo": 40.0, "modificador": 0.3},
        ]

    def atualizar_eficiencia(self):
        base = 1.0
        for item in self.itens:
            if item["ativo"]:
                base += item["modificador"]
        self.eficiencia = base

    def comprar_item(self, nome_item, dinheiro):
        for item in self.itens:
            if item["nome"] == nome_item:
                if dinheiro.subtracao(item["custo"]):
                    item["ativo"] = True
                    self.atualizar_eficiencia()


