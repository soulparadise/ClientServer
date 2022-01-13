"""
1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и
содержание соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые
представление в формат Unicode и также проверить тип и содержимое переменных.
"""

word_1, word_2, word_3 = "разработка", "сокет", "декоратор"

print(f"word_1: {word_1}, type: {type(word_1)}\n"
      f"word_2: {word_2}, type: {type(word_2)}\n"
      f"word_3: {word_3}, type: {type(word_3)}")

word_1, word_2, word_3 = "\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430", \
                         "\u0441\u043e\u043a\u0435\u0442", \
                         "\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440"

print(f"word_1: {word_1}, type: {type(word_1)}\n"
      f"word_2: {word_2}, type: {type(word_2)}\n"
      f"word_3: {word_3}, type: {type(word_3)}")
