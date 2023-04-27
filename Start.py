from DataClass import Data
from NotesClass import Notes



i = True
data = Data()

while i:
    command = input("Введите команду: ")
    if command == 'add':
        data.data.append(Notes(len(data.data), input("Введите название заметки: "), input("Введите текст заметки: "), 0, 0, 0, 0, 0))
    elif command == 'print':
        for j in data.data:
            j.printNotes()
    elif command == 'save':
        data.writeData()
    elif command == 'del':
        x = True
        while x:
            try:
                id = int(input('Введите id удаляемой заметки'))
            except:
                print('Введите целое число!')
    elif command == 'exit':
        i = False
