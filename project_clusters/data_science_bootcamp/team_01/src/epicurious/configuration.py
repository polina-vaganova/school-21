"""
Epicurious API configuration management module.
"""


import os

from typing import Any
from dotenv import load_dotenv


def get_epicurious_config() -> dict[str, Any] | None:
    """
    Return Epicurious API configuration from environment variables.

    :Returns:
        dict[str, Any]: A configuration for working with Epicurious API.
        None: If error occurs or no data is loaded.

    :Exceptions:
        FileNotFoundError: When used file does not exist.
        PermissionError: When used unresolved data.
        Exception: All other errors.
    """

    try:
        load_dotenv()

        epicurious_config: dict[str, Any] = {
            "URL": os.getenv("EPICURIOUS_URL", ),
        }

        return epicurious_config
    except FileNotFoundError as file_not_found_err:
        print("FileNotFoundError:", file_not_found_err, )
    except PermissionError as perm_err:
        print("PermissionError:", perm_err, )
    except Exception as err:
        print("Exception:", err, )
