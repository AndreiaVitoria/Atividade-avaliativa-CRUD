# 🎬 Projeto Cinema - CRUD com Flask e SQLite

Este projeto é um sistema CRUD simples para gerenciar **Diretores** e **Filmes**, desenvolvido em **Flask** com **SQLite**.

## 📌 Entidades

### 1. Diretor
Representa um diretor de cinema, com os seguintes atributos:
- **id** *(INTEGER, PK)* → Identificador único do diretor.
- **nome** *(TEXT, obrigatório)* → Nome completo do diretor.
- **nacionalidade** *(TEXT)* → País de origem.

### 2. Filme
Representa um filme e suas informações básicas:
- **id** *(INTEGER, PK)* → Identificador único do filme.
- **titulo** *(TEXT, obrigatório)* → Nome do filme.
- **ano** *(INTEGER)* → Ano em que o filme foi lançado.
- **genero** *(TEXT)* → Gênero cinematográfico (Ex.: Ação, Drama, Comédia).
- **diretor_id** *(INTEGER, obrigatório, FK)* → Referência ao diretor responsável.

## 🔗 Relacionamento
- **Um para Muitos (1:N)**  
  Um **diretor** pode ter dirigido vários **filmes**.  
  No banco, o campo `diretor_id` na tabela `filme` é uma **chave estrangeira** que referencia `diretor.id`.
- **ON DELETE CASCADE**: caso um diretor seja removido, todos os seus filmes também serão excluídos automaticamente.

## Executando o Projeto
### 1. Clone o repositório:

```bash
git clone https://github.com/AndreiaVitoria/Atividade-avaliativa-CRUD.git
cd Atividade-avaliativa-CRUD
```

### 2. Crie o ambiente virtual:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instale as dependências:
```bash
pip install --upgrade pip
#ou você pode rodar:
python.exe -m pip install --upgrade
```

Instale o Flask:
```bash
pip install Flask
```

### 4. Crie  um banco de dados:
```bash
python
from app.database.connection import init_db
init_db()
exit()
```

### 5. Execute o projeto
```bash
python run.py
```

