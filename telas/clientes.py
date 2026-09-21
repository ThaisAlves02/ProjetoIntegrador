import customtkinter as ctk
from tkinter import ttk

#----------------------------------------------------------
# CONFIGURAÇÃO DE COR
#----------------------------------------------------------
cor_fundo = "#E9E9E9"
cor_frame = "#FFFFFF"
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
        font=("Arial", 14)
    )
    subtitulo.pack( 
        anchor="w",
        padx=32,
        pady=0
    )

    botao_novo_cadastro = ctk.CTkButton(
        frame_conteudo,
        text="Novo",
        fg_color= "#262753",
        font=("Arial", 14, "bold"),
        corner_radius= 8,
    )
    botao_novo_cadastro.pack(
        anchor="w",
        padx=32,
        pady=40
    )

    #----------------------------------------------------------
    # LISTA DE CLIENTES
    #----------------------------------------------------------

    frame_lista_clientes = ctk.CTkFrame(frame_conteudo)
    frame_lista_clientes.pack(padx=20, pady=15, fill="both", expand=True)

    colunas = ("nome", "telefone", "cpf", "email", "endereco", "acoes")
    tree = ttk.Treeview(frame_lista_clientes, columns=colunas, show="headings", height=10)

    tree.heading("nome", text="Nome")
    tree.heading("telefone", text="Telefone")
    tree.heading("cpf", text="CPF")
    tree.heading("email", text="E-mail")
    tree.heading("endereco", text="Endereço")
    tree.heading("acoes", text="Ações")

    tree.column("nome", width=150)
    tree.column("telefone", width=120)
    tree.column("email", width=180)
    tree.column("endereco", width=140)
    tree.column("acoes", width=140)

    tree.pack(fill="both", expand=True, padx=5, pady=5)

