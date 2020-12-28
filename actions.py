from Marketplace import Marketplace, Categoria, Subcategoria
from log import generate_log
from db_sim import get_marketplaces_from_file

marketplaces, categorias = get_marketplaces_from_file()

def list_marketplaces_name() -> list:
    list_ = []
    for marketplace in marketplaces:
        list_.append(marketplace)
    generate_log('Acesso a listagem de marketplaces.')
    return list_

def list_marketplace_categories(name: str) -> list:
    list_ = []
    for marketplace in marketplaces:
        if marketplace.get_name() == name:
            for categoria in marketplace.get_categories():
                list_.append(categoria)
    generate_log(f'Acesso a listagem de categorias do marketplace "{name}".')
    return list_
    
def list_categorie_subcategories(name: str) -> list:
    list_ = []
    for categoria in categorias:
        if categoria.get_name() == name:
            for subcategoria in categoria.get_subcategories():
                list_.append(subcategoria)
    generate_log(f'Acesso a listagem de subcategorias da categoria "{name}".')
    return list_  
