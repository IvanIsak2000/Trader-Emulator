import os
import time
from turtledemo.forest import start

from rich import print as pr
from rich.console import Console
from rich.tree import Tree
from rich.table import Table
from rich.style import Style
from rich.text import Text
from rich.progress import track


from db.user import UserORM
from env import CLEAR, API_TOKEN

console = Console()


class TraderEmulator:
    def __init__(self, console: Console):
        self.console = console
        self.user = UserORM().get(0)

    def main_menu(self):
        os.system(CLEAR)
        self.console.print('''
        88888888888                    888                        8888888888                        888          888                     
            888                        888                        888                               888          888                     
            888                        888                        888                               888          888                     
            888  888d888  8888b.   .d88888  .d88b.  888d888       8888888    88888b.d88b.  888  888 888  8888b.  888888  .d88b.  888d888 
            888  888P"       "88b d88" 888 d8P  Y8b 888P"         888        888 "888 "88b 888  888 888     "88b 888    d88""88b 888P"   
            888  888     .d888888 888  888 88888888 888    888888 888        888  888  888 888  888 888 .d888888 888    888  888 888     
            888  888     888  888 Y88b 888 Y8b.     888           888        888  888  888 Y88b 888 888 888  888 Y88b.  Y88..88P 888     
            888  888     "Y888888  "Y88888  "Y8888  888           8888888888 888  888  888  "Y88888 888 "Y888888  "Y888  "Y88P"  888     
        ''')
        self.console.print(f'[green]UID: {self.user.uid}[/green]')
        self.console.print(f'[green]Юзернейм: {self.user.username}[/green]')
        self.console.print(f'[green]Баланс: {self.user.balance} USD[/green]')
        main = Tree(f'\nГлавное меню')
        main.add('0 - Выход', style='red')
        main.add('1 - Аккаунт', style="bright_blue")
        main.add(f'2 - Telegram бот({'[green]Включен[/green]' if API_TOKEN != '' else '[red]Выключен[/red]'})',
                 style='bright_blue')
        pr(main)
        self.start()

    def start(self):
        command = input('Command>')
        if command == '0':
            os.system(CLEAR)
            exit()

        elif command == '1':
            ...

        elif command == '2':
            # self.main_menu()
            description = Text("API-TOKEN бота, полученный в @BotFather")
            description.stylize("link https://t.me/BotFather", 22, 33)
            self.console.print(
                f"API_TOKEN - {description}",
                style="bright_blue"
            )


if __name__ == '__main__':
    user = UserORM().get(0)
    if user is None:
        console.print('[red]No found account. Do you want to create? Type Yes or No[/red]')
        res = input()
        if res == 'Yes':
            console.print('[red]Type your user name:[/red]')
            username = input()

            os.system(CLEAR)
            for i in track(range(10), description="Account creating...", show_speed=False, get_time=False):
                time.sleep(1)
            os.system(CLEAR)
            UserORM().add(username=username)
            TraderEmulator(console=console).main_menu()
    else:
        TraderEmulator(console=console).main_menu()
