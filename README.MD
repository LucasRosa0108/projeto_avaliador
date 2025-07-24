# Projeto Avaliador - Sistema de Controle de Loja

## 💡 Objetivo
Sistema desktop para controle de vendas em uma loja, utilizando Python com Tkinter, arquitetura MVC e banco de dados MySQL.

## ⚙️ Funcionalidades
- Cadastro de clientes, produtos e usuários
- Registro de vendas com múltiplos itens (em desenvolvimento)
- Interface gráfica com Tkinter
- Autenticação de usuário
- Controle de estoque básico

## 🧱 Estrutura do Projeto
- `models/`: classes de acesso ao banco
- `views/`: telas da aplicação com Tkinter
- `controllers/`: lógica de negócio e comunicação model-view
- `database/`: conexão e scripts de migrations
- `main.py`: ponto de entrada da aplicação

## 🗃 Banco de Dados
- MySQL com 5 tabelas principais (usuarios, clientes, produtos, vendas, itens_venda)
- DER disponível em `docs/DER.png`

## 📝 Documentação
- Requisitos em `docs/requisitos.txt`
- Algoritmo descritivo em `docs/algoritmo.txt`
- Modelo do banco em `docs/modelo_banco.png`

## 🔐 Configuração
1. Copie `.env.example` para `.env` e configure os dados do seu MySQL
2. Instale as dependências: `pip install -r requirements.txt`
3. Execute `python app/database/migrations.py` para criar o banco e as tabelas
4. Rode a aplicação: `python app/main.py`

## Autor
- Lucas Gabriel Rosa Moreira
- Coautoria: ChatGPT (IA assistente)

---
