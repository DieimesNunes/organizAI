# Relatório do Instrutor para Acompanhamento do Projeto OrganizAI

## 1. Identificação

**Projeto:** OrganizAI – Solução para Gestão de Salas e Laboratórios no Senac Ivaiporã  
**Instrutor:** Dieimes Nunes de Souza  
**Turma:** Ensino Médio Integrado ao Técnico em Inteligência Artificial  
**Unidades curriculares envolvidas:** Python e Banco de Dados  
**Banco de dados utilizado:** PostgreSQL  
**Ferramentas utilizadas:** VS Code, Python, Streamlit, Pandas, PostgreSQL, pgAdmin e GitHub  
**Data do registro:** 30/06/2026  

---

## 2. Finalidade deste relatório

Este relatório tem como objetivo registrar, de forma clara e organizada, as ações realizadas pelo instrutor no desenvolvimento do projeto **OrganizAI**.

O documento pode ser utilizado como prestação de contas pedagógica e técnica, caso seja necessário informar à equipe do Senac quais atividades foram realizadas, quais decisões foram tomadas e quais encaminhamentos foram adotados para viabilizar a continuidade do projeto.

A intenção é demonstrar que houve uma intervenção pedagógica planejada, com foco em recuperar o andamento do projeto, organizar o escopo, estruturar o ambiente de desenvolvimento e criar uma base funcional para que os estudantes possam compreender, testar, explicar e apresentar o protótipo.

---

## 3. Contexto do projeto

O projeto **OrganizAI** foi pensado para apoiar a gestão de salas de aula e laboratórios do Senac Ivaiporã.

A proposta surgiu a partir de uma necessidade real da unidade: melhorar a organização das informações relacionadas ao uso de ambientes educacionais, como salas, laboratórios e auditório.

Em uma instituição de ensino, diferentes turmas, instrutores e atividades utilizam espaços em horários variados. Quando esses registros não estão organizados em uma ferramenta centralizada, podem ocorrer dificuldades de consulta, falta de histórico e possíveis conflitos de horário.

Dessa forma, o projeto propõe um sistema simples para cadastrar ambientes, registrar reservas, consultar agenda, verificar conflitos e sugerir ambientes disponíveis.

---

## 4. Situação encontrada

O projeto estava atrasado em relação ao prazo previsto para desenvolvimento.

Além disso, os estudantes envolvidos pertencem ao primeiro ano do Ensino Médio Integrado ao Técnico em Inteligência Artificial e ainda estão em fase inicial de formação técnica, especialmente nos conteúdos de programação, banco de dados e desenvolvimento de sistemas.

Diante desse cenário, foi necessário realizar uma intervenção pedagógica para evitar que o projeto ficasse apenas no campo da ideia e não chegasse a um protótipo funcional.

A intervenção teve como objetivo organizar tecnicamente o projeto e criar uma base que pudesse ser compreendida e apropriada pelos alunos nas próximas etapas.

---

## 5. Decisão pedagógica adotada: desenvolvimento de um MVP

Foi definido que o projeto seria desenvolvido como um **MVP**, ou seja, um Produto Mínimo Viável.

No contexto deste projeto, MVP significa criar uma versão inicial, simples e funcional do sistema, contendo apenas as funcionalidades essenciais para demonstrar a proposta.

Essa decisão foi tomada por três motivos principais:

1. O prazo para desenvolvimento estava reduzido;
2. Os alunos ainda estão iniciando sua formação técnica;
3. O projeto precisava apresentar um protótipo funcional, mesmo que simples.

As funcionalidades priorizadas foram:

- Cadastro de ambientes;
- Cadastro de reservas;
- Consulta de agenda;
- Verificação de conflitos de horário;
- Sugestão de ambiente disponível;
- Relatórios básicos.

Essa definição permitiu manter o projeto viável, objetivo e alinhado às unidades curriculares de Python e Banco de Dados.

---

## 6. Tecnologias escolhidas e justificativa

### Python

O Python foi escolhido por ser a linguagem trabalhada na unidade curricular e por permitir construir a lógica do sistema de forma mais acessível aos alunos.

No projeto, o Python é utilizado para organizar as telas, processar dados, validar informações, conectar com o banco de dados e executar regras de negócio, como a verificação de conflitos de horário.

