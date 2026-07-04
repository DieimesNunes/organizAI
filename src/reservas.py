from psycopg.rows import dict_row

from src.db import conectar


def cadastrar_reserva(
    ambiente_id,
    turma,
    instrutor,
    unidade_curricular,
    data_reserva,
    hora_inicio,
    hora_fim,
    finalidade
):
    """
    Cadastra uma nova reserva no banco de dados PostgreSQL.
    """

    sql = """
        INSERT INTO reservas
        (
            ambiente_id,
            turma,
            instrutor,
            unidade_curricular,
            data_reserva,
            hora_inicio,
            hora_fim,
            finalidade
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        RETURNING id;
    """

    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                sql,
                (
                    ambiente_id,
                    turma,
                    instrutor,
                    unidade_curricular,
                    data_reserva,
                    hora_inicio,
                    hora_fim,
                    finalidade
                )
            )

            id_criado = cursor.fetchone()[0]

    return id_criado


def existe_conflito_reserva(ambiente_id, data_reserva, hora_inicio, hora_fim):
    """
    Verifica se já existe reserva para o mesmo ambiente,
    na mesma data, com horários que se cruzam.
    """

    sql = """
        SELECT id
        FROM reservas
        WHERE ambiente_id = %s
          AND data_reserva = %s
          AND %s < hora_fim
          AND %s > hora_inicio
        LIMIT 1;
    """

    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                sql,
                (
                    ambiente_id,
                    data_reserva,
                    hora_inicio,
                    hora_fim
                )
            )

            conflito = cursor.fetchone()

    return conflito is not None


def existe_conflito_reserva_edicao(reserva_id, ambiente_id, data_reserva, hora_inicio, hora_fim):
    """
    Verifica conflito ao editar uma reserva.

    A diferença desta função é que ela ignora a própria reserva que está sendo editada.
    """

    sql = """
        SELECT id
        FROM reservas
        WHERE id <> %s
          AND ambiente_id = %s
          AND data_reserva = %s
          AND %s < hora_fim
          AND %s > hora_inicio
        LIMIT 1;
    """

    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                sql,
                (
                    reserva_id,
                    ambiente_id,
                    data_reserva,
                    hora_inicio,
                    hora_fim
                )
            )

            conflito = cursor.fetchone()

    return conflito is not None


def listar_reservas():
    """
    Lista todas as reservas cadastradas, trazendo também o nome do ambiente.
    """

    sql = """
        SELECT
            reservas.id,
            ambientes.nome AS ambiente,
            reservas.turma,
            reservas.instrutor,
            reservas.unidade_curricular,
            reservas.data_reserva,
            reservas.hora_inicio,
            reservas.hora_fim,
            reservas.finalidade
        FROM reservas
        INNER JOIN ambientes
            ON reservas.ambiente_id = ambientes.id
        ORDER BY reservas.data_reserva, reservas.hora_inicio;
    """

    with conectar() as conexao:
        with conexao.cursor(row_factory=dict_row) as cursor:
            cursor.execute(sql)
            reservas = cursor.fetchall()

    return reservas


def obter_reserva_por_id(reserva_id):
    """
    Busca uma reserva específica pelo ID.
    """

    sql = """
        SELECT
            id,
            ambiente_id,
            turma,
            instrutor,
            unidade_curricular,
            data_reserva,
            hora_inicio,
            hora_fim,
            COALESCE(finalidade, '') AS finalidade
        FROM reservas
        WHERE id = %s;
    """

    with conectar() as conexao:
        with conexao.cursor(row_factory=dict_row) as cursor:
            cursor.execute(sql, (reserva_id,))
            reserva = cursor.fetchone()

    return reserva


def atualizar_reserva(
    reserva_id,
    ambiente_id,
    turma,
    instrutor,
    unidade_curricular,
    data_reserva,
    hora_inicio,
    hora_fim,
    finalidade
):
    """
    Atualiza os dados de uma reserva já cadastrada.
    """

    sql = """
        UPDATE reservas
        SET
            ambiente_id = %s,
            turma = %s,
            instrutor = %s,
            unidade_curricular = %s,
            data_reserva = %s,
            hora_inicio = %s,
            hora_fim = %s,
            finalidade = %s
        WHERE id = %s;
    """

    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                sql,
                (
                    ambiente_id,
                    turma,
                    instrutor,
                    unidade_curricular,
                    data_reserva,
                    hora_inicio,
                    hora_fim,
                    finalidade,
                    reserva_id
                )
            )


def excluir_reserva(reserva_id):
    """
    Exclui uma reserva do banco de dados.
    """

    sql = """
        DELETE FROM reservas
        WHERE id = %s;
    """

    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql, (reserva_id,))