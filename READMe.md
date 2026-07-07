# OrganizAI

O **OrganizAI** é um protótipo de sistema para auxiliar a organização de salas de aula, laboratórios e outros ambientes do Senac Ivaiporã.

O projeto está sendo desenvolvido por estudantes do **Ensino Médio Integrado ao Técnico em Inteligência Artificial**, com orientação do instrutor **Dieimes Nunes de Souza**, como proposta para o **Desafio EPT 2026**.

---

## Objetivo do projeto

Desenvolver uma solução simples e funcional para:

- Cadastrar ambientes da unidade;
- Registrar reservas de salas e laboratórios;
- Consultar a agenda de uso dos ambientes;
- Evitar conflitos de horário;
- Sugerir ambientes disponíveis;
- Gerar relatórios básicos;
- Permitir edição e exclusão de ambientes e reservas.

A proposta é aplicar conhecimentos de **Python** e **Banco de Dados** em um problema real do contexto educacional.

---

## Problema identificado

Em uma unidade de ensino, diferentes turmas, instrutores e atividades precisam utilizar salas, laboratórios e outros espaços em horários variados.

Quando essas informações não estão centralizadas, podem ocorrer situações como:

- dificuldade para saber quais ambientes estão disponíveis;
- reservas conflitantes para o mesmo horário;
- falta de histórico sobre o uso dos espaços;
- dificuldade para escolher o ambiente mais adequado para cada aula;
- necessidade de correção ou exclusão de registros cadastrados incorretamente.

---

## Solução proposta

O OrganizAI propõe um sistema simples para apoiar a gestão desses ambientes.

O sistema permite cadastrar ambientes, registrar reservas, consultar horários, identificar conflitos, sugerir ambientes disponíveis e visualizar relatórios.

Além disso, o sistema passou a contar com recursos de **edição e exclusão**, permitindo corrigir dados cadastrados ou remover registros quando necessário.

---

## Tecnologias utilizadas

- **Python:** linguagem principal do projeto;
- **Streamlit:** criação da interface visual no navegador;
- **PostgreSQL:** banco de dados utilizado para armazenar ambientes e reservas;
- **Pandas:** organização e exibição dos dados em tabelas e relatórios;
- **pgAdmin:** ferramenta visual para gerenciar o banco PostgreSQL;
- **GitHub:** versionamento, organização e registro do desenvolvimento.

---

## Funcionalidades implementadas

Até o momento, o protótipo possui:

- Tela inicial do sistema;
- Cadastro de ambientes;
- Listagem de ambientes;
- Edição de ambientes;
- Exclusão de ambientes;
- Cadastro de reservas;
- Listagem de reservas;
- Edição de reservas;
- Exclusão de reservas;
- Consulta de agenda por ambiente e data;
- Verificação de conflitos de horário;
- Sugestão de ambiente disponível;
- Relatórios simples de uso;
- Integração com banco de dados PostgreSQL.

---

## O que significa CRUD no projeto?

CRUD é uma sigla usada em sistemas para representar quatro operações básicas:

| Letra | Significado | No OrganizAI |
|---|---|---|
| C | Create | Cadastrar ambientes e reservas |
| R | Read | Consultar/listar ambientes e reservas |
| U | Update | Editar ambientes e reservas |
| D | Delete | Excluir ambientes e reservas |

Com essas operações, o OrganizAI fica mais próximo de um sistema real, pois permite criar, consultar, corrigir e remover registros.

---

## Estrutura do projeto

```text
organizAI/
│
├── docs/
│   ├── diario_didatico_alunos.md
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

Arquivo principal do sistema.

Nele ficam as telas criadas com Streamlit, como:

- Página inicial;
- Cadastro de ambientes;
- Gerenciamento de ambientes;
- Cadastro de reservas;
- Gerenciamento de reservas;
- Consulta de agenda;
- Sugestão de ambiente;
- Relatórios.

### `src/`

Pasta com os módulos Python responsáveis pela lógica do sistema.

- `db.py`: realiza a conexão com o banco PostgreSQL;
- `ambientes.py`: contém funções para cadastrar, listar, buscar, editar e excluir ambientes;
- `reservas.py`: contém funções para cadastrar, listar, buscar, editar, excluir e verificar conflitos de reservas;
- `sugestoes.py`: contém a lógica para sugerir ambientes disponíveis;
- `relatorios.py`: contém consultas para gerar relatórios do sistema.

### `sql/`

Pasta com os scripts SQL do projeto.

- `01_criar_tabelas.sql`: cria as tabelas do banco de dados;
- `02_dados_exemplo.sql`: insere dados fictícios para testes.

Esses arquivos são importantes porque permitem recriar o banco em outro computador.

### `docs/`

Pasta com a documentação do projeto.

- `relatorio_instrutor_senac.md`: relatório de acompanhamento do instrutor, com foco em prestação de contas pedagógica e técnica;
- `diario_didatico_alunos.md`: material explicativo para os alunos entenderem o projeto;
- `roteiro_video.md`: roteiro para organização do vídeo de apresentação.

### `imagens/`

Pasta destinada aos prints e evidências visuais do desenvolvimento do protótipo.

### `.env.example`

Modelo de configuração das variáveis de ambiente necessárias para conexão com o banco de dados.

Este arquivo pode ir para o GitHub, pois não contém senha real.

### `.env`

Arquivo local com as informações reais de conexão com o banco de dados.

Este arquivo **não deve ser enviado ao GitHub**, pois pode conter senha do banco.

Exemplo:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=organizai_db
DB_USER=postgres
DB_PASSWORD=sua_senha_aqui
```

