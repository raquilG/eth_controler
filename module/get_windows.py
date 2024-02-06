import PySimpleGUI as sg


def MyInput(key): return sg.Input('', size=(3, 1), key=key, pad=(0, 2))


def make_window1():
    layout = [
              [sg.Text('IP prise connectée', font='_ 12'),
               MyInput(0), sg.T('.'), MyInput(1), sg.T('.'),
               MyInput(2), sg.T('.'), MyInput(3)],
              [sg.Push(), sg.Button('Connect to ETH', key="-CONNECT-", 
                                    bind_return_key=True), sg.Button('Exit')]]

    return sg.Window('eth_controller', layout,
                     size=(325, 75),
                     enable_close_attempted_event=True,
                     location=sg.user_settings_get_entry('-location-',
                                                         (None, None)),
                     return_keyboard_events=True, finalize=True)


def make_window2():
    layout = [[sg.Text('Etat des prise ETH')],
              [sg.Text("Relay1"), sg.Text("", size=(3, 1), key="-RELAY1-",
                                          background_color="white",
                                          text_color="Black"),
               sg.Button("Redémarrage de la prise connectée", key="-R_RELAY1-")],
              [sg.Text("Relay2"), sg.Text("", size=(3, 1), key="-RELAY2-",
                                          background_color="white",
                                          text_color="Black"),
               sg.Button("Redémarrage de la prise connectée", key="-R_RELAY2-")],
              [sg.Push(), sg.Button('Exit')]]

    return sg.Window('Window 2', layout,
                     finalize=True, size=(335, 150),
                     location=sg.user_settings_get_entry('-location-',
                                                         (None, None)))
