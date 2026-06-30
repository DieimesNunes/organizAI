# Diário de Bordo do Instrutor – Projeto OrganizAI

## 1. Identificação do projeto

**Projeto:** OrganizAI – Solução para Gestão de Salas e Laboratórios no Senac Ivaiporã  
**Instrutor:** Dieimes Nunes de Souza  
**Turma:** Ensino Médio Integrado ao Técnico em Inteligência Artificial  
**Unidades curriculares envolvidas:** Python e Banco de Dados  
**Banco de dados utilizado:** PostgreSQL  
**Ferramentas utilizadas:** VS Code, Python, Streamlit, Pandas, PostgreSQL, pgAdmin e GitHub  
**Data do registro:** 30/06/2026  

---

## 2. Finalidade deste diário

Este diário de bordo tem como finalidade registrar, de forma organizada e transparente, as ações realizadas pelo instrutor no desenvolvimento inicial do projeto **OrganizAI**.

O documento também serve como prestação de contas pedagógica, caso seja necessário apresentar à equipe do Senac o que foi realizado, quais decisões foram tomadas e quais encaminhamentos técnicos e didáticos foram adotados.

Além disso, este registro poderá ser compartilhado com os estudantes para que compreendam o processo de desenvolvimento do projeto, identifiquem as etapas já realizadas e visualizem como um projeto de software é organizado desde sua estrutura inicial até a construção de um protótipo funcional.

---

## 3. Contexto do projeto

O OrganizAI é uma proposta de solução digital voltada para apoiar a gestão de salas de aula e laboratórios do Senac Ivaiporã.

A ideia surgiu a partir de uma necessidade real da unidade: organizar melhor o uso dos espaços educacionais, registrar reservas, consultar horários e reduzir possíveis conflitos de utilização de salas e laboratórios.

O projeto está sendo desenvolvido com alunos do primeiro ano do Ensino Médio Integrado ao Técnico em Inteligência Artificial. Como os estudantes ainda estão em fase inicial de formação em programação, banco de dados e lógica computacional, foi necessária uma intervenção pedagógica do instrutor para estruturar o projeto, reduzir o escopo e transformar a proposta em um protótipo viável.

---

## 4. Decisão pedagógica adotada

Considerando o prazo reduzido e o nível atual de conhecimento técnico da turma, foi definido que o projeto será desenvolvido como um **MVP**.

MVP significa **Produto Mínimo Viável**. Em outras palavras, é uma primeira versão funcional do sistema, com apenas as funcionalidades essenciais para demonstrar a ideia, testar a proposta e apresentar o potencial da solução.

Essa decisão foi tomada para evitar que o projeto ficasse grande demais e não pudesse ser concluído dentro do prazo. O foco passou a ser entregar uma versão simples, funcional e compreensível para os alunos.

As funcionalidades priorizadas foram:

- Cadastro de ambientes;
- Cadastro de reservas;
- Consulta de agenda;
- Verificação de conflitos de horário;
- Sugestão simples de ambiente disponível;
- Relatórios básicos de uso.

Essa escolha mantém o projeto alinhado às unidades curriculares de **Python** e **Banco de Dados**, permitindo que os alunos vivenciem uma situação prática de desenvolvimento de software aplicada a um problema real da unidade.

---

## 5. Tecnologias escolhidas e justificativa

Foram escolhidas tecnologias que permitem construir um protótipo funcional sem exigir uma complexidade muito alta dos alunos neste momento.

### Python

O Python foi escolhido por ser a linguagem trabalhada na unidade curricular e por permitir desenvolver a lógica do sistema de forma mais simples e didática.

No projeto, o Python será utilizado para:

- Organizar a lógica das telas;
- Processar os dados digitados pelo usuário;
- Verificar conflitos de horário;
- Conectar o sistema ao banco de dados;
- Gerar consultas e relatórios simples.

### Streamlit

O Streamlit foi escolhido para criar a interface visual do sistema.

Ele permite construir telas no navegador utilizando apenas código Python, sem exigir que os alunos aprendam, neste momento, HTML, CSS, JavaScript, Flask ou Django.

No projeto, o Streamlit será utilizado para:

