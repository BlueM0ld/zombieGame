import gpt_2_simple as gpt2
import pyfiglet
from pyfiglet import Figlet
from inventory import Inventory
from music import ToneMusic
sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess)



def dEndBanner():
    print("You surrendered yourself to death, unable to see any hope in this situation.")
    print()
    custom_fig = Figlet(font='standard')
    print(custom_fig.renderText('YOU     DIED'))




def snip(text):
    indexFin = text.rfind('.')
    result = text[0:indexFin+1]
    return result

def title():
    with open('zombie.txt', 'r') as f:
        for line in f:
            print(line.rstrip())
    custom_fig = Figlet(font='poison')
    print(custom_fig.renderText('JOURNEY'))
def banner():
    print("Press E to Enter | Press C to View controls| Press ANY OTHER KEY TO EXIT")
    start = input()
    if start =="e" or start == "E":
        print()
        displayintroduction()
        runGame(start)
    elif start == "C" or start == "c":
        displayControls()
        banner()

def runGame(start):
    TextGrab = []
    while start == "E":

        txt = input("You : ")
        snipText = gpt2.generate(sess,
                          length=100,
                          temperature=0.2, #0.3
                          prefix=txt,
                          nsamples=1,
                          return_as_list=True,
                          )[0]
        #understandChoice(txt, text)
        text = snip(snipText)
        TextGrab.append(text)
        #inventory = NLP(text)
        inventory = Inventory(text)
        inventory.addInventory()
        music = ToneMusic(text)
        getMusic = music.playToneMusic()
        music.run(getMusic)
        if txt == "check inventory":
            inventory.displayInventory();
            print()
            #print("inventory is in maintainence")
        elif txt == "C" or txt == "c":
            displayControls()
        elif txt == "Surrender":
            dEndBanner()
            break;
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
    #inventory = NLP(textGen)
    inventory = Inventory(textGen)
    inventory.addInventory()
    music = ToneMusic(textGen)
    getMusic = music.playToneMusic()
    music.run(getMusic)

    snipText = snip(textGen)
    print(snipText)

def displayControls():
    with open('controls.txt', 'r') as f:
        for line in f:
            print(line.rstrip())
    print()


title()
banner()
