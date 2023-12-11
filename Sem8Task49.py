'''Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной'''

import csv
import os.path
from csv import DictReader, DictWriter


class LenNumberError(Exception):
    def __init__(self, txt):
        self.txt = txt


class NameError(Exception):
    def __init__(self, txt):
        self.txt = txt


class LastNameError(Exception):
    def __init__(self, txt):
        self.txt = txt


def get_info():
    is_valid_first_name = False
    while not is_valid_first_name:
        try:
            first_name = input("Введите имя:")
            if len(first_name) < 2:
                raise NameError("Не валидное имя")
            else:
                is_valid_first_name = True
        except NameError as err:
            print(err)
            continue

    is_valid_last_name = False
    while not is_valid_last_name:
        try:
            last_name = input("Введите Фамилию: ")
            if len(last_name) < 2:
                raise LastNameError("Не валидная фамилия")
            else:
                is_valid_last_name = True
        except LastNameError as err:
            print(err)
            continue

    is_valid_phone = False
    while not is_valid_phone:
        try:
            phone_number = int(input('Введите номер: '))
            if len(str(phone_number)) != 11:
                raise LenNumberError('Неверная длина номера')
            else:
                is_valid_phone = True
        except ValueError:
            print("Не валидный номер!")
            continue
        except LenNumberError as err:
            print(err)
            continue
    return [first_name, last_name, phone_number]


def create_file(file_name):
    # with - Менеджер контекста
    with open(file_name, "w", encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()


def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as data:
        f_reader = DictReader(data)
        return list(f_reader)


def write_file(file_name, lst):
    res = read_file(file_name)
    obj = {"Имя": lst[0], 'Фамилия': lst[1], 'Телефон': lst[2]}
    res.append(obj)
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()
        f_writer.writerows(res)

def find_in_file(file_name, obj):
    res = read_file(file_name)
    for item in res:
        if obj in item.values():
            print(item)

def copy_data(file_to_copy,file_name,line):
    res = read_file(file_name)
    data=res[line]
    f_c=open(file_to_copy, "a",encoding='utf-8')
    f_c.write(str(data)+'\n')
    f_c.close()


file_name = 'phone.csv'


def main():
    while True:
        command = input("Введите команду: ")
        if command == 'q':
            break
        elif command == 'w':
            if not os.path.exists(file_name):
                create_file(file_name)
            write_file(file_name, get_info())
        elif command == 'r':
            if not os.path.exists(file_name):
                print('Файл отсутствует. Создайте его')
                continue
            print(*read_file(file_name), sep = "\n")
            # поиск элементов по фамилии
        elif command == 'f':
            second_name_to_serch = input("Введите Фамилию для поиска: ")
            print("Результаты поиска:")
            find_in_file(file_name, second_name_to_serch)
            # Копирование строки с заданным номером из исходного файла в новый
        elif command == 'c':
            file_to_copy = input("Укажите имя файла куда копировать данные: ")
            if not os.path.exists(file_to_copy):
                create_file(file_to_copy)
            line=int(input("Укажите номер строки для копирования: "))
            copy_data(file_to_copy, file_name, line)


main()
