from app.database.connection import conectar

class ClienteModel:
    def __init__(self):
        self.db = conectar()
        self.cursor = self.db.cursor(dictionary=True)

    def listar(self):
        self.cursor.execute("SELECT * FROM clientes")
        return self.cursor.fetchall()

    def criar(self, nome, email, telefone):
        sql = "INSERT INTO clientes (nome, email, telefone) VALUES (%s, %s, %s)"
        self.cursor.execute(sql, (nome, email, telefone))
        self.db.commit()

    def atualizar(self, cliente_id, nome, email, telefone):
        sql = "UPDATE clientes SET nome=%s, email=%s, telefone=%s WHERE id=%s"
        self.cursor.execute(sql, (nome, email, telefone, cliente_id))
        self.db.commit()

    def deletar(self, cliente_id):
        sql = "DELETE FROM clientes WHERE id=%s"
        self.cursor.execute(sql, (cliente_id,))
        self.db.commit()