- Criar a tela inicial;
- Criar formulários de cadastro;
- Exibir tabelas;
- Mostrar mensagens de sucesso e erro;
- Facilitar a demonstração do protótipo.

### Pandas

O Pandas foi escolhido para organizar e exibir dados em formato de tabela.

No projeto, ele será utilizado para:

- Transformar listas de dados em tabelas;
- Exibir ambientes cadastrados;
- Exibir reservas cadastradas;
- Apoiar a criação de relatórios simples.

### PostgreSQL

O PostgreSQL foi escolhido como banco de dados do projeto.

Ele será utilizado para armazenar os dados de forma permanente, substituindo o armazenamento temporário usado nas primeiras versões do protótipo.

No projeto, o PostgreSQL permitirá trabalhar conceitos de Banco de Dados, como:

- Criação de banco;
- Criação de tabelas;
- Campos e tipos de dados;
- Chave primária;
- Chave estrangeira;
- Relacionamento entre tabelas;
- Inserção e consulta de dados.

### GitHub

O GitHub foi utilizado para registrar o histórico do desenvolvimento do projeto.

Ele permite organizar os arquivos, acompanhar as alterações realizadas e demonstrar a evolução do protótipo ao longo do tempo.

---

## 6. Ações realizadas em 30/06/2026

### 6.1 Organização inicial do projeto

Foi criada a estrutura inicial do projeto no VS Code, com pastas separadas para documentação, imagens, scripts SQL e código-fonte.

