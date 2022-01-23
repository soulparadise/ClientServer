"""
Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из файлов
info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:

a. Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание
данных. В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы»,  «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно получиться четыре списка — например,
os_prod_list, os_name_list, os_code_list, os_type_list. В этой же функции создать главный список для хранения
данных отчета — например, main_data — и поместить в него названия столбцов отчета в виде списка:
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);

b. Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение данных
через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;

c. Проверить работу программы через вызов функции write_to_csv().
"""

import csv

request_result = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
file_list = ['info_1.txt', 'info_2.txt', 'info_3.txt']


def create_list(file_name):
    with open(file_name, 'r', encoding='windows-1251') as f_obj:
        file_data = f_obj.read().split('\n')
        file_data_split = []
        for el in file_data:
            file_data_split.append(el.split(':'))
        result_dict = {}
        for el in file_data_split:
            if el[0] in request_result:
                result_dict[el[0]] = el[1].strip()
    return result_dict


def get_data(file_list):
    os_prod_list, os_name_list, os_code_list, os_type_list, main_data = [], [], [], [], []
    main_data.append(request_result)
    for el in file_list:
        temp_dict = create_list(el)
        for dict_key in temp_dict:
            if dict_key == request_result[0]:
                os_prod_list.append(temp_dict[dict_key])
            elif dict_key == request_result[1]:
                os_name_list.append(temp_dict[dict_key])
            elif dict_key == request_result[2]:
                os_code_list.append(temp_dict[dict_key])
            elif dict_key == request_result[3]:
                os_type_list.append(temp_dict[dict_key])
        main_data.append([os_prod_list[-1], os_name_list[-1], os_code_list[-1], os_type_list[-1]])
    return main_data


def write_to_csv(file_name, file_list):
    with open(file_name, 'w', encoding='utf-8') as f_obj:
        csv_data = csv.writer(f_obj)
        for row in get_data(file_list):
            csv_data.writerow(row)
            print(row)


write_to_csv('kek.csv', file_list)
