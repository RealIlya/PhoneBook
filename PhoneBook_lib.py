import os

version = "v.1.1"
straights = "=" * 23
straights2 = "-" * 23


def welcome():
    print("=== PhoneBook", version, "===")
    print(straights)


def menu():
    print("Режимы работы: \n"
          "1. Вывести телефонный справочник на экран \n"
          "2. Добавить запись \n"
          "3. Редактировать запись \n"
          "4. Удалить запись \n"
          "5. Сохранить в файл \n"
          "0. БАН (Закрыть программу)")
    print(straights)


def show(phone_book):
    os.system('cls')
    print("=== Телефонный справочник ===")
    for tel in phone_book:
        value = phone_book[tel]
        temp = value[0] + " " + value[1] + " " + value[2] + ", " + value[3]
        print(tel, ':', temp)
        print(straights)


def input_data():
    temp = list()

    first_name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    patronymic = input("Введите отчество: ")
    address = input("Введите адрес: ")
    temp.append(last_name)
    temp.append(first_name)
    temp.append(patronymic)
    temp.append(address)
    return temp


def input_record(phone_book):
    tel = input("Введите номер телефона: ")
    if tel in phone_book:
        print("Такой номер уже существует")
    else:
        value = input_data()
        phone_book[tel] = value
        print("### Запись успешно добавлена ###")


def edit_record(phone_book):
    tel = input("Введите номер телефона: ")
    if tel in phone_book:
        temp = input_data()
        phone_book[tel] = temp
    else:
        print("Введенного номера не существует")


def delete_record(phone_book):
    tel = input("Введите номер телефона для удаления: ")
    if tel in phone_book:
        note = phone_book.pop(tel)
        print(f"### Запись {note} удалена ###")
    else:
        print("Введенного номера не существует")


def export_to_file(phone_book):
    with open("PhoneBook.csv", "w") as file:
        for tel in phone_book:
            value = phone_book[tel]
            temp = tel + ";" + value[0] + ";" + value[1] + ";" + value[2] + ";" + value[3] + "\n"
            file.write(temp)
