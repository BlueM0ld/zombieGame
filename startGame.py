import gpt_2_simple as gpt2
import pyfiglet
from pyfiglet import Figlet
from inventory import Inventory
from music import ToneMusic
from display import Display
sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess)


def dEndBanner():
    ToneMusic.run("ending")
    print("You surrendered yourself to death, unable to see any hope in this situation.")
    print()
    custom_fig = Figlet(font='standard')
    print(custom_fig.renderText('YOU     DIED'))
    print("Want to try again?")
    print("Type yes to start again |Press ANY OTHER KEY TO EXIT")
    start = input()
    if start == "yes" or start == "YES":
        print()
        displayintroduction()
        runGame(start)


def snip(text):
    indexFin = text.rfind('.')
    result = text[0:indexFin+1]
    return result


def banner():
    print("Press E to Enter | Press C to View controls| Press ANY OTHER KEY TO EXIT")
    start = input()
    if start == "e" or start == "E":
        print()
        displayintroduction()
        runGame(start)
    elif start == "C" or start == "c":
        Display.displayControls()
        banner()


def runGame(start):
    TextGrab = []
    while start == "E":

        txt = input("You : ")
        snipText = gpt2.generate(sess,
                                 length=100,
                                 temperature=0.2,  # 0.3
                                 prefix=txt,
                                 nsamples=1,
                                 return_as_list=True,
                                 )[0]

        text = snip(snipText)
        TextGrab.append(text)
        inventory = Inventory(text)
        inventory.addInventory()
        getMusic = ToneMusic.playToneMusic(text)
        ToneMusic.run(getMusic)
        if txt == "check inventory":
            inventory.displayInventory()
            print()
            # print("inventory is in maintainence")
        elif txt == "C" or txt == "c":
            Display.displayControls()
        elif txt == "Surrender":
            dEndBanner()
            break
        else:
            print(text)
        print()


def displayintroduction():
    TextGrab = []

    introduction = "You are in an a zombie apocalypse"
    textGen = gpt2.generate(sess,
                            length=200,
                            temperature=0.4,
                            prefix=introduction,
                            nsamples=1,
                            return_as_list=True)[0]
    TextGrab.append(textGen)
    # inventory = NLP(textGen)
    inventory = Inventory(textGen)
    inventory.addInventory()
    getMusic = ToneMusic.playToneMusic(textGen)
    ToneMusic.run(getMusic)

    snipText = snip(textGen)
    print(snipText)


Display.title()
banner()
