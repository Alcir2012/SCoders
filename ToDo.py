import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Lista de tarefas a fazer')],
            [sg.Text('Tarefa: '), sg.InputText()],
            [sg.Text('Prazo: '), sg.InputText()],
            [sg.Button('Nova tarefa'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('To Do List', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    elif event == 'Nova tarefa':
        window.extend_layout(window, [[sg.Text('Tarefa'), sg.InputText()]])
        window.extend_layout(window, [[sg.Text('Prazo: '), sg.InputText()]])
    elif event == 'Cancel':
        window.close

window.close()