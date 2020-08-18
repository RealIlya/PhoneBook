# *** PhoneBook ***
#
# tel - номер телефона, строка
# first_name - имя, строка
# last_name - фамилия, строка
# patronymic - отчество, строка
# address - адрес, строка
# {tel: [last_name, first_name, patronymic, address]}

phone_book = dict()
value = list()

tel = input("Введите номер телефона: ")
first_name = input("Введите имя: ")
last_name = input("Введите фамилию: ")
patronymic = input("Введите отчество: ")
address = input("Введите адрес: ")

value.append(last_name)
value.append(first_name)
value.append(patronymic)
value.append(address)

phone_book[tel] = value

print(phone_book)