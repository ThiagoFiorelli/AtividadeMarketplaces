from flask import Flask, render_template
from actions import list_marketplaces_name, list_marketplace_categories, list_categorie_subcategories

app = Flask(__name__)

titulo_head = 'Marketplaces'

@app.route('/')
def home():
    resultado = list_marketplaces_name()
    return render_template('home.html', titulo_head = titulo_head, lista = resultado, titulo = 'Marketplaces')

@app.route('/marketplace/<name>')
def marketplace(name):
    resultado = list_marketplace_categories(name)
    return render_template('marketplace.html', titulo_head = titulo_head, lista = resultado, nome = name, titulo = 'Marketplace')

@app.route('/categoria/<name>')
def category(name):
    resultado = list_categorie_subcategories(name)
    return render_template('category.html', titulo_head = titulo_head, lista = resultado, nome = name, titulo = 'Categoria')

app.run(debug=True)