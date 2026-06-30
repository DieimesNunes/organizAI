# Diário de Bordo do Instrutor - Projeto OrganizAI

## Identificação

**Projeto:** OrganizAI - Solução para Gestão de Salas e Laboratórios no Senac Ivaiporã  
**Instrutor:** Dieimes Nunes de Souza  
**Turma:** Ensino Médio Integrado ao Técnico em Inteligência Artificial  
**Unidades curriculares envolvidas:** Python e Banco de Dados  
**Banco de dados utilizado:** PostgreSQL  

---

## Objetivo deste diário

Este diário tem como objetivo registrar minha participação como instrutor orientador no desenvolvimento do projeto OrganizAI.

O projeto está sendo desenvolvido com estudantes do primeiro ano do Ensino Médio Integrado ao Técnico em Inteligência Artificial. Como os alunos ainda estão em fase inicial de formação em programação, foi necessário organizar uma estrutura inicial do projeto, definir tecnologias, dividir tarefas e orientar tecnicamente a equipe.

A intenção é manter transparência com os estudantes, mostrando quais partes foram estruturadas pelo instrutor e quais partes serão desenvolvidas, testadas, explicadas e apresentadas pelos alunos.

---

## Situação inicial do projeto

O projeto OrganizAI foi pensado para resolver um problema real da unidade: apoiar a organização de salas de aula e laboratórios do Senac Ivaiporã.

A proposta inicial previa a criação de uma solução simples para registrar ambientes, reservas, horários de uso e possíveis conflitos na utilização dos espaços.

Devido ao atraso no desenvolvimento e ao nível inicial de conhecimento técnico dos estudantes, foi necessária uma intervenção pedagógica para reduzir o escopo e transformar a ideia em um protótipo viável.

---

## Decisão pedagógica

Foi definido que o projeto será desenvolvido como um MVP, ou seja, uma versão mínima funcional.

O sistema terá como foco principal:

- Cadastro de ambientes;
- Cadastro de reservas;
- Consulta de reservas;
- Verificação de conflitos de horário;
- Sugestão simples de ambiente disponível;
- Relatórios básicos de uso.

Essa decisão foi tomada para garantir que o projeto seja possível de ser concluído dentro do prazo, mantendo relação direta com as unidades curriculares de Python e Banco de Dados.

---

## Tecnologias escolhidas

Foram escolhidas as seguintes tecnologias:

- Python, para a lógica do sistema;
- PostgreSQL, para armazenamento dos dados;
- Streamlit, para criação da interface visual;
- Pandas, para organização de tabelas e relatórios;
- GitHub, para versionamento e registro do desenvolvimento.

A escolha dessas ferramentas considera o nível atual da turma, a necessidade de criar um protótipo funcional e a possibilidade de os alunos compreenderem cada parte do processo.

---

## Registro das ações do instrutor

### 30/06/2026

Foi criada a estrutura inicial do projeto no VS Code, contendo as pastas:

- docs;
- imagens;
- sql;
- src.

Também foram criados arquivos iniciais para documentação, banco de dados e código-fonte.

A estrutura inicial do projeto foi organizada para facilitar a divisão de tarefas entre os alunos e permitir o acompanhamento do desenvolvimento pelo GitHub.

---

## Participação esperada dos alunos

Os alunos deverão participar das seguintes etapas:

- Compreensão do problema;
- Explicação da proposta;
- Testes do protótipo;
- Cadastro de dados fictícios;
- Validação das regras de conflito;
- Produção de prints e registros;
- Apresentação do funcionamento do sistema;
- Participação no vídeo final do projeto.

O protagonismo dos estudantes será preservado na explicação da solução, na demonstração do protótipo e na reflexão sobre os impactos do projeto.

---

## Observações importantes

Este projeto tem caráter pedagógico e será apresentado como protótipo.

Não serão utilizados dados sensíveis de alunos, instrutores ou turmas reais sem necessidade. Para os testes e demonstrações, serão utilizados dados fictícios ou genéricos, respeitando a privacidade e a imagem institucional.

---

## Próximos passos

- Instalar e configurar o Python no Windows;
- Criar o ambiente virtual do projeto;
- Instalar as bibliotecas necessárias;
- Criar o banco de dados no PostgreSQL;
- Criar as tabelas iniciais;
- Desenvolver a primeira tela do sistema com Streamlit;
- Testar o cadastro de ambientes;
- Registrar evidências para o diário de bordo e para o vídeo final.

### 30/06/2026 - Configuração inicial do ambiente Python

Foi realizada a instalação do Python no Windows e criada a estrutura inicial do ambiente virtual do projeto OrganizAI.

