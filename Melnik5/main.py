import re
import string


# Функція для сортування слів
def sort_words(words):
    return sorted(words, key=lambda word: word.lower())


# Функція для розподілу слів на українські та англійські
def split_words_by_language(words):
    ukrainian_words = []
    english_words = []
    for word in words:
        # Якщо слово містить лише українські літери
        if re.match(r'^[А-Яа-яЇїІіЄєҐґ]+$', word):
            ukrainian_words.append(word)
        # Якщо слово містить лише англійські літери
        elif re.match(r'^[A-Za-z]+$', word):
            english_words.append(word)
    return ukrainian_words, english_words


# Основна програма
def main():
    file_name = 'text.txt'
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            text = file.read()

            # Знаходимо перше речення (до першої крапки)
            first_sentence = text.split('.')[0]
            print("Перше речення:")
            print(first_sentence)

            # Видаляємо знаки пунктуації і розбиваємо на слова
            words = re.findall(r'\b\w+\b', first_sentence)

            # Розділяємо слова на українські та англійські
            ukrainian_words, english_words = split_words_by_language(words)

            # Сортуємо слова
            sorted_ukrainian_words = sort_words(ukrainian_words)
            sorted_english_words = sort_words(english_words)

            # Виводимо відсортовані слова і кількість слів
            print("\nВідсортовані українські слова:")
            print(' '.join(sorted_ukrainian_words))
            print("\nВідсортовані англійські слова:")
            print(' '.join(sorted_english_words))
            print("\nЗагальна кількість слів:", len(words))

    except FileNotFoundError:
        print(f"Помилка: файл {file_name} не знайдено.")
    except Exception as e:
        print(f"Помилка при обробці файлу: {e}")


if __name__ == "__main__":
    main()
