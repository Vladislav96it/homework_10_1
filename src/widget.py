from src.masks import card_hide, masks_account_numbers


def mask_account_card(object: str) -> str:
    """функцию, которая умеет работать как с картами, так и со счетами."""
    if object[:4] == "Счет":
        return f'{object[:5]}{masks_account_numbers(int(object[5:]))}'
    return f"{object[:-16]}{card_hide(int(object[-16:]))}"


# print(mask_account_card("Счет 73654108430135874305"))

def get_data