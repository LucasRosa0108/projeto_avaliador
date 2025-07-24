from app.models.usuario_model import UsuarioModel

class UsuarioController:
    def __init__(self):
        self.model = UsuarioModel()

    def autenticar(self, email, senha):
        usuario = self.model.buscar_por_email(email)
        if usuario and usuario['senha'] == senha:
            return True, usuario
        return False, None
