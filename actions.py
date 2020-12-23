from Marketplace import Marketplace, Categoria, Subcategoria

categorias = [{'nome' : 'Eletronico', 'subcategorias' : ['Smartphones', 'Tablet', 'TV']}
            , {'nome' : 'Cozinha', 'subcategorias' : ['Pratos', 'Talheres']}
            , {'nome' : 'Esporte', 'subcategorias' : ['Musculação', 'Futebol']}] 

marketplaces = [ {'nome' : 'Mercado Livre', 'categorias' : [categorias[0], categorias[1]]},
                      {'nome' : 'Amazon', 'categorias' : [categorias[0], categorias[2]]},
                      {'nome' : 'Magazine Luiza', 'categorias' : [categorias[1], categorias[2]]}     
                ]



def list_marketplaces_name() -> list:
    list_ = []
    for marketplace in marketplaces:
        list_.append(marketplace['nome'])
    
    return list_

def list_marketplace_categories(name: str) -> list:
    list_ = []
    for marketplace in marketplaces:
        if marketplace['nome'] == name:
            for categoria in marketplace['categorias']:
                list_.append(categoria['nome'])
    
    return list_

def list_categorie_subcategories(name: str) -> list:
    list_ = []
    for categoria in categorias:
        if categoria['nome'] == name:
            for subcategoria in categoria['subcategorias']:
                list_.append(subcategoria)
    
    return list_
    
        
