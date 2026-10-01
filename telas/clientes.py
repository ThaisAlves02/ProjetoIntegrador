import customtkinter as ctk
from tkinter import messagebox

#----------------------------------------------------------
# CÓDIGO NOVO DE IMPORTAÇÃO (Padrão MVC):
#----------------------------------------------------------
from controller.cliente_controller import (
    listar_clientes_controller,
    cadastrar_cliente_controller,
    excluir_cliente_controller,
    atualizar_cliente_controller 
)

#----------------------------------------------------------
# CONFIGURAÇÃO DE COR
#----------------------------------------------------------
cor_fundo = "#E9E9E9"
cor_frame = "#FFFFFF"
sub_titulo = "#52677F"
borda_frame = "#e0e0e0"
cor_botao = "#262753"


def tela_clientes(container):
    
    frame_conteudo = ctk.CTkFrame(container, fg_color="transparent")
    frame_conteudo.pack(expand=True, fill="both")

    titulo = ctk.CTkLabel(frame_conteudo,
        text="Clientes",
        font=("Arial", 28, "bold")
    ).pack(
        anchor="w",
        padx=32,
        pady=(30,0)
    )

    subtitulo = ctk.CTkLabel(
        frame_conteudo,
        text="Cadastro de clientes com nome, CPF, telefone, e-mail e endereço.",
        text_color=sub_titulo,
        font=("Arial", 14)
    ).pack( 
        anchor="w",
        padx=32,
        pady=0
    )

#----------------------------------------------------------
# DESIGN DA TABELA
#----------------------------------------------------------
    frame_cabecalho = ctk.CTkFrame(
        frame_conteudo,
        width=840,
        height=40,
        fg_color="#F8F9FA",
        border_width=1,
        border_color="#E0E0E0",
        corner_radius=10
    )
    frame_cabecalho.place(x=20, y=115)
    frame_cabecalho.pack_propagate(False)

    nome = ctk.CTkLabel(frame_cabecalho, text="Nome", font=ctk.CTkFont(size=14, weight="bold"), text_color="#52677F")
    nome.place(x=50, y=8)
   
    telefone = ctk.CTkLabel(frame_cabecalho, text="Telefone", font=ctk.CTkFont(size=14, weight="bold"), text_color="#52677F")
    telefone.place(x=170, y=8)

    endereco = ctk.CTkLabel(frame_cabecalho, text="Endereço", font=ctk.CTkFont(size=14, weight="bold"), text_color="#52677F")
    endereco.place(x=310, y=8)
   
    email = ctk.CTkLabel(frame_cabecalho, text="E-mail", font=ctk.CTkFont(size=14, weight="bold"), text_color="#52677F")
    email.place(x=448, y=8)
   
    cpf = ctk.CTkLabel(frame_cabecalho, text="CPF", font=ctk.CTkFont(size=14, weight="bold"), text_color="#52677F")
    cpf.place(x=580, y=8)

    acoes = ctk.CTkLabel(frame_cabecalho, text="Ações", font=ctk.CTkFont(size=14, weight="bold"), text_color="#52677F")
    acoes.place(x=700, y=8)
    
    frame_rolagem_linhas = ctk.CTkScrollableFrame(
        frame_conteudo,
        width=796,
        height=400,
        fg_color="transparent",
        orientation="vertical" 
    )
    frame_rolagem_linhas.place(x=32, y=165)

    componentes_das_linhas_da_tabela = []


#----------------------------------------------------------
# FUNÇÃO PARA ATUALIZAR A TABELA NA TELA
#----------------------------------------------------------
    def atualizar_tabela_visual():
        for c in componentes_das_linhas_da_tabela:
            c.destroy()
        componentes_das_linhas_da_tabela.clear()

        # CÓDIGO NOVO (Padrão MVC):
        clientes = listar_clientes_controller()

        if not clientes:
            frame_vazio = ctk.CTkFrame(
                frame_rolagem_linhas, 
                width=790,
                height=50, 
                fg_color="#FFFFFF", 
                border_width=1, 
                border_color="#E0E0E0", 
                corner_radius=10)
            frame_vazio.pack(pady=10, fill="x")
            componentes_das_linhas_da_tabela.append(frame_vazio)

            lbl_vazio = ctk.CTkLabel(
                frame_vazio, 
                text="Nenhum cliente cadastrado.", 
                font=ctk.CTkFont(size=14), 
                text_color="#7E8B9B")
            lbl_vazio.place(x=20, y=12)
            return
        
