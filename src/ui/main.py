import customtkinter as ctk
from tkinter import messagebox, ttk
from products.repository import *
from config.config import *
from currency import converter
import default

class Main(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.main = ctk.CTkTabview(self, corner_radius=12)
        self.main.pack(
            fill="both",
            expand=True
        )

        self._style_configured = False

        self.welcome = "Welcome"
        self.stock = "Stock"
        self.settings = "Settings"

        self.main.add(self.welcome)
        self.main.add(self.stock)
        self.main.add(self.settings)
        self.main.set(self.welcome)

        self.main._segmented_button.grid_forget()

        self.build_welcome()
        self.build_stock()
        self.build_settings()

        self.update_stock()


    def build_welcome(self):
        self.welcome_screen = ctk.CTkFrame(
            self.main.tab("Welcome"),
            fg_color="transparent"
        )
        self.welcome_screen.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        ctk.CTkLabel(
            self.welcome_screen,
            text="Jaú Auto-Atendimento",
            font=ctk.CTkFont(
                family="JetBrains Mono",
                size=30,
                weight="bold"
            )
        ).pack(pady=(100, 10))

        ctk.CTkLabel(
            self.welcome_screen,
            text="Sistema de gerenciamento de estoque",
            font=ctk.CTkFont(
                family="JetBrains Mono",
                size=14
            )
        ).pack()

        ctk.CTkLabel(
            self.welcome_screen,
            text=f"Version {default.VERSION}",
            font=ctk.CTkFont(
                family="JetBrains Mono",
                size=11
            ),
            text_color="gray"
        ).pack(pady=(10, 30))

        ctk.CTkButton(
            self.welcome_screen,
            text="Go to Stock",
            width=180,
            command=lambda: self.main.set("Stock")
        ).pack()




    def build_stock(self):
        self.stock_screen = self.main.tab(self.stock)

        # Title
        self.title_stock = ctk.CTkLabel(
            self.stock_screen,
            text="Stock",
            font=ctk.CTkFont(
                size=16,
                weight="bold",
                family="JetBrains Mono"
            )
        )
        self.title_stock.pack(
            side="top",
            anchor="w",
            padx=15,
            pady=(10, 0)
        )

        # Order
        self.order_frame = ctk.CTkFrame(
            self.stock_screen,
            fg_color="transparent"
        )
        self.order_frame.pack(
            anchor="w",
            padx=15,
            pady=(10, 5)
        )

        self.title_order = ctk.CTkLabel(
            self.order_frame,
            text="Ordenar por:"
        )
        self.title_order.grid(
            row=0,
            column=0,
            padx=(0, 8)
        )

        self.order_opt = ctk.CTkOptionMenu(
            self.order_frame,
            values=["Id", "Nome", "Preço", "Quantidade"],
            width=180,
            anchor="w",
            command=lambda _: self.update_stock()
        )
        self.order_opt.grid(
            row=0,
            column=1,
            padx=(0, 15)
        )

        # Direction
        self.direction_opt = ctk.CTkOptionMenu(
            self.order_frame,
            values=["Crescente", "Decrescente"],
            width=150,
            anchor="w",
            command=lambda _: self.update_stock()
        )
        self.direction_opt.grid(
            row=0,
            column=2
        )

        # Products
        self.stock_frame = ctk.CTkFrame(
            self.stock_screen,
            fg_color="#1a1a1a"
        )

        self.stock_frame.pack(
            fill="both",
            expand=True,
            pady=15,
            padx=20
        )

        # Product name
        self.product_name = ctk.CTkEntry(
            self.stock_screen,
            placeholder_text="Product name",
            width=250
        )
        self.product_name.pack(
            pady=5
        )

        # Product amount
        self.product_amount = ctk.CTkEntry(
            self.stock_screen,
            placeholder_text="Product amount",
            width=250
        )
        self.product_amount.pack(
            pady=5
        )

        # Unit
        self.amount_menu = ctk.CTkOptionMenu(
            self.stock_screen,
            values=["u", "mg", "g", "kg", "t"],
            width=250
        )
        self.amount_menu.pack(
            pady=5
        )

        # Product value
        self.product_value = ctk.CTkEntry(
            self.stock_screen,
            placeholder_text="Product value",
            width=250
        )
        self.product_value.pack(
            pady=5
        )

        # Save
        self.btn_save_product = ctk.CTkButton(
            self.stock_screen,
            text="Save product",
            fg_color="#008000",
            hover_color="#006400",
            font=ctk.CTkFont(
                weight="bold",
                family="JetBrains Mono"
            ),
            command=self.save_stock
        )
        self.btn_save_product.pack(
            pady=(15, 0)
        )  

    def build_settings(self):


        self.settings_screen = self.main.tab(self.settings)

        # Title
        self.title_settings = ctk.CTkLabel(
            self.settings_screen,
            text="Settings",
            font=ctk.CTkFont(
                size=16,
                weight="bold",
                family="JetBrains Mono"
            )
        )
        self.title_settings.pack(
            side="top",
            anchor="w",
            padx=15,
            pady=(10, 0)
        )

        # Subtitle
        self.subtitle_settings = ctk.CTkLabel(
            self.settings_screen,
            text="Simple Settings",
            font=ctk.CTkFont(
                size=24,
                weight="bold",
                family="JetBrains Mono"
            )
        )
        self.subtitle_settings.pack(
            side="top",
            anchor="w",
            padx=15,
            pady=(5, 20)
        )

        # Dark Mode
        self.switch_theme = ctk.CTkSwitch(
            self.settings_screen,
            text="Dark Mode",
            #command=self.switch_darkmode,
            font=ctk.CTkFont(
                family="JetBrains Mono"
            )
        )
        self.switch_theme.pack(
            side="top",
            anchor="w",
            pady=10,
            padx=15
        )

        self.switch_theme.select()

        # Currency
        self.currency_label = ctk.CTkLabel(
            self.settings_screen,
            text="Currency",
            font=ctk.CTkFont(
                size=16,
                weight="bold",
                family="JetBrains Mono"
            )
        )
        self.currency_label.pack(
            anchor="w",
            padx=15,
            pady=(15, 5)
        )
        self.currency_menu = ctk.CTkOptionMenu(
            self.settings_screen,
            values=["USD", "BRL", "EUR", "GBP", "JPY", "CAD", "CHF", "ZAR"],
            width=150,
            font=ctk.CTkFont(
                size=12,
                family="JetBrains Mono"
            ),
            command=self.switch_currency
        )
        self.currency_menu.set(load_config().get("currency"))
        self.currency_menu.pack(
            anchor="w",
            padx=15
        )

    # Functions
    def save_stock(self):
        name = self.product_name.get().strip()
        name = name[:1].upper() + name[1:]
        price = self.product_value.get().strip()
        amount = self.product_amount.get().strip()

        if not name or not price or not amount:
            messagebox.showwarning(
                "IMPUT ERROR",
                "Preencha corretamente todos os campos presentes."
            )
            return
        for product in get_all_products():
            if product.name.lower() == name.lower():
                confirm = messagebox.askyesno(
                    "Produto já existe",
                    f"Já existe um produto chamado '{product.name}'. Gostaria de adiciona-lo mesmo assim?"
            )
                if not confirm:
                    return 

        self.product_name.delete(0, "end")
        self.product_value.delete(0, "end")
        self.product_amount.delete(0, "end")
        add_product(name, price, amount)

        self.update_stock()

    def remove_stock(self, id, name):
        confirm = messagebox.askyesno(
            "CONFIRMAÇÃO",
            f"Tem certeza que deseja excluir permanentemente o produto {name}?"
        )
        if not confirm:
            return

        remove_product(id)

        self.update_stock()

    def show_tooltip(self, event, text):
        self.tooltip = ctk.CTkLabel(
            self,
            fg_color="#222222",
            corner_radius=5,
            padx=8,
            pady=4
        )
        self.tooltip.configure(text=text)

        self.tooltip.place(
            x=event.x_root - self.winfo_rootx() + 10,
            y=event.y_root - self.winfo_rooty() + 10
        )


    def hide_tooltip(self, event):
        self.tooltip.place_forget()

    def handle_tree_click(self, event):
        column = self.stock_tree.identify_column(event.x)
        row = self.stock_tree.identify_row(event.y)

        if column != "#1" or not row:
            self.stock_tree.selection_remove(
                self.stock_tree.selection()
            )
            return

        values = self.stock_tree.item(row, "values")

        product_id = values[1]
        product_name = values[2]

        self.remove_stock(product_id, product_name)

        self.stock_tree.selection_remove(
            self.stock_tree.selection()
        )

    def configure_style(self):
        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "Custom.Treeview",
            background="#1a1a1a",
            foreground="white",
            fieldbackground="#1a1a1a",
            rowheight=35,
            borderwidth=0,      
            relief="flat"
        )

        style.configure(
            "Custom.Treeview.Heading",
            background="#222222",
            foreground="white",
            font=("JetBrains Mono", 10, "bold"),
            borderwidth=0,
            relief="flat"
        )

        style.map(
            "Custom.Treeview",
            background=[("selected", "#333333")],
            foreground=[("selected", "white")]
        )

        style.map(
            "Custom.Treeview.Heading",
            background=[("active", "#222222")],
            foreground=[("active", "white")]
        )

        style.configure(
            "Custom.Vertical.TScrollbar",
            background="#222222",
            troughcolor="#1a1a1a",
            bordercolor="#1a1a1a",
            arrowcolor="white",
            relief="flat"
        )

        style.map(
            "Custom.Vertical.TScrollbar",
            background=[("active", "#333333")]
        )

        self._style_configured = True

    def order_stock(self):
        column = self.order_opt.get().strip().lower()
        direction = self.direction_opt.get().strip().lower()
        columns = {
            "Id": "id",
            "nome": "name",
            "preço": "price",
            "quantidade": "amount"
        }
        directions = {
            "crescente": "ASC",
            "decrescente": "DESC"
        }

        column = columns.get(column)
        direction = directions.get(direction)
        
        return order_by(column, direction)
        

    def update_stock(self):
        
        products = self.order_stock()
        units = self.amount_menu.get()
        currency = load_config().get("currency")
        c_symbol = converter.currencies[currency].symbol

        if not self._style_configured:
            self.configure_style()

        for widget in self.stock_frame.winfo_children():
            widget.destroy()

        self.stock_tree = ttk.Treeview(
            self.stock_frame,
            columns=("delete", "id", "product", "amount", "value"),
            show="headings",
            style="Custom.Treeview"
        )

        self.stock_tree.heading("delete", text="")
        self.stock_tree.heading("id", text="ID")
        self.stock_tree.heading("product", text="PRODUTO")
        self.stock_tree.heading("amount", text="QUANTIDADE")
        self.stock_tree.heading("value", text="VALOR")

        self.stock_tree.column(
            "delete",
            width=35,
            minwidth=35,
            stretch=False,
            anchor="center"
        )

        self.stock_tree.column(
            "id",
            width=50,
            minwidth=50,
            stretch=False,
            anchor="w"
        )

        self.stock_tree.column(
            "product",
            width=250,
            minwidth=150,
            stretch=True,
            anchor="w"
        )

        self.stock_tree.column(
            "amount",
            width=120,
            minwidth=100,
            stretch=False,
            anchor="w"
        )

        self.stock_tree.column(
            "value",
            width=100,
            minwidth=100,
            stretch=False,
            anchor="e"
        )

        for product in products:
            self.stock_tree.insert(
                "",
                "end",
                values=(
                    "X",
                    product.id,
                    product.name,
                    f"{product.amount} {units}",
                    f"{c_symbol} {product.price}"
                )
            )

        self.stock_tree.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar = ttk.Scrollbar(
            self.stock_frame,
            orient="vertical",
            command=self.stock_tree.yview,
            style="Custom.Vertical.TScrollbar"
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        self.stock_tree.configure(
            yscrollcommand=scrollbar.set
        )

        self.stock_tree.bind(
            "<Button-1>",
            self.handle_tree_click
        )

    def switch_currency(self, currency):
        config = load_config()
        if currency not in converter.symbols:
            return
        option = messagebox.askyesno(
            "convert_all_prices",
            "Você gostaria de converter todos os preços listados para a moeda selecionada?"
        )
        if not option:
            update_config("currency", currency)
            return
        convert_all_prices(currency)
        update_config("currency", currency)



        



    







