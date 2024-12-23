# Получение строки
# Предобработка строки (удаление пробелов, символов, регистра)
# Определение длины строки
# Сравнение первого символа с последним, второго с предпоследним и т.д.
# Вывод результата


def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())

    length = len(s)

    for i in range(length // 2):
        if s[i] != s[length - 1 - i]:
          return False
    return True


print(is_palindrome("ABBA"))
print(is_palindrome("Boney M"))