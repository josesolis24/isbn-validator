# src/isbn.py
import re
from typing import Optional

def normalize_isbn(s: Optional[str]) -> str:
    """Quita espacios y guiones; devuelve cadena limpia en mayúsculas.
       Si s es None o vacía, devuelve ''.
    """
    if s is None:
        return ""
    cleaned = re.sub(r'[\s\-]', '', s).upper()
    return cleaned

def is_valid_isbn10(s: Optional[str]) -> bool:
    s = normalize_isbn(s)
    if len(s) != 10:
        return False
    # primeros 9 dígitos y último dígito o 'X'
    if not re.fullmatch(r'\d{9}[0-9X]', s):
        return False
    total = 0
    for i, ch in enumerate(s):
        weight = 10 - i
        if ch == 'X':
            value = 10
        else:
            value = ord(ch) - ord('0')
        total += weight * value
    return total % 11 == 0

def is_valid_isbn13(s: Optional[str]) -> bool:
    s = normalize_isbn(s)
    if len(s) != 13:
        return False
    if not s.isdigit():
        return False
    total = 0
    for i, ch in enumerate(s):
        digit = ord(ch) - ord('0')
        weight = 1 if i % 2 == 0 else 3
        total += weight * digit
    return total % 10 == 0

def detect_isbn(s: Optional[str]) -> str:
    s_norm = normalize_isbn(s)
    if is_valid_isbn10(s_norm):
        return "ISBN-10"
    if is_valid_isbn13(s_norm):
        return "ISBN-13"
    return "INVALID"
