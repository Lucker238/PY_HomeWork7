def add_family_name():
    return input('Введите фамилию: ')
    
def add_name():
    return input('Введите имя: ')

def add_phone_number():
    return input('Введите номер телефона: ')

def add_deskription():
    return input('Введите описание: ')

def create_cont():
    new_data = [add_family_name(), add_name(), add_phone_number(), add_deskription()]
    heading = ['Фамилия', 'Имя', 'Номер телефона', 'Описание']
    return dict(zip(heading, new_data))



