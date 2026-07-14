import mysql.connector

from database import conectar

def listar_enderecos():
    # abrir conexão
    conexao = conectar()

    # criar cursor
    cursor = conexao.cursor()

    # sql da consulta
    sql = """
    SELECT
        id_endereco,
        rua,
        numero,
        bairro,
        cidade,
        estado,
        cep
    FROM Endereco
    """

    # executa sql
    cursor.execute(sql)

    # recuperar dados
    dados = cursor.fetchall()

    # exibir dados
    for endereco in dados:
        print(endereco)

    # fechar conexão
    cursor.close()
    conexao.close()


def cadastrar_endereco(rua, numero, bairro, cidade, estado, cep):

    # abrir conexão
    conexao = conectar()

    # criar cursor
    cursor = conexao.cursor()

    # sql de inserção
    sql = """
    INSERT INTO Endereco
    (rua, numero, bairro, cidade, estado, cep)
    VALUES
    (%s, %s, %s, %s, %s, %s)
    """

    valores = (
        rua,
        numero,
        bairro,
        cidade,
        estado,
        cep
    )

    # executa sql
    cursor.execute(sql, valores)
    conexao.commit()

    print("Endereço cadastrado com sucesso!")

    # fechar conexão
    cursor.close()
    conexao.close()


def atualizar_endereco(id_endereco, rua, numero, bairro, cidade, estado, cep):
    # Uma validação simples no Python antes de mandar pro banco ajuda muito:
    if len(estado) > 2:
        print("\n❌ Erro: O estado deve conter apenas a sigla de 2 letras (Ex: SP, RJ).")
        return

    try:
        conexao = conectar()
        cursor = conexao.cursor()
        sql = """UPDATE Endereco 
                 SET rua=%s, numero=%s, bairro=%s, cidade=%s, estado=%s, cep=%s 
                 WHERE id_endereco=%s"""
        cursor.execute(sql, (rua, numero, bairro, cidade, estado, cep, id_endereco))
        conexao.commit()
        print("\n✅ Endereço atualizado com sucesso!")
    except mysql.connector.errors.DataError:
        print("\n❌ Erro no banco de dados: Texto longo demais para um dos campos (Verifique o Estado).")
    finally:
        cursor.close()
        conexao.close()


def deletar_endereco(id_endereco):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        sql = "DELETE FROM Endereco WHERE id_endereco = %s"
        cursor.execute(sql, (id_endereco,))
        conexao.commit()
        print("\n✅ Endereço deletado com sucesso!")
    except mysql.connector.errors.IntegrityError:
        print("\n❌ Não é possível deletar este endereço porque ele está vinculado a um Imóvel ativo!")
    finally:
        cursor.close()
        conexao.close()