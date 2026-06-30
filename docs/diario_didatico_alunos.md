# Diário Didático dos Alunos – Projeto OrganizAI

## 1. Para que serve este documento?

Este documento foi criado para ajudar os estudantes a entenderem, passo a passo, o desenvolvimento do projeto **OrganizAI**.

A ideia é explicar de forma simples o que está sendo feito, por que cada ferramenta foi escolhida e como o sistema funciona.

Este diário não é apenas um registro técnico. Ele também serve como material de estudo para que os alunos consigam apresentar o projeto com segurança, usando suas próprias palavras.

---

## 2. O que é o OrganizAI?

O **OrganizAI** é um protótipo de sistema criado para ajudar na organização de salas de aula e laboratórios do Senac Ivaiporã.

Ele foi pensado para responder a uma situação real: a necessidade de registrar e consultar o uso dos espaços da unidade.

Com o OrganizAI, é possível:

- Cadastrar salas e laboratórios;
- Registrar reservas;
- Consultar a agenda dos ambientes;
- Verificar se existe conflito de horário;
- Sugerir ambientes disponíveis;
- Visualizar relatórios simples.

---

## 3. Qual problema estamos tentando resolver?

Em uma unidade de ensino, várias turmas e instrutores podem precisar usar salas, laboratórios e auditório.

Quando essas informações não estão bem organizadas, podem acontecer problemas, como:

- Duas turmas tentando usar a mesma sala no mesmo horário;
- Dificuldade para saber quais ambientes estão disponíveis;
- Falta de histórico sobre o uso dos espaços;
- Dificuldade para escolher o ambiente mais adequado para cada aula.

O OrganizAI tenta resolver esse problema criando uma ferramenta simples para registrar e consultar essas informações.

---

## 4. O que é um protótipo?

Um **protótipo** é uma primeira versão de uma ideia.

Ele não precisa ser perfeito nem ter todas as funcionalidades de um sistema profissional. O objetivo do protótipo é mostrar que a solução é possível e demonstrar como ela pode funcionar.

No nosso caso, o OrganizAI é um protótipo porque já possui telas e funções funcionando, mas ainda pode ser melhorado no futuro.

---

## 5. O que é MVP?

MVP significa **Produto Mínimo Viável**.

Isso quer dizer que, em vez de tentar criar um sistema enorme de uma vez, fazemos primeiro uma versão menor, com as funções mais importantes.

No OrganizAI, o MVP tem estas partes principais:

- Cadastro de ambientes;
- Cadastro de reservas;
- Consulta de agenda;
- Verificação de conflitos;
- Sugestão de ambiente disponível;
- Relatórios.

Essa escolha foi importante porque o projeto estava com pouco tempo e a turma ainda está aprendendo programação e banco de dados.

---

## 6. O que é Python no projeto?

**Python** é a linguagem de programação usada no OrganizAI.

Uma linguagem de programação serve para dar instruções ao computador.

No nosso projeto, o Python é usado para:

- Criar a lógica do sistema;
- Organizar as telas;
- Receber os dados digitados;
- Validar informações;
- Verificar conflitos de horário;
- Buscar dados no banco;
- Exibir informações na tela.

Exemplo de ideia em Python:

```python
if hora_fim <= hora_inicio:
    st.error("O horário de término deve ser maior que o horário de início.")
```

Esse trecho significa: se o horário final for menor ou igual ao horário inicial, o sistema mostra uma mensagem de erro.

---

## 7. O que é Streamlit?

**Streamlit** é uma ferramenta que permite criar telas de sistema usando Python.

Normalmente, para criar um sistema web, seria necessário aprender HTML, CSS e JavaScript. Com o Streamlit, conseguimos criar uma interface simples no navegador usando apenas Python.

No OrganizAI, o Streamlit é usado para criar:

- Menu lateral;
- Tela inicial;
- Formulários;
- Botões;
- Tabelas;
- Mensagens de erro;
- Mensagens de sucesso;
- Gráficos simples.

Exemplo:

```python
st.title("OrganizAI")
```

Esse comando cria um título na tela.

Outro exemplo:

```python
st.success("Cadastro realizado com sucesso!")
```

Esse comando mostra uma mensagem de sucesso para o usuário.

---

## 8. O que é Pandas?

**Pandas** é uma biblioteca do Python usada para trabalhar com dados em formato de tabela.

No OrganizAI, o Pandas é usado principalmente para transformar dados em tabelas visuais.

Por exemplo, quando buscamos os ambientes cadastrados no banco, o Pandas ajuda a organizar esses dados para que sejam exibidos na tela.

Exemplo:

