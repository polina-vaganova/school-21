"""
FDC API data transformation module.
"""


import os
import sys

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__, ),
        ),
    ),
)

from json import load
from pandas import DataFrame

from utils import get_conversion_multiplier_to_g


def standardize_ingredient_nutrient_data(
    ingredient_nutrient_data: list[str | None, float, str]
) -> list[str, float] | None:
    """
    Standardize ingredient nutrient data.

    :Parameters:
        ingredient_nutrient_data (list[str | None, float, str]): Ingredient
                                                                 nutrient data.

    :Returns:
        list[str, float]: Standardized ingredient nutrient data.
        None: If error occurs or no data is loaded.

    :Exceptions:
        AttributeError: When data attribute not initialized.
        IndexError: When dictionary do not contain expected values.
        ValueError: When used invalid data format.
        TypeError: When used incorrect data types.
        Exception: All other errors.
    """

    try:
        nutrient_name: str | None = ingredient_nutrient_data[0]
        nutrient_num: float = ingredient_nutrient_data[1]
        nutrient_unit: str = ingredient_nutrient_data[2]

        match nutrient_name.lower():
            case "protein":
                return [
                    "protein",
                    nutrient_num * get_conversion_multiplier_to_g(
                        nutrient_unit,
                    ),
                ]
            case "total lipid (fat)":
                return [
                    "fat",
                    nutrient_num * get_conversion_multiplier_to_g(
                        nutrient_unit,
                    ),
                ]
            case "carbohydrate, by difference":
                return [
                    "carbohydrate",
                    nutrient_num * get_conversion_multiplier_to_g(
                        nutrient_unit,
                    ),
                ]
            case "total sugars":
                return [
                    "sugars",
                    nutrient_num * get_conversion_multiplier_to_g(
                        nutrient_unit,
                    ),
                ]
            case "fiber, total dietary":
                return [
                    "fiber",
                    nutrient_num * get_conversion_multiplier_to_g(
                        nutrient_unit,
                    ),
                ]
            case "calcium, ca":
                return [
                    "calcium",
                    nutrient_num * get_conversion_multiplier_to_g(
                        nutrient_unit,
                    ),
                ]
            case "iron, fe":
                return [
                    "iron",
                    nutrient_num * get_conversion_multiplier_to_g(
                        nutrient_unit,
                    ),
                ]
            case "sodium, na":
                return [
                    "sodium",
                    nutrient_num * get_conversion_multiplier_to_g(
                        nutrient_unit,
                    ),
                ]
            case "vitamin a, iu" | "vitamin a, rae":
                return [
                    "vitamin a",
                    nutrient_num * get_conversion_multiplier_to_g(
                        nutrient_unit,
                    ),
                ]
            case "vitamin c, total ascorbic acid":
                return [
                    "vitamin c",
                    nutrient_num * get_conversion_multiplier_to_g(
                        nutrient_unit,
                    ),
                ]
            case "cholesterol":
                return [
                    "cholesterol",
                    nutrient_num * get_conversion_multiplier_to_g(
                        nutrient_unit,
                    ),
                ]
            case "fatty acids, total saturated":
                return [
                    "saturated fat",
                    nutrient_num * get_conversion_multiplier_to_g(
                        nutrient_unit,
                    ),
                ]
            case "potassium, k":
                return [
                    "potassium",
                    nutrient_num * get_conversion_multiplier_to_g(
                        nutrient_unit,
                    ),
                ]
            case "vitamin d (d2 + d3), international units" |\
                 "vitamin d (d2 + d3)":
                return [
                    "vitamin d",
                    nutrient_num * get_conversion_multiplier_to_g(
                        nutrient_unit,
                    ),
                ]
            case "magnesium, mg":
                return [
                    "magnesium",
                    nutrient_num * get_conversion_multiplier_to_g(
                        nutrient_unit,
                    ),
                ]
            case "phosphorus, p":
                return [
                    "phosphorus",
                    nutrient_num * get_conversion_multiplier_to_g(
                        nutrient_unit,
                    ),
                ]
            case "zinc, zn":
                return [
                    "zinc",
                    nutrient_num * get_conversion_multiplier_to_g(
                        nutrient_unit,
                    ),
                ]
            case "copper, cu":
                return [
                    "copper",
                    nutrient_num * get_conversion_multiplier_to_g(
                        nutrient_unit,
                    ),
                ]
            case "selenium, se":
                return [
                    "selenium",
                    nutrient_num * get_conversion_multiplier_to_g(
                        nutrient_unit,
                    ),
                ]
            case "vitamin e (alpha-tocopherol)":
                return [
                    "vitamin e",
                    nutrient_num * get_conversion_multiplier_to_g(
                        nutrient_unit,
                    ),
                ]
            case "thiamin":
                return [
                    "thiamin",
                    nutrient_num * get_conversion_multiplier_to_g(
                        nutrient_unit,
                    ),
                ]
            case "riboflavin":
                return [
                    "riboflavin",
                    nutrient_num * get_conversion_multiplier_to_g(
                        nutrient_unit,
                    ),
                ]
            case "niacin":
                return [
                    "niacin",
                    nutrient_num * get_conversion_multiplier_to_g(
                        nutrient_unit,
                    ),
                ]
            case "vitamin b-6":
                return [
                    "vitamin b 6",
                    nutrient_num * get_conversion_multiplier_to_g(
                        nutrient_unit,
                    ),
                ]
            case "folate, total":
                return [
                    "folate",
                    nutrient_num * get_conversion_multiplier_to_g(
                        nutrient_unit,
                    ),
                ]
            case "vitamin b-12":
                return [
                    "vitamin b 12",
                    nutrient_num * get_conversion_multiplier_to_g(
                        nutrient_unit,
                    ),
                ]
            case "choline, total":
                return [
                    "choline",
                    nutrient_num * get_conversion_multiplier_to_g(
                        nutrient_unit,
                    ),
                ]
            case "vitamin k (phylloquinone)":
                return [
                    "vitamin k",
                    nutrient_num * get_conversion_multiplier_to_g(
                        nutrient_unit,
                    ),
                ]
            case "manganese, mn":
                return [
                    "manganese",
                    nutrient_num * get_conversion_multiplier_to_g(
                        nutrient_unit,
                    ),
                ]
            case "pantothenic acid":
                return [
                    "pantothenic acid",
                    nutrient_num * get_conversion_multiplier_to_g(
                        nutrient_unit,
                    ),
                ]
            case "biotin":
                return [
                    "biotin",
                    nutrient_num * get_conversion_multiplier_to_g(
                        nutrient_unit,
                    ),
                ]
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

