# Alleanza Immobiliare

Sistema de gerenciamento imobiliário desenvolvido em **Python**, com persistência de dados em **MySQL**. O sistema é operado via terminal, através de um menu interativo que permite gerenciar imóveis, clientes, proprietários, corretores, contratos, vendas, aluguéis e demais entidades do negócio.

## 📋 Funcionalidades

O sistema permite realizar operações de **CRUD** (Cadastrar, Listar, Atualizar e Deletar) para as seguintes entidades:

| Módulo | Descrição |
|---|---|
| Endereço | Cadastro de endereços vinculados a imóveis |
| Proprietário | Donos dos imóveis anunciados |
| Cliente | Pessoas interessadas em comprar/alugar imóveis |
| Corretor | Responsáveis por visitas, vendas e aluguéis |
| Tipo de Imóvel | Categorias (casa, apartamento, terreno, etc.) |
| Documento | Documentos vinculados aos imóveis |
| Imóvel | Cadastro principal dos imóveis disponíveis |
| Visita | Agendamento de visitas a imóveis |
| Venda | Registro de vendas realizadas |
| Aluguel | Registro de contratos de locação |
| Contrato | Contratos formais entre cliente e imóvel |
| Pagamento | Pagamentos vinculados a contratos |
| Imóvel Documento | Associação entre imóveis e seus documentos |
| Anúncio | Anúncios publicados de imóveis |
| Foto Imóvel | Fotos vinculadas aos imóveis |

## 🗂️ Estrutura do Projeto

```
SA-MA78-AEJRR/
├── alleanza_immobiliare/          # Código-fonte da aplicação
│   ├── main.py                    # Menu principal e submenus (ponto de entrada)
│   ├── database.py                # Conexão com o banco de dados MySQL
│   ├── endereco_model.py          # CRUD de Endereço
│   ├── proprietario_model.py      # CRUD de Proprietário
│   ├── cliente_model.py           # CRUD de Cliente
│   ├── corretor_model.py          # CRUD de Corretor
│   ├── tipo_imovel_model.py       # CRUD de Tipo de Imóvel
│   ├── documento_model.py         # CRUD de Documento
│   ├── imovel_model.py            # CRUD de Imóvel
│   ├── visita_model.py            # CRUD de Visita
│   ├── venda_model.py             # CRUD de Venda
│   ├── aluguel_model.py           # CRUD de Aluguel
│   ├── contrato_model.py          # CRUD de Contrato
│   ├── pagamento_model.py         # CRUD de Pagamento
│   ├── imovel_documento_model.py  # CRUD de Imóvel Documento
│   ├── anuncio_model.py           # CRUD de Anúncio
│   ├── foto_imovel_model.py       # CRUD de Foto Imóvel
│   ├── relatorio_model.py         # Exportação de relatórios (Excel/PDF)
│   ├── requirements.txt           # Dependências Python do projeto
│   └── .env.example               # Modelo de variáveis de ambiente
├── BancoDeDados/                   # Scripts SQL do banco de dados
│   ├── 01_Criacao_Banco.sql        # Criação do banco de dados
│   ├── 02_Criacao_Tabelas.sql      # Criação das tabelas e relacionamentos
│   ├── 03_Inserts.sql              # Inserção de dados de exemplo
│   ├── 04_Consultas.sql            # Consultas de exemplo
│   ├── 05_Views.sql                # Views do banco de dados
│   ├── 06_Manipulacao_Dados.sql    # Scripts de manipulação de dados
│   └── 07_Usuarios_Seguranca.sql   # Usuários e permissões de segurança
└── README.md
```

## 🛠️ Tecnologias Utilizadas

- **Python 3** — linguagem principal da aplicação
- **MySQL** — banco de dados relacional
- **mysql-connector-python** — conexão entre Python e MySQL
- **python-dotenv** — carregamento de variáveis de ambiente (`.env`)

## ⚙️ Pré-requisitos

- Python 3.10+ instalado
- Um servidor MySQL acessível (local ou remoto)
- Gerenciador de pacotes `pip`

## 🚀 Como executar o projeto

### 1. Clone o repositório

```bash
git clone <url-do-repositorio>
cd SA-MA78-AEJRR
```

### 2. Instale as dependências

```bash
cd alleanza_immobiliare
pip install -r requirements.txt
```

### 3. Configure o banco de dados

Execute os scripts SQL da pasta `BancoDeDados/`, na ordem, em um cliente MySQL (Workbench, DBeaver, terminal `mysql`, etc.):

```bash
mysql -u seu_usuario -p < BancoDeDados/01_Criacao_Banco.sql
mysql -u seu_usuario -p < BancoDeDados/02_Criacao_Tabelas.sql
mysql -u seu_usuario -p < BancoDeDados/03_Inserts.sql   # opcional: dados de exemplo
mysql -u seu_usuario -p < BancoDeDados/05_Views.sql
mysql -u seu_usuario -p < BancoDeDados/07_Usuarios_Seguranca.sql
```

### 4. Configure as variáveis de ambiente

Copie o arquivo de exemplo e preencha com os dados do seu banco:

```bash
cd alleanza_immobiliare
cp .env.example .env
```

Edite o `.env` com suas credenciais:

```env
DB_HOST=localhost
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_PORT=3306
DB_NAME=alleanza_immobiliare
```

> ⚠️ O arquivo `.env` nunca deve ser enviado ao repositório (já está no `.gitignore`).

### 5. Execute o sistema

```bash
python main.py
```

## 🖥️ Como usar

Ao rodar `main.py`, o menu principal é exibido no terminal. Basta digitar o número da entidade desejada (ex: `7` para Imóvel) para abrir o submenu correspondente, com as opções de **Listar**, **Cadastrar**, **Atualizar** e **Deletar**. Digite `0` para voltar ao menu anterior ou encerrar o sistema.

```
========================================
      ALLEANZA IMMOBILIARE
========================================
1  - Endereço
2  - Proprietário
3  - Cliente
4  - Corretor
5  - Tipo de Imóvel
6  - Documento
7  - Imóvel
8  - Visita
9  - Venda
10 - Aluguel
11 - Contrato
12 - Pagamento
13 - Imóvel Documento
14 - Anúncio
15 - Foto Imóvel
0  - Sair
```

## 🗄️ Modelo de Dados

O banco relacional conecta as principais entidades do negócio imobiliário:

- Um **Imóvel** pertence a um **Proprietário**, tem um **Tipo de Imóvel** e um **Endereço**.
- **Visitas** relacionam **Cliente**, **Corretor** e **Imóvel**.
- **Venda**, **Aluguel** e **Contrato** formalizam as negociações entre clientes e imóveis.
- **Pagamento** está vinculado a um **Contrato**.
- **Imóvel Documento** e **Foto Imóvel** enriquecem o cadastro de cada imóvel.
- **Anúncio** representa a publicação de um imóvel para divulgação.

Os scripts completos de criação de tabelas, relacionamentos (chaves estrangeiras) e views estão disponíveis na pasta `BancoDeDados/`.

## 📄 Licença

Projeto acadêmico/demonstrativo — sem licença específica definida.
