# tests/test_isbn10.py
import pytest # type: ignore
from src import isbn

@pytest.mark.parametrize("s", [
    "0-306-40615-2",
    "0471958697",
    "0306406152",
    "0-8044-2957-X",
])
def test_valid_isbn10(s):
    assert isbn.is_valid_isbn10(s) is True
    assert isbn.detect_isbn(s) == "ISBN-10"

@pytest.mark.parametrize("s", [
    "0306406153",    # checksum mal
    "123456789",     # longitud 9
    "12345678901",   # longitud 11
    "0-8044-2957-XX",# caract ilegal / longitud
    "0-8044-295X-7", # X en posición no final
])
def test_invalid_isbn10(s):
    assert isbn.is_valid_isbn10(s) is False
