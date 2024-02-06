import re

regex_IP = r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}"
regex_number = r"[0-9]{1,3}"


def validate_IP(IP):
    return re.match(regex_IP, IP)


def validate_number(values):
    return re.match(regex_number, values)


def update_IP_input(elem, event, values, window):
    if elem is not None and elem.Key in [0, 1, 2, 3]:
        key = elem.Key
        # get value of input field that has focus
        value = values[key]
        if event == '.' and validate_number(value):                    # if a ., then advance to next field
            elem.update(value[:-1])
            value = value[:-1]
            next_elem = window[key+1]
            next_elem.set_focus()

        elif event not in '0123456789' and event != "BackSpace:8" and event != "-CONNECT-":
            elem.update(value[:-1])

        elif len(value) > 2 and key < 3:     # if 2 digits typed in, move on to next input
            next_elem = window[key+1]
            next_elem.set_focus()

        elif len(value) > 2 and key == 3:
            window['-CONNECT-'].set_focus()