"""
Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
"""

words = ['attribute', 'класс', 'функция', 'type']

for word in words:
    try:
        byte_word = word.encode('ascII')
        print(f"{byte_word} - {word}")
    except:
        print(f"{word}  - невозможно записать в байтовом типе")
