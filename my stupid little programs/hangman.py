from english_words import english_words_lower_alpha_set as s
from random import choice

def get_word():
    return choice(list(s))

def render_hangman(i):
    HANGMANPICS = ['''
       
       
       
       
       
       
         ''','''
       
       
       
       
       
       
=========''','''
      |
      |
      |
      |
      |
      |
=========''','''
  +---+
      |
      |
      |
      |
      |
=========''','''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''];return HANGMANPICS[i]


class Bot():
    def __init__(self,length):
        self.dictionary = list(s)
        for i in range(len(self.dictionary)-1):
            if len(self.dictionary[i]) != length:
                self.dictionary.pop(i)
            
        print(self.dictionary)

    def filter_words(self,guessed):
        for i in range(len(self.dictionary)-1):
            for j in range(len(guessed[i])-1):
                if guessed[j] != '-' and self.dictionary[i][j] != guessed[j]:
                    self.dictionary.pop(i)
    
        print(self.dictionary)




if __name__ == "__main__":

    word = list(get_word())
    guessed = ["_" for i in range(len(word))]
    guesses = 0
    bot = Bot(len(guessed))

    while True:

        print("".join(guessed))
        try:
            print(render_hangman(guesses))
        except:
            print("You lost! The word was","".join(word))
            break

        while True:

            guess = input("Enter your letter:\n")

            if len(guess) > 1:
                print('Please enter only one letter')
            elif guess not in 'qwertyuiopasdfghjklzxcvbnm' or guess in guessed:
                print('Please enter a valid letter')
            else:

                break

        if guess in word:
            indices = [i for i, x in enumerate(word) if x == guess]
            for i in indices:
                guessed[i] = guess
            bot.filter_words(guessed)
        else:
            guesses += 1
            print("Nope!")
        


        if "_" not in guessed:
            print("You guesssed the word in %s tries" % guesses)
            break
        

        
