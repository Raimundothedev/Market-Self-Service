import customtkinter as ctk
import default


class Sidebar(ctk.CTkFrame):
    def __init__(self, master, select_page, **kwargs):
        super().__init__(master, **kwargs)

        self.select_page = select_page

        # Header
        self.header = ctk.CTkFrame(
            self,
            fg_color="#005D92",
            corner_radius=0
        )
        self.header.pack(
            fill="x"
        )

        self.title = ctk.CTkLabel(
            self.header,
            text="JAÚ AUTO ATENDIMENTO",
            font=ctk.CTkFont(
                size=18,
                weight="bold",
                family="JetBrains Mono"
            ),
            text_color="white"
        )
        self.title.pack(
            pady=(20, 5),
            padx=15
        )

        self.subtitle = ctk.CTkLabel(
            self.header,
            text="Inventory",
            font=ctk.CTkFont(
                size=12,
                family="JetBrains Mono"
            ),
            text_color="#DDECF5"
        )
        self.subtitle.pack(
            pady=(0, 20)
        )

        # Stock button
        self.btn_stock = ctk.CTkButton(
            self,
            text="🛍️    Stock",
            font=ctk.CTkFont(
                size=15,
                family="JetBrains Mono"
            ),
            fg_color="transparent",
            hover_color="#005D92",
            text_color="white",
            anchor="w",
            command=lambda: self.select_page("Stock")
        )
        self.btn_stock.pack(
            fill="x",
            padx=5,
            pady=(5, 0)
        )

        # Settings button
        self.btn_settings = ctk.CTkButton(
            self,
            text="⚙️    Settings",
            font=ctk.CTkFont(
                size=15,
                family="JetBrains Mono"
            ),
            fg_color="transparent",
            hover_color="#005D92",
            text_color="white",
            anchor="w",
            command=lambda: self.select_page("Settings")
        )
        self.btn_settings.pack(
            fill="x",
            padx=5,
            pady=(5, 0)
        )

        # Version
        self.version = ctk.CTkLabel(
            self,
            text=default.VERSION,
            font=ctk.CTkFont(
                size=11,
                family="JetBrains Mono"
            ),
            text_color="gray"
        )
        self.version.pack(
            side="bottom",
            pady=10
        )