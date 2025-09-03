"""
Additional utilities module.
"""


def get_conversion_multiplier_to_g(unit: str = 'g') -> float | None:
    """
    Returns the multiplicatior for converting units of weight measurement to
    grams.

    :Parameters:
        unit (str): String of the measurement unit.
                    Default: 'g'.

    :Returns:
        float: Multiplicatior for conversion to grams.
        None: If error occurs or no data is loaded.

    :Exceptions:
        ValueError: When used invalid data format.
        TypeError: When used incorrect data types.
        Exception: All other errors.
    """

    try:
        match unit.lower():
            case 'g':
                return 1.0
            case "mg":
                return 0.001
            case "mcg" | "ug":
                return 0.000001
            case "iu":
                return 0.0000003
    except ValueError as val_err:
        print("ValueError:", val_err, )
    except TypeError as type_err:
        print("TypeError:", type_err, )
    except Exception as err:
        print("Exception:", err, )
