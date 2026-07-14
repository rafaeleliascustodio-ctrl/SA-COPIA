import mysql.connector

from database import conectar

def listar_contratos():

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    SELECT
        id_contrato,
        id_venda,
        id_aluguel,
        data_assinatura,
        clausulas
    FROM Contrato
    """

    cursor.execute(sql)
    dados = cursor.fetchall()

    for contrato in dados:
        print(contrato)

    cursor.close()
    conexao.close()


def cadastrar_contrato(id_venda, id_aluguel, data_assinatura, clausulas):

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO Contrato
    (id_venda,id_aluguel,data_assinatura,clausulas)
    VALUES
    (%s,%s,%s,%s)
    """

    valores = (
        id_venda,
        id_aluguel,
        data_assinatura,
        clausulas
    )

    cursor.execute(sql, valores)
    conexao.commit()

    print("Contrato cadastrado com sucesso!")

    cursor.close()
    conexao.close()


def atualizar_contrato(id_contrato, id_venda, id_aluguel, data_assinatura, clausulas):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        sql = """UPDATE Contrato 
                 SET id_venda=%s, id_aluguel=%s, data_assinatura=%s, clausulas=%s 
                 WHERE id_contrato=%s"""
        cursor.execute(sql, (id_venda, id_aluguel, data_assinatura, clausulas, id_contrato))
        conexao.commit()
        print("\n✅ Contrato atualizado com sucesso!")
    except mysql.connector.errors.IntegrityError:
        print("\n❌ Erro: Verifique se os IDs da venda ou do aluguel associados existem!")
    finally:
        cursor.close()
        conexao.close()


def deletar_contrato(id_contrato):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        sql = "DELETE FROM Contrato WHERE id_contrato = %s"
        cursor.execute(sql, (id_contrato,))
        conexao.commit()
        print("\n✅ Contrato deletado com sucesso!")
    except mysql.connector.errors.IntegrityError:
        print("\n❌ Não é possível deletar este contrato porque constam Pagamentos registrados para ele!")
    finally:
        cursor.close()
        conexao.close()