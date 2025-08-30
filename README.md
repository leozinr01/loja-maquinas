# Sistema de Gestão de Estoque e Vendas

## Sobre o Projeto

Este é um sistema completo de gestão de estoque e vendas, desenvolvido em **Python** com **FastAPI**, aplicando boas práticas de arquitetura para entregar uma solução escalável e de fácil manutenção. O projeto foi pensado para performance, organização e integração com ferramentas de análise de dados.

A aplicação é um MVP que demonstra as melhores práticas em desenvolvimento backend, aliado à integração entre programação, análise de dados e gestão de informações. Reflete um perfil proativo e analítico, unindo conhecimento em Python, SQL e Data Science para transformar dados em informação estratégica e criar soluções reais que geram valor aos negócios.

---

## Funcionalidades Principais

- Cadastro de produtos e categorias
- Controle de estoque em tempo real (entradas, saídas e ajustes)
- Registro de custos unitários e totais por operação
- Relatórios exportáveis em Excel (via Pandas), integráveis ao Power BI
- Organização modular (routers e services) para fácil expansão e manutenção

---

## Recursos Técnicos

- **Banco de Dados:** SQLite para desenvolvimento ágil, com possibilidade de migração para outros SGBDs
- **ORM:** SQLAlchemy para modelagem e manipulação dos dados
- **Versionamento:** Alembic para versionar e migrar o banco de dados de forma segura
- **Arquitetura:** Desacoplada, garantindo clareza e separação de responsabilidades
- **Injeção de Dependências:** Para conexões seguras e escaláveis
- **Tipagem Forte:** Typing + Pydantic para robustez e validação dos dados
- **Exportação de Dados:** Relatórios em Excel via Pandas, preparados para integração com Power BI
- **Estrutura preparada:** Para autenticação, permissões, e dashboards visuais

---

## Objetivo e Próximos Passos

- Criar interface interativa (React ou Streamlit)
- Implementar sistema de usuários e permissões
- Automatizar backups e criar alertas de estoque mínimo
- Expandir relatórios com análises avançadas no Power BI

---

## Como Executar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/leozinr01/loja-maquinas.git
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute as migrações do banco de dados:
   ```bash
   alembic upgrade head
   ```

4. Inicie o servidor FastAPI:
   ```bash
   uvicorn app.main:app --reload
   ```

5. Acesse a documentação interativa (Swagger) em: `http://localhost:8000/docs`

---

## Contribuição

Sinta-se à vontade para abrir issues ou pull requests com sugestões de melhoria, correções ou novas funcionalidades!

---

**Autor:** [leozinr01](https://github.com/leozinr01)
