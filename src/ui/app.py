import customtkinter as ctk
import default
from config.config import load_config, save_config
from PIL import Image
from .sidebar import Sidebar
from .main import Main

config = load_config()
ctk.set_appearance_mode(config["theme"])

class app(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title(f"Jaú Auto-Atendimento | {default.VERSION}")
        self.geometry(f"{default.WINDOW_WIDTH}x{default.WINDOW_HEIGHT}")
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
        self.main.main.set(page)
        self.main.update_stock()
        


Window = app()
Window.mainloop()