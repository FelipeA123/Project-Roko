class Dinheiro():
    def __init__(self, valor):
        self.valor = 0.0

        def adicao(self, quantia_dinheiro):
            self.valor += quantia_dinheiro
        
        def subtracao(self, quantia_dinheiro):
            if self.valor > quantia_dinheiro:
                self.valor -= quantia_dinheiro
                return True
            
            return False


            