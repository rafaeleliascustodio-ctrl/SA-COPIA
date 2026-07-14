"""
Alleanza Immobiliare - Menu principal (ponto de entrada)

Este arquivo foi reorganizado para eliminar duplicação: cada entidade descreve
seus campos uma única vez em ENTIDADES, e um único submenu genérico (`submenu`)
cuida de Listar/Cadastrar/Atualizar/Deletar para todas elas. O comportamento
para o usuário final (textos, ordem das perguntas, opções de cada menu) foi
mantido igual ao original, exceto pelas correções de bugs descritas no
CHANGELOG do projeto (campos que main.py pedia na ordem errada ou incompleta
para Contrato, Imóvel Documento, Anúncio e Foto Imóvel).
"""

from endereco_model import listar_enderecos, cadastrar_endereco, atualizar_endereco, deletar_endereco
from proprietario_model import listar_proprietarios, cadastrar_proprietario, atualizar_proprietario, deletar_proprietario
from cliente_model import listar_clientes, cadastrar_cliente, atualizar_cliente, deletar_cliente
from corretor_model import listar_corretores, cadastrar_corretor, atualizar_corretor, deletar_corretor
from tipo_imovel_model import listar_tipos_imovel, cadastrar_tipo_imovel, atualizar_tipo_imovel, deletar_tipo_imovel
from documento_model import listar_documentos, cadastrar_documento, atualizar_documento, deletar_documento
from imovel_model import listar_imoveis, cadastrar_imovel, atualizar_imovel, deletar_imovel
from visita_model import listar_visitas, cadastrar_visita, atualizar_visita, deletar_visita
from venda_model import listar_vendas, cadastrar_venda, atualizar_venda, deletar_venda
from aluguel_model import listar_alugueis, cadastrar_aluguel, atualizar_aluguel, deletar_aluguel
from contrato_model import listar_contratos, cadastrar_contrato, atualizar_contrato, deletar_contrato
from pagamento_model import listar_pagamentos, cadastrar_pagamento, atualizar_pagamento, deletar_pagamento
from imovel_documento_model import listar_imovel_documentos, cadastrar_imovel_documento, atualizar_imovel_documento, deletar_imovel_documento
from anuncio_model import listar_anuncios, cadastrar_anuncio, atualizar_anuncio, deletar_anuncio
from foto_imovel_model import listar_fotos, cadastrar_foto, atualizar_foto, deletar_foto
from relatorio_model import exportar_corretores_excel, exportar_corretores_pdf


def ler_campo(rotulo, tipo="str"):
    """Lê um campo do teclado e converte para o tipo pedido."""
    valor = input(f"{rotulo}: ")

    if tipo == "int":
        return int(valor)
    if tipo == "float":
        return float(valor)
    if tipo == "int_opcional":
        # Usado em campos que podem ficar em branco (ex.: FK opcional)
        return int(valor) if valor.strip() else None
    if tipo == "bool_sn":
        return 1 if valor.strip().upper() == "S" else 0

    return valor


def ler_campos(campos):
    """Lê uma lista de campos [(rotulo, tipo), ...] e retorna os valores na ordem."""
    return [ler_campo(rotulo, tipo) for rotulo, tipo in campos]


