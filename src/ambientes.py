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


def obter_ambiente_por_id(ambiente_id):
    """
    Busca um ambiente específico pelo ID.
    Essa função retorna os valores originais, inclusive booleanos,
    para facilitar a edição no formulário.
    """

    sql = """
        SELECT 
            id,
            nome,
            tipo,
            capacidade,
            possui_computadores,
            possui_projetor,
            COALESCE(observacao, '') AS observacao
        FROM ambientes
        WHERE id = %s;
    """

    with conectar() as conexao:
        with conexao.cursor(row_factory=dict_row) as cursor:
            cursor.execute(sql, (ambiente_id,))
            ambiente = cursor.fetchone()

    return ambiente


def atualizar_ambiente(
    ambiente_id,
    nome,
    tipo,
    capacidade,
    possui_computadores,
    possui_projetor,
    observacao
):
    """
    Atualiza os dados de um ambiente já cadastrado.
    """

    sql = """
        UPDATE ambientes
        SET
            nome = %s,
            tipo = %s,
            capacidade = %s,
            possui_computadores = %s,
            possui_projetor = %s,
            observacao = %s
        WHERE id = %s;
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
                    observacao,
                    ambiente_id
                )
            )


def contar_reservas_por_ambiente(ambiente_id):
    """
    Conta quantas reservas estão vinculadas a um ambiente.
    Essa verificação é importante antes de excluir um ambiente.
    """

    sql = """
        SELECT COUNT(*) AS total
        FROM reservas
        WHERE ambiente_id = %s;
    """

    with conectar() as conexao:
        with conexao.cursor(row_factory=dict_row) as cursor:
            cursor.execute(sql, (ambiente_id,))
            resultado = cursor.fetchone()

    return resultado["total"]


def excluir_ambiente(ambiente_id):
    """
    Exclui um ambiente do banco de dados.

    Observação:
    O ideal é excluir apenas ambientes que não possuem reservas,
    para não quebrar o relacionamento entre as tabelas.
    """

    sql = """
        DELETE FROM ambientes
        WHERE id = %s;
    """

    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql, (ambiente_id,))