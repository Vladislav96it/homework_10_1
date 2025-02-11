import pytest

from src.masks import card_hide, masks_account_numbers


@pytest.fixture
def account_number():
    return 73654108430135874305


@pytest.fixture
def card_number():
    return 7000792289606361


def test_masked_account_number(account_number):
    assert masks_account_numbers(account_number) == "**4305"


def test_masked_card_number(card_number):
    assert card_hide(card_number) == "7000 79** **** 6361"
