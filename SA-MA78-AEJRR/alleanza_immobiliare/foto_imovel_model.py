import mysql.connector

from database import conectar

def listar_fotos():

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    SELECT
        id_foto,
        id_anuncio,
        url_foto,
        principal
    FROM FotoImovel
    """

    cursor.execute(sql)

    dados = cursor.fetchall()

    for foto in dados:
        print(foto)

    cursor.close()
    conexao.close()


def cadastrar_foto(id_anuncio,url_foto,principal):

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO FotoImovel
    (id_anuncio,url_foto,principal)
    VALUES
    (%s,%s,%s)
    """

    cursor.execute(sql,(id_anuncio,url_foto,principal))
    conexao.commit()

    print("Foto cadastrada!")

    cursor.close()
    conexao.close()


def atualizar_foto(id_foto, id_anuncio, url_foto, principal):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        sql = """UPDATE FotoImovel 
                 SET id_anuncio=%s, url_foto=%s, principal=%s 
                 WHERE id_foto=%s"""
        cursor.execute(sql, (id_anuncio, url_foto, principal, id_foto))
        conexao.commit()
        print("\n✅ Dados da foto atualizados com sucesso!")
    except mysql.connector.errors.IntegrityError:
        print("\n❌ Erro: O ID de anúncio especificado não existe!")
    finally:
        cursor.close()
        conexao.close()

def deletar_foto(id_foto):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        sql = "DELETE FROM FotoImovel WHERE id_foto = %s"
        cursor.execute(sql, (id_foto,))
        conexao.commit()
        print("\n✅ Foto deletada com sucesso!")
    except mysql.connector.errors.IntegrityError:
        print("\n❌ Erro ao deletar foto devido a uma restrição de integridade.")
    finally:
        cursor.close()
        conexao.close()