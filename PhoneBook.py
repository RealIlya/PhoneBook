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

menu()
choice = int(input("Ваш выбор: "))

if choice == 1:
    print("")
elif choice == 2:
    tel = input("Введите номер телефона")
    value = input_data()

    phone_book[tel] = value

elif choice == 3:  # TODO Редактирование записи
    print()
elif choice == 4:  # TODO Удаление записи
    print()
elif choice == 0:  # TODO Выход из программы
    print()
else:
    print("Не существует")

value = list()

print(phone_book)
