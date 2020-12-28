from Marketplace import Marketplace, Categoria, Subcategoria
from db_sim import get_marketplaces_from_file

# categoria1 = Categoria('Eletronico', [Subcategoria('Smartphones'),Subcategoria('Tablet'), Subcategoria('TV')])
# categoria2 = Categoria('Cozinha', [Subcategoria('Pratos'),Subcategoria('Talheres')])
# categoria3 = Categoria('Esporte', [Subcategoria('Musculação'),Subcategoria('Futebol')])

# marketplace1 = Marketplace('Mercado Livre',[categoria1, categoria2])
# marketplace2 = Marketplace('Amazon',[categoria1, categoria3])
# marketplace3 = Marketplace('Magazine Luiza',[categoria2, categoria3])

# categorias = [categoria1, categoria2, categoria3]
# marketplaces = [marketplace1, marketplace2, marketplace3]

marketplaces, categorias = get_marketplaces_from_file()

def list_marketplaces_name() -> list:
    list_ = []
    for marketplace in marketplaces:
        list_.append(marketplace)
    
    return list_

def list_marketplace_categories(name: str) -> list:
    list_ = []
    for marketplace in marketplaces:
        if marketplace.get_name() == name:
            for categoria in marketplace.get_categories():
                list_.append(categoria)
    
    return list_
    
def list_categorie_subcategories(name: str) -> list:
    list_ = []
    for categoria in categorias:
        if categoria.get_name() == name:
            for subcategoria in categoria.get_subcategories():
                list_.append(subcategoria)
    
    return list_  

# categorias = [{'nome' : 'Eletronico', 'subcategorias' : ['Smartphones', 'Tablet', 'TV']}
#             , {'nome' : 'Cozinha', 'subcategorias' : ['Pratos', 'Talheres']}
#             , {'nome' : 'Esporte', 'subcategorias' : ['Musculação', 'Futebol']}] 

# marketplaces = [ {'nome' : 'Mercado Livre', 'categorias' : [categorias[0], categorias[1]]},
#                       {'nome' : 'Amazon', 'categorias' : [categorias[0], categorias[2]]},
#                       {'nome' : 'Magazine Luiza', 'categorias' : [categorias[1], categorias[2]]}     
#                 ]

# def list_marketplaces_name() -> list:
#     list_ = []
#     for marketplace in marketplaces:
#         list_.append(marketplace['nome'])
    
#     return list_

# def list_marketplace_categories(name: str) -> list:
#     list_ = []
#     for marketplace in marketplaces:
#         if marketplace.get_name() == name:
#             for categoria in marketplace['categorias']:
#                 list_.append(categoria['nome'])
#     return list_  

# def list_categorie_subcategories(name: str) -> list:
#     list_ = []
#     for categoria in categorias:
#         if categoria['nome'] == name:
#             for subcategoria in categoria['subcategorias']:
#                 list_.append(subcategoria)
    
#     return list_