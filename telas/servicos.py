#import customtkinter as ctk


#def tela_servicos(container):

#    titulo = ctk.CTkLabel(
#        container,
#        text="Serviços",
#        font=("Arial", 28, "bold")
#    )

#    titulo.pack(
#        anchor="w",
#        padx=32,
#        pady=30
#    )

import customtkinter as ctk
from tkinter import messagebox
from model.servicos_model import carregar_ordens, salvar_ordens



# ==================================================
# TELA DE SERVIÇOS
# ==================================================

def tela_servicos(container):

    # ==================================================
    # TÍTULO
    # ==================================================

    titulo = ctk.CTkLabel(
        container,
        text="Serviços",
        font=("Arial", 28, "bold")
    )

    titulo.pack(
        anchor="w",
        padx=32,
        pady=(20, 10)
    )

    # ==================================================
    # DADOS DA ORDEM DE SERVIÇO
    # ==================================================

    dados = ctk.CTkFrame(container)

    dados.pack(
        fill="x",
        padx=32,
        pady=5
    )

    # ==================================================
    # NÚMERO DA OS
    # ==================================================

    ctk.CTkLabel(
        dados,
        text="Nº da OS:"
    ).grid(
        row=0,
        column=0,
        padx=10,
        pady=8
    )

    # Carrega as OS existentes
    ordens = carregar_ordens()

    # Define o próximo número
    proximo_numero = len(ordens) + 1

    numero_os = ctk.CTkLabel(
        dados,
        text=f"{proximo_numero:04d}"
    )

    numero_os.grid(
        row=0,
        column=1,
        padx=10,
        pady=8
    )

    # ==================================================
    # CLIENTE
    # ==================================================

    ctk.CTkLabel(
        dados,
        text="Cliente:"
    ).grid(
        row=0,
        column=2,
        padx=10,
        pady=8
    )

    cliente = ctk.CTkEntry(
        dados,
        width=250,
        placeholder_text="Nome do cliente"
    )

    cliente.grid(
        row=0,
        column=3,
        padx=10,
        pady=8
    )

    # ==================================================
    # TIPO DO MOTOR
    # ==================================================

    ctk.CTkLabel(
        dados,
        text="Tipo do motor:"
    ).grid(
        row=1,
        column=0,
        padx=10,
        pady=8
    )

    motor = ctk.CTkEntry(
        dados,
        width=250,
        placeholder_text="Tipo do motor"
    )

    motor.grid(
        row=1,
        column=1,
        columnspan=3,
        padx=10,
        pady=8,
        sticky="w"
    )

    # ==================================================
    # DATA DE ENTRADA
    # ==================================================

    ctk.CTkLabel(
        dados,
        text="Data de entrada:"
    ).grid(
        row=2,
        column=0,
        padx=10,
        pady=8
    )

    data_entrada = ctk.CTkEntry(
        dados,
        width=150,
        placeholder_text="DD/MM/AAAA"
    )

    data_entrada.grid(
        row=2,
        column=1,
        padx=10,
        pady=8
    )

    # ==================================================
    # DATA DE ENTREGA
    # ==================================================

    ctk.CTkLabel(
        dados,
        text="Previsão de entrega:"
    ).grid(
        row=2,
        column=2,
        padx=10,
        pady=8
    )

    data_entrega = ctk.CTkEntry(
        dados,
        width=150,
        placeholder_text="DD/MM/AAAA"
    )

    data_entrega.grid(
        row=2,
        column=3,
        padx=10,
        pady=8
    )

    # ==================================================
    # TÍTULO DOS SERVIÇOS
    # ==================================================

    titulo_servicos = ctk.CTkLabel(
        container,
        text="Serviços realizados",
        font=("Arial", 20, "bold")
    )

    titulo_servicos.pack(
        anchor="w",
        padx=32,
        pady=(10, 5)
    )

    # ==================================================
    # ÁREA COM ROLAGEM
    # ==================================================

    tabela = ctk.CTkScrollableFrame(
        container,
        height=230
    )

    tabela.pack(
        fill="x",
        expand=True,
        padx=32,
        pady=5
    )

    # ==================================================
    # CABEÇALHO DA TABELA
    # ==================================================

    ctk.CTkLabel(
        tabela,
        text="Serviço",
        font=("Arial", 13, "bold")
    ).grid(
        row=0,
        column=0,
        padx=10,
        pady=8
    )

    ctk.CTkLabel(
        tabela,
        text="Quantidade",
        font=("Arial", 13, "bold")
    ).grid(
        row=0,
        column=1,
        padx=10,
        pady=8
    )

    ctk.CTkLabel(
        tabela,
        text="Valor",
        font=("Arial", 13, "bold")
    ).grid(
        row=0,
        column=2,
        padx=10,
        pady=8
    )

    ctk.CTkLabel(
        tabela,
        text="Subtotal",
        font=("Arial", 13, "bold")
    ).grid(
        row=0,
        column=3,
        padx=10,
        pady=8
    )

    # ==================================================
    # LISTA DE SERVIÇOS
    # ==================================================

    servicos = [
        "Retífica de sedes de válvulas",
        "Retífica de válvulas",
        "Esmerilhar válvulas",
        "Lavagem e montagem do cabeçote",
        "Solda",
        "Plainar face do cabeçote",
        "Plainar base do cabeçote",
        "Descarbonização do cabeçote",
        "Trocar guias de válvulas",
        "Trocar retentores de válvulas",
        "Calibragem de válvulas",
        "Teste de trincas do cabeçote",
        "Extrair parafusos",
        "Rosca de velas",
        "Restaurar face do cabeçote",
        "Alinhamento de mancal",
        "Trocar sedes de válvulas",
        "Restaurar base da carcaça",
        "Retificar cilindro",
        "Plainar face do bloco",
        "Ajustar mancais do bloco",
        "Brunir cilindro",
        "Polir virabrequim",
        "Retificar virabrequim",
        "Alinhar biela",
        "Colocar biela no pistão",
        "Embuchar biela",
        "Lavagem do motor",
        "Montagem do motor"
    ]

    # ==================================================
    # CAMPOS DOS SERVIÇOS
    # ==================================================

    campos = []

    for linha, servico in enumerate(servicos, start=1):

        nome_servico = ctk.CTkLabel(
            tabela,
            text=servico,
            anchor="w",
            width=300
        )

        nome_servico.grid(
            row=linha,
            column=0,
            padx=10,
            pady=4,
            sticky="w"
        )

        quantidade = ctk.CTkEntry(
            tabela,
            width=90,
            placeholder_text="0"
        )

        quantidade.grid(
            row=linha,
            column=1,
            padx=10,
            pady=4
        )

        valor = ctk.CTkEntry(
            tabela,
            width=110,
            placeholder_text="0,00"
        )

        valor.grid(
            row=linha,
            column=2,
            padx=10,
            pady=4
        )

        subtotal = ctk.CTkLabel(
            tabela,
            text="R$ 0,00",
            width=110
        )

        subtotal.grid(
            row=linha,
            column=3,
            padx=10,
            pady=4
        )

        # Guardamos também o nome do serviço
        campos.append(
            (
                servico,
                quantidade,
                valor,
                subtotal
            )
        )

    # ==================================================
    # VALOR TOTAL
    # ==================================================

    total_label = ctk.CTkLabel(
        container,
        text="Valor total: R$ 0,00",
        font=("Arial", 20, "bold")
    )

    total_label.pack(
        anchor="e",
        padx=32,
        pady=5
    )

    # ==================================================
    # FUNÇÃO PARA CALCULAR O TOTAL
    # ==================================================

    def calcular_total():

        total = 0

        for servico, quantidade, valor, subtotal in campos:

            try:

                qtd = float(
                    quantidade.get().replace(",", ".")
                )

                preco = float(
                    valor.get().replace(",", ".")
                )

                resultado = qtd * preco

                subtotal.configure(
                    text=f"R$ {resultado:.2f}".replace(".", ",")
                )

                total += resultado

            except ValueError:

                subtotal.configure(
                    text="R$ 0,00"
                )

        total_label.configure(
            text=f"Valor total: R$ {total:.2f}".replace(".", ",")
        )

        return total

    # ==================================================
    # BOTÃO CALCULAR
    # ==================================================

    botao_calcular = ctk.CTkButton(
        container,
        text="Calcular total",
        command=calcular_total
    )

    botao_calcular.pack(
        anchor="e",
        padx=32,
        pady=5
    )

    # ==================================================
    # FUNÇÃO PARA LIMPAR O FORMULÁRIO
    # ==================================================

    def limpar_formulario():

        cliente.delete(0, "end")
        motor.delete(0, "end")
        data_entrada.delete(0, "end")
        data_entrega.delete(0, "end")

        for servico, quantidade, valor, subtotal in campos:

            quantidade.delete(0, "end")
            valor.delete(0, "end")

            subtotal.configure(
                text="R$ 0,00"
            )

        total_label.configure(
            text="Valor total: R$ 0,00"
        )

    # ==================================================
    # FUNÇÃO PARA FINALIZAR A ORDEM DE SERVIÇO
    # ==================================================

    def finalizar_os():

        # ----------------------------------------------
        # PEGA OS DADOS DIGITADOS
        # ----------------------------------------------

        nome_cliente = cliente.get().strip()
        tipo_motor = motor.get().strip()
        entrada = data_entrada.get().strip()
        entrega = data_entrega.get().strip()

        # ----------------------------------------------
        # VALIDAÇÃO
        # ----------------------------------------------

        if not nome_cliente:

            messagebox.showwarning(
                "Atenção",
                "Informe o nome do cliente."
            )

            return

        if not tipo_motor:

            messagebox.showwarning(
                "Atenção",
                "Informe o tipo do motor."
            )

            return

        if not entrada:

            messagebox.showwarning(
                "Atenção",
                "Informe a data de entrada."
            )

            return

        if not entrega:

            messagebox.showwarning(
                "Atenção",
                "Informe a previsão de entrega."
            )

            return

        # ----------------------------------------------
        # CALCULA O TOTAL
        # ----------------------------------------------

        total = 0

        lista_servicos = []

        for servico, quantidade, valor, subtotal in campos:

            texto_quantidade = quantidade.get().strip()
            texto_valor = valor.get().strip()

            # Se os dois campos estiverem vazios,
            # significa que o serviço não foi utilizado.

            if not texto_quantidade and not texto_valor:
                continue

            try:

                qtd = float(
                    texto_quantidade.replace(",", ".")
                )

                preco = float(
                    texto_valor.replace(",", ".")
                )

            except ValueError:

                messagebox.showwarning(
                    "Atenção",
                    f"Verifique os valores do serviço:\n{servico}"
                )

                return

            if qtd <= 0:

                messagebox.showwarning(
                    "Atenção",
                    f"A quantidade do serviço deve ser maior que zero:\n{servico}"
                )

                return

            if preco < 0:

                messagebox.showwarning(
                    "Atenção",
                    f"O valor do serviço não pode ser negativo:\n{servico}"
                )

                return

            resultado = qtd * preco

            lista_servicos.append(
                {
                    "nome": servico,
                    "quantidade": qtd,
                    "valor": preco,
                    "subtotal": resultado
                }
            )

            total += resultado

        # ----------------------------------------------
        # VERIFICA SE EXISTE PELO MENOS UM SERVIÇO
        # ----------------------------------------------

        if not lista_servicos:

            messagebox.showwarning(
                "Atenção",
                "Informe pelo menos um serviço."
            )

            return

        # ----------------------------------------------
        # CARREGA AS ORDENS EXISTENTES
        # ----------------------------------------------

        ordens = carregar_ordens()

        # ----------------------------------------------
        # DEFINE O NÚMERO DA NOVA OS
        # ----------------------------------------------

        novo_numero = len(ordens) + 1

        # ----------------------------------------------
        # CRIA A NOVA ORDEM DE SERVIÇO
        # ----------------------------------------------

        nova_os = {
            "numero_os": novo_numero,
            "cliente": nome_cliente,
            "motor": tipo_motor,
            "data_entrada": entrada,
            "data_entrega": entrega,
            "servicos": lista_servicos,
            "total": total
        }

        # ----------------------------------------------
        # ADICIONA A OS À LISTA
        # ----------------------------------------------

        ordens.append(nova_os)

        # ----------------------------------------------
        # SALVA NO JSON
        # ----------------------------------------------

        try:

            salvar_ordens(ordens)

        except Exception as erro:

            messagebox.showerror(
                "Erro",
                f"Não foi possível salvar a ordem de serviço.\n\n{erro}"
            )

            return

        # ----------------------------------------------
        # MOSTRA MENSAGEM DE SUCESSO
        # ----------------------------------------------

        messagebox.showinfo(
            "Sucesso",
            f"Ordem de Serviço Nº {novo_numero:04d} "
            f"finalizada com sucesso!"
        )

        # ----------------------------------------------
        # LIMPA O FORMULÁRIO
        # ----------------------------------------------

        limpar_formulario()

        # ----------------------------------------------
        # ATUALIZA O NÚMERO DA PRÓXIMA OS
        # ----------------------------------------------

        numero_os.configure(
            text=f"{novo_numero + 1:04d}"
        )

    # ==================================================
    # BOTÃO FINALIZAR
    # ==================================================

    botao_finalizar = ctk.CTkButton(
        container,
        text="Finalizar Ordem de Serviço",
        height=40,
        command=finalizar_os
    )

    botao_finalizar.pack(
        padx=32,
        pady=(5, 20)
    )



