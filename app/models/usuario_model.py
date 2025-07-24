from app.database.connection import conectar

class UsuarioModel:
    def __init__(self):
        self.db = conectar()
        self.cursor = self.db.cursor(dictionary=True)

    def buscar_por_email(self, email):
        sql = "SELECT * FROM usuarios WHERE email = %s"
        self.cursor.execute(sql, (email,))
        return self.cursor.fetchone()

    def criar(self, nome, email, senha):
        sql = "INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)"
        self.cursor.execute(sql, (nome, email, senha))
        self.db.commit()
