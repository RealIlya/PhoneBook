version = "v.1.1"
straights = "=" * 23
straights2 = "-" * 23


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
    for tel in phone_book:
        value = phone_book[tel]
        temp = value[0] + " " + value[1] + " " + value[2] + ", " + value[3]
        print(tel, ':', temp)
