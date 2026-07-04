import streamlit as st
import pandas as pd
from datetime import time


from src.ambientes import (
    cadastrar_ambiente,
    listar_ambientes,
    obter_ambiente_por_id,
    atualizar_ambiente,
    contar_reservas_por_ambiente,
    excluir_ambiente
)
from src.reservas import (
    cadastrar_reserva,
    existe_conflito_reserva,
    existe_conflito_reserva_edicao,
    listar_reservas,
    obter_reserva_por_id,
    atualizar_reserva,
    excluir_reserva
)
from src.sugestoes import sugerir_ambientes
from src.relatorios import (
    obter_resumo_geral,
    listar_reservas_por_ambiente,
    listar_ambientes_por_tipo,
    listar_reservas_por_data
)

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

def pagina_sugestao_ambiente():
    st.title("🤖 Sugestão de Ambiente Disponível")
    st.write(
        """
        Nesta tela, o sistema sugere salas ou laboratórios disponíveis
        com base na data, horário, capacidade e recursos necessários.
        """
    )

    st.divider()

    with st.form("form_sugestao_ambiente"):
        data_reserva = st.date_input("Data desejada")
        hora_inicio = st.time_input("Horário de início", value=time(7, 15))
        hora_fim = st.time_input("Horário de término", value=time(12, 35))

        capacidade_minima = st.number_input(
            "Capacidade mínima necessária",
            min_value=1,
            max_value=100,
            value=20
        )

        precisa_computadores = st.checkbox("Precisa de computadores?")
        precisa_projetor = st.checkbox("Precisa de projetor?")

        botao_sugerir = st.form_submit_button("Buscar ambientes disponíveis")

        if botao_sugerir:
            if hora_fim <= hora_inicio:
                st.error("O horário de término deve ser maior que o horário de início.")
            else:
                try:
                    ambientes = sugerir_ambientes(
                        data_reserva=data_reserva,
                        hora_inicio=hora_inicio,
                        hora_fim=hora_fim,
                        capacidade_minima=capacidade_minima,
                        precisa_computadores=precisa_computadores,
                        precisa_projetor=precisa_projetor
                    )

                    st.divider()
                    st.header("Ambientes sugeridos")

                    if len(ambientes) == 0:
                        st.warning("Nenhum ambiente disponível foi encontrado para os critérios informados.")
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

                        st.success(f"Foram encontrados {len(ambientes)} ambiente(s) disponível(is).")
                        st.dataframe(tabela_ambientes, use_container_width=True, hide_index=True)

                except Exception as erro:
                    st.error("Erro ao buscar sugestões de ambientes.")
                    st.exception(erro)
def pagina_relatorios():
    st.title("📊 Relatórios do OrganizAI")
    st.write(
        """
        Nesta tela são apresentados relatórios simples sobre os ambientes
        e reservas cadastrados no sistema.
        """
    )

    st.divider()

    try:
        resumo = obter_resumo_geral()

        coluna1, coluna2 = st.columns(2)

        with coluna1:
            st.metric("Total de ambientes", resumo["total_ambientes"])

        with coluna2:
            st.metric("Total de reservas", resumo["total_reservas"])

    except Exception as erro:
        st.error("Erro ao carregar resumo geral.")
        st.exception(erro)
        return

    st.divider()

    st.header("Reservas por ambiente")

    try:
        dados_ambiente = listar_reservas_por_ambiente()

        if len(dados_ambiente) == 0:
            st.info("Nenhum dado encontrado.")
        else:
            tabela_ambiente = pd.DataFrame(dados_ambiente)
            tabela_ambiente = tabela_ambiente.rename(
                columns={
                    "ambiente": "Ambiente",
                    "total_reservas": "Total de Reservas"
                }
            )

            st.dataframe(tabela_ambiente, use_container_width=True, hide_index=True)

            grafico_ambiente = tabela_ambiente.set_index("Ambiente")
            st.bar_chart(grafico_ambiente)

    except Exception as erro:
        st.error("Erro ao carregar reservas por ambiente.")
        st.exception(erro)

    st.divider()

    st.header("Ambientes por tipo")

    try:
        dados_tipo = listar_ambientes_por_tipo()

        if len(dados_tipo) == 0:
            st.info("Nenhum dado encontrado.")
        else:
            tabela_tipo = pd.DataFrame(dados_tipo)
            tabela_tipo = tabela_tipo.rename(
                columns={
                    "tipo": "Tipo",
                    "total": "Total"
                }
            )

            st.dataframe(tabela_tipo, use_container_width=True, hide_index=True)

            grafico_tipo = tabela_tipo.set_index("Tipo")
            st.bar_chart(grafico_tipo)

    except Exception as erro:
        st.error("Erro ao carregar ambientes por tipo.")
        st.exception(erro)

    st.divider()

    st.header("Reservas por data")

    try:
        dados_data = listar_reservas_por_data()

        if len(dados_data) == 0:
            st.info("Nenhuma reserva cadastrada por data.")
        else:
            tabela_data = pd.DataFrame(dados_data)
            tabela_data = tabela_data.rename(
                columns={
                    "data_reserva": "Data",
                    "total_reservas": "Total de Reservas"
                }
            )

            st.dataframe(tabela_data, use_container_width=True, hide_index=True)

            grafico_data = tabela_data.set_index("Data")
            st.bar_chart(grafico_data)

    except Exception as erro:
        st.error("Erro ao carregar reservas por data.")
        st.exception(erro)
