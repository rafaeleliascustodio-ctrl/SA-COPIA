import mysql.connector

from database import conectar

def listar_vendas():

    conexao=conectar()
    cursor=conexao.cursor()

    sql="""
    SELECT
        v.id_venda,
        c.nome,
        co.nome,
        i.id_imovel,
        v.data_venda,
        v.valor_venda
    FROM Venda v
    JOIN Cliente c ON v.id_cliente=c.id_cliente
    JOIN Corretor co ON v.id_corretor=co.id_corretor
    JOIN Imovel i ON v.id_imovel=i.id_imovel
    """

    cursor.execute(sql)
    dados=cursor.fetchall()

    for venda in dados:
        print(venda)

    cursor.close()
    conexao.close()


def cadastrar_venda(id_cliente,id_corretor,id_imovel,data_venda,valor_venda):

    conexao=conectar()
    cursor=conexao.cursor()

    sql="""
    INSERT INTO Venda
    (id_cliente,id_corretor,id_imovel,data_venda,valor_venda)
    VALUES
    (%s,%s,%s,%s,%s)
    """

    valores=(
        id_cliente,
        id_corretor,
        id_imovel,
        data_venda,
        valor_venda
    )

    cursor.execute(sql,valores)
    conexao.commit()

    print("Venda cadastrada com sucesso!")

    cursor.close()
    conexao.close()


def atualizar_venda(id_venda, id_cliente, id_corretor, id_imovel, data_venda, valor_venda):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        sql = """UPDATE Venda 
                 SET id_cliente=%s, id_corretor=%s, id_imovel=%s, data_venda=%s, valor_venda=%s 
                 WHERE id_venda=%s"""
        cursor.execute(sql, (id_cliente, id_corretor, id_imovel, data_venda, valor_venda, id_venda))
        conexao.commit()
        print("\n✅ Registro de venda atualizado com sucesso!")
    except mysql.connector.errors.IntegrityError:
        print("\n❌ Erro: Verifique se os IDs do cliente, corretor e imóvel informados existem!")
    finally:
        cursor.close()
        conexao.close()

def deletar_venda(id_venda):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        sql = "DELETE FROM Venda WHERE id_venda = %s"
        cursor.execute(sql, (id_venda,))
        conexao.commit()
        print("\n✅ Registro de venda deletado com sucesso!")
    except mysql.connector.errors.IntegrityError:
        print("\n❌ Não é possível deletar esta venda porque existe um Contrato gerado e ativo para ela!")
    finally:
        cursor.close()
        conexao.close()