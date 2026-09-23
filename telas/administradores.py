import customtkinter as ctk


def tela_administradores(container):

    # TÍTULOS

    titulo3 = ctk.CTkLabel(
        container,
        text="Administradores",
        font=ctk.CTkFont(size=28, weight="bold"),
        text_color="black",
    )

    titulo3.place(x=30, y=40)


    titulo4 = ctk.CTkLabel(
        container,
        text="Cadastro de administradores com nome, telefone e e-mail.",
        font=ctk.CTkFont(size=15),
        text_color="#52677F"
    )

    titulo4.place(x=30, y=75)


    # TABELA

    nome = ctk.CTkLabel(
        container,
        text="Nome",
        font=ctk.CTkFont(size=15, weight="bold"),
        text_color="#52677F"
    )

    nome.place(x=30, y=125)


    telefone = ctk.CTkLabel(
        container,
        text="Telefone",
        font=ctk.CTkFont(size=15, weight="bold"),
        text_color="#52677F"
    )

    telefone.place(x=200, y=125)


    email = ctk.CTkLabel(
        container,
        text="E-mail",
        font=ctk.CTkFont(size=15, weight="bold"),
        text_color="#52677F"
    )

    email.place(x=380, y=125)


    endereco = ctk.CTkLabel(
        container,
        text="Endereço",
        font=ctk.CTkFont(size=15, weight="bold"),
        text_color="#52677F"
    )

    endereco.place(x=560, y=125)


    acoes = ctk.CTkLabel(
        container,
        text="Ações",
        font=ctk.CTkFont(size=15, weight="bold"),
        text_color="#52677F"
    )

    acoes.place(x=720, y=125)


    # FUNÇÃO PARA ESCONDER A TABELA

    def esconder_tabela():

        nome.place_forget()
        telefone.place_forget()
        email.place_forget()
        endereco.place_forget()
        acoes.place_forget()


    # FUNÇÃO PARA MOSTRAR A TABELA

    def mostrar_tabela():

        nome.place(x=30, y=125)
        telefone.place(x=200, y=125)
        email.place(x=380, y=125)
        endereco.place(x=560, y=125)
        acoes.place(x=720, y=125)


    # FUNÇÃO DO BOTÃO NOVO

    def novo_cadastro():

        # Esconde os títulos da tabela
        esconder_tabela()

        frame_cadastro = ctk.CTkFrame(
            container,
            width=645,
            height=395,
            fg_color="white",
            corner_radius=12
        )

        frame_cadastro.place(
            x=110,
            y=80
        )



        # TÍTULO DO FORMULÁRIO

        label_titulo = ctk.CTkLabel(
            frame_cadastro,
            text="Cadastrar Administrador",
            text_color="black",
            font=ctk.CTkFont(size=22, weight="bold")
        )

        label_titulo.place(x=30, y=25)


        # Nome

        label_nome = ctk.CTkLabel(
            frame_cadastro,
            text="Nome",
            text_color="black",
            font=ctk.CTkFont(size=14)
        )

        label_nome.place(x=30, y=80)


        entry_nome = ctk.CTkEntry(
            frame_cadastro,
            placeholder_text="Nome",
            border_width=0,
            width=400,
            height=35
        )

        entry_nome.place(x=30, y=105)


        # Telefone

        label_telefone = ctk.CTkLabel(
            frame_cadastro,
            text="Telefone",
            text_color="black",
            font=ctk.CTkFont(size=14)
        )

        label_telefone.place(x=30, y=155)


        entry_telefone = ctk.CTkEntry(
            frame_cadastro,
            placeholder_text="Telefone",
            border_width=0,
            width=400,
            height=35
        )

        entry_telefone.place(x=30, y=180)


        # E-mail

        label_email = ctk.CTkLabel(
            frame_cadastro,
            text="E-mail (Opcional)",
            text_color="black",
            font=ctk.CTkFont(size=14)
        )

        label_email.place(x=30, y=230)


        entry_email = ctk.CTkEntry(
            frame_cadastro,
            placeholder_text="E-mail",
            border_width=0,
            width=400,
            height=35
        )

        entry_email.place(x=30, y=255)


        # Botão Cadastrar

        def cadastrar():

            # Por enquanto apenas fecha o formulário
            # Depois vamos colocar aqui o Controller
            # para salvar os dados no JSON.

            frame_cadastro.destroy()
            mostrar_tabela()


        cadastrar_botao = ctk.CTkButton(
            frame_cadastro,
            text="Cadastrar",
            font=ctk.CTkFont(size=14, weight="bold"),
            width=190,
            height=40,
            command=cadastrar
        )

        cadastrar_botao.place(x=30, y=310)

        # FUNÇÃO CANCELAR:
        
        def cancelar_cadastro():
            frame_cadastro.destroy()
            mostrar_tabela()

        # Botão Cancelar

        cancelar_botao = ctk.CTkButton(
            frame_cadastro,
            text="Cancelar",
            font=ctk.CTkFont(size=14, weight="bold"),
            width=190,
            height=40,
            fg_color="#555555",
            hover_color="#444444",
            command=cancelar_cadastro
        )

        cancelar_botao.place(x=240, y=310)


    # BOTÃO NOVO

    novo = ctk.CTkButton(
        container,
        text="+ Novo",
        font=ctk.CTkFont(size=15, weight="bold"),
        width=100,
        height=40,
        fg_color="#008C9E",
        hover_color="#007A89",
        text_color="white",
        corner_radius=6,
        command=novo_cadastro
    )

    novo.place(x=750, y=35)