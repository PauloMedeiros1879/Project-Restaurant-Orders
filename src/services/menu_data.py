from src.models.dish import Dish
from src.models.ingredient import Ingredient
import pandas as pd


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        # Inicializa o conjunto de dishes como vazio
        self.dishes = set()

        # Carrega o arquivo CSV em um objeto pandas DataFrame
        self.path = pd.read_csv(source_path)

        # Cria um dicionário para armazenar
        # temporariamente os dishes e seus ingredientes
        order = dict()

        # Itera sobre cada linha do DataFrame, criando e adicionando
        # as dependências de ingredientes para cada dish
        for product, prepare, ingredient, amount in self.path.itertuples(
            index=False
        ):
            # Se o dish ainda não foi adicionado ao dicionário de ordem,
            # cria um novo dish com seu nome e instruções de preparo
            if product not in order:
                order[product] = Dish(product, prepare)

            # Adiciona a dependência do ingrediente ao dish atual
            order[product].add_ingredient_dependency(
                Ingredient(ingredient), amount
            )

        # Adiciona os dishes do dicionário de ordem ao conjunto de dishes
        self.dishes = set(order.values())
