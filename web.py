from flask import Flask, render_template
from actions import list_marketplaces_name, list_marketplace_categories, list_categorie_subcategories

app = Flask(__name__)

@app.route('/')
def home():
    resultado = list_marketplaces_name()
    return render_template('home.html', lista = resultado)

@app.route('/marketplace/<name>')
def marketplace(name):
    resultado = list_marketplace_categories(name)
    return render_template('marketplace.html', lista = resultado, nome = name)

@app.route('/categoria/<name>')
def category(name):
    resultado = list_categorie_subcategories(name)
    return render_template('category.html', lista = resultado, nome = name)

app.run(debug=True)