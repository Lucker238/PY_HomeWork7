import view as v

def create_txt_file():
    file = open('phone_numbers.txt', 'w')
    for i in v.catalog:
        for j in i:
            file.write(f'{i}: {i[j]}\n')
        file.write('\n')
    print('Текстовый файл создан!')


