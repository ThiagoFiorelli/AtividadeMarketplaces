class Marketplace:
    __nome: str
    __categorias: list

    def __init__(self, nome, categorias):
        self.__nome = nome
        self.__categorias = categorias

    def get_name(self):
        return self.__nome

    def get_categories(self):
        return self.__categorias

class Categoria:
    __nome: str
    __subcategorias: list

    def __init__(self, nome, subcategorias):
        self.__nome = nome
        self.__subcategorias = subcategorias

    def get_name(self):
        return self.__nome
    
    def get_subcategories(self):
        return self.__subcategorias

class Subcategoria:
    __nome: str

    def __init__(self, nome):
        self.__nome = nome
    
    def get_name(self):
        return self.__nome