# ==========================================================================
# Cada entidade descreve: título, função de listar, campos (na ordem exata
# esperada pelas funções de cadastrar/atualizar do respectivo *_model.py),
# e as funções de cadastrar/atualizar/deletar.
# `atualizar` pode ser None quando a entidade não oferece essa opção.
# ==========================================================================
ENTIDADES = {
    "1": {
        "titulo": "ENDEREÇO",
        "listar": listar_enderecos,
        "campos": [("Rua", "str"), ("Número", "str"), ("Bairro", "str"),
                   ("Cidade", "str"), ("Estado", "str"), ("CEP", "str")],
        "cadastrar": cadastrar_endereco,
        "atualizar": atualizar_endereco,
        "deletar": deletar_endereco,
        "id_rotulo": "ID",
    },
    "2": {
        "titulo": "PROPRIETÁRIO",
        "listar": listar_proprietarios,
        "campos": [("Nome", "str"), ("CPF/CNPJ", "str"), ("Telefone", "str"), ("Email", "str")],
        "cadastrar": cadastrar_proprietario,
        "atualizar": atualizar_proprietario,
        "deletar": deletar_proprietario,
        "id_rotulo": "ID",
    },
    "3": {
        "titulo": "CLIENTE",
        "listar": listar_clientes,
        "campos": [("Nome", "str"), ("CPF", "str"), ("Telefone", "str"), ("Email", "str")],
        "cadastrar": cadastrar_cliente,
        "atualizar": atualizar_cliente,
        "deletar": deletar_cliente,
        "id_rotulo": "ID",
    },
    "4": {
        "titulo": "CORRETOR",
        "listar": listar_corretores,
        "campos": [("Nome", "str"), ("CRECI", "str"), ("Telefone", "str"), ("Email", "str")],
        "cadastrar": cadastrar_corretor,
        "atualizar": atualizar_corretor,
        "deletar": deletar_corretor,
        "id_rotulo": "ID",
    },
    "5": {
        "titulo": "TIPO DE IMÓVEL",
        "listar": listar_tipos_imovel,
        "campos": [("Descrição", "str")],
        "cadastrar": cadastrar_tipo_imovel,
        "atualizar": atualizar_tipo_imovel,
        "deletar": deletar_tipo_imovel,
        "id_rotulo": "ID",
    },
    "6": {
        "titulo": "DOCUMENTO",
        "listar": listar_documentos,
        "campos": [("Nome do documento", "str"), ("Tipo", "str")],
        "cadastrar": cadastrar_documento,
        "atualizar": atualizar_documento,
        "deletar": deletar_documento,
        "id_rotulo": "ID",
    },
    "7": {
        "titulo": "IMÓVEL",
        "listar": listar_imoveis,
        "campos": [("ID Proprietário", "int"), ("ID Tipo Imóvel", "int"), ("ID Endereço", "int"),
                   ("Valor sugerido", "float"), ("Status", "str")],
        "cadastrar": cadastrar_imovel,
        "atualizar": atualizar_imovel,
        "deletar": deletar_imovel,
        "id_rotulo": "ID Imóvel",
    },
    "8": {
        "titulo": "VISITA",
        "listar": listar_visitas,
        "campos": [("ID Cliente", "int"), ("ID Corretor", "int"), ("ID Imóvel", "int"),
                   ("Data e Hora (AAAA-MM-DD HH:MM:SS)", "str"), ("Observações", "str")],
        "cadastrar": cadastrar_visita,
        "atualizar": atualizar_visita,
        "deletar": deletar_visita,
        "id_rotulo": "ID Visita",
    },
    "9": {
        "titulo": "VENDA",
        "listar": listar_vendas,
        "campos": [("ID Cliente", "int"), ("ID Corretor", "int"), ("ID Imóvel", "int"),
                   ("Data da Venda (AAAA-MM-DD)", "str"), ("Valor da Venda", "float")],
        "cadastrar": cadastrar_venda,
        "atualizar": atualizar_venda,
        "deletar": deletar_venda,
        "id_rotulo": "ID Venda",
    },
    "10": {
        "titulo": "ALUGUEL",
        "listar": listar_alugueis,
        "campos": [("ID Cliente", "int"), ("ID Corretor", "int"), ("ID Imóvel", "int"),
                   ("Data de Início (AAAA-MM-DD)", "str"), ("Valor do Aluguel", "float")],
        "cadastrar": cadastrar_aluguel,
        "atualizar": atualizar_aluguel,
        "deletar": deletar_aluguel,
        "id_rotulo": "ID Aluguel",
    },
    # --- CORRIGIDO: main.py pedia (id_cliente, id_imovel, tipo, data), mas
    # cadastrar_contrato/atualizar_contrato esperam
    # (id_venda, id_aluguel, data_assinatura, clausulas). Um contrato é de
    # venda OU de aluguel, então id_venda/id_aluguel são opcionais (o campo
    # pode ficar em branco no banco).
    "11": {
        "titulo": "CONTRATO",
        "listar": listar_contratos,
        "campos": [("ID Venda (Enter se não houver)", "int_opcional"),
                   ("ID Aluguel (Enter se não houver)", "int_opcional"),
                   ("Data de Assinatura (AAAA-MM-DD)", "str"), ("Cláusulas", "str")],
        "cadastrar": cadastrar_contrato,
        "atualizar": atualizar_contrato,
        "deletar": deletar_contrato,
        "id_rotulo": "ID Contrato",
    },
    "12": {
        "titulo": "PAGAMENTO",
        "listar": listar_pagamentos,
        "campos": [("ID Contrato", "int"), ("Valor", "float"),
                   ("Data pagamento (AAAA-MM-DD)", "str"), ("Método pagamento", "str")],
        "cadastrar": cadastrar_pagamento,
        "atualizar": atualizar_pagamento,
        "deletar": deletar_pagamento,
        "id_rotulo": "ID Pagamento",
    },
    # --- CORRIGIDO: main.py não pedia "Data de arquivamento", então a
    # chamada a cadastrar_imovel_documento() faltava um argumento obrigatório
    # e quebrava em tempo de execução. Também foi exposta a opção de
    # Atualizar, que já existia em imovel_documento_model.py mas não estava
    # ligada a nenhum menu.
    "13": {
        "titulo": "IMÓVEL DOCUMENTO",
        "listar": listar_imovel_documentos,
        "campos": [("ID Imóvel", "int"), ("ID Documento", "int"),
                   ("Data de arquivamento (AAAA-MM-DD)", "str")],
        "cadastrar": cadastrar_imovel_documento,
        "atualizar": atualizar_imovel_documento,
        "deletar": deletar_imovel_documento,
        "id_rotulo": "ID Imóvel Documento",
    },
    # --- CORRIGIDO: main.py não pedia "Título", campo obrigatório
    # (NOT NULL) em Anuncio; a chamada original quebrava em tempo de
    # execução.
    "14": {
        "titulo": "ANÚNCIO",
        "listar": listar_anuncios,
        "campos": [("ID Imóvel", "int"), ("Título", "str"),
                   ("Descrição", "str"), ("Data de publicação (AAAA-MM-DD)", "str")],
        "cadastrar": cadastrar_anuncio,
        "atualizar": atualizar_anuncio,
        "deletar": deletar_anuncio,
        "id_rotulo": "ID Anúncio",
    },
    # --- CORRIGIDO: main.py pedia (id_imovel, caminho), mas
    # cadastrar_foto/atualizar_foto esperam (id_anuncio, url_foto,
    # principal) -- FotoImovel se relaciona com Anuncio, não diretamente com
    # Imovel. Também foi exposta a opção de Atualizar (já existente no
    # model, mas não ligada a nenhum menu).
    "15": {
        "titulo": "FOTO IMÓVEL",
        "listar": listar_fotos,
        "campos": [("ID Anúncio", "int"), ("URL/Caminho da foto", "str"),
                   ("É a foto principal? (S/N)", "bool_sn")],
        "cadastrar": cadastrar_foto,
        "atualizar": atualizar_foto,
        "deletar": deletar_foto,
        "id_rotulo": "ID Foto",
    },
}


