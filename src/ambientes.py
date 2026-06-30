import psycopg
from psycopg.rows import dict_row

from src.db import conectar


def cadastrar_ambiente(nome, tipo, capacidade, possui_computadores, possui_projetor, observacao):
    """
    Cadastra um novo ambiente no banco de dados PostgreSQL.
    """

    sql = """
        INSERT INTO ambientes 
        (nome, tipo, capacidade, possui_computadores, possui_projetor, observacao)
        VALUES (%s, %s, %s, %s, %s, %s)
        RETURNING id;
    """

    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                sql,
                (
                    nome,
                    tipo,
                    capacidade,
                    possui_computadores,
                    possui_projetor,
                    observacao
                )
            )

            id_criado = cursor.fetchone()[0]

    return id_criado


def listar_ambientes():
    """
    Lista todos os ambientes cadastrados no banco de dados.
    """

    sql = """
        SELECT 
            id,
            nome,
            tipo,
            capacidade,
            CASE 
                WHEN possui_computadores = TRUE THEN 'Sim'
                ELSE 'Não'
            END AS possui_computadores,
            CASE 
                WHEN possui_projetor = TRUE THEN 'Sim'
                ELSE 'Não'
            END AS possui_projetor,
            COALESCE(observacao, '') AS observacao
        FROM ambientes
        ORDER BY id;
    """

    with conectar() as conexao:
        with conexao.cursor(row_factory=dict_row) as cursor:
            cursor.execute(sql)
            ambientes = cursor.fetchall()

    return ambientes