```python
tabela_ambientes = pd.DataFrame(ambientes)
```

Esse comando transforma os dados dos ambientes em uma tabela.

---

## 9. O que é PostgreSQL?

**PostgreSQL** é o banco de dados utilizado no OrganizAI.

Um banco de dados serve para armazenar informações de forma organizada e permanente.

Antes de usar o PostgreSQL, os dados ficavam apenas na memória temporária do Streamlit. Isso significava que, ao fechar o sistema, os cadastros poderiam se perder.

Com o PostgreSQL, os dados ficam salvos mesmo depois de fechar e abrir o sistema novamente.

No OrganizAI, o PostgreSQL armazena:

- Ambientes cadastrados;
- Reservas cadastradas;
- Informações usadas nas consultas e relatórios.

---

## 10. O que é uma tabela no banco de dados?

Uma tabela é uma estrutura usada para guardar dados organizados em linhas e colunas.

Pense em uma planilha do Excel.

No OrganizAI, temos principalmente duas tabelas:

```text
ambientes
reservas
```

A tabela `ambientes` guarda informações sobre salas, laboratórios e outros espaços.

A tabela `reservas` guarda informações sobre o uso desses ambientes em determinada data e horário.

---

## 11. O que existe na tabela ambientes?

A tabela `ambientes` guarda dados como:

- ID;
- Nome;
- Tipo;
- Capacidade;
- Se possui computadores;
- Se possui projetor;
- Observação.

Exemplo de ambiente:

```text
Nome: Sala 03
Tipo: Laboratório de informática
Capacidade: 30
Possui computadores: Sim
Possui projetor: Sim
```

---

## 12. O que existe na tabela reservas?

A tabela `reservas` guarda dados como:

- ID;
- Ambiente;
- Turma;
- Instrutor;
- Unidade curricular;
- Data da reserva;
- Horário de início;
- Horário de término;
- Finalidade.

Exemplo de reserva:

```text
Ambiente: Sala 03
Turma: Técnico em IA
Instrutor: Dieimes
Unidade curricular: Python
Data: 30/06/2026
Horário: 07h15 às 12h35
Finalidade: Aula prática de programação
```

---

## 13. O que é chave primária?

A **chave primária** é um identificador único de cada registro na tabela.

No OrganizAI, cada ambiente tem um `id`.

Exemplo:

```text
id = 1 → Sala 03
id = 2 → Sala 05
id = 3 → Auditório
```

Esse `id` ajuda o banco de dados a saber exatamente qual registro está sendo usado.

---

## 14. O que é chave estrangeira?

A **chave estrangeira** é um campo que liga uma tabela a outra.

No OrganizAI, a tabela `reservas` precisa saber qual ambiente foi reservado.

Por isso, ela usa o campo `ambiente_id`.

Exemplo:

```text
Reserva 1 → ambiente_id = 1
```

Isso significa que a reserva está ligada ao ambiente que possui o ID 1.

Se o ID 1 for a Sala 03, então essa reserva pertence à Sala 03.

Essa ligação mostra o relacionamento entre as tabelas `ambientes` e `reservas`.

---

## 15. Como o sistema verifica conflito de horário?

A verificação de conflito é uma das partes mais importantes do OrganizAI.

O sistema precisa impedir que o mesmo ambiente seja reservado duas vezes no mesmo horário.

Exemplo:

```text
Sala 03 já está reservada das 07h15 às 12h35.
```

Se alguém tentar reservar a mesma Sala 03 das 08h00 às 10h00, existe conflito, porque esse horário está dentro do período já reservado.

O sistema verifica:

1. É o mesmo ambiente?
2. É a mesma data?
3. Os horários se cruzam?

Se as três respostas forem sim, o sistema bloqueia a reserva.

A regra usada é:

```text
O novo horário de início é menor que o horário final da reserva existente
E
O novo horário final é maior que o horário inicial da reserva existente
```

Em linguagem mais simples: os horários se encostaram ou se sobrepuseram.

---

## 16. O que é a sugestão de ambiente disponível?

A sugestão de ambiente é uma funcionalidade que ajuda o usuário a escolher uma sala ou laboratório.

O usuário informa:

- Data;
- Horário;
- Capacidade mínima;
- Se precisa de computadores;
- Se precisa de projetor.

Depois disso, o sistema procura no banco quais ambientes atendem aos critérios e não estão reservados naquele horário.

Exemplo:

```text
Preciso de uma sala para 25 pessoas, com computadores e projetor, das 07h15 às 12h35.
```

O sistema consulta os ambientes e mostra apenas os que estão disponíveis.

