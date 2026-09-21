import customtkinter as ctk

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
