from Mecanicas.Skills import Skill

class Mestrado(Skill):
    def __init__(self):
        super().__init__()
        self.nivel_necessario = 20
        self.tempo_desbloqueio = 40

    def efeito_especial(self):
        print("Efeito especial do Mestrado ativado!")