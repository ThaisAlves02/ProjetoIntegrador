import customtkinter as ctk


def tela_administradores(container):

    # =========================================================
    # TÍTULOS
    # =========================================================

    titulo1 = ctk.CTkLabel(
        container,
        text="Administradores",
        font=ctk.CTkFont(size=28, weight="bold"),
        text_color="black",
    )

    titulo1.place(x=30, y=40)


    titulo2 = ctk.CTkLabel(
        container,
        text="Cadastro de administradores com nome, telefone e e-mail.",
        font=ctk.CTkFont(size=15),
        text_color="#52677F"
    )

    titulo2.place(x=30, y=75)


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


    # FUNÇÃO PARA CORTAR TEXTO

    def cortar_texto(texto, tamanho):

        if len(texto) > tamanho:
            return texto[:tamanho] + "..."

        return texto


    
    # LISTA DAS LINHAS DA TABELA
    
    # Aqui ficarão os widgets dos administradores que forem
    # adicionados posteriormente.

    linhas = []


    
    # ADICIONAR ADMINISTRADOR NA TABELA
    

    def adicionar_administrador(administrador, posicao):

        # DADOS
        
        nome_completo = administrador["Nome"]
        telefone_completo = administrador["Telefone"]
        email_completo = administrador["Email"]
        endereco_completo = administrador["Endereço"]

        y = 165 + (posicao * 45)


        # NOME
        
        nome_linha = ctk.CTkLabel(
            container,
            text=cortar_texto(nome_completo, 20),
            text_color="black",
            anchor="w",
            width=150,
            height=25
        )

        nome_linha.place(x=30, y=y)


        
        # TELEFONE
        

        telefone_linha = ctk.CTkLabel(
            container,
            text=telefone_completo,
            text_color="black",
            anchor="w",
            width=150,
            height=25
        )

        telefone_linha.place(x=200, y=y)


        # E-MAIL
    
        email_linha = ctk.CTkLabel(
            container,
            text=cortar_texto(email_completo, 25),
            text_color="black",
            anchor="w",
            width=150,
            height=25
        )

        email_linha.place(x=360, y=y)


        # ENDEREÇO
        

        endereco_linha = ctk.CTkLabel(
            container,
            text=cortar_texto(endereco_completo, 25),
            text_color="black",
            anchor="w",
            width=150,
            height=25
        )

        endereco_linha.place(x=540, y=y)


        
        # AÇÕES
        

        acoes_linha = ctk.CTkLabel(
            container,
            text=administrador["Ações"],
            text_color="black",
            anchor="w",
            width=100,
            height=25
        )

        acoes_linha.place(x=750, y=y)


        
        # BIND - NOME
        

        def mostrar_nome(event):

            nome_linha.configure(
                text=nome_completo
            )

            # Esconde o telefone
            telefone_linha.place_forget()

            # Coloca o nome na frente
            nome_linha.lift()


        def esconder_nome(event):

            nome_linha.configure(
                text=cortar_texto(nome_completo, 20)
            )

            # Mostra o telefone novamente
            telefone_linha.place(
                x=200,
                y=y
            )


        nome_linha.bind("<Enter>", mostrar_nome)
        nome_linha.bind("<Leave>", esconder_nome)


        
        # BIND - E-MAIL
        

        def mostrar_email(event):

            email_linha.configure(
                text=email_completo
            )

            # Esconde o endereço
            endereco_linha.place_forget()

            # Coloca o e-mail na frente
            email_linha.lift()


        def esconder_email(event):

            email_linha.configure(
                text=cortar_texto(email_completo, 25)
            )

            # Mostra o endereço novamente
            endereco_linha.place(
                x=540,
                y=y
            )


        email_linha.bind("<Enter>", mostrar_email)
        email_linha.bind("<Leave>", esconder_email)


        
        # BIND - ENDEREÇO
        

        def mostrar_endereco(event):

            endereco_linha.configure(
                text=endereco_completo
            )

            # Esconde Ações
            acoes_linha.place_forget()

            # Coloca o endereço na frente
            endereco_linha.lift()


        def esconder_endereco(event):

            endereco_linha.configure(
                text=cortar_texto(endereco_completo, 25)
            )

            # Mostra Ações novamente
            acoes_linha.place(
                x=750,
                y=y
            )


        endereco_linha.bind("<Enter>", mostrar_endereco)
        endereco_linha.bind("<Leave>", esconder_endereco)


    
        # GUARDA OS WIDGETS DA LINHA
        

        linhas.append({
            "nome": nome_linha,
            "telefone": telefone_linha,
            "email": email_linha,
            "endereco": endereco_linha,
            "acoes": acoes_linha
        })


    
    # FUNÇÃO PARA ESCONDER A TABELA
    

    def esconder_tabela():

        # ESCONDE OS TÍTULOS

        nome.place_forget()
        telefone.place_forget()
        email.place_forget()
        endereco.place_forget()
        acoes.place_forget()


        # ESCONDE OS DADOS

        for linha in linhas:

            linha["nome"].place_forget()
            linha["telefone"].place_forget()
            linha["email"].place_forget()
            linha["endereco"].place_forget()
            linha["acoes"].place_forget()


    
    # FUNÇÃO PARA MOSTRAR A TABELA
    

    def mostrar_tabela():

        # MOSTRA OS TÍTULOS

        nome.place(x=30, y=125)
        telefone.place(x=200, y=125)
        email.place(x=380, y=125)
        endereco.place(x=560, y=125)
        acoes.place(x=750, y=125)


        # MOSTRA OS DADOS

        for indice, linha in enumerate(linhas):

            y = 165 + (indice * 45)

            linha["nome"].place(
                x=30,
                y=y
            )

            linha["telefone"].place(
                x=200,
                y=y
            )

            linha["email"].place(
                x=360,
                y=y
            )

            linha["endereco"].place(
                x=540,
                y=y
            )

            linha["acoes"].place(
                x=750,
                y=y
            )


    # FUNÇÃO DO BOTÃO NOVO
    

    def novo_cadastro():

        # Esconde a tabela

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


        
        # NOME
        

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



        # TELEFONE
        

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


        
        # E-MAIL
        

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


        
        # BOTÃO CADASTRAR
        

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


        
        # FUNÇÃO CANCELAR
        

        def cancelar_cadastro():

            frame_cadastro.destroy()
            mostrar_tabela()


        
        # BOTÃO CANCELAR
        

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