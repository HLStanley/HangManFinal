import random
#ASCII art for hangman guesses
HANGMAN = ['''
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
animals = ['cat','dog','rat','lizard','cow','kangaroo','human','monkey','buffalo','goose','raven','crow','quial','ostrich']
sports = ['basketball','football','soccer','hockey','rugby','tennis','golf','chess','fencing','volleyball','handball','lacrosse']
random_words = ['wrathful','hippopotomonstrosesquippedaliophobia','supercalifragilisticexpialidocious','Monday','rocks','moon','magic','xerox','zero','alpha','random','hangman','zetta','market','hello','rain']
word_list = []
#Welcome and options
print("""
 _                                                       
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       """)
print()
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

def game_run(): #Main gameplay loop
  word = random.choice(word_list) #Chooses the word
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  letters_guessed = []
  tries = 6
  guessed = False
  print()
  print()
  print("the word contains", len(word), 'letters')
  print()
  print(len(word) * '_')
  print(letters_guessed)
  print(f"You have this many tries left {tries}")
  #guess loop
  while guessed == False:
    guess = input("Enter a letter: ").lower
    if guess in letters_guessed:
      print("Letter is guessed")
    
    
game_run()