def card_hide(card: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску."""
    s = card.split()
    number = [i for i in s if i.isdigit()]
    number = ' '.join(number)
    model = [i for i in s if i.isdigit() == False]
    model = ' '.join(model)
    mask = f"{number[:4]}{number[4:6]}2** {number[-4:]}"
    return f"{model} {mask}"


def masks_account_numbers(score: str) -> str:
    """Функция, которая маскирует номер счета"""
    numbers = score.split()[1]
    mask = f'**{numbers[-4:]}'
    return f"{score.split()[0]}"
