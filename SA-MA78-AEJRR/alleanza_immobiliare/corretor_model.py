import mysql.connector

from database import conectar

def listar_corretores():
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    SELECT
        id_corretor,
        nome,
        creci,
        telefone,
        email
    FROM Corretor
    """

    cursor.execute(sql)
    dados = cursor.fetchall()

    for corretor in dados:
        print(corretor)

    cursor.close()
    conexao.close()


def cadastrar_corretor(nome, creci, telefone, email):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO Corretor
    (nome, creci, telefone, email)
    VALUES
    (%s, %s, %s, %s)
    """

    valores = (
        nome,
        creci,
        telefone,
        email
    )

    cursor.execute(sql, valores)
    conexao.commit()

    print(f"Corretor {nome} cadastrado com sucesso!")

    cursor.close()
    conexao.close()


def atualizar_corretor(id_corretor, nome, creci, telefone, email):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        sql = """UPDATE Corretor 
                 SET nome=%s, creci=%s, telefone=%s, email=%s 
                 WHERE id_corretor=%s"""
        cursor.execute(sql, (nome, creci, telefone, email, id_corretor))
        conexao.commit()
        print("\n✅ Corretor atualizado com sucesso!")
    except mysql.connector.errors.IntegrityError:
        print("\n❌ Erro: Este CRECI já está cadastrado para outro corretor.")
    finally:
        cursor.close()
        conexao.close() 


def deletar_corretor(id_corretor):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        sql = "DELETE FROM Corretor WHERE id_corretor = %s"
        cursor.execute(sql, (id_corretor,))
        conexao.commit()
        print("\n✅ Corretor deletado com sucesso!")
    except mysql.connector.errors.IntegrityError:
        print("\n❌ Não é possível deletar este corretor porque ele está associado a Visitas, Vendas ou Aluguéis históricos!")
    finally:
        cursor.close()
        conexao.close()