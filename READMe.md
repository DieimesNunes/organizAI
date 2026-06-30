# OrganizAI

O **OrganizAI** é um protótipo de solução digital para auxiliar a gestão de salas de aula e laboratórios do Senac Ivaiporã.

O projeto está sendo desenvolvido por estudantes do **Ensino Médio Integrado ao Técnico em Inteligência Artificial**, com orientação do instrutor **Dieimes Nunes de Souza**, como proposta para o **Desafio EPT 2026**.

---

## Objetivo

Desenvolver um sistema simples para cadastrar ambientes, registrar reservas, consultar horários, verificar conflitos e sugerir salas ou laboratórios disponíveis conforme a necessidade da aula.

---

## Problema identificado

A organização de salas e laboratórios é uma atividade importante para o funcionamento das atividades pedagógicas.

Quando não há um controle centralizado, podem ocorrer situações como:

- dificuldade para consultar quais ambientes estão disponíveis;
- conflito de horários entre turmas ou atividades;
- falta de registro sobre o uso das salas e laboratórios;
- dificuldade para escolher o ambiente mais adequado para cada aula.

---

## Solução proposta

O OrganizAI propõe uma ferramenta simples, acessível e funcional para apoiar o registro, a consulta e a organização das informações sobre os ambientes da unidade.

O sistema permite cadastrar ambientes, registrar reservas, consultar agenda, verificar conflitos de horário, sugerir ambientes disponíveis e visualizar relatórios básicos.

---

## Tecnologias utilizadas

- **Python:** linguagem principal do projeto;
- **Streamlit:** criação da interface visual no navegador;
- **PostgreSQL:** banco de dados utilizado para armazenar ambientes e reservas;
- **Pandas:** organização e exibição de dados em tabelas e relatórios;
- **pgAdmin:** gerenciamento visual do banco PostgreSQL;
- **GitHub:** versionamento, organização e registro do desenvolvimento.

---

## Funcionalidades implementadas

- Tela inicial do sistema;
- Cadastro de salas e laboratórios;
- Cadastro de reservas;
- Consulta de agenda por ambiente e data;
- Verificação de conflitos de horário;
- Sugestão de ambiente disponível;
- Relatórios simples de uso;
- Integração com banco de dados PostgreSQL.

---

## Estrutura do projeto

```text
organizAI/
│
├── docs/
│   ├── diario_bordo.md
│   ├── diario_didatico_alunos.md
│   ├── metodologia.md
│   ├── problema.md
│   ├── relatorio_instrutor_senac.md
│   └── roteiro_video.md
│
├── imagens/
│   └── primeira_tela_organizai.png
│
├── sql/
│   ├── 01_criar_tabelas.sql
│   └── 02_dados_exemplo.sql
│
├── src/
│   ├── ambientes.py
│   ├── db.py
│   ├── relatorios.py
│   ├── reservas.py
│   └── sugestoes.py
│
├── app.py
├── README.md
├── requirements.txt
├── .env.example
└── .gitignore
```

---

## Descrição das principais pastas e arquivos

### `app.py`

Arquivo principal do sistema. É nele que ficam as telas criadas com Streamlit, como página inicial, cadastro de ambientes, cadastro de reservas, consulta de agenda, sugestão de ambiente e relatórios.

### `src/`

Pasta com os módulos Python responsáveis pela lógica do sistema.

- `db.py`: faz a conexão com o banco PostgreSQL;
- `ambientes.py`: contém funções para cadastrar e listar ambientes;
- `reservas.py`: contém funções para cadastrar, listar e verificar conflitos de reservas;
- `sugestoes.py`: contém a lógica para sugerir ambientes disponíveis;
- `relatorios.py`: contém consultas para gerar relatórios do sistema.

### `sql/`

Pasta com os scripts SQL do projeto.

- `01_criar_tabelas.sql`: cria as tabelas do banco de dados;
- `02_dados_exemplo.sql`: insere dados fictícios para testes.

### `docs/`

Pasta com a documentação do projeto.

- `relatorio_instrutor_senac.md`: relatório de acompanhamento do instrutor, com foco em prestação de contas pedagógica e técnica;
- `diario_didatico_alunos.md`: material explicativo para os alunos entenderem o projeto;
- `roteiro_video.md`: roteiro para organização do vídeo de apresentação;
- `problema.md`: documento de apoio sobre o problema identificado;
- `metodologia.md`: documento de apoio sobre a metodologia do projeto;
- `diario_bordo.md`: registro geral da equipe, caso seja utilizado pelos alunos.

### `imagens/`

Pasta destinada aos prints e evidências visuais do desenvolvimento do protótipo.

### `.env.example`

Modelo de configuração das variáveis de ambiente necessárias para conexão com o banco de dados.

Este arquivo pode ir para o GitHub, pois não contém senha real.

### `.env`

Arquivo local com as informações reais de conexão com o banco de dados.

Este arquivo **não deve ser enviado ao GitHub**.

---

## Configuração do banco de dados

O projeto utiliza o banco PostgreSQL.

Banco utilizado no desenvolvimento:

```text
organizai_db
```

As tabelas principais são:

```text
ambientes
reservas
```

A tabela `ambientes` armazena informações sobre salas, laboratórios e outros espaços.

A tabela `reservas` armazena os registros de uso dos ambientes em determinada data e horário.

---

## Como executar o projeto

### 1. Criar o ambiente virtual

```bash
py -m venv .venv
```

### 2. Ativar o ambiente virtual no Windows

```bash
.venv\Scripts\Activate.ps1
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar o arquivo `.env`

Criar um arquivo `.env` na raiz do projeto com o seguinte modelo:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=organizai_db
DB_USER=postgres
DB_PASSWORD=sua_senha_aqui
```

### 5. Criar o banco de dados

No PostgreSQL/pgAdmin, criar o banco:

```text
organizai_db
```

Depois executar os scripts:

```text
sql/01_criar_tabelas.sql
sql/02_dados_exemplo.sql
```

### 6. Executar o sistema

```bash
streamlit run app.py
```

---

## Situação atual do protótipo

O projeto já possui uma versão funcional com cadastro de ambientes, cadastro de reservas, consulta de agenda, verificação de conflitos, sugestão de ambientes disponíveis, relatórios simples e integração com PostgreSQL.

---

## Cuidados com dados sensíveis

Este projeto tem caráter educacional e será apresentado como protótipo.

Durante os testes e demonstrações, devem ser utilizados dados fictícios ou genéricos.

O arquivo `.env`, que pode conter senha do banco de dados, não deve ser enviado ao GitHub.

---

## Próximos passos

- Revisar o funcionamento do sistema com os alunos;
- Testar o protótipo com dados fictícios;
- Registrar prints e evidências;
- Ajustar a documentação;
- Ensaiar a apresentação;
- Gravar o vídeo final do projeto.
```
