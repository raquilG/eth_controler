import json

configuration = {
    "password": "password",
    "time_to_reboot": "200",
    "log_directory" : "C:/ProBird_log",
    "site_name": "Parc_Test",
    "script_name": "eth_controler",

    "admin_mode": 0
}


def create_config_file():
    with open("config.json", "w") as f:
        json.dump(configuration, f, indent=4)