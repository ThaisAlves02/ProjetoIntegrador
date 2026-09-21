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
        pady=30
    )

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
        text="Cadastre-se",
        font=("Arial", 18, "bold")
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

    botao_salvar = ctk.CTkButton(frame_cadastro, width=420, height=42, text="Salvar Cliente", font=("Arial", 14, "bold"), fg_color=cor_botao, hover_color="#A0BEDD" )
    botao_salvar.pack(pady=(30, 0))