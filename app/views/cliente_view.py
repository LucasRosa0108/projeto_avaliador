import tkinter as tk
from tkinter import messagebox, ttk
from app.controllers.cliente_controller import ClienteController
# ❌ Removido o import direto de MenuView para evitar importação circular

class ClienteView:
    def __init__(self, master):
        self.master = master
        self.controller = ClienteController()
        self.frame = tk.Frame(master)
        self.frame.pack(fill='both', expand=True, padx=20, pady=20)

        tk.Label(self.frame, text="Clientes", font=("Arial", 20)).pack(pady=10)

        self.tree = ttk.Treeview(self.frame, columns=("ID", "Nome", "Email", "Telefone"), show='headings')
        for col in ("ID", "Nome", "Email", "Telefone"):
            self.tree.heading(col, text=col)
        self.tree.pack(fill='both', expand=True)

        self.carregar_clientes()

        form_frame = tk.Frame(self.frame)
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Nome:").grid(row=0, column=0)
        self.nome_entry = tk.Entry(form_frame)
        self.nome_entry.grid(row=0, column=1)

        tk.Label(form_frame, text="Email:").grid(row=1, column=0)
        self.email_entry = tk.Entry(form_frame)
        self.email_entry.grid(row=1, column=1)

        tk.Label(form_frame, text="Telefone:").grid(row=2, column=0)
        self.telefone_entry = tk.Entry(form_frame)
        self.telefone_entry.grid(row=2, column=1)

        btn_frame = tk.Frame(self.frame)
        btn_frame.pack(pady=10)

        self.btn_add = tk.Button(btn_frame, text="Adicionar", command=self.adicionar_cliente)
        self.btn_add.grid(row=0, column=0, padx=5)

        self.btn_edit = tk.Button(btn_frame, text="Editar", command=self.editar_cliente)
        self.btn_edit.grid(row=0, column=1, padx=5)

        self.btn_del = tk.Button(btn_frame, text="Excluir", command=self.excluir_cliente)
        self.btn_del.grid(row=0, column=2, padx=5)

        self.btn_back = tk.Button(btn_frame, text="Voltar", command=self.voltar_menu)
        self.btn_back.grid(row=0, column=3, padx=5)

        self.selecionado_id = None
        self.tree.bind('<<TreeviewSelect>>', self.selecionar_cliente)

    def carregar_clientes(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        clientes = self.controller.listar()
        for c in clientes:
            self.tree.insert('', 'end', values=(c['id'], c['nome'], c['email'], c['telefone']))

    def selecionar_cliente(self, event):
        selected = self.tree.focus()
        if selected:
            values = self.tree.item(selected, 'values')
            self.selecionado_id = values[0]
            self.nome_entry.delete(0, 'end')
            self.nome_entry.insert(0, values[1])
            self.email_entry.delete(0, 'end')
            self.email_entry.insert(0, values[2])
            self.telefone_entry.delete(0, 'end')
            self.telefone_entry.insert(0, values[3])

    def adicionar_cliente(self):
        nome = self.nome_entry.get()
        email = self.email_entry.get()
        telefone = self.telefone_entry.get()
        if not nome or not email or not telefone:
            messagebox.showwarning("Aviso", "Preencha todos os campos")
            return
        self.controller.criar(nome, email, telefone)
        self.carregar_clientes()
        self.limpar_campos()

    def editar_cliente(self):
        if not self.selecionado_id:
            messagebox.showwarning("Aviso", "Selecione um cliente para editar")
            return
        nome = self.nome_entry.get()
        email = self.email_entry.get()
        telefone = self.telefone_entry.get()
        if not nome or not email or not telefone:
            messagebox.showwarning("Aviso", "Preencha todos os campos")
            return
        self.controller.atualizar(self.selecionado_id, nome, email, telefone)
        self.carregar_clientes()
        self.limpar_campos()

    def excluir_cliente(self):
        if not self.selecionado_id:
            messagebox.showwarning("Aviso", "Selecione um cliente para excluir")
            return
        self.controller.deletar(self.selecionado_id)
        self.carregar_clientes()
        self.limpar_campos()

    def limpar_campos(self):
        self.nome_entry.delete(0, 'end')
        self.email_entry.delete(0, 'end')
        self.telefone_entry.delete(0, 'end')
        self.selecionado_id = None

    def voltar_menu(self):
        from app.views.menu_view import MenuView  # ✅ Importação movida para dentro da função
        self.frame.destroy()
        MenuView(self.master)
