import view as v

def find_by_family():
    name = input('Введите фамилию: ')
    for contact in v.catalog:
        if name in contact.values():
            return contact
    return 'Нет контакта с таким именем.'


def find_by_number():
    number = input('Введите номер: ')
    for contact in v.catalog:
        if number in contact.values():
            return contact
    return 'Нет контакта с таким номером.'

