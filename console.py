from actions import list_marketplaces_name, list_marketplace_categories, list_categorie_subcategories

def get_marketplaces() -> None:
    marketplaces_list = list_marketplaces_name()
    return marketplaces(marketplaces_list)

def marketplaces(marketplaces_list: list) -> str:

    if not marketplaces_list:
        print('Nao existem marketplaces.')
    else:
        print('\n Marketplaces: ')

        for option in marketplaces_list:
            print(option)

        op = input('Escolha um marketplace pelo nome: ')

        if op not in marketplaces_list:
            print('Nenhum marketplace com esse nome foi encontrado.')
            op = marketplaces(marketplaces_list)
            
        return op

def get_categorias(marketplace: str) -> None:
    categorias_list = list_marketplace_categories(marketplace)
    return categorias(categorias_list)

def categorias(categorias_list: list) -> list:

    if not categorias_list:
        print('Esse marketplace não possui categorias.')
    else:
        print('\n Categorias: ')

        for option in categorias_list:
            print(option)

        op = input('Escolha uma categoria pelo nome: ')

        if op not in categorias_list:
            print('Nenhuma categoria com esse nome foi encontrado.')
            op = categorias(categorias_list)

        return op

def get_subcategorias(categoria: str) -> None:
    subcategorias_list = list_categorie_subcategories(categoria)
    subcategorias(subcategorias_list)

def subcategorias(subcategorias_list: str) -> None:

    if not subcategorias_list:
        print('Essa categoria não possui subcategorias.')
    
    else:
        print('\n Subcategorias: ')

        for option in subcategorias_list:
            print(option)
    
    while True:
            op = input('Deseja sair? S/N: ').lower()
            
            if op == 's':
                exit(0)
            elif op == 'n':
                break

while True:
    try:
        marketplace = get_marketplaces()
        categoria = get_categorias(marketplace)
        get_subcategorias(categoria)

    except ValueError as err:
        print('Error de valor: ', err)
