from app.database.connection import conectar

class ProdutoModel:
    def __init__(self):
        self.db = conectar()
        self.cursor = self.db.cursor(dictionary=True)

    def listar(self):
        self.cursor.execute("SELECT * FROM produtos")
        return self.cursor.fetchall()

    def criar(self, nome, preco, estoque):
        sql = "INSERT INTO produtos (nome, preco, estoque) VALUES (%s, %s, %s)"
        self.cursor.execute(sql, (nome, preco, estoque))
        self.db.commit()

    def atualizar(self, produto_id, nome, preco, estoque):
        sql = "UPDATE produtos SET nome=%s, preco=%s, estoque=%s WHERE id=%s"
        self.cursor.execute(sql, (nome, preco, estoque, produto_id))
        self.db.commit()

    def deletar(self, produto_id):
        sql = "DELETE FROM produtos WHERE id=%s"
        self.cursor.execute(sql, (produto_id,))
        self.db.commit()
