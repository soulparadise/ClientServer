"""
Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах.
Написать скрипт, автоматизирующий его заполнение данными. Для этого:

a. Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity),
цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря
в файл orders.json. При записи данных указать величину отступа в 4 пробельных символа;

b. Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
"""
import json


def write_order_to_json(item, quantity, price, buyer, date):
    old_data = dict()
    try:
        with open('orders.json', 'r') as json_obj:
            old_data = json.load(json_obj)
    except json.decoder.JSONDecodeError:
        with open('orders.json', 'w') as json_obj:
            json.dump({}, json_obj, indent=4)
    if not 'orders' in old_data:
        old_data['orders'] = []
    old_data['orders'].append({
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date
    })

    with open('orders.json', 'w') as json_obj:
        json.dump(old_data, json_obj, indent=4)


write_order_to_json('Blizzard', 1, 123, 'Microsoft', '18.01.2022')
