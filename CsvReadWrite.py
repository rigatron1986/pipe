import csv

file = 'D:/temp/asset.csv'

# write csv files

cfile = open(file, 'w')
for items in list:
    cfile.write(items + '\n')
cfile.close()

CsvFileReader = csv.reader(open(file, 'rb'), delimiter=',', quotechar='|')

defaultList = []
for column in CsvFileReader:
    print column[0]
    defaultList.append(column[0])
print defaultList