#----------------------------------------------------------
# LINHA DE DADOS / STATUS DA TABELA
#----------------------------------------------------------
        for _, cliente in enumerate(clientes): #Alterado o I por _
            frame_linha = ctk.CTkFrame(
                frame_rolagem_linhas, 
                height=50, 
                fg_color="#FFFFFF", 
                border_width=1, 
                border_color="#E0E0E0", 
                corner_radius=10)
            
            frame_linha.pack(pady=4, fill="x", padx=2)
            frame_linha.pack_propagate(False) 
            componentes_das_linhas_da_tabela.append(frame_linha)

            nome_completo = f"{cliente.get('Nome', '')} {cliente.get('Sobrenome', '')}"

            endereco_texto = cliente.get('Endereço', 'Não informado')
            if len(endereco_texto) > 22:
                endereco_texto = endereco_texto[:19] + "..."

            email_texto = cliente.get('Email', 'Não informado')
            if len(email_texto) > 22:
                email_texto = email_texto[:19] + "..."

            ctk.CTkLabel(frame_linha, text=nome_completo, font=("Arial", 13), text_color="black").place(x=30, y=12)  
            ctk.CTkLabel(frame_linha, text=cliente.get('Telefone', ''), font=("Arial", 13), text_color="black").place(x=150, y=12)
            ctk.CTkLabel(frame_linha, text=endereco_texto, font=("Arial", 13), text_color="black").place(x=287, y=12)
            ctk.CTkLabel(frame_linha, text=email_texto, font=("Arial", 13), text_color="black").place(x=390, y=12)
            ctk.CTkLabel(frame_linha, text=cliente.get('CPF', ''), font=("Arial", 13), text_color="black").place(x=535, y=12)

            # CÓDIGO NOVO (Padrão MVC):
            def deletar_cliente(c=cliente):
                if messagebox.askyesno("Confirmar Exclusão", f"Deseja realmente excluir o cadastro de {c['Nome']}?"):
                    excluir_cliente_controller(['Nome'], c['Telefone'])
                    atualizar_tabela_visual()

            botao_editar = ctk.CTkButton(
                frame_linha, text="Editar", font=("Arial", 12, "bold"),
                fg_color="#262753", hover_color="#1A1B3A", width=65, height=28,
                command=lambda c=cliente: novo_cadastro(cliente_para_editar=c) # Envia os dados do cliente para a função editar
            )
            botao_editar.place(x=635, y=11)

            botao_excluir = ctk.CTkButton(
                frame_linha, text="Excluir", font=("Arial", 12, "bold"),
                fg_color="#FF4D4D", hover_color="#CC0000", width=65, height=28,
                command=deletar_cliente
            )
            botao_excluir.place(x=710, y=11)

