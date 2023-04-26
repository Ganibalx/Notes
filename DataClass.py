class Data:

    def __init__(self):
        data = open('Data.csv', 'r')
        file = data.read()
        if len(file) < 10:
            self.data = []
        else:
            list = file.split('/n')
            self.data = []
            for i in list:
                self.data.append(i.split(';'))
        data.close()

    def writeData(self):
        data = open('Data.csv', 'a')
        data.writelines('тестовая строка 4\n')
        data.close()