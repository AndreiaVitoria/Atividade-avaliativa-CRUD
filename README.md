# 🎬 Projeto Cinema - CRUD com Flask e SQLite

Este projeto é um sistema CRUD simples para gerenciar **Diretores** e **Filmes**, desenvolvido em **Flask** com **SQLite**.

## 📌 Entidades

### 1. Diretor
Representa um diretor de cinema, com os seguintes atributos:
- **id** *(INTEGER, PK)* → Identificador único do diretor.
- **nome** *(TEXT, obrigatório)* → Nome completo do diretor.
- **nacionalidade** *(TEXT)* → País de origem.
- **data_nascimento** *(DATE)* → Data de nascimento.

### 2. Filme
Representa um filme e suas informações básicas:
- **id** *(INTEGER, PK)* → Identificador único do filme.
- **titulo** *(TEXT, obrigatório)* → Nome do filme.
- **ano_lancamento** *(INTEGER)* → Ano em que o filme foi lançado.
- **genero** *(TEXT)* → Gênero cinematográfico (Ex.: Ação, Drama, Comédia).
- **id_diretor** *(INTEGER, obrigatório, FK)* → Referência ao diretor responsável.

## 🔗 Relacionamento
- **Um para Muitos (1:N)**  
  Um **diretor** pode ter dirigido vários **filmes**.  
  No banco, o campo `diretor_id` na tabela `filme` é uma **chave estrangeira** que referencia `diretor.id`.
- **ON DELETE CASCADE**: caso um diretor seja removido, todos os seus filmes também serão excluídos automaticamente.

