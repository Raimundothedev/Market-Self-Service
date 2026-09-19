import customtkinter as ctk
import config
from PIL import Image
from .sidebar import Sidebar
from .main import Main

ctk.set_appearance_mode(config.THEME)

class app(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title(f"Jaú Auto-Atendimento | {config.VERSION}")
        self.geometry(f"{config.WINDOW_WIDTH}x{config.WINDOW_HEIGHT}")
        self.resizable = False

        self.create_widgets()


    def create_widgets(self):
        # Sidebar
        self.sidebar = Sidebar(
        self,
        self.select_page
        )
        self.sidebar.pack(
        side="left",
        fill="y"
        )

        # Main
        self.main = Main(self)

        self.main.pack(
            side="right",
            fill="both",
            expand=True,
            padx=(5, 10),
            pady=10
        )

    def select_page(self, page):
        self.main.set(page)


Window = app()
Window.mainloop()