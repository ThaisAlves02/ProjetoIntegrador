import customtkinter as ctk


def tela_servicos(container):

    titulo = ctk.CTkLabel(
        container,
        text="Serviços",
        font=("Arial", 28, "bold")
    )

    titulo.pack(
        anchor="w",
        padx=32,
        pady=30
    )