#----------------------------------------------------------
# FUNÇÃO BOTÃO NOVO CADASTRO
#----------------------------------------------------------
    def novo_cadastro(cliente_para_editar=None): # Adicionado o parâmetro opcional
        frame_cabecalho.place_forget()
        for c in componentes_das_linhas_da_tabela:
            c.pack_forget()

        frame_cadastro = ctk.CTkFrame(
            frame_conteudo, 
            width=500,
            height=460,
            fg_color=cor_frame,
            border_width=1,
            border_color=borda_frame,
            corner_radius=12
        )
        frame_cadastro.pack_propagate(False) 
        frame_cadastro.place(x=180, y=100)

        titulo = ctk.CTkLabel(
            frame_cadastro, 
            text="Cadastrar novo cliente", 
            font=("Arial", 22, "bold"), 
            text_color="black")
        titulo.pack(padx=50, pady=(25,15))

        entry_nome = ctk.CTkEntry(frame_cadastro, placeholder_text="Nome *", border_width=2, width=420, height=40, text_color="black", fg_color="white", border_color="gray")
        entry_nome.pack(pady=6)

        entry_sobrenome = ctk.CTkEntry(frame_cadastro, placeholder_text="Sobrenome *", border_width=2, width=420, height=40, text_color="black", fg_color="white", border_color="gray")
        entry_sobrenome.pack(pady=6)

        entry_telefone = ctk.CTkEntry(frame_cadastro, placeholder_text="Telefone (DDD) 99999-9999 *", border_width=2, width=420, height=40, text_color="black", fg_color="white", border_color="gray")
        entry_telefone.pack(pady=6)

        entry_endereco = ctk.CTkEntry(frame_cadastro, placeholder_text="Endereço", border_width=2, width=420, height=40, text_color="black", fg_color="white", border_color="gray")
        entry_endereco.pack(pady=6)

        entry_email = ctk.CTkEntry(frame_cadastro, placeholder_text="E-mail (Opcional)", border_width=2, width=420, height=40, text_color="black", fg_color="white", border_color="gray")
        entry_email.pack(pady=6)

        entry_cpf = ctk.CTkEntry(frame_cadastro, placeholder_text="CPF *", border_width=2, width=420, height=40, text_color="black", fg_color="white", border_color="gray")
        entry_cpf.pack(pady=6)

        # CÓDIGO NOVO (Padrão MVC):
        def executar_cadastro():
            nome = entry_nome.get().strip()
            sobrenome = entry_sobrenome.get().strip()
            telefone = entry_telefone.get().strip()
            endereco = entry_endereco.get().strip()
            email = entry_email.get().strip()
            cpf = entry_cpf.get().strip()

            sucesso, mensagem = cadastrar_cliente_controller(
                nome, sobrenome, telefone, endereco, email, cpf
            )

            if sucesso:
                messagebox.showinfo("Sucesso", mensagem)
                frame_cadastro.destroy()
                frame_cabecalho.place(x=32, y=115)
                atualizar_tabela_visual()
            else:
                messagebox.showerror("Erro", mensagem)

        def cancelar():
            frame_cadastro.destroy()
            frame_cabecalho.place(x=32, y=115)

            for c in componentes_das_linhas_da_tabela:
                c.pack(pady=4, fill="x", padx=2)

        # Botão Cadastrar
        cadastrar_botao = ctk.CTkButton(
            frame_cadastro,
            text="Cadastrar",
            font=ctk.CTkFont(size=14, weight="bold"),
            width=190,
            height=40,
            command=executar_cadastro
        )
        cadastrar_botao.place(x=57, y=383)

        # Botão Cancelar
        cancelar_botao = ctk.CTkButton(
            frame_cadastro,
            text="Cancelar",
            font=ctk.CTkFont(size=14, weight="bold"),
            width=190,
            height=40,
            fg_color="#555555",
            hover_color="#444444",
            command=cancelar
        )
        cancelar_botao.place(x=252, y=383)

        # ----------------------------------------------------------
        # FUNÇÃO EDITAR SEGUINDO O PADRÃO MVC (Ajustada)
        # ----------------------------------------------------------
        if cliente_para_editar:
            telefone_antigo = cliente_para_editar.get('Telefone')

            entry_nome.insert(0, cliente_para_editar.get('Nome', ''))
            entry_sobrenome.insert(0, cliente_para_editar.get('Sobrenome', ''))
            entry_telefone.insert(0, cliente_para_editar.get('Telefone', ''))
            entry_endereco.insert(0, cliente_para_editar.get('Endereço', ''))
            entry_email.insert(0, cliente_para_editar.get('Email', ''))
            entry_cpf.insert(0, cliente_para_editar.get('CPF', ''))

            def executar_atualizacao():
                nome_novo = entry_nome.get().strip()
                sobrenome_novo = entry_sobrenome.get().strip()
                telefone_novo = entry_telefone.get().strip()
                endereco_novo = entry_endereco.get().strip()
                email_novo = entry_email.get().strip()
                cpf_novo = entry_cpf.get().strip()

                sucesso, mensagem = atualizar_cliente_controller(
                    telefone_antigo, nome_novo, sobrenome_novo, telefone_novo, endereco_novo, email_novo, cpf_novo
                )

                if sucesso:
                    messagebox.showinfo("Sucesso", mensagem)
                    frame_cadastro.destroy()
                    frame_cabecalho.place(x=32, y=115)
                    atualizar_tabela_visual()
                else:
                    messagebox.showerror("Erro", mensagem)

            cadastrar_botao.configure(text="Salvar Alterações", command=executar_atualizacao)
            titulo.configure(text="Editar cliente")
        
    # BOTÃO NOVO
    novo = ctk.CTkButton(
        frame_conteudo,
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

    atualizar_tabela_visual()