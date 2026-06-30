# Roteiro do Vídeo - Projeto OrganizAI

## Informações gerais

**Nome da equipe:** OrganizAI  
**Projeto:** OrganizAI - Solução para Gestão de Salas e Laboratórios no Senac Ivaiporã  
**Curso:** Ensino Médio Integrado ao Técnico em Inteligência Artificial  
**Unidade:** Senac Ivaiporã  
**Instrutor orientador:** Dieimes Nunes de Souza  

## Integrantes

- Brayner Lohan de Jesus Dias dos Santos
- Christopher Barbosa Silveira
- Gabriel Rodrigues Lima Ronque
- Kauan Henrique Jesus de Oliveira
- Pablo Henrique de Rezende Salustiano
- Tainara Botelho Pereira

---

## Tempo total estimado

Entre 7 e 9 minutos.

---

## 1. Abertura e identificação da equipe
**Tempo estimado:** 40 segundos  
**Responsável sugerido:** Aluno 1

Olá, somos a equipe OrganizAI, formada por estudantes do Ensino Médio Integrado ao Técnico em Inteligência Artificial do Senac Ivaiporã.

Nosso projeto se chama **OrganizAI: Solução para Gestão de Salas e Laboratórios no Senac Ivaiporã**.

O projeto foi desenvolvido com orientação do instrutor Dieimes Nunes de Souza e envolve principalmente as unidades curriculares de Python e Banco de Dados.

---

## 2. Problema identificado
**Tempo estimado:** 1 minuto  
**Responsável sugerido:** Aluno 2

O problema que identificamos está relacionado à organização do uso de salas de aula, laboratórios e outros ambientes da unidade.

Em uma instituição de ensino, diferentes turmas, instrutores e atividades precisam utilizar os espaços em horários variados. Quando essas informações não estão organizadas em um sistema, podem ocorrer dificuldades de consulta, conflitos de horário e falta de registro sobre o uso dos ambientes.

A partir dessa necessidade, pensamos em uma solução simples, digital e funcional para apoiar a gestão desses espaços.

---

## 3. Ideia e solução proposta
**Tempo estimado:** 1 minuto  
**Responsável sugerido:** Aluno 3

A solução proposta é o OrganizAI, um protótipo de sistema para cadastrar ambientes, registrar reservas, consultar agendas, verificar conflitos de horário, sugerir espaços disponíveis e gerar relatórios simples.

A proposta não é substituir todos os processos administrativos da unidade, mas criar uma ferramenta de apoio, capaz de organizar melhor as informações e facilitar a tomada de decisão.

O sistema foi desenvolvido como um protótipo educacional, utilizando tecnologias estudadas no curso.

---

## 4. Tecnologias utilizadas
**Tempo estimado:** 1 minuto  
**Responsável sugerido:** Aluno 4

Para desenvolver o projeto, utilizamos algumas tecnologias.

O **Python** foi usado para construir a lógica do sistema.

O **Streamlit** foi utilizado para criar a interface visual, permitindo que o sistema funcione no navegador.

O **PostgreSQL** foi usado como banco de dados, armazenando os ambientes e reservas cadastrados.

Também usamos o **Pandas** para organizar dados em tabelas e apoiar a criação de relatórios.

Além disso, utilizamos o **GitHub** para registrar o histórico do desenvolvimento e organizar os arquivos do projeto.

---

## 5. Demonstração do protótipo
**Tempo estimado:** 2 a 3 minutos  
**Responsável sugerido:** Aluno 5

Agora vamos demonstrar o funcionamento do protótipo.

### Tela inicial

Na tela inicial, o sistema apresenta o nome do projeto, o objetivo e as principais funcionalidades previstas.

### Cadastro de ambientes

Na tela de cadastro de ambientes, é possível registrar salas, laboratórios e outros espaços da unidade.

O cadastro inclui informações como nome do ambiente, tipo, capacidade, se possui computadores, se possui projetor e observações.

Esses dados são gravados no banco de dados PostgreSQL.

### Cadastro de reservas

Na tela de cadastro de reservas, é possível escolher um ambiente, informar turma, instrutor, unidade curricular, data, horário de início, horário de término e finalidade da reserva.

O sistema verifica se já existe uma reserva para o mesmo ambiente, na mesma data e em horário conflitante.

Quando existe conflito, o sistema exibe uma mensagem de erro e impede o cadastro.

### Consulta de agenda

Na consulta de agenda, é possível visualizar as reservas já cadastradas, filtrando por ambiente e data.

### Sugestão de ambiente

Na tela de sugestão de ambiente, o usuário informa data, horário, capacidade mínima e recursos necessários.

O sistema consulta o banco de dados e apresenta os ambientes disponíveis que atendem aos critérios informados.

### Relatórios

Na tela de relatórios, o sistema apresenta informações como total de ambientes, total de reservas, reservas por ambiente, ambientes por tipo e reservas por data.

---

## 6. Metodologia de desenvolvimento
**Tempo estimado:** 1 minuto  
**Responsável sugerido:** Aluno 6

O projeto foi desenvolvido em etapas.

Primeiro, identificamos o problema e definimos o objetivo da solução.

Depois, organizamos o escopo do protótipo, priorizando as funcionalidades mais importantes.

Em seguida, foi criada a estrutura do projeto no VS Code e no GitHub.

Depois foram desenvolvidas as telas em Python com Streamlit.

Também foi criado o banco de dados PostgreSQL, com tabelas para ambientes e reservas.

Por fim, o sistema foi integrado ao banco de dados, permitindo que os cadastros fiquem salvos de forma permanente.

---

## 7. Resultados esperados e impactos
**Tempo estimado:** 1 minuto  
**Responsável sugerido:** Aluno 1 ou 2

O principal resultado esperado é demonstrar que uma solução simples pode ajudar na organização de salas e laboratórios.

O OrganizAI pode contribuir para evitar conflitos de horário, facilitar consultas, registrar o uso dos espaços e apoiar decisões sobre qual ambiente utilizar.

Além disso, o projeto tem impacto pedagógico, pois permitiu aplicar conhecimentos de Python e Banco de Dados em uma situação real da unidade.

---

## 8. Viabilidade técnica e econômica
**Tempo estimado:** 50 segundos  
**Responsável sugerido:** Aluno 3 ou 4

O projeto é tecnicamente viável porque utiliza ferramentas acessíveis e adequadas ao contexto educacional.

Python, Streamlit, PostgreSQL e GitHub podem ser utilizados sem custo de licença para o desenvolvimento do protótipo.

Como a solução foi pensada de forma simples, ela pode ser testada e melhorada aos poucos, conforme novas necessidades forem identificadas.

---

## 9. Considerações finais
**Tempo estimado:** 40 segundos  
**Responsável sugerido:** Aluno 5 ou 6

O OrganizAI mostra como conhecimentos técnicos podem ser usados para resolver problemas reais do ambiente escolar.

Mesmo sendo um protótipo, o sistema já permite cadastrar ambientes, registrar reservas, consultar agenda, verificar conflitos, sugerir salas disponíveis e visualizar relatórios.

Com isso, o projeto integra teoria e prática, envolvendo as unidades curriculares de Python e Banco de Dados em uma proposta aplicada ao cotidiano do Senac Ivaiporã.

Obrigado.