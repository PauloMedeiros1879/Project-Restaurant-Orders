from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
import pytest


# Req 2
def test_dish():
    dish_macarrão = Dish("Macarrão", 20.5)
    dish2_macarrão = Dish("Macarrão", 20.5)
    dish_sopa = Dish("Sopa", 17.0)

    assert repr(dish_macarrão) == "Dish('Macarrão', R$20.50)"
    assert dish_macarrão.name == "Macarrão"
    assert dish_macarrão == dish2_macarrão != dish_sopa
    assert hash(dish_macarrão) == hash(dish2_macarrão) != hash(dish_sopa)

    with pytest.raises(ValueError):
        Dish("Batata Gratinada", -900)

    with pytest.raises(TypeError):
        Dish("Batata Gratinada", None)

    bacon_ingredient = Ingredient("bacon")
    manga_ingredient = Ingredient("manga")
    dish_porco = Dish("Porco Agridoce", 30.0)

    dish_porco.add_ingredient_dependency(bacon_ingredient, 2)
    dish_porco.add_ingredient_dependency(manga_ingredient, 1)

    assert len(dish_porco.get_restrictions()) == 2
    assert dish_porco.get_ingredients() == set(
        [manga_ingredient, bacon_ingredient]
    )
    assert dish_porco.recipe.get(manga_ingredient) == 1
    assert dish_porco.recipe.get(bacon_ingredient) == 2
