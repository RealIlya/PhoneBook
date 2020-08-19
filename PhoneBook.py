# === PhoneBook ===

# tel - номер телефона, строка
# first_name - имя, строка
# last_name - фамилия, строка
# patronymic - отчество, строка
# address - адрес, строка
# {tel: [last_name, first_name, patronymic, address]}

from PhoneBook_lib import *

phone_book = dict()

welcome()  # Ввод приветствия программы

while True:
    menu()  # Вывод пунктов меню
    choice = int(input("Ваш выбор: "))

    if choice == 1:  # Вывести телефонный справочник на экран
        show(phone_book)

    elif choice == 2:  # Добавить запись
        input_record(phone_book)

    elif choice == 3:  # Редактирование записи
        edit_record(phone_book)

    elif choice == 4:  # Удалить запись
        delete_record(phone_book)

    elif choice == 5:  # Сохранить в файл
        export_to_file(phone_book)

    elif choice == 0:  # Закрыть программу
        print("Оки-доки")
        break

    else:
        print("Не существует")