---

## Banco de dados

O projeto utiliza o banco **PostgreSQL**.

Nome do banco utilizado no desenvolvimento:

```text
organizai_db
```

Tabelas principais:

```text
ambientes
reservas
```

A tabela `ambientes` armazena informações sobre salas, laboratórios e outros espaços.

A tabela `reservas` armazena os registros de uso dos ambientes em determinada data e horário.

A tabela `reservas` se relaciona com a tabela `ambientes`, pois cada reserva pertence a um ambiente.

---

## Como executar o projeto em outro computador

### 1. Clonar o repositório

```powershell
git clone https://github.com/DieimesNunes/organizAI.git
```

Entrar na pasta do projeto:

```powershell
cd organizAI
```

### 2. Criar o ambiente virtual

```powershell
py -m venv .venv
```

### 3. Ativar o ambiente virtual no Windows

```powershell
.\.venv\Scripts\Activate.ps1
```

Quando o ambiente virtual estiver ativo, o terminal deve mostrar algo parecido com:

```text
(.venv) PS C:\...\organizAI>
```

Se o PowerShell bloquear a ativação, execute:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Depois tente ativar novamente:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Instalar as dependências

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 5. Criar o arquivo `.env`

Na raiz do projeto, crie um arquivo chamado:

```text
.env
```

Dentro dele, coloque:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=organizai_db
DB_USER=postgres
DB_PASSWORD=sua_senha_do_postgres
```

A senha deve ser a mesma configurada na instalação do PostgreSQL.

### 6. Criar o banco de dados

O banco pode ser criado pelo **pgAdmin** ou pelo terminal.

#### Opção A: usando pgAdmin

1. Abrir o pgAdmin;
2. Criar um banco chamado `organizai_db`;
3. Abrir o **Query Tool** dentro do banco;
4. Executar o conteúdo do arquivo `sql/01_criar_tabelas.sql`;
5. Executar o conteúdo do arquivo `sql/02_dados_exemplo.sql`.

#### Opção B: usando terminal

Criar o banco:

```powershell
psql -U postgres -c "CREATE DATABASE organizai_db;"
```

Criar as tabelas:

```powershell
psql -U postgres -d organizai_db -f .\sql\01_criar_tabelas.sql
```

Inserir os dados fictícios de exemplo:

```powershell
psql -U postgres -d organizai_db -f .\sql\02_dados_exemplo.sql
```

### 7. Executar o sistema

```powershell
streamlit run app.py
```

Ou:

```powershell
python -m streamlit run app.py
```

Depois disso, o navegador deve abrir o sistema OrganizAI.

---

## Como testar o sistema

Após abrir o sistema, recomenda-se testar nesta ordem:

1. Acessar **Cadastro de ambientes**;
2. Cadastrar uma sala ou laboratório;
3. Acessar **Gerenciar ambientes**;
4. Editar um ambiente cadastrado;
5. Cadastrar uma reserva em **Cadastro de reservas**;
6. Acessar **Gerenciar reservas**;
7. Editar uma reserva;
8. Tentar cadastrar uma reserva conflitante;
9. Verificar se o sistema bloqueia o conflito;
10. Testar a **Sugestão de ambiente**;
11. Abrir a tela de **Relatórios**;
12. Excluir uma reserva de teste;
13. Excluir um ambiente que não tenha reservas vinculadas.

---

## Regra de segurança na exclusão de ambientes

O sistema não deve permitir a exclusão de um ambiente que possui reservas vinculadas.

Isso evita problemas no banco de dados, pois uma reserva precisa estar ligada a um ambiente existente.

Exemplo:

```text
A Sala 03 possui reservas cadastradas.
Nesse caso, ela não deve ser excluída diretamente.
```

Para excluir esse ambiente, primeiro seria necessário remover as reservas vinculadas a ele.

---

## Cuidados com dados sensíveis

Este projeto tem caráter educacional e será apresentado como protótipo.

Durante os testes e demonstrações, devem ser utilizados dados fictícios ou genéricos.

O arquivo `.env`, que pode conter senha do banco de dados, não deve ser enviado ao GitHub.

---

## Situação atual do protótipo

O projeto possui uma versão funcional com:

- Cadastro, consulta, edição e exclusão de ambientes;
- Cadastro, consulta, edição e exclusão de reservas;
- Consulta de agenda;
- Verificação de conflitos de horário;
- Sugestão de ambientes disponíveis;
- Relatórios simples;
- Integração com PostgreSQL;
- Documentação de apoio;
- Roteiro para apresentação.

---

## Próximos passos

- Revisar o funcionamento do sistema com os alunos;
- Testar o protótipo com dados fictícios;
- Registrar prints e evidências;
- Atualizar os materiais impressos, se necessário;
- Ensaiar a apresentação;
- Gravar o vídeo final do projeto;
- Preparar o envio conforme as orientações do Desafio EPT 2026.

---

## Observação final

O OrganizAI é um protótipo educacional.

Ele foi criado para demonstrar como conhecimentos de Python e Banco de Dados podem ser aplicados na resolução de um problema real: a organização de salas e laboratórios do Senac Ivaiporã.
