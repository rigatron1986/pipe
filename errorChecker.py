import os


def errorCheck(write, name='logReport'):
    towriteDest = 'C:/temp/errorCheck/'
    if not os.path.exists(towriteDest):
        os.makedirs(towriteDest)

    toWriteFile = open(towriteDest + name + '.csv', 'a')
    toWriteFile.write('\n' + write)
    toWriteFile.close()
