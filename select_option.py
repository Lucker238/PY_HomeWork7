import view as v
import find_contact as fc
import create_contact as cc
import txt_archive as ta
import csv_archive as ca

def lets_get_it_started():
    check = True
    while check:
        v.show_menu()
        temp = input('Введите опцию: ')
        if temp == '1':
            v.show_catalog()
        elif temp == '2':
            print(fc.find_by_family())
        elif temp == '3':
            print(fc.find_by_number())
        elif temp == '4':
            data = cc.create_cont()
            ca.add_to_archive(data)
        elif temp == '5':
            ta.create_txt_file()
        elif temp == '6':
            check = False
        else:
            print("Вы ввели что то не то, попробуйте еще раз")

