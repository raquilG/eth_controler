import threading
import time

import PySimpleGUI as sg

from module import controler
import utils
from module.get_windows import make_window1, make_window2


THREAD_EVENT = '-THREAD-'
window2 = None
window1 = make_window1()
eth = None


def the_thread(eth, window):
    """
    The thread that communicates with the application through the window's events.

    Once a second wakes and sends a new event and associated value to the window
    """

    while True:
        time.sleep(0.5)
        try:
            update_relay_state(eth=eth, window=window2)
        except TypeError:
            break
        window.write_event_value('-THREAD-', (0, 1))      # Data sent is a tuple of thread name and counter


def relay_controle(eth, relay_nb):
    reponse = sg.popup_yes_no(f"Etes-vous sur de vouloir redémarrer le relai de la prise connectée {relay_nb}", location=window.current_location())
    if eth and reponse == "Yes" and relay_nb != 0:
        if not controler.reboot_relay(eth, relay_nb):
            sg.popup_error(f"Relai {relay} de la prise connectée déjà eteinte, veuillez patientez.")


def update_relay_state(eth, window):
    state_relay1, state_relay2 = controler.get_state(eth)
    window["-RELAY1-"].update(state_relay1)
    window["-RELAY2-"].update(state_relay2)


while True:
    window, event, values = sg.read_all_windows()
    if event in ('Exit', sg.WINDOW_CLOSE_ATTEMPTED_EVENT) and window == window1:
        sg.user_settings_set_entry('-location-', window.current_location())  
        break

    if event == "-CONNECT-":
        IP = f"{values[0]}.{values[1]}.{values[2]}.{values[3]}"
        if utils.validate_IP(IP):
            eth = controler.connect_to_eth(IP)
            if eth:
                window1.hide()
                window2 = make_window2()
                threading.Thread(target=the_thread, args=(eth, window,), daemon=True).start()

            else:
                sg.popup_error(f"Impossible de communiquer a l'ETH-002-b {IP}")

    if window == window2 and (event in (sg.WIN_CLOSED, 'Exit')):
        sg.user_settings_set_entry('-location-', window.current_location())
        window2.close()
        window2 = None
        window1.un_hide()
        for i in range(4):
            window1[i].update('')

    if window == window1:
        elem = window.find_element_with_focus()
        utils.update_IP_input(elem, event, values, window)

    if window == window2:
        relay = 1 if event == "-R_RELAY1-" else 2 if event == "-R_RELAY2-" else 0
        relay_controle(eth, relay)

window.close()
