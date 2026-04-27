"""Arquivo de testes."""

from src.main import get_full_name, get_age


def test_get_full_name():
    """Testa nome completo."""
    assert get_full_name("fulano", "silva") == "Fulano Silva"


def test_get_age():
    """Testa idade."""
    assert get_age(24) == "24"
