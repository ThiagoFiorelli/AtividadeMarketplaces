from Marketplace import Marketplace, Categoria, Subcategoria

categorias_txt = 'categorias.txt'
marketplaces_txt = 'marketplaces.txt'

def get_marketplaces_from_file() -> list and list:
    categorias = get_categorias()
    marketplaces = get_marketplaces(categorias)
    return marketplaces, categorias

def get_marketplaces(categorias: list) -> list:
    marketplaces = []

    with open(marketplaces_txt, 'r', encoding='utf-8') as marketplaces_file:

        for line in marketplaces_file:
            result = line.strip().split(';')
            marketplace = next((item for item in marketplaces if item.get_name() == result[0]), None)
            if not marketplace:
                marketplace = Marketplace(result[0])
                marketplaces.append(marketplace)
            categoria = next((item for item in categorias if item.get_name() == result[1]), None)
            if categoria is not None:
                marketplace.set_categories(categoria)

    return marketplaces

def get_categorias() -> list:
    categorias = []

    with open(categorias_txt, 'r', encoding='utf-8') as categories_file:

        for line in categories_file:
            result = line.strip().split(';')
            categoria = next((item for item in categorias if item.get_name() == result[0]), None)
            if not categoria:
                categoria = Categoria(result[0])
                categorias.append(categoria)
            categoria.set_subcategories(Subcategoria(result[1]))

    return categorias