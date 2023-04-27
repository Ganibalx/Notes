from NotesClass import Notes


class Data:

    def __init__(self):
        data = open('Data.csv', 'r')
        file = data.read()
        if len(file) < 10:
            self.data = []*1
        else:
            list = file.split('/n')
            self.data = []
            for i in range(0, len(list)):
                if len(list[i]) > 0:
                    per = list[i].split(';')
                    self.data.append(Notes(i, per[1], per[2], per[3], per[4], per[5], per[6], per[7]))
        data.close()

    def writeData(self):
        data = open('Data.csv', 'w')
        for i in range(0, len(self.data)):
            data.writelines(self.data[i].toStringNotes(i))
        data.close()