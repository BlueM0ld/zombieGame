import nltk
from nltk.tokenize import PunktSentenceTokenizer
from nltk.tree import Tree


class NLP:
    global itemsList
    itemsList = []

    def __init__(self,text):
            self.text = text
            self.chunkList = []

    def addInventory(self):
        cstokenizer = PunktSentenceTokenizer(self.text)
        tokenized = cstokenizer.tokenize(self.text)
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            chunkGram = r"Chunk:{<VB.?><PRP.?><NN?>+}"
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            for elem in chunked:
                if isinstance(elem, nltk.Tree):
                    itemPickupStr = ""
                    for (text, tag) in elem:
                        itemPickupStr += text+ " "
                    self.chunkList.append(itemPickupStr)

        itemsStr =   " ".join(self.chunkList)
        cstokenizer = PunktSentenceTokenizer(itemsStr)
        tokenized2 = cstokenizer.tokenize(itemsStr)
        for i in tokenized2:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            chunkGram = r"Chunk:{<NN>+}"
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            for elem in chunked:
                if isinstance(elem, nltk.Tree):
                    item = ""
                    for (text, tag) in elem:
                        item += text+ " "
                    itemsList.append(item)

    def displayInventory(self):
        print("Inventory")
        print()
        print(itemsList)
