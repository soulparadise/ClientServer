'''
Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое.
'''
import locale

words = ['сетевое программирование', 'сокет', 'декоратор']

with open('test_file.txt', 'w+') as f_obj:
    for el in words:
        f_obj.write(el + '\n')

    f_obj.seek(0)

    print(f_obj)

def_coding = locale.getpreferredencoding()

print(def_coding)

with open('test_file.txt', encoding=def_coding) as f_obj:
    print(f_obj.read())
with open('test_file.txt', encoding='utf-8', errors='replace') as f_obj:
    print(f_obj.read())
