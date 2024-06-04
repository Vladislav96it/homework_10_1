def card_hide(card_number: int) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску."""
    return f"{str(card_number)[:4]} {str(card_number)[4:6]}** **** {str(card_number)[-4:]}"


def masks_account_numbers(score: int) -> str:
    """Функция, которая маскирует номер счета"""
    return f'**{str(score)[-4:]}'
