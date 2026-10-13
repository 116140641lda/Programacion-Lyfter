import PySimpleGUI as sg

layout = [
    [sg.Text("Felicidades por crear una GUI")],
]

window = sg.Window("Primer programa", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

window.close()

# print(sg.__file__)