def standardize_ingredient_nutrients_data(
    ingredient_nutrients_data: list[list[str | None, float, str]]
) -> list[list[str, float]] | None:
    """
    Standardize ingredient nutrients data.

    :Parameters:
        ingredient_nutrients_data (list[list[str | None, float, str]]):
        Ingredient nutrients data.

    :Returns:
        list[list[str, float]]: Standardized ingredient nutrients data.
        None: If error occurs or no data is loaded.

    :Exceptions:
        Exception: All other errors.
    """

    try:
        prep_ingredient_nutrients_data: list = []

        for ingredient_nutrient_data in ingredient_nutrients_data:
            loc_ingredient_nutrient_data: list[
                str, float
            ] | None = standardize_ingredient_nutrient_data(
                ingredient_nutrient_data,
            )

            if loc_ingredient_nutrient_data is not None:
                prep_ingredient_nutrients_data.append(
                    loc_ingredient_nutrient_data,
                )

        return prep_ingredient_nutrients_data
    except Exception as err:
        print("Exception:", err, )

def standardize_ingredients_nutrients_data(
    ingredients_nutrients_data: list[list[list[str | None, float, str]]]
) -> list[list[list[str, float]]] | None:
    """
    Standardize ingredients nutrients data.

    :Parameters:
        ingredients_nutrients_data (list[list[list[str | None, float, str]]]):
        Ingredients nutrients data.

    :Returns:
        list[list[list[str, float]]]: Standardized ingredients nutrients data.
        None: If error occurs or no data is loaded.

    :Exceptions:
        Exception: All other errors.
    """

    try:
        prep_ingredients_nutrients_data: list = []

        for ingredient_nutrients_data in ingredients_nutrients_data:
            prep_ingredients_nutrients_data.append(
                standardize_ingredient_nutrients_data(
                    ingredient_nutrients_data,
                ),
            )

        return prep_ingredients_nutrients_data
    except Exception as err:
        print("Exception:", err, )

