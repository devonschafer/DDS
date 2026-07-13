#DevonDataStructure
#v1.2.0
import os


class DDS():
    
    filename1 = 'dds_docs.dds'
    filename2 = 'testdata.dds'

    filename = filename1

    virtual_filename = '''virtual_filename = 'apptitle::DDS V1,,v2,,v3,,v4,,v5''''
    
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
    
    def writeFile(filename, option, values):
        saveFile = open(filename, 'w')
        if isinstance(option, str) and values == 'save':
            saveFile.write('%s' % option)
        saveFile.close()
    
    def virtualRead(filename, option, values):
        line = filename.split('\n')
        if '' in line:
                line.remove('')
        if isinstance(option, tuple) and values == 'value':
            if '::' in line[option[0]-1]:
                l = line[option[0]-1].split('::')
                opt = l[1].split(',,')
                return opt[option[1]-1]
        elif isinstance(option, int) and values =='key':
            if '::' in line[option-1]:
                l = line[option-1].split('::')
                return l[0]
    
    def countLines(filename, option, values):
        openFile = open(filename, 'r')
        if option == 'all' and values == 'count':
            line = openFile.readlines()
            return len(line)
        openFile.close()
    #no work, need to fix
    def virtualLines(filename, option, values):
        line = filename.split('\n')
        if option == 'all' and values == 'count':
            if '' in line:
                line.remove('')
            return len(line)
        openFile.close()
            
#t = DDS.readFile(DDS.filename, 'all', None)
#t = DDS.returnLine(DDS.filename, 3, None)
#t = DDS.returnKey(DDS.filename, 8, 'key')
#t = DDS.returnKey(DDS.filename, 'DDS V1', 'key')
#t = DDS.returnMultipleKeys(DDS.filename, (1,8), 'key')
#t = DDS.returnValue(DDS.filename, 3, 'value')
#t = DDS.returnValue(DDS.filename, 'apptitle', 'value')
#t = DDS.valuesToList(DDS.filename, 3, 'value')
#t = DDS.returnSpecificValue(DDS.filename, (3,1), 'value')
#t = DDS.appendFile(DDS.filename, 'Append::Append to file, instead of write.', 'save')
#t = DDS.writeFile('testfile.dds', 'Mistake::Shows', 'save')
#t = DDS.searchByKey(DDS.filename, 'Hello', (1,8))
#t = DDS.virtualRead(DDS.virtual_filename, (4,1), 'value')
#t = DDS.virtualRead(DDS.virtual_filename, 4, 'key')
#t = DDS.countLines(DDS.filename, 'all', 'count')
#t = DDS.virtualLines(DDS.virtual_filename, 'all', 'count')
#print(t)
