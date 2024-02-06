# coding=utf-8

from .model import Eth002

# from . import view
from .log_writer import Log
from .config import create_config
# from . import utils
config = create_config()
log = Log(config)


def connect_to_eth(IP):
    """
        permet la connection a la prise connecter grace
        a l'adresse IP passé à la vue
        return eth->class ETH002 si connection réussie
               False->bool si échec de la connection
    """
    if not IP:
        return IP
    eth = Eth002(ip=IP, password=config.password)
    try:
        eth.connect()
        print("connection au controlleur réussi")
        #utils.add_eth_to_historical(IP)
    except TimeoutError:
        print(f"""
!!!la prise connecter avec l'adresse IP {eth.ip} n'a pas été trouvé!!!""")
        return False
    except Exception as err:
        log.add(f"{type(err)}: {err}")
        return False
    return eth


def reboot_relay(eth, number):
    """
        permet d'éteindre et de ralumer un relay qui est uniquement actif

    """
    if number == 1 and not eth.getDO1State():
        ok = True
    elif number == 2 and not eth.getDO2State():
        ok = True
    else:
        ok = False
    if ok:
        message = f"0x3A:DOA,{number},{config.time_to_reboot},{config.password}"
        print(message)
        try:
            eth.write(message.encode("ascii"))
            eth.read(1)
        except Exception as err:
            log.add(f"{type(err)}: {err}")
            return False
        else:
            message_log = f"redémarrage de la prise connectée {eth.ip} relai n°{number}"
            log.add(message_log)
            return True
    return ok


def controle_relay(eth, relay):
    if relay == "1":
        eth.toggleDO1()
        return True
    if relay == "2":
        eth.toggleDO2()
        return True
    return False


def get_state(module):
    """
        permet de formaliser et d'afficher les statues des relais

    """
    eth_state = module.getDigitalOutputs()
    eth_relay1 = ""
    eth_relay2 = ""
    if eth_state == [0]:
        eth_relay1 = 0
        eth_relay2 = 0
    elif eth_state == [1]:
        eth_relay1 = 1
        eth_relay2 = 0
    elif eth_state == [2]:
        eth_relay1 = 0
        eth_relay2 = 1
    elif eth_state == [3]:
        eth_relay1 = 1
        eth_relay2 = 1
    return eth_relay1, eth_relay2


if __name__ == "__main__":
    eth = connect_to_eth()
    print(reboot_relay(eth, "1"))
