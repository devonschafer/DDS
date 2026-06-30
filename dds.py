#DevonDataStructure
#v1.0.0
import os


class DDS():

    virtual_filename = 'apptitle::DDS V1,,v2,,v3,,v4,,v5'
    
    def readFile(filename, option, values):
        openFile = open(filename, 'r')
        if option == 'all' and values == None:
            readFile = openFile.read()
            return readFile
        openFile.close()

    def returnLine(filename, option, values):
        openFile = open(filename, 'r')
        if isinstance(option, int) and values == None:
            line = openFile.readlines()
            return line[option-1]
        openFile.close()

    def returnKey(filename, option, values):
        openFile = open(filename, 'r')
        if isinstance(option, str) and values == 'key':
            line = openFile.readlines()
            for lines in line:
                if option in lines:
                    value = lines.split('::')
                    return value[0]
        elif isinstance(option, int) and values == 'key':
            line = openFile.readlines()
            line = line[option-1].split('::')
            return line[0]
        openFile.close()

    def returnMultipleKeys(filename, option, values):
        openFile = open(filename, 'r')
        if isinstance(option, tuple) and 0 not in option and values == 'key':
            i = []
            line = openFile.readlines()
            for k in range((option[0]-1), option[1]):
                skey = line[k].split('::')
                i.append(skey[0])
            return i
        openFile.close()

    def returnValue(filename, option, values):
        openFile = open(filename, 'r')
        if isinstance(option, str) and values == 'value':
            line = openFile.readlines()
            for lines in line:
                if lines.startswith(option):
                    value = lines.split('::')
                    return value[1]
        elif isinstance(option, int) and values == 'value':
            line = openFile.readlines()
            line = line[option-1].split('::')
            return line[1]
        openFile.close()

    def valuesToList(filename, option, values):
        openFile = open(filename, 'r')
        if isinstance(option, int) and values == 'value':
            line = openFile.readlines()
            line = line[option-1].split('::')
            v = line[1].split(',,')
            return v
        openFile.close()

    def returnSpecificValue(filename, option, values):
        openFile = open(filename, 'r')
        if isinstance(option, tuple) and values == 'value':
            line = openFile.readlines()
            line = line[option[0]-1].split('::')
            opt = line[1].split(',,')
            return opt[option[1]-1]
        openFile.close()

    def appendFile(filename, option, values):
        saveFile = open(filename, 'a')
        if isinstance(option, str) and values == 'save':
            saveFile.write('\n%s' % option)
        saveFile.close()

    def virtualFile(filename, option, values):
        if option == None and values == 'key':
            return filename.split('::')[0]
        elif isinstance(option, int) and values == 'value':
            line = filename.split('::')[1]
            opt = line.split(',,')
            return opt[option-1]
        elif option == None and values == 'value':
            return filename.split('::')[1]

            
#t = DDS.readFile('testdata.dds', 'all', None)
#t = DDS.returnLine('testdata.dds', 3, None)
#t = DDS.returnKey('testdata.dds', 3, 'key')
#t = DDS.returnKey('testdata.dds', 'This works', 'key')
#t = DDS.returnMultipleKeys('testdata.dds', (1,8), 'key')
#t = DDS.returnValue('testdata.dds', 3, 'value')
#t = DDS.returnValue('testdata.dds', 'latte', 'value')
#t = DDS.valuesToList('testdata.dds', 3, 'value')
#t = DDS.returnSpecificValue('testdata.dds', (3,4), 'value')
#t = DDS.appendFile('testdata.dds', 'Testing Again::This is working', 'save')
#t = DDS.searchByKey('testdata.dds', 'Hello', (1,8))
#t = DDS.virtualFile(DDS.virtual_filename, None, 'key')
#t = DDS.virtualFile(DDS.virtual_filename, None, 'value')
#t = DDS.virtualFile(DDS.virtual_filename, 5, 'value')
#print(t)
    