def pagina_gerenciar_ambientes():
    st.title("🛠️ Gerenciar Ambientes")
    st.write("Nesta tela é possível editar ou excluir ambientes cadastrados.")

    st.divider()

    try:
        ambientes = listar_ambientes()
    except Exception as erro:
        st.error("Erro ao buscar ambientes no banco de dados.")
        st.exception(erro)
        return

    if len(ambientes) == 0:
        st.info("Nenhum ambiente cadastrado até o momento.")
        return

    aba_editar, aba_excluir = st.tabs(["Editar ambiente", "Excluir ambiente"])

    with aba_editar:
        st.subheader("Editar ambiente")

        ambiente_selecionado = st.selectbox(
            "Selecione o ambiente que deseja editar",
            ambientes,
            format_func=lambda ambiente: f'{ambiente["id"]} - {ambiente["nome"]}',
            key="select_editar_ambiente"
        )

        ambiente_completo = obter_ambiente_por_id(ambiente_selecionado["id"])

        tipos = [
            "Sala de aula",
            "Laboratório de informática",
            "Laboratório de hardware",
            "Auditório",
            "Outro"
        ]

        indice_tipo = tipos.index(ambiente_completo["tipo"]) if ambiente_completo["tipo"] in tipos else 0

        with st.form("form_editar_ambiente"):
            nome = st.text_input("Nome do ambiente", value=ambiente_completo["nome"])

            tipo = st.selectbox(
                "Tipo de ambiente",
                tipos,
                index=indice_tipo
            )

            capacidade = st.number_input(
                "Capacidade de pessoas",
                min_value=1,
                max_value=100,
                value=ambiente_completo["capacidade"]
            )

            possui_computadores = st.checkbox(
                "Possui computadores?",
                value=ambiente_completo["possui_computadores"]
            )

            possui_projetor = st.checkbox(
                "Possui projetor?",
                value=ambiente_completo["possui_projetor"]
            )

            observacao = st.text_area(
                "Observação",
                value=ambiente_completo["observacao"]
            )

            botao_salvar = st.form_submit_button("Salvar alterações")

            if botao_salvar:
                if nome.strip() == "":
                    st.error("Informe o nome do ambiente.")
                else:
                    try:
                        atualizar_ambiente(
                            ambiente_id=ambiente_completo["id"],
                            nome=nome,
                            tipo=tipo,
                            capacidade=capacidade,
                            possui_computadores=possui_computadores,
                            possui_projetor=possui_projetor,
                            observacao=observacao
                        )

                        st.success("Ambiente atualizado com sucesso!")
                        st.rerun()

                    except Exception as erro:
                        st.error("Erro ao atualizar ambiente.")
                        st.exception(erro)

    with aba_excluir:
        st.subheader("Excluir ambiente")
        st.warning(
            """
            Atenção: um ambiente só deve ser excluído se não possuir reservas cadastradas.
            Isso evita problemas no relacionamento entre as tabelas do banco de dados.
            """
        )

        ambiente_excluir = st.selectbox(
            "Selecione o ambiente que deseja excluir",
            ambientes,
            format_func=lambda ambiente: f'{ambiente["id"]} - {ambiente["nome"]}',
            key="select_excluir_ambiente"
        )

        total_reservas = contar_reservas_por_ambiente(ambiente_excluir["id"])

        st.write(f"Reservas vinculadas a este ambiente: **{total_reservas}**")

        confirmar = st.checkbox(
            "Confirmo que desejo excluir este ambiente.",
            key="confirmar_excluir_ambiente"
        )

        if st.button("Excluir ambiente"):
            if not confirmar:
                st.error("Marque a confirmação antes de excluir.")
            elif total_reservas > 0:
                st.error(
                    "Este ambiente possui reservas vinculadas e não pode ser excluído. "
                    "Exclua as reservas primeiro ou mantenha o ambiente cadastrado."
                )
            else:
                try:
                    excluir_ambiente(ambiente_excluir["id"])
                    st.success("Ambiente excluído com sucesso!")
                    st.rerun()

                except Exception as erro:
                    st.error("Erro ao excluir ambiente.")
                    st.exception(erro)
