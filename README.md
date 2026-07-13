# DDS
A new data structure using python.

DDS v1.2.0
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
v1.2.0,,Third digit, increased by 2, is the version of the GUI(frontend),,Second digit, increased by 2, is the version of the dds module(backend),,First digit, increased by 1, is the version of the entire project when the third, second, or both digits have reached 8 (or fourth revision).

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
Returns the number of lines in a DDS formatted variable. Does not completely work yet.
filename=variable_in_dds_format, option=str('all'), values=str('count').
