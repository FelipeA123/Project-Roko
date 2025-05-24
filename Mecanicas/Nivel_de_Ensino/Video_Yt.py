from Mecanicas.Skills import Skill

class VideoYoutube(Skill):
    def __init__(self):
        super().__init__()
        self.nivel_necessario = 10
        self.tempo_desbloqueio = 5

    def efeito_especial(self):
        # Implemente o efeito especial aqui
        print("Efeito especial do VideoYoutube ativado!")