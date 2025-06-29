import time
import threading
from Mecanicas.Skills import Skill
from Mecanicas.Dinheiro import Dinheiro
from Mecanicas.Eficiencia import Eficiencia

from Progresso.Variaveis_Globais import CLASSES_ATIVAS


class Cursinho(Skill):
    def __init__(self):
        super().__init__()
        self.nivel_necessario = 15
        self.tempo_desbloqueio = 10
        self.taxa_inscricao = 50.0
        self._taxa_thread = None
        self._taxa_ativa = False
        global CLASSES_ATIVAS

    def efeito_especial(self):
        CLASSES_ATIVAS["Faculdade"] = True
        print("Faculdade desbloqueada, agora você pode fazer estágio para ganhar dinheiro.")

    def subir_nivel(self, eficiencia):
        super().subir_nivel(eficiencia)
        print("Você se esforça para prestar atenção apesar da lentidão")

    def ganhar_dinheiro(self, dinheiro: Dinheiro, eficiencia: Eficiencia):
        print("Realizando teste de usabilidade...")
        segundos = 0.0
        while segundos < 10:
            time.sleep(1)
            segundos += eficiencia.eficiencia
        dinheiro.adicao(50.0)
        print ("Você foi pago em 50 reais, nada mal!")

    def _pagamento_taxa_loop(self, dinheiro: Dinheiro):
        while self._taxa_ativa:
            time.sleep(60)
            self.pagar_taxa(dinheiro)

    def _iniciar_pagamento_taxa(self):
        if not self._taxa_ativa:
            self._taxa_ativa = True
            self._taxa_thread = threading.Thread(target=self._pagamento_taxa_loop, args=(Dinheiro(),), daemon=True)
            self._taxa_thread.start()

    def parar_pagamento_taxa(self):
        self._taxa_ativa = False
        print("Pagamento automático da taxa do Cursinho parado.")

    def pagar_taxa(self, dinheiro: Dinheiro):
        if not CLASSES_ATIVAS["Cursinho"]:
            return
        if CLASSES_ATIVAS["Faculdade"]:
            print("Faculdade ativa! Não é mais necessário pagar a inscrição do Cursinho.")
            return

        if dinheiro.subtracao(self.taxa_inscricao):
            print(f"Taxa de inscrição de R${self.taxa_inscricao:.2f} paga para manter o Cursinho ativo.")
        else:
            print("Saldo insuficiente para pagar a inscrição do Cursinho. Cursinho será desativado.")
            CLASSES_ATIVAS["Cursinho"] = False
            self.parar_pagamento_taxa()