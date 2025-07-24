import tkinter as tk
from app.views.cliente_view import ClienteView
from app.views.produto_view import ProdutoView

class MenuView:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master)
        self.frame.pack(pady=100)

        tk.Label(self.frame, text="Menu Principal", font=("Arial", 20)).pack(pady=10)

        btn_clientes = tk.Button(self.frame, text="Clientes", width=20, command=self.abrir_clientes)
        btn_clientes.pack(pady=5)

        btn_produtos = tk.Button(self.frame, text="Produtos", width=20, command=self.abrir_produtos)
        btn_produtos.pack(pady=5)

    def abrir_clientes(self):
        self.frame.destroy()
        ClienteView(self.master)

    def abrir_produtos(self):
        self.frame.destroy()
        ProdutoView(self.master)
