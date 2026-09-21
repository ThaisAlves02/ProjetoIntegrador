import customtkinter as ctk


def tela_dashboard(container):

    titulo = ctk.CTkLabel(
        container,
        text="Dashboard",
        font=("Arial", 28, "bold"),
        text_color="#122B43"
    )

    titulo.pack(
        anchor="w",
        padx=32,
        pady=(30, 5)
    )


    subtitulo = ctk.CTkLabel(
        container,
        text="Visão geral dos cadastros do sistema.",
        font=("Arial", 14),
        text_color="#52677D"
    )

    subtitulo.pack(
        anchor="w",
        padx=32
    )


    # ==============================
    # ÁREA DOS CARDS
    # ==============================

    frame_cards = ctk.CTkFrame(
        container,
        fg_color="transparent"
    )

    frame_cards.pack(
        fill="x",
        padx=32,
        pady=30
    )


    # Card Administradores

    card_admin = ctk.CTkFrame(
        frame_cards,
        height=120,
        fg_color="white",
        corner_radius=10
    )

    card_admin.pack(
        side="left",
        fill="both",
        expand=True,
        padx=(0, 8)
    )

    ctk.CTkLabel(
        card_admin,
        text="Administradores",
        font=("Arial", 14),
        text_color="#52677D"
    ).pack(
        anchor="w",
        padx=20,
        pady=(20, 5)
    )

    ctk.CTkLabel(
        card_admin,
        text="0",
        font=("Arial", 30, "bold"),
        text_color="#122B43"
    ).pack(
        anchor="w",
        padx=20
    )


    # Card Clientes

    card_clientes = ctk.CTkFrame(
        frame_cards,
        height=120,
        fg_color="white",
        corner_radius=10
    )

    card_clientes.pack(
        side="left",
        fill="both",
        expand=True,
        padx=8
    )

    ctk.CTkLabel(
        card_clientes,
        text="Clientes",
        font=("Arial", 14),
        text_color="#52677D"
    ).pack(
        anchor="w",
        padx=20,
        pady=(20, 5)
    )

    ctk.CTkLabel(
        card_clientes,
        text="0",
        font=("Arial", 30, "bold"),
        text_color="#122B43"
    ).pack(
        anchor="w",
        padx=20
    )


    # Card Serviços

    card_servicos = ctk.CTkFrame(
        frame_cards,
        height=120,
        fg_color="white",
        corner_radius=10
    )

    card_servicos.pack(
        side="left",
        fill="both",
        expand=True,
        padx=(8, 0)
    )

    ctk.CTkLabel(
        card_servicos,
        text="Serviços",
        font=("Arial", 14),
        text_color="#52677D"
    ).pack(
        anchor="w",
        padx=20,
        pady=(20, 5)
    )

    ctk.CTkLabel(
        card_servicos,
        text="0",
        font=("Arial", 30, "bold"),
        text_color="#122B43"
    ).pack(
        anchor="w",
        padx=20
    )


    # ==============================
    # ÚLTIMAS ORDENS
    # ==============================

    frame_ordens = ctk.CTkFrame(
        container,
        fg_color="white",
        corner_radius=10
    )

    frame_ordens.pack(
        fill="x",
        padx=32,
        pady=(0, 20)
    )


    ctk.CTkLabel(
        frame_ordens,
        text="Últimas ordens de serviço",
        font=("Arial", 16, "bold"),
        text_color="#122B43"
    ).pack(
        anchor="w",
        padx=24,
        pady=(25, 10)
    )


    ctk.CTkLabel(
        frame_ordens,
        text="Nenhuma ordem cadastrada ainda.",
        font=("Arial", 13),
        text_color="#52677D"
    ).pack(
        anchor="w",
        padx=24,
        pady=(0, 25)
    )