import streamlit as st
import pandas as pd
from datetime import time

from src.ambientes import cadastrar_ambiente, listar_ambientes
from src.reservas import cadastrar_reserva, existe_conflito_reserva, listar_reservas

st.set_page_config(
    page_title="OrganizAI",
    page_icon="🏫",
    layout="wide"
)


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

    st.success("Sistema OrganizAI carregado com sucesso!")


def pagina_cadastro_ambientes():
    st.title("🏫 Cadastro de Ambientes")
    st.write("Nesta tela será possível cadastrar salas de aula, laboratórios e outros espaços da unidade.")

    st.divider()

    with st.form("form_cadastro_ambiente"):
        nome = st.text_input("Nome do ambiente", placeholder="Exemplo: Sala 03")

        tipo = st.selectbox(
            "Tipo de ambiente",
            [
                "Sala de aula",
                "Laboratório de informática",
                "Laboratório de hardware",
                "Auditório",
                "Outro"
            ]
        )

        capacidade = st.number_input(
            "Capacidade de pessoas",
            min_value=1,
            max_value=100,
            value=20
        )

        possui_computadores = st.checkbox("Possui computadores?")
        possui_projetor = st.checkbox("Possui projetor?")

        observacao = st.text_area(
            "Observação",
            placeholder="Exemplo: ambiente usado para aulas práticas."
        )

        botao_cadastrar = st.form_submit_button("Cadastrar ambiente")

        if botao_cadastrar:
            if nome.strip() == "":
                st.error("Informe o nome do ambiente.")
            else:
                try:
                    id_criado = cadastrar_ambiente(
                        nome=nome,
                        tipo=tipo,
                        capacidade=capacidade,
                        possui_computadores=possui_computadores,
                        possui_projetor=possui_projetor,
                        observacao=observacao
                    )

                    st.success(f"Ambiente '{nome}' cadastrado com sucesso! ID gerado: {id_criado}")

                except Exception as erro:
                    st.error("Erro ao cadastrar ambiente no banco de dados.")
                    st.exception(erro)

    st.divider()

    st.header("Ambientes cadastrados no banco de dados")

    try:
        ambientes = listar_ambientes()

        if len(ambientes) == 0:
            st.info("Nenhum ambiente cadastrado até o momento.")
        else:
            tabela_ambientes = pd.DataFrame(ambientes)

            tabela_ambientes = tabela_ambientes.rename(
                columns={
                    "id": "ID",
                    "nome": "Nome",
                    "tipo": "Tipo",
                    "capacidade": "Capacidade",
                    "possui_computadores": "Possui computadores",
                    "possui_projetor": "Possui projetor",
                    "observacao": "Observação"
                }
            )

            st.dataframe(tabela_ambientes, use_container_width=True, hide_index=True)

            st.write(f"Total de ambientes cadastrados: **{len(ambientes)}**")

    except Exception as erro:
        st.error("Erro ao listar ambientes cadastrados.")
        st.exception(erro)


