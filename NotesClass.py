from datetime import datetime


class Notes:

    def __init__(self, id, name, text, year, month, day, hour, minute):
        self.id = id
        self.name = name
        self.text = text
        self.date = [0]*5
        if year == 0:
            self.date[0] = datetime.now().year
            self.date[1] = datetime.now().month
            self.date[2] = datetime.now().day
            self.date[3] = datetime.now().hour
            self.date[4] = datetime.now().minute
        else:
            self.date[0] = year
            self.date[1] = month
            self.date[2] = day
            self.date[3] = hour
            self.date[4] = minute

    def printNotes(self):
        print(f'{self.id}\t{self.name}\n'
              f'{self.text}\n'
              f'{self.date[0]}.{self.date[1]}.{self.date[2]} {self.date[3]}:{self.date[4]}\n\n')

    def toStringNotes(self, id):
        return f'{id};{self.name};{self.text};{self.date[0]};{self.date[1]};{self.date[2]};{self.date[3]};{self.date[4]}\n'

    def editNote(self, text):
        self.text = text
        self.date[0] = datetime.now().year
        self.date[1] = datetime.now().month
        self.date[2] = datetime.now().day
        self.date[3] = datetime.now().hour
        self.date[4] = datetime.now().minute

    def setId(self, id):
        self.id = id

    def dataConvert(self):
        rez = str(self.date[0])
        for i in range(1, len(self.date)):
            if len(str(self.date[i])) == 1:
                rez = rez + '0' +str(self.date[i])
            else:
                rez = rez + str(self.date[i])
        return rez