def submenu(entidade):
    """Submenu genérico de Listar/Cadastrar/Atualizar/Deletar para uma entidade."""
    while True:
        print(f"\n===== {entidade['titulo']} =====")
        print("1 - Listar")
        print("2 - Cadastrar")
        if entidade["atualizar"]:
            print("3 - Atualizar")
        print("4 - Deletar")
        print("0 - Voltar")

        escolha = input("Escolha: ")

        if escolha == "1":
            entidade["listar"]()

        elif escolha == "2":
            valores = ler_campos(entidade["campos"])
            entidade["cadastrar"](*valores)

        elif escolha == "3" and entidade["atualizar"]:
            id_valor = ler_campo(entidade["id_rotulo"], "int")
            valores = ler_campos(entidade["campos"])
            entidade["atualizar"](id_valor, *valores)

        elif escolha == "4":
            id_valor = ler_campo(entidade["id_rotulo"], "int")
            entidade["deletar"](id_valor)

        elif escolha == "0":
            break


def menu_relatorios():
    while True:
        print("\n===== CENTRAL DE RELATÓRIOS 📊 =====")
        print("1 - Exportar Corretores para Excel (.xlsx)")
        print("2 - Exportar Corretores para PDF (.pdf)")
        print("0 - Voltar ao Menu Principal")

        escolha = input("Escolha: ")

        if escolha == "1":
            exportar_corretores_excel()
        elif escolha == "2":
            exportar_corretores_pdf()
        elif escolha == "0":
            break


def menu_principal():
    opcoes_titulos = [(num, e["titulo"].title()) for num, e in ENTIDADES.items()]

    while True:
        print("\n========================================")
        print("      ALLEANZA IMMOBILIARE")
        print("========================================")
        for num, titulo in opcoes_titulos:
            print(f"{num:<2} - {titulo}")
        print("16 - Gerar Relatórios 📊")
        print("0  - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "0":
            print("Sistema encerrado.")
            break
        elif opcao == "16":
            menu_relatorios()
        elif opcao in ENTIDADES:
            submenu(ENTIDADES[opcao])
        else:
            print("\n❌ Opção inválida.")


if __name__ == "__main__":
    menu_principal()