def get_ingredient_nutrients_data(
    necess_nutrients: list[str],
    ingredient_nutrients_data: list[list[str, float]]
) -> dict[str, float] | None:
    """
    Return ingredient nutrients data.

    :Parameters:
        necess_nutrients (list[str]): A necessary nutrients names.
        ingredient_nutrients_data (list[list[str, float]]): Ingredient nutrients
                                                            data.

    :Returns:
        dict[str, float]: Ingredient nutrients data.
        None: If error occurs or no data is loaded.

    :Exceptions:
        IndexError: When dictionary do not contain expected values.
        TypeError: When used incorrect data types.
        Exception: All other errors.
    """

    try:
        nutrients: dict[str, float] = {
            nutrient: 0
            for nutrient
            in necess_nutrients
        }

        for ingredient_nutrient_data in ingredient_nutrients_data:
            nutrients[ingredient_nutrient_data[0]] = ingredient_nutrient_data[1]

        return nutrients
    except IndexError as idx_err:
        print("IndexError:", idx_err, )
    except TypeError as type_err:
        print("TypeError:", type_err, )
    except Exception as err:
        print("Exception:", err, )

def get_ingredients_nutrients_data(
    nutrients_file: str,
    nutrients_file_path: str,
    ingredients_nutrients_data: list[list[list[str, float]]]
) -> list[dict[str, float]] | None:
    """
    Return ingredients nutrients data.

    :Parameters:
        nutrients_file (str): File with necessary nutrients names.
        nutrients_file_path (str): Path to file with necessary nutrients names.
        ingredients_nutrients_data (list[list[list[str, float]]]): Ingredients
                                                                   nutrients
                                                                   data.

    :Returns:
        list[dict[str, float]]: Ingredients nutrients data.
        None: If error occurs or no data is loaded.

    :Exceptions:
        FileNotFoundError: When file was not found.
        IndexError: When dictionary do not contain expected values.
        Exception: All other errors.
    """

    try:
        with open(
            mode="r",
            encoding="utf-8",
            file=nutrients_file_path + nutrients_file,
        ) as file:
            food_data: dict[str, list[str]] = load(file, )
            nutrients: list[str] = food_data["nutrients"]

        prep_ingredients_nutrients_data: list = []

        for ingredient_nutrients_data in ingredients_nutrients_data:
            prep_ingredients_nutrients_data.append(
                get_ingredient_nutrients_data(
                    nutrients,
                    ingredient_nutrients_data,
                ),
            )

        return prep_ingredients_nutrients_data
    except FileNotFoundError as file_not_found_err:
        print("FileNotFoundError:", file_not_found_err, )
    except IndexError as idx_err:
        print("IndexError:", idx_err, )
    except Exception as err:
        print("Exception:", err, )

def get_ingredients_nutrients_dataframe(
    ingredients: list[str],
    ingredients_nutrients_data: list[dict[str, float]]
) -> DataFrame | None:
    """
    Return ingredients nutrients data in Pandas DataFrame.

    :Parameters:
        ingredients (list[str]): A necessary nutrients names.
        ingredients_nutrients_data (list[dict[str, float]]): Ingredients
                                                             nutrients data.

    :Returns:
        DataFrame: Ingredients nutrients data in Pandas DataFrame.
        None: If error occurs or no data is loaded.

    :Exceptions:
        AttributeError: When data attribute not initialized.
        IndexError: When dictionary do not contain expected values.
        ValueError: When used invalid data format.
        TypeError: When used incorrect data types.
        Exception: All other errors.
    """

    try:
        prep_ingredients_nutrients_data: list = []

        for ingredient, ingredient_nutrients_data in zip(
            ingredients,
            ingredients_nutrients_data,
        ):
            ingredient_nutrients_data["name"] = ingredient
            prep_ingredients_nutrients_data.append(ingredient_nutrients_data, )

        return DataFrame(prep_ingredients_nutrients_data, )
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
