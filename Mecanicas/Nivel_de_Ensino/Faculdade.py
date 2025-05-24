from Mecanicas.Skills import Skill

class Faculdade(Skill):
    def __init__(self):
        super().__init__()
        self.nivel_necessario = 20
        self.tempo_desbloqueio = 20

    def efeito_especial(self):
        print("Efeito especial da Faculdade ativado!")