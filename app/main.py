
import tkinter as tk
from app.views.login_view import LoginView

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Controle de Loja")
        self.geometry("800x600")
        self.resizable(False, False)

        # Inicia a primeira janela (login)
        self.show_login()

    def show_login(self):
        self.clear_window()
        LoginView(self)

    def show_menu(self):
        from app.views.menu_view import MenuView
        self.clear_window()
        MenuView(self)

    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == '__main__':
    app = App()
    app.mainloop()
