def count_vowels(s):
    # Определяем набор гласных букв
    vowels = 'aeiouAEIOU'
    count = 0

    # Проходим по каждому символу в строке
    for char in s:
        if char in vowels:
            count += 1

    return count


# Пример использования
# input_string = input("Введите строку: ")
# vowel_count = count_vowels(input_string)
# print(f"Количество гласных в строке: {vowel_count}")


