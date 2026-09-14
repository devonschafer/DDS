#DevonDataStructure
#v1.4.2
import os
import datetime


class DDS():

    filename = 'testdata.dds'

    letter_alignment = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
             'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
             'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
             'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
             'Y', 'Z', '!', '@', '#', '$', '%', '^', '&', '*',
             '(', ')', ',', '.', '-', '_']
    
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
        if option == 'all' and values == 'key':
            i = []
            line = openFile.readlines()
            for k in range(len(line)):
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
            saveFile.write('%s\n' % option)
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

    def pathValidation(filepath, option, values):
        if isinstance(filepath, str):
            if os.path.exists(filepath):
                return True
            else:
                return False

    #NEW---------------
    def createHash(filename, key, password, pin):
        encrypted_key = ''
        if isinstance(password, str) and isinstance(pin, int):
            for a in range(len(password)):
                index = DDS.letter_alignment.index(password[a])
                encrypted_password += '%s' % index
                masked_password = int(encrypted_password) * int(pin)
        DDS.writeFile(filename, '%s::%s' % (key, masked_password), 'save')

    def verifyHash(filename, password, pin):
        encrypted_password = ''
        if isinstance(password, str) and isinstance(pin, int):
            for a in range(len(password)):
                    index = DDS.letter_alignment.index(password[a])
                    encrypted_password += '%s' % index
                    masked_password = int(encrypted_password) * int(pin)
        if int(masked_password) == int(DDS.returnValue(filename, 1, 'value')):
            return True
        else:
            return False

    def recursiveReturn(filename, option, values):
        l = DDS.countLines(filename, 'all', 'count')
        openFile = open(filename, 'r')
        lines = openFile.readlines()
        output = []
        if isinstance(option, int) and values == 'recursive':
            for a in range(l):
                next_line = lines[a].split('::')
                opt = next_line[1].split(',,')
                if '\n' in opt[option-1]:
                    mod = opt[option-1].replace('\n', '')
                    output.append(mod)
                else:
                    output.append(opt[option-1])
            return output
        openFile.close()

    def setTimestamp(filename, option, hours, minutes):
        currenttime = datetime.datetime.now().replace(microsecond=0)
        productiontime = currenttime + datetime.timedelta(hours=int(hours), minutes=int(minutes)) 
        DDS.appendFile(filename, '%s::%s' % (option, productiontime), 'save')

    def beforeTimestamp(filename, option, values):
        timestamp = DDS.returnValue(filename, option, 'value')
        pretty = timestamp.split()
        date = pretty[0].split('-')
        y, m, d = date[0], date[1], date[2]
        time = pretty[1].split(':')
        h, mn, s = time[0], time[1], time[2]
        currenttime = datetime.datetime.now().replace(microsecond=0)
        if currenttime < datetime.datetime(int(y), int(m), int(d), int(h), int(mn), int(s)):
            return True
        else:
            return False

    def afterTimestamp(filename, option, values):
        timestamp = DDS.returnValue(filename, option, 'value')
        pretty = timestamp.split()
        date = pretty[0].split('-')
        y, m, d = date[0], date[1], date[2]
        time = pretty[1].split(':')
        h, mn, s = time[0], time[1], time[2]
        currenttime = datetime.datetime.now().replace(microsecond=0)
        if currenttime > datetime.datetime(int(y), int(m), int(d), int(h), int(mn), int(s)):
            return True
        else:
            return False

    def equalTimestamp(filename, option, values):
        timestamp = DDS.returnValue(filename, option, 'value')
        pretty = timestamp.split()
        date = pretty[0].split('-')
        y, m, d = date[0], date[1], date[2]
        time = pretty[1].split(':')
        h, mn, s = time[0], time[1], time[2]
        currenttime = datetime.datetime.now().replace(microsecond=0)
        if currenttime == datetime.datetime(int(y), int(m), int(d), int(h), int(mn), int(s)):
            return True
        else:
            return False

    def togoTimestamp(filename, option, values):
        timestamp = DDS.returnValue(filename, option, 'value')
        pretty = timestamp.split()
        date = pretty[0].split('-')
        y, m, d = date[0], date[1], date[2]
        time = pretty[1].split(':')
        h, mn, s = time[0], time[1], time[2]
        currenttime = datetime.datetime.now().replace(microsecond=0)
        #returns h:mn:s until timestamp
        return datetime.datetime(int(y), int(m), int(d), int(h), int(mn), int(s)) - currenttime
        
    def elapsedTimestamp(filename, option, values):
        timestamp = DDS.returnValue(filename, option, 'value')
        pretty = timestamp.split()
        date = pretty[0].split('-')
        y, m, d = date[0], date[1], date[2]
        time = pretty[1].split(':')
        h, mn, s = time[0], time[1], time[2]
        currenttime = datetime.datetime.now().replace(microsecond=0)
        #returns h:mn:s since the timestamp
        return currenttime - datetime.datetime(int(y), int(m), int(d), int(h), int(mn), int(s))

            
#t = DDS.readFile(DDS.filename, 'all', None)
#t = DDS.returnLine(DDS.filename, 3, None)
#t = DDS.returnKey(DDS.filename, 8, 'key')
#t = DDS.returnKey(DDS.filename, 'DDS V1', 'key')
#t = DDS.returnMultipleKeys(DDS.filename, 'all', 'key')
#t = DDS.returnValue(DDS.filename, 3, 'value')
#t = DDS.returnValue('log.dds', 'soggybob', 'value')
#t = DDS.valuesToList(DDS.filename, 3, 'value')
#t = DDS.returnSpecificValue(DDS.filename, (3,1), 'value')
#t = DDS.appendFile('testingtime.dds', 'Append::Append to file, instead of write.', 'save')
#t = DDS.writeFile('testfile.dds', 'Mistake::Shows', 'save')
#t = DDS.searchByKey(DDS.filename, 'Hello', (1,8))
#t = DDS.virtualRead(DDS.store, (4,1), 'value')
#t = DDS.virtualRead(DDS.store, 4, 'key')
#t = DDS.countLines(DDS.filename, 'all', 'count')
#t = DDS.virtualLines(DDS.store, 'all', 'count')
#NEW-------------
#t = DDS.pathValidation('/home/devon/Documents/terminal_hatch_browser/pages/search.py', None, None)
#t = DDS.createHash('test_create_hash.dds', 'helloworld', 123456)
#t = DDS.verifyHash('test_create_account.dds', 'helloworld', 123456)
#t = DDS.recursiveReturn('factory_floor.dds', 1, 'recursive')
#t = DDS.setTimestamp('testingtime.dds', 'assembler 3', 0, 0)
#t = DDS.beforeTimestamp('testingtime.dds', 'assembler 3', None)
#t = DDS.afterTimestamp('testingtime.dds', 'assembler 3', None)
#t = DDS.equalTimestamp('testingtime.dds', 'assembler 3', None)
#t = DDS.togoTimestamp('testingtime.dds', 'assembler 3', None)
#t = DDS.elapsedTimestamp('testingtime.dds', 'assembler 3', None)
#print(t)
