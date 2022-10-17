def show_menu():
    print("\nВыберите необходимое действие:\n"
    "1. Отобразить весь справочник\n"
    "2. Найти абонента по фамилии\n"
    "3. Найти абонента по номеру телефона\n"
    "4. Добавить абонента в справочник\n"
    "5. Сохранить справочник в текстовом формате\n"
    "6. Закончить работу")


def read_csv():
    catalog = list()
    heading = ['Фамилия', 'Имя', 'Номер телефона', 'Описание']
    with open('phone_numbers.csv','r') as file:
        for string in file:
            contact = dict(zip(heading, string[:-1].split(',')))
            catalog.append(contact)
    return catalog

catalog = read_csv()

def show_catalog():
    global catalog
    for i in catalog:
        print(i)

