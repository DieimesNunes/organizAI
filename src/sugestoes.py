from psycopg.rows import dict_row

from src.db import conectar


def sugerir_ambientes(
    data_reserva,
    hora_inicio,
    hora_fim,
    capacidade_minima,
    precisa_computadores,
    precisa_projetor
):
    """
    Sugere ambientes disponíveis com base na data, horário,
    capacidade mínima e recursos necessários.
    """

    sql = """
        SELECT
            ambientes.id,
            ambientes.nome,
            ambientes.tipo,
            ambientes.capacidade,
            CASE 
                WHEN ambientes.possui_computadores = TRUE THEN 'Sim'
                ELSE 'Não'
            END AS possui_computadores,
            CASE 
                WHEN ambientes.possui_projetor = TRUE THEN 'Sim'
                ELSE 'Não'
            END AS possui_projetor,
            COALESCE(ambientes.observacao, '') AS observacao
        FROM ambientes
        WHERE ambientes.capacidade >= %s
          AND (%s = FALSE OR ambientes.possui_computadores = TRUE)
          AND (%s = FALSE OR ambientes.possui_projetor = TRUE)
          AND NOT EXISTS (
              SELECT 1
              FROM reservas
              WHERE reservas.ambiente_id = ambientes.id
                AND reservas.data_reserva = %s
                AND %s < reservas.hora_fim
                AND %s > reservas.hora_inicio
          )
        ORDER BY ambientes.capacidade ASC, ambientes.nome ASC;
    """

    with conectar() as conexao:
        with conexao.cursor(row_factory=dict_row) as cursor:
            cursor.execute(
                sql,
                (
                    capacidade_minima,
                    precisa_computadores,
                    precisa_projetor,
                    data_reserva,
                    hora_inicio,
                    hora_fim
                )
            )

            ambientes = cursor.fetchall()

    return ambientes