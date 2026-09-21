import customtkinter as ctk

from telas.dashboard import tela_dashboard
from telas.administradores import tela_administradores
from telas.clientes import tela_clientes
from telas.servicos import tela_servicos


# ==================================================
# CONFIGURAÇÕES
# ==================================================

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


# ==================================================
# JANELA PRINCIPAL
# ==================================================

janela = ctk.CTk()

janela.title("Sistema de Cadastro")
janela.geometry("1100x650")
janela.resizable(False, False)


# ==================================================
# SIDEBAR
# ==================================================

sidebar = ctk.CTkFrame(
    janela,
    width=220,
    corner_radius=0,
    fg_color="#122B43"
)

sidebar.pack(
    side="left",
    fill="y"
)

sidebar.pack_propagate(False)


# Título da Sidebar

ctk.CTkLabel(
    sidebar,
    text="Sistema de Cadastro",
    font=("Arial", 18, "bold"),
    text_color="white"
).pack(
    pady=(30, 35)
)


# ==================================================
# CONTAINER
# ==================================================

container = ctk.CTkFrame(
    janela,
    fg_color="#F5F9FC",
    corner_radius=0
)

container.pack(
    side="right",
    fill="both",
    expand=True
)


# ==================================================
# FUNÇÃO PARA LIMPAR O CONTAINER
# ==================================================

def limpar_container():

    for widget in container.winfo_children():
        widget.destroy()


# ==================================================
# FUNÇÃO PARA TROCAR DE TELA
# ==================================================

def abrir_tela(tela):

    limpar_container()

    tela(container)


# ==================================================
# BOTÕES DA SIDEBAR
# ==================================================

ctk.CTkButton(
    sidebar,
    text="Dashboard",
    command=lambda: abrir_tela(tela_dashboard),
    fg_color="#294967",
    hover_color="#355C7D"
).pack(
    padx=15,
    pady=5,
    fill="x"
)


ctk.CTkButton(
    sidebar,
    text="Administradores",
    command=lambda: abrir_tela(tela_administradores),
    fg_color="transparent",
    hover_color="#294967"
).pack(
    padx=15,
    pady=5,
    fill="x"
)


ctk.CTkButton(
    sidebar,
    text="Clientes",
    command=lambda: abrir_tela(tela_clientes),
    fg_color="transparent",
    hover_color="#294967"
).pack(
    padx=15,
    pady=5,
    fill="x"
)


ctk.CTkButton(
    sidebar,
    text="Serviços",
    command=lambda: abrir_tela(tela_servicos),
    fg_color="transparent",
    hover_color="#294967"
).pack(
    padx=15,
    pady=5,
    fill="x"
)


# ==================================================
# TELA INICIAL
# ==================================================

abrir_tela(tela_dashboard)


# ==================================================
# LOOP PRINCIPAL
# ==================================================


janela.mainloop()