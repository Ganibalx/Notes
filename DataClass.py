from NotesClass import Notes


class Data:

    def __init__(self):
        data = open('Data.csv', 'r')
        file = data.read()
        if len(file) < 2:
            self.data = []*1
        else:
            list = file.split('\n')
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

    def delNotes(self, id):
        del self.data[id]
        for i in range(0, len(self.data)):
            self.data[i].setId(i)

    def sortAlg(self):
        for i in range(0, len(self.data)-1):
            for j in range(i+1, len(self.data)):
                if int(self.data[i].dataConvert()) > int(self.data[j].dataConvert()):
                    self.data[i], self.data[j] = self.data[j], self.data[i]
        for i in range(0, len(self.data)):
            self.data[i].setId(i)


