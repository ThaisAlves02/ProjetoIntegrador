import re
from model.cliente_model import carregar_clientes, salvar_clientes

def validar_email(email):
    if not email:
        return True
    padrao = r"^[\w\.\-]+@[\w\-]+\.[a-zA-Z]{2,}$"
    return re.match(padrao, email) is not None

def validar_telefone(telefone):
    padrao = r"^(\(\d{2}\)\s?)?\d{4,5}-?\d{4}$"
    return re.match(padrao, telefone) is not None

def listar_clientes_controller():
    return carregar_clientes()

def cadastrar_cliente_controller(nome, sobrenome, telefone, endereco, email, cpf):
    if not nome or not sobrenome or not telefone or not cpf:
        return False, "Campos com asterisco (*) são obrigatórios."

    if not validar_email(email):
        return False, "E-mail inválido. Use o formato nome@dominio.com"

    if not validar_telefone(telefone):
        return False, "Telefone inválido. Use (85) 99999-9999 ou 85999999999"

    novo_cliente = {
        "Nome": nome,
        "Sobrenome": sobrenome,
        "Telefone": telefone,
        "Endereço": endereco if endereco else "Não informado",
        "Email": email,
        "CPF": cpf
    }

    lista_atual = carregar_clientes()
    lista_atual.append(novo_cliente)
    salvar_clientes(lista_atual)
    return True, "Cliente cadastrado com sucesso!"

def excluir_cliente_controller(cliente_para_deletar):
    lista_atual = carregar_clientes()

    for cliente in lista_atual:
        if cliente['Nome'] == cliente_para_deletar['Nome'] and cliente['Telefone'] == cliente_para_deletar['Telefone']:
            lista_atual.remove(cliente)
            break  

    salvar_clientes(lista_atual)
    return True

#----------------------------------------------------------
# ATUALIZAR CLIENTE
#----------------------------------------------------------
def atualizar_cliente_controller(telefone_antigo, nome, sobrenome, telefone, endereco, email, cpf):
    if not nome or not sobrenome or not telefone or not cpf:
        return False, "Campos com asterisco (*) são obrigatórios."

    if not validar_email(email):
        return False, "E-mail inválido. Use o formato nome@dominio.com"

    if not validar_telefone(telefone):
        return False, "Telefone inválido. Use (85) 99999-9999 ou 85999999999"

    if telefone != telefone_antigo:
        lista_atual = carregar_clientes()
        for cliente in lista_atual:
            if cliente.get('Telefone') == telefone:
                return False, "Este novo número de telefone já está cadastrado para outro cliente."

    dados_atualizados = {
        "Nome": nome,
        "Sobrenome": sobrenome,
        "Telefone": telefone,
        "Endereço": endereco if endereco else "Não informado",
        "Email": email if email else "Não informado",
        "CPF": cpf
    }

    lista_atual = carregar_clientes()
    for index, cliente in enumerate(lista_atual):
        if cliente.get('Telefone') == telefone_antigo:
            lista_atual[index] = dados_atualizados
            salvar_clientes(lista_atual) # Salva a lista de volta no JSON
            return True, "Cliente atualizado com sucesso!"

    return False, "Cliente não encontrado para atualização."