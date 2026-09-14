DDS v1.4.2
DevonDataStructure
The vision of the project:
Why was dds developed?. The vision is to create a data structure that is simple to write and understand. A data structure that can be read and written to from programs or by hand. In my years of working with other data structures and data sets, I wanted certain data structures to work differently. Hopefully others will see the value in dds too.

Readme:
Welcome. This is vanilla dds. This uses python3, and the built-in tkinter library for the "docs & examples" gui(ddsdocs.py). Both the v1 dds module and the v1 "docs & examples" gui(ddsdocs.py) will not use modules or libraries other than those built-in to python3. The goal of dds is to keep things simple, no third party installations, dds.py is meant to be added to your python3 PATH or simply copied to your project's directory. Once copied to your project's directory you can import the module by "from dds import DDS". You do not have to interact with the "docs & examples" gui(ddsdocs.py), this is to show one way that dds can be used and to explain the documentation.
dds_docs.dds contains the documentation in dds format.
testdata.dds contains test data in dds format.
dds.py is the module.
ddsdocs.py is the documentation and examples gui built in python3-tkinter.

Version:
v1.4.2,,Third digit, increased by 2, is the version of the GUI(frontend),,Second digit, increased by 2, is the version of the dds module(backend),,First digit, increased by 1, is the version of the entire project when the third, second, or both digits have reached 8 (or fourth revision).

Documentation: Methods,
DDS.readFile(filename, option, values)
DDS.returnLine(filename, option, values)
DDS.returnKey(filename, option, values)
DDS.return Multiplekeys(filename, option, values)
DDS.returnValue(filename, option, values)
DDS.valuesToList(filename, option, values)
DDS.returnSpecificValue(filename, option, values)
DDS.appendFile(filename, option, values)
DDS.writeFile(filename, option, values)
DDS.searchByKey(filename, option, values)
DDS.countlines(filename, option, values)
DDS.virtualRead(filename, option, values)
DDS.virtualLines(filename, 'all', values)

NEW!

DDS.pathValidation(filepath, option, values)
DDS.createHash(filename, key, password, pin)
DDS.verifyHash(filename, key, pin)
DDS.recursiveReturn(filename, option, values)
DDS.setTimestamp(filename, option, hours, minutes)
DDS.beforeTimestamp(filename, option, values)
DDS.afterTimestamp(filename, option, values)
DDS.equalTimestamp(filename, option, values)
DDS.togoTimestamp(filename, option, values)
DDS.elapsedTimestamp(filename, option, values)

DDS.readFile
Example:DDS.readFile('testdata.dds', 'all', None)
Returns the entire dds file as a string. filename=path_to_file.dds, option=str('all'), values=None.

DDS.returnLine
Example:DDS.returnLine('testdata.dds', 3, None)
Returns entire specific line as a string. Line numbers start with 1 not 0. filename=path_to_file.dds, option=line_number, values=None.

DDS.returnKey
Example:DDS.returnKey('testdata.dds', 3, 'key')
DDS.returnKey('testdata.dds', 'This works', 'key')
Return a key as a string when using a line number. filename=path_to_file.dds, option=line_number, values=('key')
Return a key as a string when using a value. filenname=path_to_file.dds, option=str('value'), values=str('key').

DDS.returnMultipleKeys
Example:DDS.returnMultipleKeys('testdata.dds', (1,8), 'key')
Returns several keys as a list. Line numbers start with 1 not 0. filename=path_to_file.dds, option=tuple(line, numbers), values=str('key').

DDS.returnValue
Example:DDS.returnValue('testdata.dds', 3, 'value')
DDS.returnValue('testdata.dds', 'latte', 'value')
Return a value as a string when using a line number. filename=path_to_file.dds, option=line_number, values=str('value')
Return a value as a string when using a key. filename=path_to_file.dds, option=str('key'), values=str('value').

DDS.valuesToList
Example:DDS.valuesToList('testdata.dds', 3, 'value')
Returns a value, or several values, as a list when using a line_number. Line numbers start with 1 not 0. filename=path_to_file.dds, option=line_number, values=str('value').

DDS.returnSpecificValue
Example:DDS.returnSpecificValue('testdata.dds', (3,4), 'value')
Return a specific value, when multiple values are present. Line numbers start with 1 not 0. filename=path_to_file.dds, option=tuple(line_number, value_number), values=str('value').

