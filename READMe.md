# OrganizAI

O **OrganizAI** é um protótipo de solução digital para auxiliar a gestão de salas de aula e laboratórios do Senac Ivaiporã.

O projeto está sendo desenvolvido por estudantes do Ensino Médio Integrado ao Técnico em Inteligência Artificial, com orientação do instrutor Dieimes Nunes de Souza, como proposta para o Desafio EPT 2026.

## Objetivo

Desenvolver um sistema simples para cadastrar ambientes, registrar reservas, consultar horários, verificar conflitos e sugerir salas ou laboratórios disponíveis conforme a necessidade da aula.

## Problema identificado

A organização de salas e laboratórios é uma atividade importante para o funcionamento das atividades pedagógicas. Quando não há um controle centralizado, podem ocorrer conflitos de horário, dificuldade de consulta e falta de registro sobre o uso dos espaços.

## Solução proposta

O OrganizAI propõe uma ferramenta simples, acessível e funcional para apoiar o registro e a consulta de informações sobre os ambientes da unidade.

## Tecnologias utilizadas

- Python
- Streamlit
- PostgreSQL
- Pandas
- GitHub

## Funcionalidades previstas

- Cadastro de salas e laboratórios;
- Cadastro de reservas;
- Consulta de agenda;
- Verificação de conflitos de horário;
- Sugestão de ambiente disponível;
- Relatórios simples de uso.

## Estrutura do projeto

```text
organizAI/
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
│   └── sugestoes.py
│
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
