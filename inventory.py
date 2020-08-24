import nltk
from nltk.corpus import wordnet
from nltk.tokenize import PunktSentenceTokenizer
from nltk.tree import Tree


class Inventory:
    global itemsList
    itemsList = {}

    def __init__(self,text):
            self.text = text
            self.chunkList = []
            #self.itemsList = []

    def addInventory(self):

        weapons = ["crowbar","watch","gun"]
        cstokenizer = PunktSentenceTokenizer(self.text)
        tokenized = cstokenizer.tokenize(self.text)
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            #r"Chunk:{<VB.?><R.?>*<DT><NN>+}"
            chunkGram = r"Chunk:{<VB.?><PRP.?><NN?>+}"
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            #print("This is the chunked data")
            #print(chunked)
        for lemmasW in self.text.split():
            for weaponItem in weapons:
                if weaponItem == lemmasW:
                    if(weaponItem not in itemsList):
                        itemsList.update({weaponItem:wordnet.synsets(weaponItem)[0].definition()})
                    else:
                        continue

    def displayInventory(self):
        print("Inventory")
        print("-" * 40)
        for key,val in itemsList.items():
            print(key, "--- ", val)

        print("-" * 40)
