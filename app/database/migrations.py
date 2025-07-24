# app/database/migrations.py
from app.database.connection import conectar

def criar_tabelas():
    db = conectar()
    cursor = db.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100),
            email VARCHAR(100) UNIQUE,
            senha VARCHAR(100)
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100),
            email VARCHAR(100),
            telefone VARCHAR(20)
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100),
            preco DECIMAL(10,2),
            estoque INT
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vendas (
            id INT AUTO_INCREMENT PRIMARY KEY,
            cliente_id INT,
            data_venda DATETIME DEFAULT NOW(),
            total DECIMAL(10,2),
            FOREIGN KEY(cliente_id) REFERENCES clientes(id)
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS itens_venda (
            id INT AUTO_INCREMENT PRIMARY KEY,
            venda_id INT,
            produto_id INT,
            quantidade INT,
            preco_unitario DECIMAL(10,2),
            FOREIGN KEY(venda_id) REFERENCES vendas(id),
            FOREIGN KEY(produto_id) REFERENCES produtos(id)
        );
    """)

    db.commit()
    db.close()
    print("Tabelas criadas com sucesso.")

if __name__ == '__main__':
    criar_tabelas()
