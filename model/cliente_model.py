import json
import os

#----------------------------------------------------------
# FUNÇÕES DO BANCO DE DADOS (JSON)
#----------------------------------------------------------
def carregar_clientes():
    if not os.path.exists("clientes.json"):
        with open("clientes.json", "w", encoding="utf-8") as arquivo:
            json.dump([], arquivo, indent=4)
        return []
    with open("clientes.json", "r", encoding="utf-8") as arquivo:
        try:
            return json.load(arquivo)
        except json.JSONDecodeError:
            return []

def salvar_clientes(lista_clientes):
    with open("clientes.json", "w", encoding="utf-8") as arquivo:
        json.dump(lista_clientes, arquivo, indent=4, ensure_ascii=False)
