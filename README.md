# Loja de Máquinas

## Sobre o projeto

A **Loja de Máquinas** é uma aplicação desenvolvida para facilitar a gestão de vendas, estoque e clientes em estabelecimentos que comercializam máquinas e equipamentos. Com ela, é possível realizar o cadastro de produtos, controlar o estoque, gerenciar pedidos de compra/venda, cadastrar clientes e acompanhar o histórico de movimentações de forma prática e intuitiva.

## Funcionalidades

- Cadastro, edição e exclusão de máquinas/equipamentos.
- Controle de estoque com alertas de quantidade mínima.
- Gestão de pedidos de venda e compra.
- Cadastro de clientes e histórico de compras.
- Dashboard com indicadores de desempenho da loja.

## Stacks utilizadas

- **Frontend:** React.js com TypeScript, Styled Components.
- **Backend:** Node.js com Express, TypeScript.
- **Banco de Dados:** MongoDB.
- **Autenticação:** JWT (JSON Web Token).
- **Containerização:** Docker.
- **Versionamento:** Git e GitHub.

*(Edite conforme necessário caso sua stack seja diferente)*

## Arquitetura

A arquitetura utilizada segue o padrão **MVC (Model-View-Controller)**, onde:

- **Model:** Responsável por representar e manipular os dados do negócio, interagindo diretamente com o banco de dados.
- **View:** Interface visual desenvolvida em React, consumindo a API do backend via requisições HTTP.
- **Controller:** Camada responsável pela lógica de negócio, validação e controle do fluxo de dados entre Model e View.

Além disso, os serviços estão divididos entre frontend e backend, podendo ser executados separadamente (arquitetura desacoplada), facilitando a escalabilidade e manutenção. A comunicação entre as camadas é feita via API RESTful.

## Como executar o projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/leozinr01/loja-maquinas.git
   ```

2. Instale as dependências do frontend e backend:
   ```bash
   cd loja-maquinas/frontend
   npm install

   cd ../backend
   npm install
   ```

3. Configure as variáveis de ambiente conforme os exemplos `.env.example`.

4. Suba os serviços com Docker (opcional):
   ```bash
   docker-compose up
   ```

5. Acesse o frontend pelo navegador e comece a usar!

## Contribuição

Sinta-se à vontade para abrir issues ou pull requests com sugestões de melhoria, correções ou novas funcionalidades!

---

**Autor:** [leozinr01](https://github.com/leozinr01)
