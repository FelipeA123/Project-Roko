class Dinheiro():
    def __init__(self):
        self.valor = 0.0
        self.quantia_dinheiro = 0.0

    def adicao(self):
        self.valor += self.quantia_dinheiro
        
    def subtracao(self):
        if self.valor > self.quantia_dinheiro:
            self.valor -= self.quantia_dinheiro
            return True
            
        return False