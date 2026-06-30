import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="OrganizAI",
    page_icon="🏫",
    layout="wide"
)

# Lista temporária de ambientes.
# Depois vamos trocar isso pelo PostgreSQL.
if "ambientes" not in st.session_state:
    st.session_state.ambientes = []


def pagina_inicial():
    st.title("🏫 OrganizAI")
    st.subheader("Solução para Gestão de Salas e Laboratórios no Senac Ivaiporã")

    st.write(
        """
        O OrganizAI é um protótipo desenvolvido por estudantes do Ensino Médio Integrado
        ao Técnico em Inteligência Artificial, com o objetivo de apoiar a organização
        de salas de aula e laboratórios da unidade.
        """
    )

    st.divider()

    st.header("Objetivo do sistema")

    st.write(
        """
        O sistema permitirá cadastrar ambientes, registrar reservas, consultar horários,
        verificar conflitos e sugerir salas disponíveis conforme a necessidade da aula.
        """
    )

    st.header("Funcionalidades previstas")

    st.markdown(
        """
        - Cadastro de salas e laboratórios;
        - Cadastro de reservas;
        - Consulta de agenda;
        - Verificação de conflitos de horário;
        - Sugestão de ambiente disponível;
        - Relatórios simples de uso.
        """
    )

    st.success("Primeira versão do OrganizAI carregada com sucesso!")


def pagina_cadastro_ambientes():
    st.title("🏫 Cadastro de Ambientes")
    st.write("Nesta tela será possível cadastrar salas de aula, laboratórios e outros espaços da unidade.")

    st.divider()

    with st.form("form_cadastro_ambiente"):
        nome = st.text_input("Nome do ambiente", placeholder="Exemplo: Sala 03")
        tipo = st.selectbox(
            "Tipo de ambiente",
            ["Sala de aula", "Laboratório de informática", "Laboratório de hardware", "Auditório", "Outro"]
        )
        capacidade = st.number_input("Capacidade de pessoas", min_value=1, max_value=100, value=20)
        possui_computadores = st.checkbox("Possui computadores?")
        possui_projetor = st.checkbox("Possui projetor?")
        observacao = st.text_area("Observação", placeholder="Exemplo: ambiente usado para aulas práticas.")

        botao_cadastrar = st.form_submit_button("Cadastrar ambiente")

        if botao_cadastrar:
            if nome.strip() == "":
                st.error("Informe o nome do ambiente.")
            else:
                ambiente = {
                    "Nome": nome,
                    "Tipo": tipo,
                    "Capacidade": capacidade,
                    "Possui computadores": "Sim" if possui_computadores else "Não",
                    "Possui projetor": "Sim" if possui_projetor else "Não",
                    "Observação": observacao
                }

                st.session_state.ambientes.append(ambiente)
                st.success(f"Ambiente '{nome}' cadastrado com sucesso!")

    st.divider()

    st.header("Ambientes cadastrados")

    if len(st.session_state.ambientes) == 0:
        st.info("Nenhum ambiente cadastrado até o momento.")
    else:
        tabela_ambientes = pd.DataFrame(st.session_state.ambientes)
        st.dataframe(tabela_ambientes, use_container_width=True)

        st.write(f"Total de ambientes cadastrados: **{len(st.session_state.ambientes)}**")


st.sidebar.title("Menu")
pagina = st.sidebar.radio(
    "Escolha uma opção:",
    ["Página inicial", "Cadastro de ambientes"]
)

if pagina == "Página inicial":
    pagina_inicial()
elif pagina == "Cadastro de ambientes":
    pagina_cadastro_ambientes()