### Streamlit

O Streamlit foi escolhido para criar a interface visual do sistema.

A escolha se justifica porque o Streamlit permite criar telas no navegador utilizando apenas Python. Isso reduz a complexidade do projeto, pois evita a necessidade de trabalhar, neste momento, com HTML, CSS, JavaScript, Flask ou Django.

Essa ferramenta facilita a criação de um protótipo demonstrável e compreensível para os estudantes.

### Pandas

O Pandas foi utilizado para organizar os dados em formato de tabela.

No projeto, ele apoia a visualização de ambientes cadastrados, reservas registradas e relatórios simples. Dessa forma, os dados vindos do banco podem ser apresentados de maneira mais clara na interface do sistema.

### PostgreSQL

O PostgreSQL foi escolhido como banco de dados do projeto.

Ele permite armazenar os dados de forma permanente, substituindo o armazenamento temporário das primeiras versões do protótipo.

Com ele, é possível trabalhar conceitos importantes da unidade curricular de Banco de Dados, como tabelas, campos, tipos de dados, chave primária, chave estrangeira, relacionamento entre tabelas, inserção e consulta de dados.

### GitHub

O GitHub foi utilizado para registrar a evolução do projeto.

Por meio dele, é possível acompanhar os arquivos desenvolvidos, os commits realizados e a organização do código-fonte. O GitHub também serve como evidência do processo de desenvolvimento.

---

## 7. Atividades realizadas em 30/06/2026

### 7.1 Organização inicial da estrutura do projeto

Foi criada a estrutura inicial do projeto no VS Code, separando os arquivos por finalidade.

A estrutura foi organizada em pastas para documentação, imagens, scripts SQL e código-fonte.

Estrutura geral:

```text
OrganizAI/
│
├── docs/
│   ├── diario_bordo.md
│   ├── diario_bordo_instrutor.md
│   ├── metodologia.md
│   ├── problema.md
│   └── roteiro_video.md
│
├── imagens/
│
├── sql/
│   ├── 01_criar_tabelas.sql
│   └── 02_dados_exemplo.sql
│
├── src/
│   ├── ambientes.py
│   ├── db.py
│   ├── reservas.py
│   ├── sugestoes.py
│   └── relatorios.py
│
├── app.py
├── README.md
├── requirements.txt
├── .env.example
└── .gitignore
```

Essa organização facilita a manutenção do projeto e permite que os estudantes compreendam melhor a função de cada arquivo.

---

### 7.2 Configuração do ambiente Python

Foi realizada a configuração do ambiente Python no Windows.

Também foi criado um ambiente virtual chamado `.venv`, utilizado para isolar as bibliotecas do projeto.

Foram instaladas as bibliotecas necessárias para o protótipo:

- Streamlit;
- Pandas;
- python-dotenv;
- psycopg.

Essa etapa foi necessária para preparar o computador para executar o sistema e desenvolver as funcionalidades.

---

### 7.3 Criação da primeira interface em Streamlit

Foi criada a primeira tela do sistema OrganizAI utilizando Streamlit.

A tela inicial apresenta o nome do projeto, a descrição da solução, o objetivo geral e as funcionalidades previstas.

Essa etapa foi importante porque transformou a proposta em uma primeira interface visual, permitindo visualizar o projeto funcionando no navegador.

---

### 7.4 Criação e configuração do repositório no GitHub

O projeto foi enviado para um repositório no GitHub.

O repositório passou a armazenar a estrutura inicial do projeto, o código-fonte, os scripts SQL, a documentação e os registros de desenvolvimento.

Também foi configurado o arquivo `.gitignore` para impedir o envio de arquivos sensíveis ou desnecessários, como:

- `.env`;
- `.venv/`;
- arquivos de cache do Python;
- arquivos temporários de teste.

Esse cuidado é importante porque o arquivo `.env` pode conter informações de acesso ao banco de dados.

---

### 7.5 Criação da tela de cadastro de ambientes

Foi desenvolvida a funcionalidade de cadastro de ambientes.

Essa tela permite registrar informações como:

- Nome do ambiente;
- Tipo de ambiente;
- Capacidade;
- Presença de computadores;
- Presença de projetor;
- Observações.

