# === PhoneBook ===

# tel - номер телефона, строка
# first_name - имя, строка
# last_name - фамилия, строка
# patronymic - отчество, строка
# address - адрес, строка
# {tel: [last_name, first_name, patronymic, address]}

from PhoneBook_lib import *

phone_book = dict()

welcome()

while True:
    menu()
    choice = int(input("Ваш выбор: "))

    if choice == 1:
        print("")

    elif choice == 2:   # TODO Сделать проверку существования телефона в записи
        tel = input("Введите номер телефона")
        value = input_data()
        phone_book[tel] = value

    elif choice == 3:  # TODO Редактирование записи
        print()

    elif choice == 4:  # TODO Удаление записи
        print()

    elif choice == 0:
        print("Оки-доки")
        break

    else:
        print("Не существует")
        continue
