from functions import card_hide, masks_account_numbers


def defend (object: str) -> str:
    """функцию, которая умеет работать как с картами, так и со счетами."""
    text = ''
    ind = 0
    while object[ind].isdigit() != True:
        text += object[ind]
        ind += 1
    text = text[:4]
    if text == 'Счет':
        return masks_account_numbers(object)
    else:
        return card_hide(object)