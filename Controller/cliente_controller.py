from models.cliente_model import carregar_clientes, salvar_clientes

def deletar_cliente(c=cliente):
    clientes = carregar_clientes()
    if messagebox.askyesno("Confirmar Exclusão", f"Deseja realmente excluir o cadastro de {c['Nome']}?"):
        lista_atual = carregar_clientes()
        lista_nova = []

        for cliente_da_vez in lista_atual:
            if cliente_da_vez['Nome'] == c['Nome'] and cliente_da_vez['Telefone'] == c['Telefone']:
                continue 
            lista_nova.append(cliente_da_vez)

        salvar_clientes(lista_nova)
        atualizar_tabela_visual()

def listar_clientes():
    return carregar_clientes()

def executar_cadastro():
    nome = entry_nome.get().strip()
    sobrenome = entry_sobrenome.get().strip()
    telefone = entry_telefone.get().strip()
    endereco = entry_endereco.get().strip()
    email = entry_email.get().strip()
    cpf = entry_cpf.get().strip()

    if not nome or not sobrenome or not telefone or not cpf:
        return("Erro", "Campos com asterisco (*) são obrigatórios.")
        

    if not validar_email(email):
        return("Erro", "Email inválido. Use o formato nome@dominio.com")
        

    if not validar_telefone(telefone):
        return("Erro", "Telefone inválido. Use (85) 99999-9999 ou 85999999999")
        

    novo_cliente = {
        "Nome": nome,
        "Sobrenome": sobrenome,
        "Telefone": telefone,
        "Endereço": endereco if endereco else "Não informado",
        "Email": email
    }

    lista_atual = carregar_clientes()
    lista_atual.append(novo_cliente)
    salvar_clientes(lista_atual)


def validar_email(email):
    if not email: # Se estiver vazio é válido já que é opcional.
        return True
    padrao = r"^[\w\.\-]+@[\w\-]+\.[a-zA-Z]{2,}$"
    return re.match(padrao, email) is not None


def validar_telefone(telefone):
    padrao = r"^(\(\d{2}\)\s?)?\d{4,5}-?\d{4}$"
    return re.match(padrao, telefone) is not None