import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(f"logs/{__name__}.log", mode="w")
file_formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def card_hide(card_number: int) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску."""
    logger.info("Маскируем номер карты")
    return f"{str(card_number)[:4]} {str(card_number)[4:6]}** **** {str(card_number)[-4:]}"


def masks_account_numbers(score: int) -> str:
    """Функция, которая маскирует номер счета"""
    logger.info("Маскируем номер счета")
    return f"**{str(score)[-4:]}"
