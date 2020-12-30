from Marketplace import Marketplace, Categoria, Subcategoria
from log import generate_log
from db_sim import get_marketplaces, add_marketplace, get_categories

def create_marketplace(name: str, categories: str) -> None:
    marketplace = Marketplace(name)
    marketplace.categories.extend(categories)
    add_marketplace(marketplace)
    generate_log(f'Adicionado o marketplace "{marketplace.name}" ao database.')


def list_marketplaces_name() -> list:
    marketplaces = get_marketplaces()
    list_ = []
    for marketplace in marketplaces:
        list_.append(marketplace)
    generate_log('Acesso a listagem de marketplaces.')
    return list_

def list_marketplace_categories(name: str) -> list:
    marketplaces = get_marketplaces()
    print(marketplaces)
    print(name)
    list_ = []
    for marketplace in marketplaces:
        if marketplace.name == name:
            for category in marketplace.categories:
                list_.append(category)
    generate_log(f'Acesso a listagem de categorias do marketplace "{name}".')
    return list_

def list_categories() -> list:
    categories = get_categories()
    return categories
    
def list_categorie_subcategories(name: str) -> list:
    list_ = []
    categories = get_categories()
    for category in categories:
        if category.name == name:
            for subcategory in category.subcategories:
                list_.append(subcategory)
    generate_log(f'Acesso a listagem de subcategorias da categoria "{name}".')
    return list_  
