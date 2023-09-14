from datetime import datetime
path: str = 'notes.csv'

count = 0
def counter():
    global count
    count += 1
    return count

class Note:
    def __init__(self, id=str(counter()), title="текст", body="текст",
                 date=str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))):
        self.id = id
        self.title = title
        self.body = body
        self.date = date

    def get_id(note):
        return note.id

    def get_title(note):
        return note.title

    def get_body(note):
        return note.body

    def get_date(note):
        return note.date

    def set_id(note):
        note.id = str(counter())

    def set_title(note):
        note.title = note

    def set_body(note):
        note.body = note

    def set_date(note):
        note.date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

    def to_string(note):
        return note.id + ';' + note.title + ';' + note.body + ';' + note.date

    def map_note(note):
        return '\nID: ' + note.id + '\n' + 'Название: ' + note.title + '\n' + 'Описание: ' + note.body + '\n' + 'Дата публикации: ' + note.date

def read_file():
    try:
        array = []
        file = open(path, "r", encoding='utf-8')
        notes = file.read().strip().split("\n")
        for n in notes:
            split_n = n.split(';')
            note = Note(
                id = split_n[0], title = split_n[1], body = split_n[2], date = split_n[3])
            array.append(note)
    except Exception:
        print('журнал заметок пустой')
    finally:
        return array
    
def write_file(array, mode):
    file = open(path, mode='w', encoding='utf-8')
    file.seek(0)
    file.close()
    file = open(path, mode=mode, encoding='utf-8')
    for notes in array:
        file.write(Note.to_string(notes))
        file.write('\n')
    file.close


def show_All():
    print("ЖУРНАЛ ЗАМЕТОК:")
    array_notes = read_file()
    for i in array_notes:
        print(Note.map_note(i))

def show_All_ID():
    array_notes = read_file()
    for i in array_notes:
        print("ID: ", Note.get_id(i))
    id = input("\nВведите id заметки: ")
    flag = True
    for i in array_notes:
        if id == Note.get_id(i):
            print(Note.map_note(i))
            flag = False
    if flag:
        print("Нет такого ID")

def show_All_Date():
    array_notes = read_file()
    date = input("Введите дату в формате: dd.mm.yyyy: ")
    flag = True
    for i in array_notes:
        date_note = str(Note.get_date(i))
        if date == date_note[:10]:
            print(Note.map_note(i))
            flag = False
        if flag:
            print("Нет такой даты")

def add_note():
    
    title = input("Введите заголовок заметки:\n")
    body = input("Введите описание заметки:\n")
    note = Note(title=title, body=body)
    array_notes = read_file()
    for i in array_notes:
        if Note.get_id(note) == Note.get_id(i):
            Note.set_id(note)
    array_notes.append(note)
    write_file(array_notes, 'a')
    print("Заметка добавлена в журнал!")


def change_note():
    id = input("Введите ID изменяемой заметки: ")
    array_notes = read_file()
    flag = True
    array_notes_new = []
    for i in array_notes:
        if id == Note.get_id(i):
            i.title = input("измените  заголовок:\n")
            i.body = input("измените  описание:\n")
            Note.set_date(i)
            logic = False
        array_notes_new.append(i)

    if flag:
        write_file(array_notes_new, 'a')
        print("Заметка с id: ", id, " успешно изменена!")
    else:
        print("нет такого id")

def del_notes():
    id = input("Введите ID удаляемой заметки: ")
    array_notes = read_file()
    flag = False

    for i in array_notes:
        if id == Note.get_id(i):
            array_notes.remove(i)
            flag = True

    if flag:
        write_file(array_notes, 'a')
        print("Заметка с id: ", id, " успешно удалена!")
    else:
        print("нет такого id")

def read_file():
    try:
        array = []
        file = open("notes.csv", "r", encoding='utf-8')
        notes = file.read().strip().split("\n")
        for n in notes:
            split_n = n.split(';')
            note = Note(
                id = split_n[0], title = split_n[1], body = split_n[2], date = split_n[3])
            array.append(note)
    except Exception:
        print('журнал заметок пустой')
    finally:
        return array

def menu() -> int:
    main_menu = '''Главное меню ЗАМЕТКИ:
    1. Показать все заметки
    2. Добавить заметку
    3. Показать заметки по id
    4. Выбор заметки по дате
    5. Изменить заметку
    6. Удалить заметку
    7.Выход'''
    print(main_menu)
    while True:
        select = input('Выберите пункт меню: ')
        if select.isdigit() and 0 < int(select) < 8:
            return int(select)
        print('Ошибка ввода, введите ЧИСЛО от 1 до 7')


while True:
    select = menu()
    match select:
        case 1:
            show_All()
        case 2:
            add_note()
        case 3:
            show_All_ID()
        case 4:
            show_All_Date()
        case 5:
            show_All()
            change_note()
        case 6:
            show_All()
            del_notes()
        case 7:
            print('До свидания! До новых встреч')
            break
