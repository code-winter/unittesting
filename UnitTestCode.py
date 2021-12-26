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


def get_person(docs, doc_num):
    # doc_number = input("Введите номер документа: ")
    for person in docs:
        if person["number"] == doc_num:
            # print(f'Документ принадлежит человеку, с именем {person["name"]}')
            return 'OK'
    err_msg = "Документ не найден, введите заново."
    return err_msg


def get_shelf(dir_list):
    while True:
        doc_number = input("Введите номер документа: ")
        for dir_key, dir_value in dir_list.items():
            for val in dir_value:
                if val == doc_number:
                    print(f'Документ лежит на полке номер {dir_key}')
                    return
        print("Документ не найден, введите заново.")


def print_doc(doc_list):
    for person in doc_list:
        for doc_key, doc_value in person.items():
            print(doc_value, end=' ')
        print()


def add_doc(docs, dirs, doc_type, doc_number, doc_name, dir_number):
    while True:
        # doc_type = input('Введите тип документа: ')
        # doc_number = input('Введите номер документа: ')
        # doc_name = input('Введите имя и фамилию человека: ')
        # dir_number = input('Введите номер полки: ')
        for dir_keys, dir_values in dirs.items():
            if dir_keys == dir_number:
                docs.append({'type': doc_type, 'number': doc_number, 'name': doc_name})
                dir_values.append(doc_number)
                return docs[-1]
        err_msg = 'Такой полки не существуйте, попробуйте снова.'
        return err_msg


def delete_doc(docs, dirs, doc_number):
    # doc_number = input("Введите номер документа: ")
    for list_id, person in enumerate(docs):
        if doc_number in person.values():
            if person["number"] == doc_number:
                for dir_key, dir_value in dirs.items():
                    for elem_value in dir_value:
                        if elem_value == doc_number:
                            dir_value.remove(elem_value)
                            docs.pop(list_id)
                            msg = 'OK'
                            return msg
    err_msg = 'Документ не найден, введите заново'
    return err_msg


def move_docs():
    while True:
        doc_number = input('Введите номер документа: ')
        shelf_number = input('Введите номер полки для перемещения: ')
        if directories.get(shelf_number) != None:
            for shelf, docs in directories.items():
                for item in docs:
                    if item == doc_number:
                        docs.remove(item)
                        directories[shelf_number].append(doc_number)
                        return
            print("Документ не найден, введите заново")
        else:
            print("Полка не существует, введите существующий номер полки")


def add_shelf():
    while True:
        shelf_num = input("Введите номер полки, который нужно добавить: ")
        if shelf_num not in directories.keys():
            directories.setdefault(shelf_num, list())
            return
        else:
            print("Полка уже существует, введите другой номер")


def main():
    print("Здравствуйте! Что вы хотите сделать?")
    while True:
        print()
        print("Доступные команды: p, s, l, a, d, m, as, help, doc, dir, quit,")
        command_str = input("Введите команду: ")
        print()
        if command_str.lower() == 'help':
            print(
                "Справка: \n p: Найти человека по номеру документа \n s: Найти номер полки по номеру документа \n l: Вывести информацию по документам \n a: Добавить новую запись в перечень документов и в список полок \n d: Удалить запись из перечня документов и списка полок \n m: Переместить документ на другую полку \n as: Добавить в список полок новую полку \n help: Вывести справку по командам \n doc: Вывести информацию по документам (debug) \n dir: Вывести информацию по полкам (debug) \n quit: Завершить работу программы")

        if command_str.lower() == 'doc':
            for person in documents:
                for person_key, person_value in person.items():
                    print(f'[{person_key}: {person_value}]', end=' ')
                print()

        if command_str.lower() == 'dir':
            for shelf, number in directories.items():
                print(f'{shelf}: {number}')

        if command_str.lower() == 'p':
            get_person(documents)

        if command_str.lower() == 's':
            get_shelf(directories)

        if command_str.lower() == 'l':
            print_doc(documents)

        if command_str.lower() == 'a':
            add_doc()

        if command_str.lower() == 'd':
            delete_doc()

        if command_str.lower() == 'm':
            move_docs()

        if command_str.lower() == 'as':
            add_shelf()

        if command_str.lower() == 'quit':
            print("Всего доброго! Завершаю работу.")
            break


if __name__ == '__main__':
    main()
