import pyfiglet
from pyfiglet import Figlet
from music import ToneMusic


class Display:

    @staticmethod
    def displayControls():
        with open('controls.txt', 'r') as f:
            for line in f:
                print(line.rstrip())
        print()

    @staticmethod
    def title():
        ToneMusic.run("ending")
        with open('zombie.txt', 'r') as f:
            for line in f:
                print(line.rstrip())
        custom_fig = Figlet(font='poison')
        print(custom_fig.renderText('JOURNEY'))
