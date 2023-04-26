from datetime import datetime


class Notes():

    def __init__(self, id, name, text):
        self.id = id
        self.name = name
        self.text = text
        self.date = datetime.now()

    def printNotes(self):
        print(f'{self.id}\t{self.name}\n'
              f'{self.text}\n'
              f'{self.date.year}.{self.date.month}.{self.date.day} {self.date.hour}:{self.date.minute}\n\n')

    def editNote(self, text):
        self.text = text
        self.date = datetime.now()

