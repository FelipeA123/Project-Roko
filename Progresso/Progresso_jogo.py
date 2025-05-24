
class Progresso_Jogo():
    def __init__(self):
        self.fase_terminada = False
        self.progresso = 0.0

    def progresso_concluido(self):
        if self.progresso >= 100.0:
            self.fase_terminada = True
