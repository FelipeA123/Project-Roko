from Mecanicas.Skills import *
from Mecanicas.Dinheiro import *
from Mecanicas.Eficiencia import *
from Personagens.Jogador import *
from Mecanicas.FazerRoko import *
from Mecanicas.Nivel_de_Ensino.Cursinho import *
from Mecanicas.Nivel_de_Ensino.Faculdade import *
from Mecanicas.Nivel_de_Ensino.Mestrado import *
from Mecanicas.Nivel_de_Ensino.Doutorado import *

class Fase1:
    def rodar_jogo(self):
        dinheiro = Dinheiro()
        skill = Skill()
        eficiencia = Eficiencia()
        fazerroko = FazerRoko()

        while not fazerroko.roko_criado:
            while not CLASSES_ATIVAS["Cursinho"]:
            