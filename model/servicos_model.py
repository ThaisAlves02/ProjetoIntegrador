import json
import os

# ==================================================
# ARQUIVO ONDE AS ORDENS SERÃO SALVAS
# ==================================================

ARQUIVO_OS = "ordens_servico.json"
#ARQUIVO_OS = os.path.join(
 #   os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
  #  "ordens_servico.json"
#)

# ==================================================
# FUNÇÃO PARA CARREGAR AS ORDENS DE SERVIÇO
# ==================================================

def carregar_ordens():

    if not os.path.exists(ARQUIVO_OS):
        return []

    try:

        with open(ARQUIVO_OS, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)

    except (json.JSONDecodeError, FileNotFoundError):

        return []


# ==================================================
# FUNÇÃO PARA SALVAR AS ORDENS DE SERVIÇO
# ==================================================

def salvar_ordens(ordens):

    with open(
        ARQUIVO_OS,
        "w",
        encoding="utf-8"
    ) as arquivo:

        json.dump(
            ordens,
            arquivo,
            ensure_ascii=False,
            indent=4
        )