Inicialmente, os dados foram armazenados de forma temporária dentro do próprio Streamlit, utilizando o `session_state`.

Depois, essa funcionalidade foi integrada ao PostgreSQL, passando a gravar os dados permanentemente na tabela `ambientes`.

---

### 7.6 Criação da tela de cadastro de reservas

Foi desenvolvida a funcionalidade de cadastro de reservas.

Essa tela permite informar:

- Ambiente;
- Turma;
- Instrutor;
- Unidade curricular;
- Data;
- Horário de início;
- Horário de término;
- Finalidade da reserva.

A funcionalidade foi posteriormente integrada ao PostgreSQL, gravando os dados na tabela `reservas`.

---

### 7.7 Implementação da verificação de conflitos

Foi implementada uma regra para verificar conflitos de horário.

O sistema verifica se já existe uma reserva para o mesmo ambiente, na mesma data e em horário que se cruza com a nova reserva solicitada.

Exemplo: se a Sala 03 já estiver reservada das 07h15 às 12h35, o sistema não permite cadastrar outra reserva para a mesma sala, na mesma data, dentro desse intervalo.

Essa funcionalidade é central para o projeto, pois responde diretamente ao problema de organização dos ambientes.

---

### 7.8 Criação da consulta de agenda

Foi criada uma tela de consulta de agenda.

Essa tela permite visualizar as reservas cadastradas e aplicar filtros por ambiente e data.

A funcionalidade permite demonstrar como o sistema pode apoiar a consulta rápida sobre a ocupação dos espaços.

---

### 7.9 Criação dos scripts SQL

Foram preparados os scripts SQL iniciais do projeto.

O arquivo `01_criar_tabelas.sql` contém a criação das tabelas principais:

- `ambientes`;
- `reservas`.

O arquivo `02_dados_exemplo.sql` contém dados fictícios para testes.

Essa etapa conecta o projeto à unidade curricular de Banco de Dados e permite demonstrar conceitos como tabelas, campos, chave primária, chave estrangeira e relacionamento entre entidades.

---

### 7.10 Instalação e configuração do PostgreSQL

Foi realizada a instalação do PostgreSQL no Windows.

Por meio do pgAdmin, foi criado o banco de dados:

```text
organizai_db
```

Em seguida, foram executados os scripts SQL para criar as tabelas e inserir dados de exemplo.

---

### 7.11 Conexão entre Python e PostgreSQL

Foi criado o arquivo `src/db.py`, responsável por centralizar a conexão entre o Python e o banco de dados PostgreSQL.

Também foi configurado o arquivo `.env`, utilizado para armazenar as informações de acesso ao banco de dados sem expor esses dados diretamente no código-fonte.

Foi realizado um teste de conexão e o Python conseguiu acessar o banco `organizai_db` com sucesso.

---

### 7.12 Integração do cadastro de ambientes com PostgreSQL

A tela de cadastro de ambientes foi integrada ao PostgreSQL.

A partir dessa etapa, os ambientes cadastrados passaram a ser gravados permanentemente no banco de dados.

Também foi criada a função de listagem dos ambientes, permitindo que o sistema busque os dados diretamente da tabela `ambientes`.

---

### 7.13 Integração do cadastro de reservas com PostgreSQL

A tela de cadastro de reservas foi integrada ao PostgreSQL.

Cada reserva passou a ser gravada na tabela `reservas`, relacionada a um ambiente previamente cadastrado na tabela `ambientes`.

Essa etapa reforça a aplicação prática do conceito de chave estrangeira, pois cada reserva depende de um ambiente existente.

---

### 7.14 Criação da sugestão de ambiente disponível

Foi criada a funcionalidade de sugestão de ambiente disponível.

Nessa tela, o usuário informa:

- Data desejada;
- Horário de início;
- Horário de término;
- Capacidade mínima;
- Necessidade de computadores;
- Necessidade de projetor.

Com base nesses critérios, o sistema consulta o banco de dados e retorna apenas os ambientes disponíveis.

Essa funcionalidade representa uma evolução do protótipo, pois o sistema deixa de apenas registrar dados e passa também a apoiar a tomada de decisão.

---

### 7.15 Criação da tela de relatórios

Foi criada a tela de relatórios do projeto.

A tela apresenta:

