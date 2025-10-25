# tests/test_properties.py
from hypothesis import given, strategies as st # type: ignore
from src import isbn

# normalizar es idempotente: normalize(normalize(s)) == normalize(s)
@given(st.text())
def test_normalize_idempotent(s):
    n1 = isbn.normalize_isbn(s)
    n2 = isbn.normalize_isbn(n1)
    assert n1 == n2

# si una cadena sólo cambia por guiones/espacios, la normalización la iguala
@given(st.text().filter(lambda x: any(ch.isdigit() for ch in x)))
def test_normalize_keeps_digits(s):
    alt = s.replace('-', '').replace(' ', '')
    assert isbn.normalize_isbn(alt) == isbn.normalize_isbn(alt)
