"""
FDC API data fetching module.
"""


from typing import Any
from httpx import (
    AsyncClient,
    ConnectError,
    ConnectTimeout,
)

from .configuration import get_fdc_config


async def fetch_ingredient_data(
    ingredient: str,
    async_client: AsyncClient,
    fdc_config: dict[str, Any]
) -> dict[str, Any] | None:
    """
    Fetch ingredient data from FDC API.

    :Parameters:
        ingredient (str): Ingredient name to fetch from FDC database.
        async_client (AsyncClient): Asynchronous client for requests.
        fdc_config (dict[str, Any]): FDC API configuration for requests.

    :Returns:
        dict[str, Any]: Raw ingredient data.
        None: If error occurs or no data is loaded.

    :Exceptions:
        ConnectTimeout: When connection runtime is out.
        ConnectError: When can not connect to server.
        ValueError: When used invalid data format.
        TypeError: When used incorrect data types.
        Exception: All other errors.
    """

    try:
        resp: Any = await async_client.get(
            fdc_config["URL"],
            params={
                "pageSize": 1,
                "query": ingredient,
                "requireExactMatch": True,
                "api_key": fdc_config["API_KEY"],
            },
        )

        if resp.status_code == 200:
            ingredient_data: dict[str, Any] = resp.json()

            return ingredient_data

        print(
            "ERROR!\n" +
            f"Ingredient: {ingredient}.\n" +
            f"Status code: {resp.status_code}.\n",
        )
    except ConnectTimeout as conn_timeout_err:
        print("ConnectTimeout:", conn_timeout_err, )
    except ConnectError as conn_err:
        print("ConnectError:", conn_err, )
    except ValueError as val_err:
        print("ValueError:", val_err, )
    except TypeError as type_err:
        print("TypeError:", type_err, )
    except Exception as err:
        print("Exception:", err, )

async def fetch_ingredients_data(
    ingredients: list[str]
) -> list[dict[str, Any] | None] | None:
    """
    Fetch ingredients data from FDC API.

    :Parameters:
        ingredients (list[str]): List of ingredients names to fetch from FDC
                                 database.

    :Returns:
        list[dict[str, Any] | None]: Raw ingredients data.
        None: If error occurs or no data is loaded.

    :Exceptions:
        Exception: All other errors.
    """

    ingredients_data: list = []

    try:
        fdc_config: dict[str, Any] | None = get_fdc_config()

        async with AsyncClient() as async_client:
            for ingredient in ingredients:
                ingredients_data.append(await fetch_ingredient_data(
                    ingredient,
                    async_client,
                    fdc_config,
                ), )

        return ingredients_data
    except Exception as err:
        print("Exception:", err, )
