documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
    }


def shelf(doc_num):
    find_status = False
    for shelf in directories:
        if doc_num in directories[shelf]:
            print(f'Документ лежит на полке {shelf}.')
            find_status = True
    if find_status == False:
        print('Введенный документ не найден')


def people(doc_num):
    find_status = False
    for document in documents:
        if document['number'] == doc_num:
            print(document['name'])
            find_status = True
    if find_status == False:
        print('Введенный документ не найден')


def list():
    for document in documents:
        print(document['type'], document['number'], document['name'])


def add():
    doc_num = input('Введите номер документа: ')
    doc_type = input('Введите тип документа: ')
    doc_name = input('Введите имя владельца: ')
    shelf_num = input('Введите номер полки, на которой'
                      ' вы хотите расположить документ:')

    while shelf_num not in directories:
        shelf_list = []
        for shelf in directories:
            shelf_list.append(shelf)
            shelf_str = ', '.join(shelf_list)
        shelf_num = input(f'Введенный номер полки не найден. '
                          f'Пожалуйста, введите один из этих номеров: {shelf_str}')
    document = {'type': doc_type, 'number': doc_num, 'name': doc_name}
    documents.append(document)
    directories[shelf_num].append(doc_num)


while True:
    command = input('Введите команду: ')
    if command == 'q':
        print('Спасибо за ипользование терминала!')
        break
    elif command == 'p':
        doc_num = input('Введите номер документа: ')
        people(doc_num)
    elif command == 's':
        shelf_num = input('Введите номер документа: ')
        shelf(shelf_num)
    elif command == 'l':
        list()
    elif command == 'a':
        add()
    else:
        print('Неизвестная команда')
