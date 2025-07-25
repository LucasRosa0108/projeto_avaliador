import tkinter as tk
from tkinter import messagebox, ttk
from app.controllers.produto_controller import ProdutoController

class ProdutoView:
    def __init__(self, master):
        self.master = master
        self.controller = ProdutoController()
        self.frame = tk.Frame(master)
        self.frame.pack(fill='both', expand=True, padx=20, pady=20)

        tk.Label(self.frame, text="Produtos", font=("Arial", 20)).pack(pady=10)

        self.tree = ttk.Treeview(self.frame, columns=("ID", "Nome", "Preço", "Estoque"), show='headings')
        for col in ("ID", "Nome", "Preço", "Estoque"):
            self.tree.heading(col, text=col)
        self.tree.pack(fill='both', expand=True)

        self.carregar_produtos()

        form_frame = tk.Frame(self.frame)
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Nome:").grid(row=0, column=0)
        self.nome_entry = tk.Entry(form_frame)
        self.nome_entry.grid(row=0, column=1)

        tk.Label(form_frame, text="Preço:").grid(row=1, column=0)
        self.preco_entry = tk.Entry(form_frame)
        self.preco_entry.grid(row=1, column=1)

        tk.Label(form_frame, text="Estoque:").grid(row=2, column=0)
        self.estoque_entry = tk.Entry(form_frame)
        self.estoque_entry.grid(row=2, column=1)

        btn_frame = tk.Frame(self.frame)
        btn_frame.pack(pady=10)

        self.btn_add = tk.Button(btn_frame, text="Adicionar", command=self.adicionar_produto)
        self.btn_add.grid(row=0, column=0, padx=5)

        self.btn_edit = tk.Button(btn_frame, text="Editar", command=self.editar_produto)
        self.btn_edit.grid(row=0, column=1, padx=5)

        self.btn_del = tk.Button(btn_frame, text="Excluir", command=self.excluir_produto)
        self.btn_del.grid(row=0, column=2, padx=5)

        self.btn_back = tk.Button(btn_frame, text="Voltar", command=self.voltar_menu)
        self.btn_back.grid(row=0, column=3, padx=5)

        self.selecionado_id = None
        self.tree.bind('<<TreeviewSelect>>', self.selecionar_produto)

    def carregar_produtos(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        produtos = self.controller.listar()
        for p in produtos:
            self.tree.insert('', 'end', values=(p['id'], p['nome'], p['preco'], p['estoque']))

    def selecionar_produto(self, event):
        selected = self.tree.focus()
        if selected:
            values = self.tree.item(selected, 'values')
            self.selecionado_id = values[0]
            self.nome_entry.delete(0, 'end')
            self.nome_entry.insert(0, values[1])
            self.preco_entry.delete(0, 'end')
            self.preco_entry.insert(0, values[2])
            self.estoque_entry.delete(0, 'end')
            self.estoque_entry.insert(0, values[3])

    def adicionar_produto(self):
        nome = self.nome_entry.get()
        preco = self.preco_entry.get()
        estoque = self.estoque_entry.get()
        if not nome or not preco or not estoque:
            messagebox.showwarning("Aviso", "Preencha todos os campos")
            return
        try:
            preco = float(preco)
            estoque = int(estoque)
        except ValueError:
            messagebox.showwarning("Aviso", "Preço deve ser número e estoque inteiro")
            return
        self.controller.criar(nome, preco, estoque)
        self.carregar_produtos()
        self.limpar_campos()

    def editar_produto(self):
        if not self.selecionado_id:
            messagebox.showwarning("Aviso", "Selecione um produto para editar")
            return
        nome = self.nome_entry.get()
        preco = self.preco_entry.get()
        estoque = self.estoque_entry.get()
        if not nome or not preco or not estoque:
            messagebox.showwarning("Aviso", "Preencha todos os campos")
            return
        try:
            preco = float(preco)
            estoque = int(estoque)
        except ValueError:
            messagebox.showwarning("Aviso", "Preço deve ser número e estoque inteiro")
            return
        self.controller.atualizar(self.selecionado_id, nome, preco, estoque)
        self.carregar_produtos()
        self.limpar_campos()

    def excluir_produto(self):
        if not self.selecionado_id:
            messagebox.showwarning("Aviso", "Selecione um produto para excluir")
            return
        self.controller.deletar(self.selecionado_id)
        self.carregar_produtos()
        self.limpar_campos()

    def limpar_campos(self):
        self.nome_entry.delete(0, 'end')
        self.preco_entry.delete(0, 'end')
        self.estoque_entry.delete(0, 'end')
        self.selecionado_id = None

    def voltar_menu(self):
        self.frame.destroy()
        from app.views.menu_view import MenuView
        MenuView(self.master)
