from flask import Flask, render_template, request
from actions import list_marketplaces_name, list_marketplace_categories, list_categorie_subcategories, list_categories, create_marketplace

app = Flask(__name__)

titulo_head = 'Marketplaces'

@app.route('/')
def home():
    return render_template('home.html', titulo_head = titulo_head)

@app.route('/marketplaces')
def marketplaces():
    resultado = list_marketplaces_name()
    return render_template('marketplaces.html', titulo_head = titulo_head, lista = resultado, titulo = 'Marketplaces')

@app.route('/cadastro_marketplace')
def cadastro_marketplace():
    resultado = list_categories()
    return render_template('cadastro_marketplace.html', titulo_head = titulo_head, lista_categorias = resultado)

@app.route('/create')
def create():
    tipo = request.args.get('type')
    nome = request.args.get('name')

    if tipo == 'marketplace':
        args_dict = request.args.to_dict(flat=False)
        categorias = args_dict['categories']
        create_marketplace(nome, categorias)
    elif tipo == 'categoria':
        pass
    elif tipo == 'subcategoria':
        pass


    return f'Sucesso ao cadastrar!'

@app.route('/marketplace/<name>')
def marketplace(name):
    resultado = list_marketplace_categories(name)
    return render_template('marketplace.html', titulo_head = titulo_head, lista = resultado, nome = name, titulo = 'Marketplace')

@app.route('/categoria/<name>')
def category(name):
    resultado = list_categorie_subcategories(name)
    return render_template('category.html', titulo_head = titulo_head, lista = resultado, nome = name, titulo = 'Categoria')

app.run(debug=True)