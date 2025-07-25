import tkinter as tk
from tkinter import messagebox

from app.controllers.usuario_controller import UsuarioController
from app.views.menu_view import MenuView

class LoginView:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master)
        self.frame.pack(pady=100)

        tk.Label(self.frame, text="Login", font=("Arial", 20)).grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(self.frame, text="Email:").grid(row=1, column=0, sticky='e')
        self.email_entry = tk.Entry(self.frame, width=30)
        self.email_entry.grid(row=1, column=1)

        tk.Label(self.frame, text="Senha:").grid(row=2, column=0, sticky='e')
        self.senha_entry = tk.Entry(self.frame, width=30, show='*')
        self.senha_entry.grid(row=2, column=1)

        self.btn_login = tk.Button(self.frame, text="Entrar", command=self.login)
        self.btn_login.grid(row=3, column=0, columnspan=2, pady=10)

        self.controller = UsuarioController()

    def login(self):
        email = self.email_entry.get()
        senha = self.senha_entry.get()

        if not email or not senha:
            messagebox.showwarning("Aviso", "Preencha todos os campos")
            return

        valido, usuario = self.controller.autenticar(email, senha)
        if valido:
            messagebox.showinfo("Sucesso", f"Bem-vindo, {usuario['nome']}!")
            self.frame.destroy()
            MenuView(self.master)
        else:
            messagebox.showerror("Erro", "Email ou senha inválidos")
