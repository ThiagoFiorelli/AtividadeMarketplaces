class Subcategoria:
    __name: str

    def __init__(self, name: str):
        self.__name = name
    
    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name

class Categoria:
    __name: str
    __subcategories: list

    def __init__(self, name: str):
        self.__name = name
        self.__subcategories = []

    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
    
    @property
    def subcategories(self) -> list:
        return self.__subcategories
    
    @subcategories.setter
    def subcategories(self, subcategoria: Subcategoria):
        self.__subcategories.append(subcategoria)

class Marketplace:
    __name: str
    __categories: list

    def __init__(self, name: str):
        self.__name = name
        self.__categories = []

    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def categories(self) -> list:
        return self.__categories

    @categories.setter
    def categories(self, categoria: Categoria):
        self.__categories.append(categoria)