from Progresso.Progresso_jogo import SalvarJogo
from Mecanicas.Dinheiro import Dinheiro

dinheiro = Dinheiro()
dinheiro.valor = 100.0

salvar = SalvarJogo(dinheiro)
# Para salvar a cada 1 minuto:
salvar.salvar_periodicamente(60)