Também foram instaladas as bibliotecas iniciais necessárias para o desenvolvimento do protótipo, incluindo Streamlit, Pandas, python-dotenv e psycopg.

O Streamlit foi testado no terminal e retornou a versão instalada, confirmando que a ferramenta está disponível para uso no projeto.

Essa etapa foi importante para preparar o ambiente de desenvolvimento e permitir a criação da primeira interface visual do sistema.

### 30/06/2026 - Primeira tela do OrganizAI

Foi criada a primeira interface visual do projeto OrganizAI utilizando Streamlit.

A tela inicial apresenta o nome do projeto, sua finalidade, o objetivo do sistema e as funcionalidades previstas, como cadastro de ambientes, cadastro de reservas, consulta de agenda, verificação de conflitos, sugestão de ambiente disponível e relatórios simples.

Também foi registrado um print da primeira tela do sistema na pasta imagens, servindo como evidência do andamento inicial do protótipo.

Essa etapa marcou o início prático do desenvolvimento da solução.

### 30/06/2026 - Envio do projeto para o GitHub

O projeto OrganizAI foi enviado para um repositório no GitHub, permitindo o registro do histórico de desenvolvimento e a organização dos arquivos do protótipo.

O repositório contém a estrutura inicial do projeto, incluindo documentação, arquivos SQL, código-fonte em Python, imagem da primeira tela, arquivo de dependências e configuração do Git.

Essa etapa é importante para documentar o andamento do projeto, facilitar o acompanhamento das alterações e permitir que os estudantes visualizem a evolução da solução.

### 30/06/2026 - Criação da tela de cadastro de ambientes

Foi criada a primeira funcionalidade prática do protótipo OrganizAI: a tela de cadastro de ambientes.

A tela permite registrar informações como nome do ambiente, tipo, capacidade, presença de computadores, presença de projetor e observações.

Nesta etapa, os dados ainda são armazenados temporariamente dentro da aplicação, utilizando o recurso `session_state` do Streamlit. Também foi utilizado o Pandas para exibir os ambientes cadastrados em formato de tabela.

Essa funcionalidade servirá como base para, posteriormente, integrar o sistema ao banco de dados PostgreSQL.

### 30/06/2026 - Cadastro de reservas e verificação de conflitos

Foi criada a funcionalidade de cadastro de reservas no protótipo OrganizAI.

A nova tela permite selecionar um ambiente previamente cadastrado, informar turma, instrutor, unidade curricular, data, horário de início, horário de término e finalidade da reserva.

Também foi implementada uma regra simples de verificação de conflitos. O sistema identifica quando uma tentativa de reserva utiliza o mesmo ambiente, na mesma data, em horários que se cruzam com uma reserva já existente.

Essa etapa representa um avanço importante no protótipo, pois aproxima o sistema do problema real de gestão de salas e laboratórios.

### 30/06/2026 - Preparação dos scripts SQL

Foram preparados os primeiros scripts SQL do projeto OrganizAI.

O arquivo `01_criar_tabelas.sql` contém a estrutura inicial do banco de dados, com as tabelas de ambientes e reservas.

O arquivo `02_dados_exemplo.sql` contém dados fictícios de ambientes da unidade, permitindo realizar testes sem utilizar informações sensíveis.

Essa etapa aproxima o projeto da unidade curricular de Banco de Dados, pois permite trabalhar conceitos como tabelas, campos, chave primária, chave estrangeira, tipos de dados e relacionamento entre entidades.

### 30/06/2026 - Instalação do PostgreSQL

Foi iniciada a configuração do PostgreSQL no Windows para integrar o projeto OrganizAI à unidade curricular de Banco de Dados.

A escolha do PostgreSQL permite trabalhar conceitos importantes, como criação de banco de dados, tabelas, tipos de dados, chave primária, chave estrangeira e comandos SQL.

Essa etapa será fundamental para substituir o armazenamento temporário do Streamlit por um banco de dados real.

### 30/06/2026 - Teste de conexão entre Python e PostgreSQL

Foi configurada a conexão entre o Python e o banco de dados PostgreSQL do projeto OrganizAI.

Para isso, foi criado o arquivo `src/db.py`, responsável por centralizar a conexão com o banco. Também foi criado o arquivo `.env`, utilizado para armazenar as informações de acesso ao banco de dados sem expor a senha diretamente no código-fonte.

Foi realizado um teste de conexão, confirmando que o Python consegue acessar o banco `organizai_db`.

Essa etapa é importante porque prepara o projeto para substituir o armazenamento temporário do Streamlit por dados reais armazenados no PostgreSQL.