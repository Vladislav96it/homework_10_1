def card_hide(card: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску."""
    return f"{card[:4]} {card[4:6] + '*' * 2} **** {card[-4:]}"


def masks_account_numbers(nums: str) ->str:
    """Функция, которая маскирует номер счета"""
    return f"Счет **{nums[-4:]}"