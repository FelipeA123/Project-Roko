from Mecanicas.Dinheiro import Dinheiro

class Eficiencia():
    def __init__(self):
        self.eficiencia = 1.0
        self.itens = [
            {"nome": "cafe_aguado", "ativo": False, "quantidade": 0, "custo": 5.0, "modificador": 10.5},
            {"nome": "cafe_gourmet", "ativo": False, "quantidade": 0, "custo": 50.0, "modificador": 0.2},
            {"nome": "cafe_quantico", "ativo": False, "quantidade": 0, "custo": 200.0, "modificador": 0.3},

            {"nome": "poster_elon_musk", "ativo": False, "quantidade": 0, "custo": 10.0, "modificador": 0.1},
            {"nome": "poster_steve_jobs", "ativo": False, "quantidade": 0, "custo": 30.0, "modificador": 0.2},
            {"nome": "poster_linus_torvalds", "ativo": False, "quantidade": 0, "custo": 100.0, "modificador": 0.3},

            {"nome": "teclado_mecanico", "ativo": False, "quantidade": 0, "custo": 50.0, "modificador": 0.1},
            {"nome": "teclado_gamer", "ativo": False, "quantidade": 0, "custo": 200.0, "modificador": 0.2},
            {"nome": "teclado_ergonomico", "ativo": False, "quantidade": 0, "custo": 300.0, "modificador": 0.3},

            {"nome": "monitor_led", "ativo": False, "quantidade": 0, "custo": 300.0, "modificador": 1.1},
            {"nome": "monitor_curvado", "ativo": False, "quantidade": 0, "custo": 1000.0, "modificador": 0.4},
            {"nome": "monitor_oculus_rift", "ativo": False, "quantidade": 0, "custo": 2000.0, "modificador": 0.6},

            {"nome": "cadeira_escritorio", "ativo": False, "quantidade": 0, "custo": 300.0, "modificador": 0.2},
            {"nome": "cadeira_gamer", "ativo": False, "quantidade": 0, "custo": 1000.0, "modificador": 0.4},
            {"nome": "cadeira_bola_de_exercicio", "ativo": False, "quantidade": 0, "custo": 2000.0, "modificador": 0.6},

            {"nome": "computador_dos_pais", "ativo": False, "quantidade": 0, "custo": 800.0, "modificador": 0.3},
            {"nome": "computador_gamer", "ativo": False, "quantidade": 0, "custo": 3000.0, "modificador": 0.6},
            {"nome": "computador_da_NASA", "ativo": False, "quantidade": 0, "custo": 8000.0, "modificador": 9.9},

            {"nome": "meias_programador", "ativo": False, "quantidade": 0, "custo": 50.0, "modificador": 0.3},
            {"nome": "patinho_debugger", "ativo": False, "quantidade": 0, "custo": 20.0, "modificador": 0.3},
            {"nome": "caneca_programador", "ativo": False, "quantidade": 0, "custo": 40.0, "modificador": 0.3},
        ]

    def atualizar_eficiencia(self):
        """Recalcula eficiência baseando-se na soma dos modificadores * quantidade.

        Mantemos `ativo` por compatibilidade, mas o valor determinante agora é
        `quantidade` (int)."""
        base = 1.0
        for item in self.itens:
            qty = item.get("quantidade", 0)
            if qty > 0:
                base += item["modificador"] * qty
            else:
                # manter campo `ativo` coerente com `quantidade`
                item["ativo"] = False
        self.eficiencia = base

    def comprar_item(self, nome_item: str, dinheiro: Dinheiro, quantidade: int = 1, retornar_quantidade: bool = False):
        """Tenta comprar `quantidade` cópias do item `nome_item`.

        - Se `retornar_quantidade` for False (padrão) retorna booleano: True se ao menos
          uma unidade foi comprada, False caso contrário (compatível com código antigo).
        - Se `retornar_quantidade` for True retorna o número de unidades compradas (int).
        """
        if quantidade <= 0:
            return 0 if retornar_quantidade else False

        for item in self.itens:
            if item["nome"] == nome_item:
                compradas = 0
                for _ in range(quantidade):
                    if dinheiro.subtracao(item["custo"]):
                        item["quantidade"] = item.get("quantidade", 0) + 1
                        item["ativo"] = True
                        compradas += 1
                    else:
                        break

                if compradas > 0:
                    self.atualizar_eficiencia()

                if retornar_quantidade:
                    return compradas
                return True if compradas > 0 else False

        return 0 if retornar_quantidade else False

    def comprar_max(self, nome_item: str, dinheiro: Dinheiro):
        """Compra o máximo possível do item até o dinheiro acabar. Retorna quantidade comprada."""
        for item in self.itens:
            if item["nome"] == nome_item:
                compradas = 0
                while dinheiro.subtracao(item["custo"]):
                    item["quantidade"] = item.get("quantidade", 0) + 1
                    item["ativo"] = True
                    compradas += 1

                if compradas > 0:
                    self.atualizar_eficiencia()
                return compradas

        return 0