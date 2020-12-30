from Marketplace import Marketplace, Categoria, Subcategoria

categorias_txt = 'categorias.txt'
marketplaces_txt = 'marketplaces.txt'

def add_marketplace(marketplace: Marketplace) -> None:
    with open(marketplaces_txt, 'a', encoding='utf-8') as marketplaces_file:
        for category in marketplace.categories:
            marketplaces_file.write(f'{marketplace.name};{category}\n')


def get_marketplaces() -> list:
    marketplaces = []
    categories = get_categories()
    with open(marketplaces_txt, 'r', encoding='utf-8') as marketplaces_file:

        for line in marketplaces_file:
            result = line.strip().split(';')
            marketplace = next((item for item in marketplaces if item.name == result[0]), None)
            if not marketplace:
                marketplace = Marketplace(result[0])
                marketplaces.append(marketplace)
            category = next((item for item in categories if item.name == result[1]), None)
            if category is not None:
                marketplace.categories.append(category)

    return marketplaces

def get_categories() -> list:
    categories = []

    with open(categorias_txt, 'r', encoding='utf-8') as categories_file:

        for line in categories_file:
            result = line.strip().split(';')
            category = next((item for item in categories if item.name == result[0]), None)
            if not category:
                category = Categoria(result[0])
                categories.append(category)
            category.subcategories.append(Subcategoria(result[1]))

    return categories
