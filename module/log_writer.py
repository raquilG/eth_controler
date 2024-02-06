# coding=utf-8

# Created by Giovanni Raquil from Sens Of Life on 01/01/2022.
# Copyright © 2021-2022 Sens Of Life. All rights reserved.

"""
    écriture du ficheir log
"""

import inspect
from datetime import datetime
import os
import io

frame = inspect.currentframe()


class Log():
    """
        permet la création d'un logger
    """
    def __init__(self, config):
        """
            param A = class config -> Config

        """
        self.config = config
        self.path = self.create_logger_directory()

    def create_logger_directory(self):
        """
            permet la création du dossier ou seront stocker les logs
        """
        try:
            directory = self.config.log_directory
            # Create the main folder name on D HDD
            if not os.path.exists(directory):
                os.makedirs(directory)
            else:
                print('Folder ', directory, ' already there')
            return directory

        except Exception as e:
            print(e)
            pass

    def add(self, message):
        """
            permet d'écrire le log

            param A = message a écrire -> str

            return A message complet ( rajout du temps, du nom du parc ,
            du nom script et de la ligne ou le logger a été apeller)
        """
        today = datetime.now().strftime('%Y-%m-%d')
        log_path = self.path+"/"+today+".log"
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        message = now+"--"+message+"--"+self.config.site_name.upper()
        message += "--"+self.config.script_name.upper()+"--"+str(frame.f_lineno)+"\n"
        if not os.path.isfile(log_path):
            write = "w"
        else:
            write = "a"
        try:
            with io.open(log_path, write) as f:
                f.write(message)
                return message
        except Exception as e:
            print("Erreur d'écriture dans le log " + str(e))
