import random
class Player:

    def __init__(self, name):
        self.name = name
        self.letters = []

    def getName(self):
        return self.name

    def getLetters(self):
        return self.letters

    def drawLetter(self):
        letters = 'aaaaaaaaabbccddddeeeeeeeeeeeeffggghhiiiiiiiiijkllllmmnnnnnnooooooooppqrrrrrrssssttttttuuuuvvwwxyyz'
        randlet = random.randint(range(len(letters)))
        self.letters.append(letters[randlet])

    def printLetters(self):
        
