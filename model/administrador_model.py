import os
import json


def carregar_administradores():
    if not os.path.exists("administradores.json"):
        with open("administradores.json", "w", encoding="utf-8") as arquivo:
            json.dump([], arquivo, indent=4)
        return []
    
    with open("administradores.json", "r", encoding="utf-8") as arquivo:
        try:
            return json.load(arquivo)
        except json.JSONDecodeError:
            return []


def salvar_administradores(lista_administradores):
    with open("administradores.json", "w", encoding="utf-8") as arquivo:
        json.dump(lista_administradores, arquivo, indent=4, ensure_ascii=False)