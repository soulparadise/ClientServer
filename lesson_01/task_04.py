'''
Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое
и выполнить обратное преобразование (используя методы encode и decode).
'''

words = ['разработка', 'администрирование', 'protocol', 'standart']
for word in words:
    word_encode = word.encode('utf-8')
    print(word, word_encode, type(word_encode))
    word_decode = bytes.decode(word_encode, 'utf-8')
    print(word_decode, type(word_decode))
    print('#' * 20)
