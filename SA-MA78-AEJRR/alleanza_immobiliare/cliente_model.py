import mysql.connector

from database import conectar

def listar_clientes():
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    SELECT
        id_cliente,
        nome,
        cpf,
        telefone,
        email
    FROM Cliente
    """

    cursor.execute(sql)
    dados = cursor.fetchall()

    for cliente in dados:
        print(cliente)

    cursor.close()
    conexao.close()


def cadastrar_cliente(nome, cpf, telefone, email):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO Cliente
    (nome, cpf, telefone, email)
    VALUES
    (%s, %s, %s, %s)
    """

    valores = (nome, cpf, telefone, email)

    cursor.execute(sql, valores)
    conexao.commit()

    print(f"Cliente {nome} cadastrado com sucesso!")

    cursor.close()
    conexao.close()


def atualizar_cliente(id_cliente, nome, cpf, telefone, email):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        sql = """UPDATE Cliente 
                 SET nome=%s, cpf=%s, telefone=%s, email=%s 
                 WHERE id_cliente=%s"""
        cursor.execute(sql, (nome, cpf, telefone, email, id_cliente))
        conexao.commit()
        print("\n✅ Cliente atualizado com sucesso!")
    except mysql.connector.errors.IntegrityError:
        print("\n❌ Erro: Este CPF já está cadastrado para outro cliente.")
    finally:
        cursor.close()
        conexao.close()


def deletar_cliente(id_cliente):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        sql = "DELETE FROM Cliente WHERE id_cliente = %s"
        cursor.execute(sql, (id_cliente,))
        conexao.commit()
        print("\n✅ Cliente deletado com sucesso!")
    except mysql.connector.errors.IntegrityError:
        print("\n❌ Não é possível deletar este cliente porque ele possui registros de Visitas, Vendas ou Aluguéis vinculados!")
    finally:
        cursor.close()
        conexao.close()