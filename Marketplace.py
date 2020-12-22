class Marketplace:
    nome: str
    categorias: list

    def __init__(self, nome, categorias):
        self.nome = nome
        self.categorias = categorias

class Categoria:
    nome: str
    subcategorias: list

    def __init__(self, nome, subcategorias):
        self.nome = nome
        self.subcategorias = subcategorias

class Subcategoria:
    nome: str

    def __init__(self, nome):
        self.nome = nome
