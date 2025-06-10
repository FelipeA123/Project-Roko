import json
import os

# Variáveis globais
CLASSES_ATIVAS = {}
SALDO = 0.0
ROKO_CRIADO = False
PROGRESSO_ROKO = 0.0

CAMINHO_SAVE = os.path.join("Progresso", "save.json")

def carregar_dados():
    global CLASSES_ATIVAS, SALDO, ROKO_CRIADO, PROGRESSO_ROKO

    if os.path.exists(CAMINHO_SAVE):
        with open(CAMINHO_SAVE, "r") as f:
            try:
                dados = json.load(f)
                SALDO = dados.get("dinheiro", 0.0)
                CLASSES_ATIVAS = dados.get("classes_ativas", {})
                ROKO_CRIADO = dados.get("roko_criado", False)
                PROGRESSO_ROKO = dados.get("progresso_roko", 0.0)
            except Exception:
                # Em caso de erro, usa valores padrão
                SALDO = 0.0
                CLASSES_ATIVAS = {}
                ROKO_CRIADO = False
                PROGRESSO_ROKO = 0.0
    else:
        # Inicializa com valores padrão
        SALDO = 0.0
        CLASSES_ATIVAS = {
            "Doutorado": False,
            "Mestrado": False,
            "Faculdade": False,
            "Cursinho": False
        }
        ROKO_CRIADO = False
        PROGRESSO_ROKO = 0.0