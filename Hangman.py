import random
#ASCII art for hangman guesses
HANMAN = ['''
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
=========''']
#Categoreys you can select
animals = ["dog"]
sports = ["john"]
random_words = ["ok","hangman", "dogs"]
word_list = []
#Welcome and options
print('WELCOME TO HANGMAN.')
print('Choose a categorery')
print('A for animals')
print('S for sports')
print('R for random')
option = input("Enter the category: ")
#Wordlist is choosen
if option == 'a':
    word_list = animals
elif option =='s':
    word_list = sports
else:
    word_list = random_words

word = random.choice(word_list) #Chooses the word