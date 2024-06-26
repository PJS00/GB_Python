def work_with_phonebook():
    choice = show_menu()
    phone_book = read_txt('phon.txt')
    while (choice != 9):
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            last_name = input('Введите фамилию: ')
            print(find_by_lastname(phone_book, last_name))
        elif choice == 3:
            number = input('Введите номер телефона: ')
            print(find_by_number(phone_book, number))
        elif choice == 4:
            user_data = input('Введите данные нового абонента через пробел: ')
            add_user(phone_book, user_data)
        elif choice == 5:
            last_name = input('Введите фамилию: ')
            new_number = input('Введите новый номер телефона: ')
            phone_book = change_number(phone_book, last_name, new_number)
        elif choice == 6:
            last_name = input('Введите фамилию: ')
            phone_book = delete_by_lastname(phone_book, last_name)
        elif choice == 7:
            write_txt('phon.txt', phone_book)
        elif choice == 8:
            line_number = int(input("Введите номер строки для копирования: "))
            filename_destination = input("Введите имя файла назначения: ")
            copy_line_to_file(phone_book, line_number, filename_destination)
            print("Данные успешно скопированы.")
            # input("Press Enter to continue...")

        choice = show_menu()


phonbook_keys = ['Фамилия', 'Имя', 'Телефон', 'Описание']


def print_result(data):
    '''эта функция должна распечатывать phone_book в читаемый вид'''
    # print('\t'.join(list(data[0].keys())))
    print(
        f"{phonbook_keys[0]:<15}{phonbook_keys[1]:<15}{phonbook_keys[2]:<15}{phonbook_keys[3]}")
    for user_data in data:
        # print('\t'.join(user_data.values()))
        print(f"{user_data.get('Фамилия'):<15}{user_data.get('Имя'):<15}{user_data.get('Телефон'):<15}{user_data.get('Описание')}")


def find_by_lastname(data, last_name):
    '''Найти абонента по фамилии'''
    for user_data in data:
        if user_data['Фамилия'] == last_name:
            return user_data


def find_by_number(data, number):
    '''Найти абонента по номеру телефона'''
    for user_data in data:
        if user_data['Телефон'] == number:
            return user_data


def add_user(data, new_user_data):
    '''Добавить абонента в справочник'''
    phonbook_keys = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    new_user = dict(zip(phonbook_keys, new_user_data.split()))
    data.append(new_user)
    return data


def change_number(data, last_name, new_number):
    '''изменить номер телефона'''
    for i in range(len(data)):
        if data[i]['Фамилия'] == last_name:
            data[i]['Телефон'] = new_number
    return data


def delete_by_lastname(data, last_name):
    '''удалить по фамилии'''
    for i in range(len(data)):
        if data[i]['Фамилия'] == last_name:
            data.pop(i)
            return data

def copy_line_to_file(phone_book, line_number, filename_destination):
    if 1 <= line_number <= len(phone_book):
        entry = phone_book[line_number - 1]
        with open(filename_destination, "a", encoding="utf-8") as file:
            file.write(
                f"{entry['Фамилия']:<15}{entry['Имя']:<15}{entry['Телефон']:<15}{entry['Описание']}\n"
            )
    else:
        print("Неверный номер строки.")

def show_menu():
    print("\n Выберите необходимое действие:\n",
          "1. Отобразить весь справочник\n",
          "2. Найти абонента по фамилии\n",
          "3. Найти абонента по номеру телефона\n",
          "4. Добавить абонента в справочник\n",
          "5. Изменить номер телефона абонента\n",
          "6. Удалить абонента по фамилии\n",
          "7. Сохранить справочник в текстовом формате\n",
          "8. Копировать данные из одного файла в другой\n",
          "9. Закончить работу")
    choice = int(input(">> "))
    return choice


def read_txt(filename):
    '''считать данные из файла txt'''
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line[:-1].split(',')))
            phone_book.append(record)
    return phone_book


def write_txt(filename, phone_book):
    '''Сохранить справочник в текстовом формате'''
    with open(filename, 'w', encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s = ''
            for v in phone_book[i].values():
                s = s + v + ','
            phout.write(f'{s[:-1]}\n')


if __name__ == "__main__":
    work_with_phonebook()


