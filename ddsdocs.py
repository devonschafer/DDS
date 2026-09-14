#DevonDataStructure
#v1.4.2
from tkinter import *
from dds import DDS

ddsfile = 'dds_docs.dds'
size = '%sx%s' % (DDS.returnSpecificValue(ddsfile, (2,1), 'value'), DDS.returnSpecificValue(ddsfile, (2,2), 'value'))
root = Tk()
root.geometry(size)
root.title(DDS.returnValue(ddsfile, 1, 'value'))

frame_top = Frame(root)
frame_top.pack(side=TOP)
frame_left = Frame(root)
frame_left.pack(side=LEFT, anchor='n', expand=True, fill=Y)
frame_right = Frame(root)
frame_right.pack(side=RIGHT, anchor='n', expand=True, fill=Y)

title = Label(frame_top, text=DDS.returnSpecificValue(ddsfile, (3,1), 'value'),
          font=DDS.returnSpecificValue(ddsfile, (3,2), 'value')) 
title.pack(side=TOP)


def func1():
    description_box.delete("1.0","end")
    description_box.insert(END, DDS.returnSpecificValue(ddsfile, (5,1), 'value'))
    description_box.insert(END, DDS.returnSpecificValue(ddsfile, (5,2), 'value'))

def func2():
    description_box.delete("1.0","end")
    description_box.insert(END, DDS.returnSpecificValue(ddsfile, (6,1), 'value'))
    description_box.insert(END, DDS.returnSpecificValue(ddsfile, (6,2), 'value'))

def func3():
    description_box.delete("1.0","end")
    description_box.insert(END, DDS.returnSpecificValue(ddsfile, (7,1), 'value'))
    description_box.insert(END, DDS.returnSpecificValue(ddsfile, (7,2), 'value'))
    description_box.insert(END, DDS.returnSpecificValue(ddsfile, (7,3), 'value'))
    description_box.insert(END, DDS.returnSpecificValue(ddsfile, (7,4), 'value'))

def func4():
    description_box.delete("1.0","end")
    description_box.insert(END, DDS.returnSpecificValue(ddsfile, (8,1), 'value'))
    description_box.insert(END, DDS.returnSpecificValue(ddsfile, (8,2), 'value'))

def func5():
    description_box.delete("1.0","end")
    description_box.insert(END, DDS.returnSpecificValue(ddsfile, (9,1), 'value'))
    description_box.insert(END, DDS.returnSpecificValue(ddsfile, (9,2), 'value'))
    description_box.insert(END, DDS.returnSpecificValue(ddsfile, (9,3), 'value'))
    description_box.insert(END, DDS.returnSpecificValue(ddsfile, (9,4), 'value'))

def func6():
    description_box.delete("1.0","end")
    description_box.insert(END, DDS.returnSpecificValue(ddsfile, (10,1), 'value'))
    description_box.insert(END, DDS.returnSpecificValue(ddsfile, (10,2), 'value'))

def func7():
    description_box.delete("1.0","end")
    description_box.insert(END, DDS.returnSpecificValue(ddsfile, (11,1), 'value'))
    description_box.insert(END, DDS.returnSpecificValue(ddsfile, (11,2), 'value'))

def func8():
    description_box.delete("1.0","end")
    description_box.insert(END, DDS.returnSpecificValue(ddsfile, (12,1), 'value'))
    description_box.insert(END, DDS.returnSpecificValue(ddsfile, (12,2), 'value'))

def func9():
    description_box.delete("1.0","end")
    description_box.insert(END, DDS.returnSpecificValue(ddsfile, (13,1), 'value'))
    description_box.insert(END, DDS.returnSpecificValue(ddsfile, (13,2), 'value'))

def func10():
    description_box.delete("1.0","end")
    description_box.insert(END, DDS.returnSpecificValue(ddsfile, (14,1), 'value'))
    description_box.insert(END, DDS.returnSpecificValue(ddsfile, (14,2), 'value'))
    description_box.insert(END, DDS.returnSpecificValue(ddsfile, (14,3), 'value'))
    description_box.insert(END, DDS.returnSpecificValue(ddsfile, (14,4), 'value'))

def func11():
    description_box.delete("1.0","end")
    description_box.insert(END, DDS.returnSpecificValue(ddsfile, (15,1), 'value'))
    description_box.insert(END, DDS.returnSpecificValue(ddsfile, (15,2), 'value'))

def func12():
    description_box.delete("1.0","end")
    description_box.insert(END, DDS.returnSpecificValue(ddsfile, (16,1), 'value'))
    description_box.insert(END, DDS.returnSpecificValue(ddsfile, (16,2), 'value'))

def func13():
    description_box.delete("1.0","end")
    description_box.insert(END, DDS.returnSpecificValue(ddsfile, (17,1), 'value'))
    description_box.insert(END, DDS.returnSpecificValue(ddsfile, (17,2), 'value'))

def func14():
    description_box.delete("1.0","end")
    description_box.insert(END, DDS.returnSpecificValue(ddsfile, (18,1), 'value'))
    description_box.insert(END, DDS.returnSpecificValue(ddsfile, (18,2), 'value'))

def func15():
    description_box.delete("1.0","end")
    description_box.insert(END, DDS.returnSpecificValue(ddsfile, (19,1), 'value'))
    description_box.insert(END, DDS.returnSpecificValue(ddsfile, (19,2), 'value'))

