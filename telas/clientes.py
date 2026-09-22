import customtkinter as ctk
from tkinter import ttk

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

    titulo = ctk.CTkLabel(
        frame_conteudo,
        text="Clientes",
        font=("Arial", 28, "bold")
    )
    titulo.pack(
        anchor="w",
        padx=32,
        pady=(30,0)
    )

    subtitulo = ctk.CTkLabel(
        frame_conteudo,
        text="Cadastro de clientes com nome, telefone, endereço, e-mail e CPF.",
        text_color=sub_titulo,
        font=("Arial", 14)
    )
    subtitulo.pack( 
        anchor="w",
        padx=32,
        pady=0
    )

#----------------------------------------------------------
# TABELA - NOME, TELEFONE, E-MAIL E AÇÕES
#----------------------------------------------------------
    nome = ctk.CTkLabel(
        frame_conteudo,
        text="Nome",
        font=ctk.CTkFont(size=15, weight="bold"),
        text_color="#52677F"
    )
    nome.place(x=100, y=125)
   
    telefone = ctk.CTkLabel(
        frame_conteudo,
        text="Telefone",
        font=ctk.CTkFont(size=15, weight="bold"),
        text_color="#52677F"
    )
    telefone.place(x=300, y=125)
   
    email = ctk.CTkLabel(
        frame_conteudo,
        text="E-mail",
        font=ctk.CTkFont(size=15, weight="bold"),
        text_color="#52677F"
    )
    email.place(x=530, y=125)
   
    acoes = ctk.CTkLabel(
        frame_conteudo,
        text="Ações",
        font=ctk.CTkFont(size=15, weight="bold"),
        text_color="#52677F"
    )
    acoes.place(x=750, y=125)
   
#----------------------------------------------------------
# FUNÇÃO BOTÃO NOVO
#----------------------------------------------------------
    def novo_cadastro():
   
        frame_cadastro = ctk.CTkFrame(
        frame_conteudo, 
        width=500,
        height=400,
        fg_color=cor_frame,
        border_width=1,
        border_color=borda_frame
        )
    
        frame_cadastro.pack_propagate(False) 
        
        frame_cadastro.pack(expand=True, padx=32, pady=(0, 32))

        titulo = ctk.CTkLabel(
            frame_cadastro,
            text="Cadastrar novo cliente",
            font=("Arial", 22, "bold")
        )
        titulo.pack(padx = 50, pady = (35,25))

        entry_nome = ctk.CTkEntry(
            frame_cadastro,
            placeholder_text="Nome",
            border_width=2,
            width=420,
            height=40,
            text_color="black",
            fg_color="white",
            border_color="gray",
        )
        entry_nome.pack(pady = 8)

        entry_sobrenome = ctk.CTkEntry(
            frame_cadastro,
            placeholder_text="Sobrenome",
            border_width=2,
            width=420,
            height=40,
            text_color="black",
            fg_color="white",
            border_color="gray",
        )
        entry_sobrenome.pack(pady = 8)

        entry_telefone = ctk.CTkEntry(
            frame_cadastro,
            placeholder_text="(DDD) 99999-9999",
            border_width=2,
            width=420,
            height=40,
            text_color="black",
            fg_color="white",
            border_color="gray",
        )
        entry_telefone.pack(pady = 8)

        entry_email = ctk.CTkEntry(
            frame_cadastro,
            placeholder_text="E-mail (Opcional)",
            border_width=2,
            width=420,
            height=40,
            text_color="black",
            fg_color="white",
            border_color="gray",
        )
        entry_email.pack(pady = 8)

        # Botão Cadastrar
        cadastrar_botao = ctk.CTkButton(
            frame_cadastro,
            text="Cadastrar",
            font=ctk.CTkFont(size=14, weight="bold"),
            width=190,
            height=40
        )
        cadastrar_botao.place(x= 57, y=320)
   
        # Botão Cancelar
        cancelar_botao = ctk.CTkButton(
            frame_cadastro,
            text="Cancelar",
            font=ctk.CTkFont(size=14, weight="bold"),
            width=190,
            height=40,
            fg_color="#555555",
            hover_color="#444444"
        )
        cancelar_botao.place(x=252, y=320)
   
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
