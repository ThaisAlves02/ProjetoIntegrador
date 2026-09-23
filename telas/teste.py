import customtkinter as ctk


def tela_administradores(container):

    # TESTE:
    administrador_teste = {
        "Nome":"Maria Silva castro Holanda Silva",
        "Telefone":"85 985694857",
        "Email": "mariarosarioalmeidacampos@gmail.com",
        "Endereço": "Rua Limoeironortesulleste nº 10",
        "Ações": "Zeladora"
    }

    def cortar_texto(texto, tamanho):

        if len(texto) > tamanho:
            return texto[:tamanho] + "..."

        return texto

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

    acoes.place(x=750, y=125)


    # DADOS DO ADMINISTRADOR DE TESTE

    nome_teste = ctk.CTkLabel(
    container,
    text=administrador_teste["Nome"],
    text_color="black",
    anchor="w",
    width=150,
    height=25
    )

    nome_teste.place(x=30, y=165)



    telefone_teste = ctk.CTkLabel(
    container,
    text=administrador_teste["Telefone"],
    text_color="black",
    anchor="w",
    width=150,
    height=25
)

    telefone_teste.place(x=200, y=165)



    email_teste = ctk.CTkLabel(
        container,
        text=administrador_teste["Email"],
        text_color="black"
    )
    email_teste.place(x=360, y=165)


    endereco_teste = ctk.CTkLabel(
        container,
        text=administrador_teste["Endereço"],
        text_color="black"
    )
    endereco_teste.place(x=540, y=165)


    acoes_teste = ctk.CTkLabel(
        container,
        text=administrador_teste["Ações"],
        text_color="black"
    )
    acoes_teste.place(x=750, y=165)

# =========================
# TEXTO COMPLETO
# =========================

    nome_completo = administrador_teste["Nome"]
    email_completo = administrador_teste["Email"]
    endereco_completo = administrador_teste["Endereço"]



# NOME

    nome_teste.configure(
        text=cortar_texto(nome_completo, 20)
    )


    def mostrar_nome(event):

        nome_teste.configure(
            text=nome_completo
        )

        # Esconde o telefone
        telefone_teste.place_forget()

        # Coloca o nome na frente
        nome_teste.lift()


    def esconder_nome(event):

        nome_teste.configure(
            text=cortar_texto(nome_completo, 20)
        )

        # Mostra o telefone novamente
        telefone_teste.place(
            x=200,
            y=165
        )


    nome_teste.bind("<Enter>", mostrar_nome)
    nome_teste.bind("<Leave>", esconder_nome)



# E-MAIL


    email_teste.configure(
        text=cortar_texto(email_completo, 25)
    )


    def mostrar_email(event):

        email_teste.configure(
            text=email_completo
        )

        # Esconde o endereço
        endereco_teste.place_forget()

        # Coloca o e-mail na frente
        email_teste.lift()


    def esconder_email(event):

        email_teste.configure(
            text=cortar_texto(email_completo, 25)
        )

        # Mostra o endereço novamente
        endereco_teste.place(
            x=540,
            y=165
        )


    email_teste.bind("<Enter>", mostrar_email)
    email_teste.bind("<Leave>", esconder_email)



# ENDEREÇO

    endereco_teste.configure(
        text=cortar_texto(endereco_completo, 25)
    )


    def mostrar_endereco(event):

        endereco_teste.configure(
            text=endereco_completo
        )

        # Esconde Ações
        acoes_teste.place_forget()

        # Coloca o endereço na frente
        endereco_teste.lift()


    def esconder_endereco(event):

        endereco_teste.configure(
            text=cortar_texto(endereco_completo, 25)
        )

        # Mostra Ações novamente
        acoes_teste.place(
            x=750,
            y=165
        )


    endereco_teste.bind("<Enter>", mostrar_endereco)
    endereco_teste.bind("<Leave>", esconder_endereco)




    # FUNÇÃO PARA ESCONDER A TABELA

    def esconder_tabela():

        # ESCONDE A TEBELA:
        nome.place_forget()
        telefone.place_forget()
        email.place_forget()
        endereco.place_forget()
        acoes.place_forget()

        # ESCONDE OS DADOS:

        nome_teste.place_forget()
        telefone_teste.place_forget()
        email_teste.place_forget()
        endereco_teste.place_forget()
        acoes_teste.place_forget()



    # FUNÇÃO PARA MOSTRAR A TABELA

    def mostrar_tabela():
        # MOSTRA A TABELA NOVAMENTE:

        nome.place(x=30, y=125)
        telefone.place(x=200, y=125)
        email.place(x=380, y=125)
        endereco.place(x=560, y=125)
        acoes.place(x=750, y=125)

        # MOSTRA OS DADOS NOVAMENTE:

        nome_teste.place(x=30, y=165)
        telefone_teste.place(x=200, y=165)
        email_teste.place(x=360, y=165)
        endereco_teste.place(x=540, y=165)
        acoes_teste.place(x=750, y=165)


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




