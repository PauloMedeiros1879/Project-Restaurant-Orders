from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1 - Iniciando projeto
def test_ingredient():
    banana_ingredient = Ingredient("banana")
    cereja_ingredient = Ingredient("cereja")
    bacon_ingredient = Ingredient("bacon")
    bacon_ingredient2 = Ingredient("bacon")

    assert banana_ingredient != cereja_ingredient
    assert bacon_ingredient == bacon_ingredient2

    assert banana_ingredient.name == "banana"

    assert hash(banana_ingredient) != hash(cereja_ingredient)
    assert hash(bacon_ingredient) == hash(bacon_ingredient2)

    assert repr(banana_ingredient) != "Ingredient('cereja')"
    assert repr(banana_ingredient) == "Ingredient('banana')"

    assert len(bacon_ingredient.restrictions) == 2
