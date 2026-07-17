# OrganizAI

O **OrganizAI** é um protótipo de sistema para auxiliar a organização de salas de aula, laboratórios e outros ambientes do Senac Ivaiporã.

O projeto foi desenvolvido no contexto do **Desafio EPT 2026**, com estudantes do **Ensino Médio Integrado ao Técnico em Inteligência Artificial**, integrando principalmente conhecimentos das unidades curriculares de **Python** e **Banco de Dados**.

---

## Identificação do projeto

**Nome do projeto:** OrganizAI – Solução para Gestão de Salas e Laboratórios no Senac Ivaiporã  
**Unidade:** Senac Ivaiporã  
**Curso:** Ensino Médio Integrado ao Técnico em Inteligência Artificial  
**Ano:** 2026  
**Instrutor orientador:** Dieimes Nunes de Souza  
**Unidades curriculares envolvidas:** Python e Banco de Dados  
**Banco de dados utilizado:** PostgreSQL  

---

## Equipe do projeto

O projeto OrganizAI foi desenvolvido com a participação dos seguintes estudantes:

- Brayner Lohan de Jesus Dias dos Santos;
- Christopher Barbosa Silveira;
- Gabriel Rodrigues Lima Ronque;
- Kauan Henrique Jesus de Oliveira;
- Pablo Henrique de Rezende Salustiano;
- Tainara Botelho Pereira.

## Objetivo do projeto

Desenvolver uma solução simples e funcional para apoiar a gestão de ambientes educacionais da unidade, permitindo cadastrar salas e laboratórios, registrar reservas, consultar agenda, evitar conflitos de horário, sugerir ambientes disponíveis e gerar relatórios básicos.

A proposta busca aplicar conhecimentos de **programação em Python** e **banco de dados PostgreSQL** em uma situação real do contexto escolar.

---

## Problema identificado

Em uma unidade de ensino, diferentes turmas, instrutores e atividades precisam utilizar salas, laboratórios e outros espaços em horários variados.

Quando essas informações não estão centralizadas, podem ocorrer situações como:

- dificuldade para saber quais ambientes estão disponíveis;
- possibilidade de reserva duplicada no mesmo horário;
- falta de registro organizado sobre o uso dos espaços;
- dificuldade para escolher o ambiente mais adequado para determinada aula;
- necessidade de corrigir ou excluir informações cadastradas incorretamente.

Diante dessa realidade, o OrganizAI foi pensado como uma solução simples para apoiar o registro, a consulta e a organização dessas informações.

---

## Solução proposta

O OrganizAI propõe um sistema web simples, acessado pelo navegador, que permite organizar informações sobre ambientes e reservas.

O sistema foi desenvolvido como um **protótipo educacional**, com foco em demonstrar uma solução funcional e viável para o problema identificado.

A solução permite:

- cadastrar ambientes da unidade;
- consultar ambientes cadastrados;
- editar dados de ambientes;
- excluir ambientes, quando não houver reservas vinculadas;
- cadastrar reservas;
- consultar reservas cadastradas;
- editar reservas;
- excluir reservas;
- verificar conflitos de horário;
- sugerir ambientes disponíveis;
- visualizar relatórios simples.

---

## Funcionalidades implementadas

Até o momento, o protótipo possui as seguintes funcionalidades:

- Tela inicial de apresentação do sistema;
- Cadastro de ambientes;
- Listagem de ambientes cadastrados;
- Edição de ambientes;
- Exclusão de ambientes;
- Cadastro de reservas;
- Listagem de reservas cadastradas;
- Edição de reservas;
- Exclusão de reservas;
- Consulta de agenda por ambiente e data;
- Verificação automática de conflitos de horário;
- Sugestão de ambiente disponível com base em data, horário, capacidade e recursos necessários;
- Relatórios simples de uso;
- Integração com banco de dados PostgreSQL.

---

## O que o sistema evita?

Uma das funções mais importantes do OrganizAI é impedir conflitos de horário.

Por exemplo:

```text
Se a Sala 03 já estiver reservada das 07h15 às 12h35,
o sistema não deve permitir outra reserva para a mesma sala,
na mesma data e dentro desse mesmo intervalo.
```

Essa regra ajuda a evitar duplicidade no uso dos ambientes.

---

## O que significa CRUD no projeto?

CRUD é uma sigla utilizada em sistemas para representar quatro operações básicas:

| Operação | Significado | Aplicação no OrganizAI |
|---|---|---|
| Create | Criar/cadastrar | Cadastrar ambientes e reservas |
| Read | Ler/consultar | Listar ambientes, reservas e agenda |
| Update | Atualizar/editar | Editar ambientes e reservas |
| Delete | Excluir | Excluir ambientes e reservas |

