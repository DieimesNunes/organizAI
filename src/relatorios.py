from psycopg.rows import dict_row

from src.db import conectar


def obter_resumo_geral():
    """
    Retorna informações gerais do sistema:
    total de ambientes e total de reservas.
    """

    sql = """
        SELECT
            (SELECT COUNT(*) FROM ambientes) AS total_ambientes,
            (SELECT COUNT(*) FROM reservas) AS total_reservas;
    """

    with conectar() as conexao:
        with conexao.cursor(row_factory=dict_row) as cursor:
            cursor.execute(sql)
            resumo = cursor.fetchone()

    return resumo


def listar_reservas_por_ambiente():
    """
    Retorna a quantidade de reservas por ambiente.
    """

    sql = """
        SELECT
            ambientes.nome AS ambiente,
            COUNT(reservas.id) AS total_reservas
        FROM ambientes
        LEFT JOIN reservas
            ON reservas.ambiente_id = ambientes.id
        GROUP BY ambientes.nome
        ORDER BY total_reservas DESC, ambientes.nome ASC;
    """

    with conectar() as conexao:
        with conexao.cursor(row_factory=dict_row) as cursor:
            cursor.execute(sql)
            dados = cursor.fetchall()

    return dados


def listar_ambientes_por_tipo():
    """
    Retorna a quantidade de ambientes por tipo.
    """

    sql = """
        SELECT
            tipo,
            COUNT(*) AS total
        FROM ambientes
        GROUP BY tipo
        ORDER BY total DESC, tipo ASC;
    """

    with conectar() as conexao:
        with conexao.cursor(row_factory=dict_row) as cursor:
            cursor.execute(sql)
            dados = cursor.fetchall()

    return dados


def listar_reservas_por_data():
    """
    Retorna a quantidade de reservas por data.
    """

    sql = """
        SELECT
            data_reserva,
            COUNT(*) AS total_reservas
        FROM reservas
        GROUP BY data_reserva
        ORDER BY data_reserva ASC;
    """

    with conectar() as conexao:
        with conexao.cursor(row_factory=dict_row) as cursor:
            cursor.execute(sql)
            dados = cursor.fetchall()

    return dados