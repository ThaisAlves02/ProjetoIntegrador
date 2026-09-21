import customtkinter as ctk


def tela_administradores(container):

    titulo = ctk.CTkLabel(
        container,
        text="Administradores",
        font=("Arial", 28, "bold")
    )

    titulo.pack(
        anchor="w",
        padx=32,
        pady=30
    )