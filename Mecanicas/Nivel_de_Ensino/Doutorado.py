from Mecanicas.Skills import Skill

class Doutorado(Skill):
    def __init__(self):
        super().__init__()
        self.nivel_necessario = 20
        self.tempo_desbloqueio = 80

    def efeito_especial(self):
        print("Efeito especial do Doutorado ativado!")