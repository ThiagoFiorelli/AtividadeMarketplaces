from actions import list_marketplaces_name, list_marketplace_categories, list_categorie_subcategories

def marketplaces():
    marketplaces = list_marketplaces_name()

    print('\n Marketplaces: ')

    for option in marketplaces:
        print(option)

    op = input('Escolha um marketplace pelo nome: ')
    return op

def categorias(marketplace):
    categorias = list_marketplace_categories(marketplace)

    print('\n Categorias: ')

    for option in categorias:
        print(option)

    op = input('Escolha uma categoria pelo nome: ')
    return op

def subcategorias(categoria):
    subcategorias = list_categorie_subcategories(categoria)

    print('\n Subcategorias: ')

    for option in subcategorias:
        print(option)

    while True:
        op = input('Deseja sair? S/N: ').lower()
        
        if op == 's':
            exit(0)
        elif op == 'n':
            break


while True:
    try:
        marketplace = marketplaces()
        categoria = categorias(marketplace)
        subcategorias(categoria)

    except ValueError as err:
        print('Error de valor: ', err)
