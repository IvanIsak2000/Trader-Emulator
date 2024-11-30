import os
import time

import textual

from db.user import UserORM
from env import CLEAR, API_TOKEN


class TraderEmulator:
    def __init__(self):
        self.user = UserORM().get(0)

    def main_menu(self):
        os.system(CLEAR)
        print('''
88888888888                    888                        8888888888                        888          888                     
    888                        888                        888                               888          888                     
    888                        888                        888                               888          888                     
    888  888d888  8888b.   .d88888  .d88b.  888d888       8888888    88888b.d88b.  888  888 888  8888b.  888888  .d88b.  888d888 
    888  888P"       "88b d88" 888 d8P  Y8b 888P"         888        888 "888 "88b 888  888 888     "88b 888    d88""88b 888P"   
    888  888     .d888888 888  888 88888888 888    888888 888        888  888  888 888  888 888 .d888888 888    888  888 888     
    888  888     888  888 Y88b 888 Y8b.     888           888        888  888  888 Y88b 888 888 888  888 Y88b.  Y88..88P 888     
    888  888     "Y888888  "Y88888  "Y8888  888           8888888888 888  888  888  "Y88888 888 "Y888888  "Y888  "Y88P"  888     
        ''')


if __name__ == '__main__':
    user = UserORM().get(0)
    if user is None:
        print('[red]No found account. Do you want to create? Type Yes or No[/red]')
        res = input()
        if res == 'Yes':
            print('[red]Type your user name:[/red]')
            username = input()
            os.system(CLEAR)
            UserORM().add(username=username)
            TraderEmulator().main_menu()
    else:
        TraderEmulator().main_menu()
