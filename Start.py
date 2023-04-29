from DataClass import Data
from NotesClass import Notes


i = True
data = Data()
print('Список возможных команд: \nadd - добавить заметку;\nprint - вывод на экран заметку;\nprintall - вывести все заметки в хронологическом порядке\n'
      'save - сохранить файл\ndel - удалить заметку;\nedit - изменить заметку;\nexit - выход.')
while i:
    command = input("Введите команду: ")
    if command == 'add':
        data.data.append(Notes(len(data.data), input("Введите название заметки: ").replace(';', ''), input("Введите текст заметки: ").replace(';', ''), 0, 0, 0, 0, 0))
    elif command == 'printall':
        data.sortAlg()
        for j in data.data:
            j.printNotes()
    elif command == 'save':
        data.writeData()
    elif command == 'del':
        x = True
        while x:
            try:
                id = int(input('Введите id удаляемой заметки: '))
                data.delNotes(id)
                x = False
            except:
                print('Введите целое число, либо такого id не существует!')
    elif command == 'exit':
        i = False
    elif command == 'edit':
        x = True
        while x:
            try:
                id = int(input('Введите id заметки для редактирования: '))
                data.data[id].editNote(input('Введите новый текст: ').replace(';', ''))
                x = False
            except:
                print('Введите целое число, либо такого id не существует!')
    elif command == 'print':
        x = True
        while x:
            try:
                id = int(input('Введите id заметки для печати: '))
                data.data[id].printNotes()
                x = False
            except:
                print('Введите целое число, либо такого id не существует!')
