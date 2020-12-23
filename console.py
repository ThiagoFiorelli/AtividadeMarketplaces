from actions import list_marketplaces_name, list_marketplace_categories, list_categorie_subcategories

def get_marketplaces() -> list:
    marketplaces_list = list_marketplaces_name()
    return marketplaces(marketplaces_list)

def marketplaces(marketplaces_list: list) -> str:

    if not marketplaces_list:
        print('Nao existem marketplaces.')
    else:
        print('\n Marketplaces: ')

        list_ = []
        for option in marketplaces_list:
            list_.append(option.get_name())
            print(option.get_name())
        
        op = input('Escolha um marketplace pelo nome: ')

        if op not in list_:
            print('Nenhum marketplace com esse nome foi encontrado.')
            op = marketplaces(marketplaces_list)
            
        return op

def get_categorias(marketplace: str) -> list:
    categorias_list = list_marketplace_categories(marketplace)
    return categorias(categorias_list)

def categorias(categorias_list: list) -> str:

    if not categorias_list:
        print('Esse marketplace não possui categorias.')
    else:
        print('\n Categorias: ')

        list_ = []
        for option in categorias_list:
            list_.append(option.get_name())
            print(option.get_name())

        op = input('Escolha uma categoria pelo nome: ')

        if op not in list_:
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
            print(option.get_name())
    
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