- Total de ambientes cadastrados;
- Total de reservas registradas;
- Reservas por ambiente;
- Ambientes por tipo;
- Reservas por data.

Os dados são buscados no PostgreSQL e organizados com apoio do Pandas.

Essa etapa demonstra como os registros armazenados no banco podem gerar informações úteis para análise e acompanhamento.

---

### 7.16 Organização inicial do roteiro do vídeo

Foi iniciado o roteiro do vídeo de apresentação do projeto.

O roteiro busca orientar os estudantes sobre como apresentar:

- Identificação da equipe;
- Problema identificado;
- Solução proposta;
- Tecnologias utilizadas;
- Demonstração do protótipo;
- Metodologia de desenvolvimento;
- Impactos esperados;
- Viabilidade técnica e econômica;
- Considerações finais.

Essa etapa é importante para preservar o protagonismo estudantil na apresentação.

---

## 8. Resultados alcançados

Ao final das atividades, o projeto passou a contar com um protótipo funcional contendo:

- Tela inicial;
- Cadastro de ambientes;
- Cadastro de reservas;
- Consulta de agenda;
- Verificação de conflitos;
- Sugestão de ambiente disponível;
- Tela de relatórios;
- Banco de dados PostgreSQL;
- Repositório no GitHub;
- Documentação inicial.

O projeto deixou de ser apenas uma proposta escrita e passou a ter uma aplicação funcional, demonstrável e alinhada ao problema identificado.

---

## 9. Relação com as unidades curriculares

### Python

O projeto permite trabalhar:

- Funções;
- Condicionais;
- Listas e dicionários;
- Datas e horários;
- Validação de dados;
- Organização de código;
- Criação de interfaces com Streamlit;
- Conexão com banco de dados.

### Banco de Dados

O projeto permite trabalhar:

- Criação de banco;
- Criação de tabelas;
- Campos e tipos de dados;
- Chave primária;
- Chave estrangeira;
- Relacionamento entre tabelas;
- Inserção de registros;
- Consultas SQL;
- Consultas com `JOIN`;
- Regras de negócio baseadas em dados.

---

## 10. Participação prevista dos estudantes

Mesmo com a intervenção técnica do instrutor, os estudantes continuarão participando do projeto.

A participação esperada envolve:

- Testar o sistema;
- Cadastrar dados fictícios;
- Verificar se a regra de conflito funciona;
- Validar a sugestão de ambientes;
- Produzir prints e registros;
- Explicar as telas do sistema;
- Relacionar o projeto com Python e Banco de Dados;
- Participar do vídeo de apresentação.

O protagonismo estudantil será preservado principalmente na explicação do problema, na demonstração do protótipo e na apresentação dos impactos esperados.

---

## 11. Cuidados adotados

Foram adotados cuidados para evitar exposição de dados sensíveis.

Durante testes e demonstrações, serão utilizados dados fictícios ou genéricos.

O arquivo `.env`, que pode conter senha do banco de dados, foi mantido fora do GitHub por meio do `.gitignore`.

O projeto possui caráter educacional e será apresentado como protótipo.

---

## 12. Próximos encaminhamentos

Os próximos encaminhamentos são:

1. Revisar o funcionamento do sistema com os estudantes;
2. Explicar cada tela do protótipo de forma didática;
3. Realizar testes com dados fictícios;
4. Registrar evidências em imagens;
5. Atualizar o README do projeto, se necessário;
6. Ajustar o roteiro do vídeo;
7. Dividir as falas entre os alunos;
8. Ensaiar a apresentação;
9. Gravar o vídeo final;
10. Preparar o envio conforme orientação do Desafio EPT.

---

## 13. Considerações finais

As atividades realizadas foram fundamentais para recuperar o andamento do projeto OrganizAI.

A intervenção do instrutor foi necessária para organizar tecnicamente a proposta, reduzir o escopo, criar uma base funcional e permitir que os alunos avancem com mais segurança.

O projeto agora possui um protótipo demonstrável, com funcionalidades relacionadas diretamente ao problema de gestão de ambientes da unidade.

A solução está alinhada às unidades curriculares de Python e Banco de Dados e permite que os estudantes compreendam, na prática, como a tecnologia pode ser aplicada para resolver problemas reais do contexto educacional.
