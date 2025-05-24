from Mecanicas.Skills import Skill

class Cursinho(Skill):
    def __init__(self):
        super().__init__()
        self.nivel_necessario = 15
        self.tempo_desbloqueio = 10

    def efeito_especial(self):
        print("Efeito especial do Cursinho ativado!")