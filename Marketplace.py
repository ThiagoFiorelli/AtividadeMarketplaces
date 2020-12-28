class Subcategoria:
    __nome: str

    def __init__(self, nome: str):
        self.__nome = nome
    
    def get_name(self) -> str:
        return self.__nome

class Categoria:
    __nome: str
    __subcategorias: list

    def __init__(self, nome: str):
        self.__nome = nome
        self.__subcategorias = []

    def get_name(self) -> str:
        return self.__nome
    
    def get_subcategories(self) -> list:
        return self.__subcategorias
    
    def set_subcategories(self, subcategoria: Subcategoria):
        self.__subcategorias.append(subcategoria)

class Marketplace:
    __nome: str
    __categorias: list

    def __init__(self, nome: str):
        self.__nome = nome
        self.__categorias = []

    def get_name(self) -> str:
        return self.__nome

    def get_categories(self) -> list:
        return self.__categorias

    def set_categories(self, categoria: Categoria):
        self.__categorias.append(categoria)