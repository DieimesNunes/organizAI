import streamlit as st

st.set_page_config(
    page_title="OrganizAI",
    page_icon="🏫",
    layout="wide"
)

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