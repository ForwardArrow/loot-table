import PySimpleGUI as sg

sg.theme('DarkAmber')	# Look at themes for this

#variables
filename = 'test.txt'
tName = '-TITLE'
tList = '-ITEM-'

# Window layout
layout = [  [sg.Text('Table name:'), sg.In(key=tName, size=(25, 1))],
            [sg.Text('Table item:'), sg.In(size=(30, 1), do_not_clear=False, key=tList)],
            [sg.Button('Add Item'), sg.Button('Done')] ]

# Create the Window
window = sg.Window('Table Input', layout)

file = open(filename, 'a')
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Done'):	# if user closes window or clicks cancel
        break
    file.write(values[tName])
    file.write(': ')
    file.write(values[tList])
    file.write('\n')

window.close()
file.close()