def pagina_gerenciar_reservas():
    st.title("🛠️ Gerenciar Reservas")
    st.write("Nesta tela é possível editar ou excluir reservas cadastradas.")

    st.divider()

    try:
        reservas = listar_reservas()
        ambientes = listar_ambientes()
    except Exception as erro:
        st.error("Erro ao buscar dados no banco de dados.")
        st.exception(erro)
        return

    if len(reservas) == 0:
        st.info("Nenhuma reserva cadastrada até o momento.")
        return

    if len(ambientes) == 0:
        st.warning("Não existem ambientes cadastrados.")
        return

    aba_editar, aba_excluir = st.tabs(["Editar reserva", "Excluir reserva"])

    with aba_editar:
        st.subheader("Editar reserva")

        reserva_selecionada = st.selectbox(
            "Selecione a reserva que deseja editar",
            reservas,
            format_func=lambda reserva: (
                f'{reserva["id"]} - {reserva["ambiente"]} - '
                f'{reserva["data_reserva"]} - {reserva["hora_inicio"]} às {reserva["hora_fim"]}'
            ),
            key="select_editar_reserva"
        )

        reserva_completa = obter_reserva_por_id(reserva_selecionada["id"])

        ids_ambientes = [ambiente["id"] for ambiente in ambientes]
        indice_ambiente = ids_ambientes.index(reserva_completa["ambiente_id"])

        with st.form("form_editar_reserva"):
            ambiente = st.selectbox(
                "Ambiente",
                ambientes,
                index=indice_ambiente,
                format_func=lambda ambiente: ambiente["nome"]
            )

            turma = st.text_input("Turma", value=reserva_completa["turma"])
            instrutor = st.text_input("Instrutor", value=reserva_completa["instrutor"])

            unidade_curricular = st.text_input(
                "Unidade curricular",
                value=reserva_completa["unidade_curricular"] or ""
            )

            data_reserva = st.date_input(
                "Data da reserva",
                value=reserva_completa["data_reserva"]
            )

            hora_inicio = st.time_input(
                "Horário de início",
                value=reserva_completa["hora_inicio"]
            )

            hora_fim = st.time_input(
                "Horário de término",
                value=reserva_completa["hora_fim"]
            )

            finalidade = st.text_area(
                "Finalidade",
                value=reserva_completa["finalidade"]
            )

            botao_salvar = st.form_submit_button("Salvar alterações")

            if botao_salvar:
                if turma.strip() == "":
                    st.error("Informe a turma.")
                elif instrutor.strip() == "":
                    st.error("Informe o instrutor.")
                elif hora_fim <= hora_inicio:
                    st.error("O horário de término deve ser maior que o horário de início.")
                elif existe_conflito_reserva_edicao(
                    reserva_id=reserva_completa["id"],
                    ambiente_id=ambiente["id"],
                    data_reserva=data_reserva,
                    hora_inicio=hora_inicio,
                    hora_fim=hora_fim
                ):
                    st.error("Conflito encontrado! Já existe outra reserva para esse ambiente nesse horário.")
                else:
                    try:
                        atualizar_reserva(
                            reserva_id=reserva_completa["id"],
                            ambiente_id=ambiente["id"],
                            turma=turma,
                            instrutor=instrutor,
                            unidade_curricular=unidade_curricular,
                            data_reserva=data_reserva,
                            hora_inicio=hora_inicio,
                            hora_fim=hora_fim,
                            finalidade=finalidade
                        )

                        st.success("Reserva atualizada com sucesso!")
                        st.rerun()

                    except Exception as erro:
                        st.error("Erro ao atualizar reserva.")
                        st.exception(erro)

    with aba_excluir:
        st.subheader("Excluir reserva")
        st.warning("A exclusão de uma reserva remove o registro do banco de dados.")

        reserva_excluir = st.selectbox(
            "Selecione a reserva que deseja excluir",
            reservas,
            format_func=lambda reserva: (
                f'{reserva["id"]} - {reserva["ambiente"]} - '
                f'{reserva["data_reserva"]} - {reserva["hora_inicio"]} às {reserva["hora_fim"]}'
            ),
            key="select_excluir_reserva"
        )

        confirmar = st.checkbox(
            "Confirmo que desejo excluir esta reserva.",
            key="confirmar_excluir_reserva"
        )

        if st.button("Excluir reserva"):
            if not confirmar:
                st.error("Marque a confirmação antes de excluir.")
            else:
                try:
                    excluir_reserva(reserva_excluir["id"])
                    st.success("Reserva excluída com sucesso!")
                    st.rerun()

                except Exception as erro:
                    st.error("Erro ao excluir reserva.")
                    st.exception(erro)

st.sidebar.title("Menu")

pagina = st.sidebar.radio(
    "Escolha uma opção:",
    [
        "Página inicial",
        "Cadastro de ambientes",
        "Gerenciar ambientes",
        "Cadastro de reservas",
        "Gerenciar reservas",
        "Consulta de agenda",
        "Sugestão de ambiente",
        "Relatórios"
    ]
)

if pagina == "Página inicial":
    pagina_inicial()
elif pagina == "Cadastro de ambientes":
    pagina_cadastro_ambientes()
elif pagina == "Gerenciar ambientes":
    pagina_gerenciar_ambientes()
elif pagina == "Cadastro de reservas":
    pagina_cadastro_reservas()
elif pagina == "Gerenciar reservas":
    pagina_gerenciar_reservas()
elif pagina == "Consulta de agenda":
    pagina_consulta_agenda()
elif pagina == "Sugestão de ambiente":
    pagina_sugestao_ambiente()
elif pagina == "Relatórios":
    pagina_relatorios()