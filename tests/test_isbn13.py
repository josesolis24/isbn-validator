# tests/test_isbn13.py
import pytest
from src import isbn

@pytest.mark.parametrize("s", [
    "9780306406157",
    "978-3-16-148410-0",
])
def test_valid_isbn13(s):
    assert isbn.is_valid_isbn13(s) is True
    assert isbn.detect_isbn(s) == "ISBN-13"

@pytest.mark.parametrize("s", [
    "9780306406158",    # checksum mal
    "978030640615",     # longitud 12
    "97803064061570",   # longitud 14
    "97803064061A7",    # caracter ilegal
])
def test_invalid_isbn13(s):
    assert isbn.is_valid_isbn13(s) is False
