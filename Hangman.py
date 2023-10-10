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
animals = []
sports = []
random_words = []
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
    word_list = random
#Chooses Word
word = random(word_list)
