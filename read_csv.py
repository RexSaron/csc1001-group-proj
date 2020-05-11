class Read:
    def __init__(self,filename = 'train.csv'):
        self.filename = filename

    def loadCsv(self):
        csvFile = open(self.filename, 'r', encoding="UTF-8-sig",)

        nested_list = csvFile.readlines()
        nested_list.remove(nested_list[0])
        
        for lines in range(len(nested_list)):
            nested_list[lines] = nested_list[lines].split(', ')
            nested_list[lines][-1] = nested_list[lines][-1][0]
            
            for data in range(len(nested_list[lines])):
                nested_list[lines][data] = float(nested_list[lines][data])

        return nested_list

R = Read()
print(R.loadCsv())
