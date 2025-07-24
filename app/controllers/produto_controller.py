from app.models.produto_model import ProdutoModel

class ProdutoController:
    def __init__(self):
        self.model = ProdutoModel()

    def listar(self):
        return self.model.listar()

    def criar(self, nome, preco, estoque):
        self.model.criar(nome, preco, estoque)

    def atualizar(self, produto_id, nome, preco, estoque):
        self.model.atualizar(produto_id, nome, preco, estoque)

    def deletar(self, produto_id):
        self.model.deletar(produto_id)
