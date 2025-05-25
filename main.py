from Progresso.Progresso_jogo import SalvarJogo
from Mecanicas.Dinheiro import Dinheiro
from Fases.Fase1 import *

dinheiro = Dinheiro()
dinheiro.valor = 100.0

salvar = SalvarJogo(dinheiro)
# Para salvar a cada 1 minuto:
salvar.salvar_periodicamente(60)

fase_1 = Fase1()
fase_1.rodar_jogo()

