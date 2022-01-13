'''
Выполнить пинг веб-ресурсов yandex.ru, youtube.com
и преобразовать результаты из байтовового в строковый тип на кириллице.
'''

import subprocess

args = [['ping', 'google.com'], ['ping', 'yandex.ru']]

for el in args:

    subproc_ping = subprocess.Popen(el, stdout=subprocess.PIPE)

    for line in subproc_ping.stdout:
        line = line.decode('cp866').encode('utf-8')
        print(line.decode('utf-8'))
