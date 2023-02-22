filename = 'new_phonebook.txt'

def add_contact():
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    phone_number = input('Введите номер телефона: ')
    phonebook = last_name +' ' + first_name + ' ' + phone_number + ' '
    with open('new_phonebook.txt', 'a',) as file:
        file.write(phonebook)
        file.write('\n')
           
def all_contacts():
    with open('new_phonebook.txt', 'r') as file:
        contacts = file.read()
        print(contacts)
        
def find_contact():
    contact = input('Введите имя для поиска: ')
    with open('new_phonebook.txt', 'r') as file:
        for line in file:
            if contact in line:
                print(line)
          
def del_contact():
    contact = input('Введите имя для удаления: ')
    with open('new_phonebook.txt', 'r') as file:
        lines = file.readlines()
    with open('new_phonebook.txt', 'w') as file:
        for line in lines:
            if contact not in line:
                file.write(line)

def chg_contact():
    old_name = input('Введите изменяемое имя: ')
    new_name = input('Введите новое имя: ')
    with open('new_phonebook.txt', 'r') as file:
        lines = file.read()
        lines = lines.replace(old_name, new_name, 1)
    with open('new_phonebook.txt', 'w') as file:
        file.write(lines)

def main():
    while True:
        print('\nТелефонный справочник')
        print('1. Добавить контакт')
        print('2. Найти контакт')
        print('3. Показать все контакты')
        print('4. Удалить контакт')
        print('5. Изменить контакт')
        print('6. Выход')
        choice = input('Выберите действие: ')
        if choice == '1':
            add_contact()
        elif choice == '2':
            find_contact()
        elif choice == '3':
            all_contacts()
        elif choice == '4':
            del_contact()
        elif choice == '5':
            chg_contact()
        elif choice == '6':
            break
        else:
            print('Некорректный выбор')

main()