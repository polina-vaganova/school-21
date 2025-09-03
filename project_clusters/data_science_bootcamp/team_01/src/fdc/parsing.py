"""
FDC API data parsing module.
"""


from typing import Any


def parse_ingredient_nutrients_data(
    ingredient_data: dict[str, Any]
) -> list[list[str | None, float, str]] | None:
    """
    Extracts nutrients data from FDC API ingredient response.

    :Parameters:
        ingredient_data (dict[str, Any]): Response from FDC API containing
                                          ingredient data.

    :Returns:
        list[list[str | None, float, str]]: Ingredient nutrients data.
        None: If error occurs or no data is loaded.

    :Exceptions:
        AttributeError: When data attribute not initialized.
        IndexError: When dictionary do not contain expected values.
        ValueError: When used invalid data format.
        TypeError: When used incorrect data types.
        Exception: All other errors.
    """

    ingredient_nutrients_data: list = []

    try:
        nutrients_data: list[dict[str, Any]] = ingredient_data.get(
            "foods",
            None,
        )[0].get(
            "foodNutrients",
            None,
        )

        for nutrient_data in nutrients_data:
            ingredient_nutrients_data.append([
                nutrient_data.get(
                    "nutrientName",
                    None,
                ),
                nutrient_data.get(
                    "value",
                    0,
                ),
                nutrient_data.get(
                    "unitName",
                    'g',
                ),
            ], )

        return ingredient_nutrients_data
    except AttributeError as attr_err:
        print("AttributeError:", attr_err, )
    except IndexError as idx_err:
        print("IndexError:", idx_err, )
    except ValueError as val_err:
        print("ValueError:", val_err, )
    except TypeError as type_err:
        print("TypeError:", type_err, )
    except Exception as err:
        print("Exception:", err, )

def parse_ingredients_nutrients_data(
    ingredients_data: list[dict[str, Any]]
) -> list[list[list[str | None, float, str]]] | None:
    """
    Extracts nutrients data from ingredients.

    :Parameters:
        ingredients_data (list[dict[str, Any]]): List of responses from FDC API
                                                 containing ingredients data.

    :Returns:
        list[list[list[str | None, float, str]]]: Ingredients nutrients data.
        None: If error occurs or no data is loaded.

    :Exceptions:
        Exception: All other errors.
    """

    ingredients_nutrients_data: list = []

    try:
        for ingredient_data in ingredients_data:
            ingredients_nutrients_data.append(parse_ingredient_nutrients_data(
                ingredient_data,
            ), )

        return ingredients_nutrients_data
    except Exception as err:
        print("Exception:", err, )
