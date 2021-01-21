import PySimpleGUI as sg
from dado import dado

sg.theme('Default1')

layout = [
    [sg.Text('Defina a quantidade de lados do dado:')],
    [sg.InputText('6')],
    [sg.Text('Aperte o botão e gire o dado')],
    [sg.Button('Rodar')],
]


window = sg.Window('Dado', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == 'Rodar':
        resultado = [sg.popup(str(dado(values[0])))]

window.close()