DDS.appendFile
Example:DDS.appendFile('testdata.dds', 'string', 'save')
Appends a line to the end of the dds file. filename=path_to_file.dds, option=string_of_data, values=str('save').

DDS.searchByKey
Example:DDS.searchByKey('testdata.dds', 'Hello', (1,8))
Not finished. Might need this to be a search function unlike returnKey or returnValue. filename=path_to_file.dds, option=str('key'), values=tuple(line_number_start, line_number_end).

DDS.countLines
Example:DDS.countLines('testdata.dds', 'all', 'count')
Returns the number of lines in a DDS file. filename=path_to_file.dds, option=str('all'), values=str('count').

DDS.virtualRead (Changed from V1.0.0 DDS.virtualFile)
Example:DDS.virtualRead(DDS.virtual_filename, (4,1), 'value')
Used to reference a variable in dds format instead of interacting with a dds file. filename=variable_in_dds_format, option=tuple, values=str('value')
filename=variable_in_dds_format, option=int, values=str('key')
Example:DDS.virtualRead(DDS.virtual_filename, (4,1), 'value')
Example:DDS.virtualRead(DDS.virtual_filename, 4, 'key')
When option is a tuple and values is 'value', this will return the value at the specific index.
When option is a int and values is 'key', this will return the key for line int.
filename=variable_in_dds_format, option=tuple, values=str('value').
filename=variable_in_dds_format, option=int(), values=str('key').

DDS.virtualLines
Example:DDS.virtualLines(DDS.virtual_filename, 'all', 'count')
Returns the number of lines in a DDS formatted variable. Does not completely work yet. filename=variable_in_dds_format, option=str('all'), values=str('count').

NEW!

DDS.pathValidation
Example:DDS.pathValidation('/path/to/file/testdata.dds', None, None)
Returns True if the given file exists. filepath=/path/to/file.txt, option=None, values=None.

DDS.createHash
Example:DDS.createHash('test_create_hash.dds', 'devon', 'password', 123456)
Creates a dds formatted file with the given key and encrypts the password, hashes with pin, as the value. filename=path_to_file.dds, key=str('key'), password=str('password'), pin=int(pin).

DDS.verifyHash
Example:DDS.verifyHash('test_create_hash.dds', 'password', 123456)
Given the password and pin, this function will verify the given against the saved hash file and return True if given is the correct password or False if not. filename=path_to_file.dds, password=str('password'), pin=int(pin).

DDS.recursiveReturn
Example:DDS.recursiveReturn('testdata.dds', 2, 'recursive')
With a large dds file with multiple values per line, this will return a requested value for each line. filename=path_to_file.dds, option=int(value), values='recursive'.

DDS.setTimestamp
Example:DDS.setTimestamp('testingtime.dds', 'assembler 3', 0, 0)
Saves a timestamp in a dds formatted file. If hours and minutes=0, then current time will be used for timestamp. Hours and minutes can be projected out, Ex: hours=1, minutes=30, to set the timestamp for an additional 1.5 hours in the future instead of the current time. filename=path_to_file.dds, option=str('key'), hours=int(hour), minutes=int(minutes).

DDS.beforeTimestamp
Example:DDS.beforeTimestamp('testingtime.dds', 'assembler 3', None)
Given the timestamp file that was created, return True if current time is before timestamp. filename=path_to_timestamp_file.dds, option=str('key'), values=None)

DDS.afterTimestamp
Example:DDS.afterTimestamp('testingtime.dds', 'assembler 3', None)
Given the timestamp file that was created, return True if current time is after timestamp. filename=path_to_timestamp_file.dds, option=str('key'), values=None)

DDS.equalTimestamp
Example:DDS.equalTimestamp('testingtime.dds', 'assembler 3', None)
Given the timestamp file that was created, return True if current time is equal to timestamp. filename=path_to_timestamp_file.dds, option=str('key'), values=None)

DDS.togoTimestamp
Example:DDS.togoTimestamp('testingtime.dds', 'assembler 3', None)
Given the timestamp file that was created, compare to timestamp, how much time to go. filename=path_to_timestamp_file.dds, option=str('key'), values=None)

DDS.elapsedTimestamp
Example:DDS.elapsedTimestamp('testingtime.dds', 'assembler 3', None)
Given the timestamp file that was created, compare to timestamp, how much time has elapsed. filename=path_to_timestamp_file.dds, option=str('key'), values=None)
