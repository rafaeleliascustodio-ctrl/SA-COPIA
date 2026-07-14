import mysql.connector

from database import conectar

def listar_pagamentos():

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    SELECT
        p.id_pagamento,
        p.id_contrato,
        p.valor_pago,
        p.data_pagamento,
        p.forma_pagamento
    FROM Pagamento p
    """

    cursor.execute(sql)

    dados = cursor.fetchall()

    for pagamento in dados:
        print(pagamento)

    cursor.close()
    conexao.close()


def cadastrar_pagamento(id_contrato,valor_pago,data_pagamento,forma_pagamento):

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO Pagamento
    (id_contrato,valor_pago,data_pagamento,forma_pagamento)
    VALUES
    (%s,%s,%s,%s)
    """

    valores = (
        id_contrato,
        valor_pago,
        data_pagamento,
        forma_pagamento
    )

    cursor.execute(sql,valores)
    conexao.commit()

    print("Pagamento cadastrado!")

    cursor.close()
    conexao.close()


def atualizar_pagamento(id_pagamento, id_contrato, valor_pago, data_pagamento, forma_pagamento):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        sql = """UPDATE Pagamento 
                 SET id_contrato=%s, valor_pago=%s, data_pagamento=%s, forma_pagamento=%s 
                 WHERE id_pagamento=%s"""
        cursor.execute(sql, (id_contrato, valor_pago, data_pagamento, forma_pagamento, id_pagamento))
        conexao.commit()
        print("\n✅ Pagamento atualizado com sucesso!")
    except mysql.connector.errors.IntegrityError:
        print("\n❌ Erro: O ID de contrato especificado não existe!")
    finally:
        cursor.close()
        conexao.close()


def deletar_pagamento(id_pagamento):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        sql = "DELETE FROM Pagamento WHERE id_pagamento = %s"
        cursor.execute(sql, (id_pagamento,))
        conexao.commit()
        print("\n✅ Registro de pagamento deletado com sucesso!")
    except mysql.connector.errors.IntegrityError:
        print("\n❌ Erro ao deletar pagamento devido a uma restrição de integridade.")
    finally:
        cursor.close()
        conexao.close()