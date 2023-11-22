from typing import Any


def has_var(obj: Any, var_name: str) -> bool:
    try:
        if isinstance(obj.__getattribute__(var_name), int):
            return True
    except AttributeError:
        try:
            if isinstance(obj.__getattr__(__name=var_name), int):
                return True
        except AttributeError:
            return False
    return False
