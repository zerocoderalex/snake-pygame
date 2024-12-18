import pytest
from main import count_vowels

def test_count_vowels():
    assert count_vowels("alex") == 2
    assert count_vowels("mkrt") == 0
    assert count_vowels("alex24") == 2

# Проверьте, что функция правильно считает гласные в строке, содержащей только гласные.
# Проверьте, что функция возвращает 0 для строки, не содержащей гласных.
# Проверьте, что функция правильно считает гласные в смешанных строках (включая прописные и строчные буквы).