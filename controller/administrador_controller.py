import re
from telas.administradores import mostrar_erro, mostrar_aviso, mostrar_confirmar, mostrar_sucesso
from Model.administrador_model import carregar_administradores


def validar_administrador(nome, telefone, email, endereco):
    if not nome or not telefone or not endereco:
        mostrar_erro("Preencha os campos obrigatórios.")
        return

    if not validar_email(email):
        mostrar_erro("Email inválido. Use o formato nome@dominio.com")
        return

    if not validar_telefone(telefone):
        mostrar_erro("Telefone inválido. Use (85) 99999-9999 ou 85999999999")
        return


def verificacao_de_cadastro(nome, telefone, email):
    administradores = carregar_administradores()

    for adm in administradores:
        if adm["nome"].lower() == nome.lower():
            mostrar_erro("Já existe um administrador com esse nome!")
            return True

        if adm["telefone"] == telefone:
            mostrar_erro("Telefone já cadastrado!")
            return True

        if email and adm["email"].lower() == email.lower():
            mostrar_erro("E-mail já cadastrado!")
            return True

    return False


def validar_email(email):
        if not email: 
            return True
        padrao = r"^[\w\.\-]+@[\w\-]+\.[a-zA-Z]{2,}$"
        return re.match(padrao, email) is not None


def validar_telefone(telefone):
        padrao = r"^(\(\d{2}\) \s?)?\d{4,5}-?\d{4}$"
        return re.match(padrao, telefone) is not None