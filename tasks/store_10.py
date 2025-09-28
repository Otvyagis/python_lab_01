def store():
    goods = {
        'Лампа': '12345',
        'Стол': '23456',
        'Диван': '34567',
        'Стул': '45678',
    }

    store = {
        '12345': [
            {'quantity': 27, 'price': 42},
        ],
        '23456': [
            {'quantity': 22, 'price': 510},
            {'quantity': 32, 'price': 520},
        ],
        '34567': [
            {'quantity': 2, 'price': 1200},
            {'quantity': 1, 'price': 1150},
        ],
        '45678': [
            {'quantity': 50, 'price': 100},
            {'quantity': 12, 'price': 95},
            {'quantity': 43, 'price': 97},
        ],
    }

    lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
    lamp_code = goods['Лампа']
    lamps_item = store[lamp_code][0]
    lamps_quantity = lamps_item['quantity']
    lamps_price = lamps_item['price']
    lamps_cost = lamps_quantity * lamps_price
    print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

    table_code = goods['Стол']
    table_quantity = store[table_code][0]['quantity'] + store[table_code][1]['quantity']
    table_cost = store[table_code][0]['quantity'] * store[table_code][0]['price'] + \
                store[table_code][1]['quantity'] * store[table_code][1]['price']
    print('Стол -', table_quantity, 'шт, стоимость', table_cost, 'руб')

    sofa_code = goods['Диван']
    sofa_quantity = store[sofa_code][0]['quantity'] + store[sofa_code][1]['quantity']
    sofa_cost = store[sofa_code][0]['quantity'] * store[sofa_code][0]['price'] + \
                store[sofa_code][1]['quantity'] * store[sofa_code][1]['price']
    print('Диван -', sofa_quantity, 'шт, стоимость', sofa_cost, 'руб')

    chair_code = goods['Стул']
    chair_quantity = store[chair_code][0]['quantity'] + store[chair_code][1]['quantity'] + store[chair_code][2]['quantity']
    chair_cost = store[chair_code][0]['quantity'] * store[chair_code][0]['price'] + \
                store[chair_code][1]['quantity'] * store[chair_code][1]['price'] + \
                store[chair_code][2]['quantity'] * store[chair_code][2]['price']
    print('Стул -', chair_quantity, 'шт, стоимость', chair_cost, 'руб')
store()