A estrutura inicial ficou organizada da seguinte forma:

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
│   └── primeira_tela_organizai.png
│
├── sql/
│   ├── 01_criar_tabelas.sql
│   └── 02_dados_exemplo.sql
│
├── src/
│   ├── ambientes.py
│   ├── db.py
│   ├── reservas.py
│   └── sugestoes.py
│
├── app.py
├── README.md
├── requirements.txt
├── .env.example
└── .gitignore
```

Essa organização foi importante para que o projeto ficasse mais claro, tanto para o instrutor quanto para os alunos. Cada pasta possui uma função específica, facilitando a divisão das tarefas e o entendimento do funcionamento geral do sistema.

---

### 6.2 Instalação e configuração do Python

Foi realizada a instalação do Python no Windows e configurado o ambiente de desenvolvimento para o projeto.

Também foi criado um ambiente virtual chamado `.venv`, utilizado para isolar as bibliotecas instaladas no projeto.

Essa prática é importante porque evita conflitos com outros projetos Python e permite que todas as dependências fiquem organizadas em um único ambiente.

Foram instaladas as bibliotecas iniciais necessárias ao projeto:

- Streamlit;
- Pandas;
- python-dotenv;
- psycopg.

Após a instalação, o Streamlit foi testado no terminal, confirmando que estava funcionando corretamente.

---

### 6.3 Criação da primeira tela do sistema

Foi criada a primeira interface visual do OrganizAI utilizando Streamlit.

A tela inicial apresenta:

- Nome do projeto;
- Descrição da proposta;
- Objetivo do sistema;
- Funcionalidades previstas;
- Mensagem de confirmação de carregamento.

Essa etapa marcou o início prático do desenvolvimento do protótipo, pois permitiu visualizar o projeto funcionando no navegador.

Também foi salvo um print da primeira tela na pasta `imagens`, servindo como evidência do desenvolvimento realizado.

---

### 6.4 Criação do repositório no GitHub

O projeto foi enviado para um repositório no GitHub com o nome **organizAI**.

O repositório foi configurado com:

- Arquivos do projeto;
- Estrutura de pastas;
- README inicial;
- Descrição do projeto;
- Tópicos relacionados às tecnologias utilizadas;
- Histórico de commits.

Essa etapa permite registrar a evolução do projeto e comprovar as alterações realizadas ao longo do desenvolvimento.

Também foi configurado o arquivo `.gitignore`, com o objetivo de impedir o envio de arquivos sensíveis ou desnecessários ao GitHub, como:

- `.env`;
- `.venv/`;
- Arquivos de cache do Python;
- Arquivos temporários de teste.

---

### 6.5 Criação da tela de cadastro de ambientes

Foi criada a primeira funcionalidade prática do protótipo: o cadastro de ambientes.

A tela permite registrar informações como:

- Nome do ambiente;
- Tipo de ambiente;
- Capacidade;
- Presença de computadores;
- Presença de projetor;
- Observações.

Nesta primeira versão, os dados foram armazenados temporariamente dentro da aplicação, utilizando o recurso `session_state` do Streamlit.

Também foi utilizado o Pandas para exibir os ambientes cadastrados em formato de tabela.

Essa funcionalidade serviu como base para demonstrar aos alunos como um formulário pode ser construído em Python e como os dados podem ser organizados em uma estrutura tabular.

---

### 6.6 Criação da tela de cadastro de reservas

Foi criada a funcionalidade de cadastro de reservas.

A tela permite registrar:

- Ambiente reservado;
- Turma;
- Instrutor;
- Unidade curricular;
- Data da reserva;
- Horário de início;
- Horário de término;
- Finalidade da reserva.

Essa funcionalidade aproxima o sistema do problema real da unidade, pois permite simular o uso das salas e laboratórios em determinados horários.

---

### 6.7 Implementação da verificação de conflitos

Foi implementada uma regra simples para verificar conflitos de horário.

O sistema identifica se já existe uma reserva para o mesmo ambiente, na mesma data, em um horário que se cruza com a nova reserva.

Por exemplo: se a Sala 03 já estiver reservada das 07h15 às 12h35, o sistema deve impedir uma nova reserva para a mesma sala e data dentro desse intervalo.

Essa etapa é importante porque representa uma lógica de tomada de decisão dentro do sistema. Ela demonstra aos alunos que um software pode analisar informações e ajudar a evitar erros no processo de organização.

---

### 6.8 Criação da consulta de agenda

Foi criada uma tela de consulta de agenda.

A tela permite visualizar as reservas cadastradas e aplicar filtros por ambiente e data.

Essa funcionalidade ajuda a demonstrar a utilidade prática do sistema, pois permite consultar rapidamente quais espaços estão reservados em determinado dia.

---

### 6.9 Preparação dos scripts SQL

Foram preparados os primeiros scripts SQL do projeto.

O arquivo `01_criar_tabelas.sql` contém a estrutura inicial do banco de dados, incluindo as tabelas:

- `ambientes`;
- `reservas`.

O arquivo `02_dados_exemplo.sql` contém dados fictícios de ambientes, permitindo realizar testes sem utilizar informações sensíveis.

Essa etapa conecta diretamente o projeto à unidade curricular de Banco de Dados, pois permite trabalhar com os alunos os conceitos de:

- Tabelas;
- Campos;
- Tipos de dados;
- Chave primária;
- Chave estrangeira;
- Relacionamento entre entidades;
- Inserção de dados.

---

### 6.10 Instalação e configuração do PostgreSQL

Foi realizada a instalação do PostgreSQL no Windows.

Também foi utilizado o pgAdmin para criar o banco de dados:

```text
organizai_db
```

Em seguida, foram executados os scripts SQL para criar as tabelas e inserir os dados de exemplo.

Essa etapa foi essencial para transformar o projeto em uma aplicação conectada a um banco de dados real.

---

### 6.11 Configuração da conexão entre Python e PostgreSQL

Foi criado o arquivo `src/db.py`, responsável por centralizar a conexão entre o Python e o PostgreSQL.

Também foi criado o arquivo `.env`, utilizado para armazenar as informações de conexão com o banco de dados, como host, porta, nome do banco, usuário e senha.

O arquivo `.env` não deve ser enviado para o GitHub, pois pode conter informações sensíveis.

Para fins de demonstração e documentação, foi mantido o arquivo `.env.example`, que mostra a estrutura esperada das variáveis de ambiente sem expor a senha real.

Foi realizado um teste de conexão com o banco de dados, e o Python conseguiu acessar o PostgreSQL com sucesso.

---

## 7. Aprendizagens trabalhadas com os alunos

O desenvolvimento realizado permite trabalhar com os alunos diversos conceitos importantes das unidades curriculares envolvidas.

### Em Python

- Organização de código;
- Funções;
- Condicionais;
- Listas;
- Dicionários;
- Manipulação de datas e horários;
- Criação de interfaces simples com Streamlit;
- Validação de dados;
- Mensagens de erro e sucesso.

### Em Banco de Dados

- Criação de banco;
- Criação de tabelas;
- Definição de campos;
- Tipos de dados;
- Chave primária;
- Chave estrangeira;
- Inserção de dados;
- Relacionamento entre ambientes e reservas;
- Conexão entre aplicação e banco.

### Em Projeto Integrador

- Levantamento de problema real;
- Definição de escopo;
- Organização de etapas;
- Desenvolvimento de protótipo;
- Registro de evidências;
- Trabalho em equipe;
- Apresentação de solução.

---

## 8. Participação esperada dos estudantes

Mesmo com a intervenção técnica do instrutor, a participação dos estudantes continua sendo fundamental.

Os alunos deverão atuar nas próximas etapas do projeto, principalmente em:

- Compreensão do problema;
- Explicação da proposta;
- Testes do sistema;
- Cadastro de dados fictícios;
- Validação das regras de conflito;
- Produção de prints;
- Registro no diário de bordo da equipe;
- Organização da apresentação;
- Demonstração do protótipo;
- Participação no vídeo final.

O protagonismo dos estudantes será preservado principalmente na explicação do problema, na demonstração do funcionamento do sistema e na reflexão sobre os impactos da solução.

---

## 9. Cuidados adotados

Foram adotados cuidados para evitar exposição de dados sensíveis.

Durante os testes e demonstrações, serão utilizados dados fictícios ou genéricos.

Também foi configurado o `.gitignore` para impedir que arquivos sensíveis sejam enviados ao GitHub, especialmente o arquivo `.env`, que pode conter senha do banco de dados.

O projeto tem caráter educacional e será apresentado como protótipo.

---

## 10. Situação atual do projeto ao final do dia

Ao final das atividades realizadas em 30/06/2026, o projeto encontra-se com os seguintes avanços:

- Estrutura inicial organizada;
- Repositório criado no GitHub;
- README do projeto atualizado;
- Ambiente Python configurado;
- Streamlit instalado e testado;
- Primeira tela do sistema criada;
- Tela de cadastro de ambientes criada;
- Tela de cadastro de reservas criada;
- Consulta de agenda criada;
- Regra de verificação de conflitos implementada;
- Scripts SQL preparados;
- PostgreSQL instalado;
- Banco de dados `organizai_db` criado;
- Tabelas `ambientes` e `reservas` criadas;
- Dados fictícios inseridos;
- Conexão entre Python e PostgreSQL testada com sucesso.

---

## 11. Próximos encaminhamentos

Os próximos passos do projeto serão:

1. Substituir o armazenamento temporário do Streamlit pelo armazenamento definitivo no PostgreSQL;
2. Fazer o cadastro de ambientes gravar diretamente no banco de dados;
3. Fazer a listagem de ambientes buscar os dados do banco;
4. Fazer o cadastro de reservas utilizar os ambientes registrados no PostgreSQL;
5. Implementar a verificação de conflitos utilizando consultas SQL;
6. Criar uma funcionalidade simples de sugestão de ambiente disponível;
7. Criar relatórios básicos de uso;
8. Atualizar a documentação do projeto;
9. Preparar os alunos para explicar cada parte do sistema;
10. Organizar o roteiro do vídeo de apresentação.

---

## 12. Considerações finais

As atividades realizadas neste dia foram fundamentais para recuperar o andamento do projeto e transformar a proposta inicial em um protótipo em desenvolvimento.

A intervenção do instrutor foi necessária para estruturar tecnicamente o projeto, organizar o ambiente de desenvolvimento, definir o escopo mínimo e criar uma base funcional que possa ser compreendida, testada e apresentada pelos alunos.

A partir dessa base, os estudantes poderão participar de forma mais objetiva, realizando testes, explicando as funcionalidades, registrando evidências e colaborando na construção da versão final do protótipo.

O projeto segue alinhado às unidades curriculares de Python e Banco de Dados, além de responder a uma necessidade real da unidade: melhorar a organização de salas e laboratórios do Senac Ivaiporã.
