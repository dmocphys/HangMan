__author__ = 'Thomas Hauth, Martin Heck'

class HangManEngine:
  def __init__(self, secretWord):
    self.userInput = None
    self.secretword = secretWord

  def getMessage(self):
    return\
    'This is a game of hangman. For an explanation, please search the web.'

  def readInput(self, chosenInput=None):
    if chosenInput is None:
        self.userInput = input("Please insert your letter: ")
    else:
        self.userInput = chosenInput
    return self.userInput
