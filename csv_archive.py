def add_to_archive(data):
    file = open('phone_numbers.csv', 'a')
    for i in data:
        file.write(f'{data[i]},')
    file.write("\n")
