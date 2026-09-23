import customtkinter as ctk
from tkinter import messagebox
import re

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
        text="Cadastro de clientes com nome, CPF, telefone, e-mail e endereço.",
        text_color=sub_titulo,
        font=("Arial", 14)
    )
    subtitulo.pack( 
        anchor="w",
        padx=32,
        pady=0
    )

#----------------------------------------------------------
# DESIGN DA TABELA (CABEÇALHO ARREDONDADO)
#----------------------------------------------------------
    frame_cabecalho = ctk.CTkFrame(
        frame_conteudo,
        width=800,
        height=40,
        fg_color="#F8F9FA",
        border_width=1,
        border_color="#E0E0E0",
        corner_radius=10
    )
    frame_cabecalho.place(x=32, y=115)

    nome = ctk.CTkLabel(
        frame_cabecalho,
        text="Nome",
        font=ctk.CTkFont(size=14, weight="bold"),
        text_color="#52677F"
    )
    nome.place(x=20, y=8)

    cpf = ctk.CTkLabel(
        frame_cabecalho,
        text="CPF",
        font=ctk.CTkFont(size=14, weight="bold"),
        text_color="#52677F"
    )
    cpf.place(x=240, y=8)
   
    telefone = ctk.CTkLabel(
        frame_cabecalho,
        text="Telefone",
        font=ctk.CTkFont(size=14, weight="bold"),
        text_color="#52677F"
    )
    telefone.place(x=390, y=8)

    endereco = ctk.CTkLabel(
        frame_cabecalho,
        text="Endereço",
        font=ctk.CTkFont(size=14, weight="bold"),
        text_color="#52677F"
    )
    endereco.place(x=540, y=8)
   
    email = ctk.CTkLabel(
        frame_cabecalho,
        text="E-mail",
        font=ctk.CTkFont(size=14, weight="bold"),
        text_color="#52677F"
    )
    email.place(x=720, y=8)
   
    acoes = ctk.CTkLabel(
        frame_cabecalho,
        text="Ações",
        font=ctk.CTkFont(size=14, weight="bold"),
        text_color="#52677F"
    )
    acoes.place(x=930, y=8)

#----------------------------------------------------------
# LINHA DE DADOS / STATUS DA TABELA
#----------------------------------------------------------
    frame_linhas = ctk.CTkFrame(
        frame_conteudo,
        width=800,
        height=50,
        fg_color="#FFFFFF",
        border_width=1,
        border_color="#E0E0E0",
        corner_radius=10
    )
    frame_linhas.place(x=32, y=154)

    linha_tabela = ctk.CTkLabel(
        frame_linhas,
        text="Nenhum cliente cadastrado.",
        font=ctk.CTkFont(size=14),
        text_color="#7E8B9B"
    )
    linha_tabela.place(x=20, y=12)

#----------------------------------------------------------
# FUNÇÕES VALIDAR E-MAIL E VALIDAR TELEFONE
#----------------------------------------------------------

    def validar_email(email):
        padrao = r"^[\w\.\-]+@[\w\-]+\.[a-zA-Z]{2,}$"
        return re.match(padrao, email) is not None


    def validar_telefone(telefone):
        padrao = r"^(\(\d{2}\)\s?)?\d{4,5}-?\d{4}$"
        return re.match(padrao, telefone) is not None

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

        def executar_cadastro():
            nome = entry_nome.get().strip()
            sobrenome = entry_sobrenome.get().strip()
            telefone = entry_telefone.get().strip()
            email = entry_email.get().strip()

            if not nome or not sobrenome or not telefone or not email:
                messagebox.showerror("Erro", "Preencha todos os campos.")
                return

            if not validar_email(email):
                messagebox.showerror("Erro", "Email inválido. Use o formato nome@dominio.com")
                return

            if not validar_telefone(telefone):
                messagebox.showerror("Erro", "Telefone inválido. Use (85) 99999-9999 ou 85999999999")
                return

            messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
            frame_cadastro.destroy()

        # Botão Cadastrar
        cadastrar_botao = ctk.CTkButton(
            frame_cadastro,
            text="Cadastrar",
            font=ctk.CTkFont(size=14, weight="bold"),
            width=190,
            height=40,
            command=executar_cadastro
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
            hover_color="#444444",
            command=frame_cadastro.destroy
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
