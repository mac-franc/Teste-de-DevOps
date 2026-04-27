from src.main import *
from unittest.mock import patch


def test_get_full_name():
    result = get_full_name("Fulano", "da Silva")
    assert result == "Fulano Da Silva"


def test_get_age():
    result = get_age(24)
    assert result == "24"
