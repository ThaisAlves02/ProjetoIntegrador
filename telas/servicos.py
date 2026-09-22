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

def tela_servicos(container):

    #=================================================================#
    # TÍTULO #
    #=================================================================#

    titulo = ctk.CTkLabel(
        container,
        text = "Serviços",
        font = ("Arial", 28, "bold")
    )

    titulo.pack(
        anchor = "w",
        padx = 32,
        pady = (20, 10)
    )

    #====================================================================#
    # DADOS DA ORDEM DE SERVIÇO #
    #====================================================================#

    
    dados = ctk.CTkFrame(container)

    dados.pack(
        fill="x",
        padx=32,
        pady=5
    )

    # Número da OS
    ctk.CTkLabel(
        dados,
        text="Nº da OS:"
    ).grid(
        row=0,
        column=0,
        padx=10,
        pady=8
    )

    numero_os = ctk.CTkLabel(
        dados,
        text="0001"
    )

    numero_os.grid(
        row=0,
        column=1,
        padx=10,
        pady=8
    )

    # Cliente
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

    # Tipo do motor
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

    # Data de entrada
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

    # Previsão de entrega
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
    # TÍTULO DA TABELA
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
        height=300
    )

    tabela.pack(
        fill="both",
        expand=True,
        padx=32,
        pady=5
    )

    # ==================================================
    # CABEÇALHO
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
    # SERVIÇOS
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

        campos.append(
            (quantidade, valor, subtotal)
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
    # FUNÇÃO PARA CALCULAR
    # ==================================================

    def calcular_total():

        total = 0

        for quantidade, valor, subtotal in campos:

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

                total = total + resultado

            except ValueError:

                subtotal.configure(
                    text="R$ 0,00"
                )

        total_label.configure(
            text=f"Valor total: R$ {total:.2f}".replace(".", ",")
        )

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
    # BOTÃO FINALIZAR
    # ==================================================

    botao_finalizar = ctk.CTkButton(
        container,
        text="Finalizar Ordem de Serviço",
        height=40
    )

    botao_finalizar.pack(
        padx=32,
        pady=(5, 20)
    )
