from app.models.cliente_model import ClienteModel

class ClienteController:
    def __init__(self):
        self.model = ClienteModel()

    def listar(self):
        return self.model.listar()

    def criar(self, nome, email, telefone):
        self.model.criar(nome, email, telefone)

    def atualizar(self, cliente_id, nome, email, telefone):
        self.model.atualizar(cliente_id, nome, email, telefone)

    def deletar(self, cliente_id):
        self.model.deletar(cliente_id)