Com essas operações, o OrganizAI fica mais próximo de um sistema real, pois permite criar, consultar, corrigir e remover registros.

---

## Tecnologias utilizadas

- **Python:** linguagem principal utilizada para desenvolver a lógica do sistema;
- **Streamlit:** ferramenta utilizada para criar a interface visual no navegador;
- **PostgreSQL:** banco de dados utilizado para armazenar ambientes e reservas;
- **pgAdmin:** ferramenta utilizada para criar e gerenciar o banco PostgreSQL;
- **Pandas:** biblioteca utilizada para organizar e exibir dados em tabelas e relatórios;
- **GitHub:** plataforma utilizada para versionamento, organização e registro do desenvolvimento.

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

## Descrição dos principais arquivos

### `app.py`

Arquivo principal do sistema. Nele ficam as telas criadas com Streamlit:

- Página inicial;
- Cadastro de ambientes;
- Gerenciamento de ambientes;
- Cadastro de reservas;
- Gerenciamento de reservas;
- Consulta de agenda;
- Sugestão de ambiente;
- Relatórios.

### `src/db.py`

Arquivo responsável pela conexão entre o Python e o banco PostgreSQL.

### `src/ambientes.py`

Contém as funções relacionadas aos ambientes, como:

- cadastrar ambiente;
- listar ambientes;
- buscar ambiente por ID;
- editar ambiente;
- excluir ambiente;
- verificar se um ambiente possui reservas vinculadas.

### `src/reservas.py`

Contém as funções relacionadas às reservas, como:

- cadastrar reserva;
- listar reservas;
- buscar reserva por ID;
- editar reserva;
- excluir reserva;
- verificar conflitos de horário.

### `src/sugestoes.py`

Contém a lógica para sugerir ambientes disponíveis de acordo com data, horário, capacidade mínima e recursos necessários.

### `src/relatorios.py`

Contém consultas utilizadas para gerar relatórios simples, como total de ambientes, total de reservas, reservas por ambiente, ambientes por tipo e reservas por data.

### `sql/01_criar_tabelas.sql`

Script responsável pela criação das tabelas do banco de dados.

### `sql/02_dados_exemplo.sql`

Script com dados fictícios para testes e demonstração do sistema.

### `.env.example`

Modelo de configuração do arquivo `.env`.

Este arquivo pode ir para o GitHub porque não contém senha real.

### `.env`

Arquivo local com as informações reais de conexão com o banco de dados.

Este arquivo **não deve ser enviado ao GitHub**, pois pode conter senha.

---

## Banco de dados

O projeto utiliza o banco **PostgreSQL**.

Nome do banco utilizado:

```text
organizai_db
```

Tabelas principais:

```text
ambientes
reservas
```

A tabela `ambientes` armazena informações sobre salas, laboratórios e outros espaços.

A tabela `reservas` armazena informações sobre o uso desses ambientes em determinada data e horário.

Cada reserva fica vinculada a um ambiente, permitindo trabalhar conceitos de banco de dados como **chave primária**, **chave estrangeira** e **relacionamento entre tabelas**.

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

Se o PowerShell bloquear a ativação, executar:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Depois ativar novamente:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Instalar as dependências

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 5. Criar o arquivo `.env`

Na raiz do projeto, criar um arquivo chamado:

```text
.env
```

Dentro dele, colocar:

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
5. Tentar excluir um ambiente com reserva vinculada;
6. Cadastrar uma reserva em **Cadastro de reservas**;
7. Acessar **Gerenciar reservas**;
8. Editar uma reserva;
9. Tentar cadastrar uma reserva conflitante;
10. Verificar se o sistema bloqueia o conflito;
11. Testar a **Sugestão de ambiente**;
12. Abrir a tela de **Relatórios**;
13. Excluir uma reserva de teste;
14. Excluir um ambiente sem reservas vinculadas.

---

## Regra de segurança na exclusão de ambientes

O sistema não deve permitir a exclusão de um ambiente que possui reservas vinculadas.

Essa regra evita inconsistência no banco de dados, pois uma reserva precisa estar associada a um ambiente existente.

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
- Roteiro para apresentação;
- Vídeo de apresentação do projeto.

---

## Possíveis melhorias futuras

Como o OrganizAI é um protótipo, algumas melhorias podem ser desenvolvidas futuramente, como:

- criação de tela de login;
- perfis de usuário;
- exportação de relatórios;
- filtros mais avançados;
- painel administrativo;
- publicação do sistema em servidor;
- melhoria visual da interface;
- integração com ferramentas institucionais.

---

## Observação final

O OrganizAI é um protótipo educacional.

Ele demonstra como conhecimentos de **Python** e **Banco de Dados** podem ser aplicados para resolver um problema real: a organização de salas e laboratórios do Senac Ivaiporã.