def pagina_cadastro_reservas():
    st.title("📅 Cadastro de Reservas")
    st.write("Nesta tela será possível registrar o uso de salas e laboratórios.")

    st.divider()

    try:
        ambientes = listar_ambientes()
    except Exception as erro:
        st.error("Erro ao buscar ambientes no banco de dados.")
        st.exception(erro)
        return

    if len(ambientes) == 0:
        st.warning("Antes de cadastrar uma reserva, cadastre pelo menos um ambiente.")
        return

    with st.form("form_cadastro_reserva"):
        ambiente_selecionado = st.selectbox(
            "Ambiente",
            ambientes,
            format_func=lambda ambiente: ambiente["nome"]
        )

        turma = st.text_input("Turma", placeholder="Exemplo: 202600049 - Técnico em IA")
        instrutor = st.text_input("Instrutor", placeholder="Exemplo: Dieimes Nunes")
        unidade_curricular = st.text_input("Unidade curricular", placeholder="Exemplo: Python")
        data_reserva = st.date_input("Data da reserva")
        hora_inicio = st.time_input("Horário de início", value=time(7, 15))
        hora_fim = st.time_input("Horário de término", value=time(12, 35))
        finalidade = st.text_area("Finalidade", placeholder="Exemplo: Aula prática de programação em Python.")

        botao_cadastrar = st.form_submit_button("Cadastrar reserva")

        if botao_cadastrar:
            ambiente_id = ambiente_selecionado["id"]

            if turma.strip() == "":
                st.error("Informe a turma.")
            elif instrutor.strip() == "":
                st.error("Informe o instrutor.")
            elif hora_fim <= hora_inicio:
                st.error("O horário de término deve ser maior que o horário de início.")
            elif existe_conflito_reserva(ambiente_id, data_reserva, hora_inicio, hora_fim):
                st.error("Conflito encontrado! Esse ambiente já possui reserva nessa data e horário.")
            else:
                try:
                    id_criado = cadastrar_reserva(
                        ambiente_id=ambiente_id,
                        turma=turma,
                        instrutor=instrutor,
                        unidade_curricular=unidade_curricular,
                        data_reserva=data_reserva,
                        hora_inicio=hora_inicio,
                        hora_fim=hora_fim,
                        finalidade=finalidade
                    )

                    st.success(f"Reserva cadastrada com sucesso! ID gerado: {id_criado}")

                except Exception as erro:
                    st.error("Erro ao cadastrar reserva no banco de dados.")
                    st.exception(erro)

    st.divider()

    st.header("Reservas cadastradas no banco de dados")

    try:
        reservas = listar_reservas()

        if len(reservas) == 0:
            st.info("Nenhuma reserva cadastrada até o momento.")
        else:
            tabela_reservas = pd.DataFrame(reservas)

            tabela_reservas = tabela_reservas.rename(
                columns={
                    "id": "ID",
                    "ambiente": "Ambiente",
                    "turma": "Turma",
                    "instrutor": "Instrutor",
                    "unidade_curricular": "Unidade Curricular",
                    "data_reserva": "Data",
                    "hora_inicio": "Início",
                    "hora_fim": "Fim",
                    "finalidade": "Finalidade"
                }
            )

            st.dataframe(tabela_reservas, use_container_width=True, hide_index=True)

            st.write(f"Total de reservas cadastradas: **{len(reservas)}**")

    except Exception as erro:
        st.error("Erro ao listar reservas cadastradas.")
        st.exception(erro)


def pagina_consulta_agenda():
    st.title("🔎 Consulta de Agenda")
    st.write("Nesta tela será possível consultar as reservas registradas no sistema.")

    st.divider()

    try:
        reservas = listar_reservas()
    except Exception as erro:
        st.error("Erro ao buscar reservas no banco de dados.")
        st.exception(erro)
        return

    if len(reservas) == 0:
        st.info("Nenhuma reserva cadastrada até o momento.")
        return

    tabela_reservas = pd.DataFrame(reservas)

    ambientes = ["Todos"] + sorted(tabela_reservas["ambiente"].unique().tolist())
    ambiente_filtro = st.selectbox("Filtrar por ambiente", ambientes)

    data_filtro = st.date_input("Filtrar por data")

    tabela_filtrada = tabela_reservas.copy()

    if ambiente_filtro != "Todos":
        tabela_filtrada = tabela_filtrada[tabela_filtrada["ambiente"] == ambiente_filtro]

    tabela_filtrada = tabela_filtrada[tabela_filtrada["data_reserva"] == data_filtro]

    tabela_filtrada = tabela_filtrada.rename(
        columns={
            "id": "ID",
            "ambiente": "Ambiente",
            "turma": "Turma",
            "instrutor": "Instrutor",
            "unidade_curricular": "Unidade Curricular",
            "data_reserva": "Data",
            "hora_inicio": "Início",
            "hora_fim": "Fim",
            "finalidade": "Finalidade"
        }
    )

    st.header("Resultado da consulta")

    if len(tabela_filtrada) == 0:
        st.warning("Nenhuma reserva encontrada para os filtros selecionados.")
    else:
        st.dataframe(tabela_filtrada, use_container_width=True, hide_index=True)


st.sidebar.title("Menu")

pagina = st.sidebar.radio(
    "Escolha uma opção:",
    [
        "Página inicial",
        "Cadastro de ambientes",
        "Cadastro de reservas",
        "Consulta de agenda"
    ]
)

if pagina == "Página inicial":
    pagina_inicial()
elif pagina == "Cadastro de ambientes":
    pagina_cadastro_ambientes()
elif pagina == "Cadastro de reservas":
    pagina_cadastro_reservas()
elif pagina == "Consulta de agenda":
    pagina_consulta_agenda()