def func16():
    description_box.delete("1.0","end")
    description_box.insert(END, DDS.returnSpecificValue(ddsfile, (20,1), 'value'))
    description_box.insert(END, DDS.returnSpecificValue(ddsfile, (20,2), 'value'))

def func17():
    description_box.delete("1.0","end")
    description_box.insert(END, DDS.returnSpecificValue(ddsfile, (21,1), 'value'))
    description_box.insert(END, DDS.returnSpecificValue(ddsfile, (21,2), 'value'))

def func18():
    description_box.delete("1.0","end")
    description_box.insert(END, DDS.returnSpecificValue(ddsfile, (22,1), 'value'))
    description_box.insert(END, DDS.returnSpecificValue(ddsfile, (22,2), 'value'))

def func19():
    description_box.delete("1.0","end")
    description_box.insert(END, DDS.returnSpecificValue(ddsfile, (23,1), 'value'))
    description_box.insert(END, DDS.returnSpecificValue(ddsfile, (23,2), 'value'))

def func20():
    description_box.delete("1.0","end")
    description_box.insert(END, DDS.returnSpecificValue(ddsfile, (24,1), 'value'))
    description_box.insert(END, DDS.returnSpecificValue(ddsfile, (24,2), 'value'))

def func21():
    description_box.delete("1.0","end")
    description_box.insert(END, DDS.returnValue(ddsfile, 25, 'value'))

def func22():
    description_box.delete("1.0","end")
    description_box.insert(END, DDS.returnValue(ddsfile, 26, 'value'))

def func23():
    description_box.delete("1.0","end")
    description_box.insert(END, DDS.returnSpecificValue(ddsfile, (27,1), 'value'))
    description_box.insert(END, DDS.returnSpecificValue(ddsfile, (27,2), 'value'))
    description_box.insert(END, DDS.returnSpecificValue(ddsfile, (27,3), 'value'))
    description_box.insert(END, DDS.returnSpecificValue(ddsfile, (27,4), 'value'))    
    

method_menu = Menubutton(frame_left, text=DDS.returnKey(ddsfile, 4, 'key'), relief=RAISED)    
method_menu.menu = Menu(method_menu) 
method_menu["menu"]= method_menu.menu

method_menu.menu.add_command(label=DDS.returnSpecificValue(ddsfile, (4,1), 'value'), command=func1)
method_menu.menu.add_command(label=DDS.returnSpecificValue(ddsfile, (4,2), 'value'), command=func2)
method_menu.menu.add_command(label=DDS.returnSpecificValue(ddsfile, (4,3), 'value'), command=func3)
method_menu.menu.add_command(label=DDS.returnSpecificValue(ddsfile, (4,4), 'value'), command=func4)
method_menu.menu.add_command(label=DDS.returnSpecificValue(ddsfile, (4,5), 'value'), command=func5) 
method_menu.menu.add_command(label=DDS.returnSpecificValue(ddsfile, (4,6), 'value'), command=func6)
method_menu.menu.add_command(label=DDS.returnSpecificValue(ddsfile, (4,7), 'value'), command=func7)
method_menu.menu.add_command(label=DDS.returnSpecificValue(ddsfile, (4,8), 'value'), command=func8)
method_menu.menu.add_command(label=DDS.returnSpecificValue(ddsfile, (4,9), 'value'), command=func9)
method_menu.menu.add_command(label=DDS.returnSpecificValue(ddsfile, (4,10), 'value'), command=func10)
method_menu.menu.add_command(label=DDS.returnSpecificValue(ddsfile, (4,11), 'value'), command=func11)
method_menu.menu.add_command(label=DDS.returnSpecificValue(ddsfile, (4,12), 'value'), command=func12)
method_menu.menu.add_command(label=DDS.returnSpecificValue(ddsfile, (4,13), 'value'), command=func13)
method_menu.menu.add_command(label=DDS.returnSpecificValue(ddsfile, (4,14), 'value'), command=func14)
method_menu.menu.add_command(label=DDS.returnSpecificValue(ddsfile, (4,15), 'value'), command=func15)
method_menu.menu.add_command(label=DDS.returnSpecificValue(ddsfile, (4,16), 'value'), command=func16)
method_menu.menu.add_command(label=DDS.returnSpecificValue(ddsfile, (4,17), 'value'), command=func17)
method_menu.menu.add_command(label=DDS.returnSpecificValue(ddsfile, (4,18), 'value'), command=func18)
method_menu.menu.add_command(label=DDS.returnSpecificValue(ddsfile, (4,19), 'value'), command=func19)
method_menu.menu.add_command(label=DDS.returnSpecificValue(ddsfile, (4,20), 'value'), command=func20)

method_menu.menu.add_command(label=DDS.returnSpecificValue(ddsfile, (4,21), 'value'), command=func21)
method_menu.menu.add_command(label=DDS.returnSpecificValue(ddsfile, (4,22), 'value'), command=func22)
method_menu.menu.add_command(label=DDS.returnSpecificValue(ddsfile, (4,23), 'value'), command=func23)

method_menu.pack(padx=100, pady=0)

description_box = Text(frame_right, wrap=WORD, relief=FLAT, width=65)
description_box.pack(expand=True, fill=Y)

func22()

root.mainloop()
