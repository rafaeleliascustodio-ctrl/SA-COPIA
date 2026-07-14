import mysql.connector

from database import conectar

def listar_tipos_imovel():
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    SELECT
        id_tipo_imovel,
        descricao
    FROM TipoImovel
    """

    cursor.execute(sql)
    dados = cursor.fetchall()

    for tipo in dados:
        print(tipo)

    cursor.close()
    conexao.close()


def cadastrar_tipo_imovel(descricao):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO TipoImovel
    (descricao)
    VALUES
    (%s)
    """

    cursor.execute(sql, (descricao,))
    conexao.commit()

    print("Tipo de imóvel cadastrado com sucesso!")

    cursor.close()
    conexao.close()


def atualizar_tipo_imovel(id_tipo_imovel, descricao):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        sql = "UPDATE TipoImovel SET descricao=%s WHERE id_tipo_imovel=%s"
        cursor.execute(sql, (descricao, id_tipo_imovel))
        conexao.commit()
        print("\n✅ Tipo de imóvel atualizado com sucesso!")
    except Exception as err:
        print(f"\n❌ Erro ao atualizar tipo de imóvel: {err}")
    finally:
        cursor.close()
        conexao.close()


def deletar_tipo_imovel(id_tipo_imovel):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        sql = "DELETE FROM TipoImovel WHERE id_tipo_imovel = %s"
        cursor.execute(sql, (id_tipo_imovel,))
        conexao.commit()
        print("\n✅ Tipo de imóvel deletado com sucesso!")
    except mysql.connector.errors.IntegrityError:
        print("\n❌ Não é possível deletar este tipo de imóvel porque existem Imóveis cadastrados com esta descrição!")
    finally:
        cursor.close()
        conexao.close()