Essa funcionalidade é importante porque o sistema não apenas guarda informações, mas também ajuda na tomada de decisão.

---

## 17. O que são relatórios?

Relatórios são formas de visualizar os dados do sistema.

No OrganizAI, os relatórios mostram:

- Quantos ambientes existem cadastrados;
- Quantas reservas foram registradas;
- Quantas reservas existem por ambiente;
- Quantos ambientes existem por tipo;
- Quantas reservas existem por data.

Essas informações ajudam a entender melhor o uso dos espaços.

---

## 18. O que é GitHub?

O **GitHub** é uma plataforma usada para guardar e acompanhar projetos de programação.

No OrganizAI, o GitHub é usado para:

- Salvar os arquivos do projeto;
- Registrar o histórico de alterações;
- Mostrar a evolução do sistema;
- Organizar a documentação;
- Facilitar a prestação de contas do desenvolvimento.

Cada vez que uma parte importante do projeto é finalizada, fazemos um **commit**.

---

## 19. O que é commit?

Um **commit** é como uma fotografia de uma etapa do projeto.

Ele registra uma alteração feita no código ou na documentação.

Exemplo de commit:

```text
Adiciona tela de cadastro de ambientes
```

Esse commit mostra que, naquele momento, foi criada a funcionalidade de cadastro de ambientes.

Os commits ajudam a acompanhar a evolução do projeto.

---

## 20. O que já está funcionando no OrganizAI?

Até o momento, o protótipo possui:

- Tela inicial;
- Cadastro de ambientes;
- Cadastro de reservas;
- Consulta de agenda;
- Verificação de conflitos;
- Sugestão de ambiente disponível;
- Relatórios;
- Banco de dados PostgreSQL;
- Projeto no GitHub.

Isso significa que o sistema já pode ser demonstrado como protótipo funcional.

---

## 21. O que os alunos precisam entender para apresentar?

Os alunos não precisam decorar código.

O mais importante é entender a ideia do projeto e conseguir explicar com suas próprias palavras.

Cada aluno deve conseguir responder perguntas como:

- Qual problema o OrganizAI tenta resolver?
- Por que esse problema é importante?
- O que o sistema faz?
- Como o sistema evita conflitos de horário?
- Por que usamos Python?
- Por que usamos PostgreSQL?
- O que é um banco de dados?
- O que são ambientes e reservas?
- Como a sugestão de ambiente funciona?
- Quais melhorias poderiam ser feitas no futuro?

---

## 22. Sugestão de divisão entre os alunos

### Aluno 1 – Abertura e objetivo

Explica o nome do projeto, quem é a equipe e qual é o objetivo geral.

### Aluno 2 – Problema identificado

Explica a dificuldade de organizar salas e laboratórios.

### Aluno 3 – Solução proposta

Explica o que é o OrganizAI e quais funcionalidades ele possui.

### Aluno 4 – Tecnologias utilizadas

Explica Python, Streamlit, PostgreSQL, Pandas e GitHub de forma simples.

### Aluno 5 – Demonstração do sistema

Mostra as telas: cadastro de ambientes, cadastro de reservas, consulta e sugestão.

### Aluno 6 – Impacto, viabilidade e fechamento

Explica por que o projeto é útil, viável e como pode ser melhorado.

---

## 23. Checklist para a apresentação

Antes de gravar o vídeo, verificar:

- A equipe sabe explicar o problema;
- A equipe sabe explicar a solução;
- O sistema abre corretamente;
- Existem ambientes cadastrados;
- Existem reservas cadastradas;
- A verificação de conflito funciona;
- A sugestão de ambiente funciona;
- A tela de relatórios possui dados;
- O vídeo mostra o protótipo funcionando;
- Todos os alunos participam da apresentação.

---

## 24. Frase simples para explicar o projeto

Uma forma simples de explicar o OrganizAI é:

> O OrganizAI é um protótipo de sistema criado para ajudar na organização de salas e laboratórios do Senac Ivaiporã. Ele permite cadastrar ambientes, registrar reservas, evitar conflitos de horário, sugerir espaços disponíveis e gerar relatórios simples, utilizando Python e PostgreSQL.

---

## 25. Conclusão para os alunos

O OrganizAI mostra que a programação pode ser usada para resolver problemas reais.

Mesmo sendo um protótipo, ele já possui funcionalidades importantes e demonstra a integração entre Python e Banco de Dados.

O papel dos alunos agora é entender o funcionamento, testar o sistema, registrar evidências e apresentar a solução com clareza.

Mais importante do que decorar termos técnicos é compreender a lógica do projeto e explicar como ele pode ajudar na organização dos ambientes da unidade.
