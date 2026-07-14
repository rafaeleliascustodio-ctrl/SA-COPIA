import mysql.connector

from database import conectar

def listar_imoveis():
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    SELECT
        i.id_imovel,
        p.nome AS proprietario,
        t.descricao AS tipo_imovel,
        e.rua,
        e.numero,
        i.valor_sugerido,
        i.status
    FROM Imovel i
    JOIN Proprietario p
        ON i.id_proprietario = p.id_proprietario
    JOIN TipoImovel t
        ON i.id_tipo_imovel = t.id_tipo_imovel
    JOIN Endereco e
        ON i.id_endereco = e.id_endereco
    """

    cursor.execute(sql)
    dados = cursor.fetchall()

    for imovel in dados:
        print(imovel)

    cursor.close()
    conexao.close()


def cadastrar_imovel(id_proprietario,
                      id_tipo_imovel,
                      id_endereco,
                      valor_sugerido,
                      status):

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO Imovel
    (
        id_proprietario,
        id_tipo_imovel,
        id_endereco,
        valor_sugerido,
        status
    )
    VALUES
    (%s,%s,%s,%s,%s)
    """

    valores = (
        id_proprietario,
        id_tipo_imovel,
        id_endereco,
        valor_sugerido,
        status
    )

    cursor.execute(sql, valores)
    conexao.commit()

    print("Imóvel cadastrado com sucesso!")

    cursor.close()
    conexao.close()


def atualizar_imovel(id_imovel, id_proprietario, id_tipo_imovel, id_endereco, valor_sugerido, status):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        sql = """UPDATE Imovel 
                 SET id_proprietario=%s, id_tipo_imovel=%s, id_endereco=%s, valor_sugerido=%s, status=%s 
                 WHERE id_imovel=%s"""
        cursor.execute(sql, (id_proprietario, id_tipo_imovel, id_endereco, valor_sugerido, status, id_imovel))
        conexao.commit()
        print("\n✅ Imóvel atualizado com sucesso!")
    except mysql.connector.errors.IntegrityError:
        print("\n❌ Erro de Integridade: Verifique se o ID do proprietário, tipo do imóvel e endereço existem!")
    finally:
        cursor.close()
        conexao.close()


def deletar_imovel(id_imovel):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        sql = "DELETE FROM Imovel WHERE id_imovel = %s"
        cursor.execute(sql, (id_imovel,))
        conexao.commit()
        print("\n✅ Imóvel deletado com sucesso!")
    except mysql.connector.errors.IntegrityError:
        print("\n❌ Não é possível deletar este imóvel porque ele está associado a Visitas, Anúncios, Documentos, Vendas ou Aluguéis!")
    finally:
        cursor.close()
        conexao.close()