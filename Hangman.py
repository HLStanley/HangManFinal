import random
while True:

#Categories you can select
  animals = ['cat','dog','rat','lizard','cow','kangaroo','human','monkey','buffalo','goose','raven','crow','quial','ostrich']
  sports = ['basketball','football','soccer','hockey','rugby','tennis','golf','chess','fencing','volleyball','handball','lacrosse']
  random_words = ['wrathful','hippopotomonstrosesquippedaliophobia','supercalifragilisticexpialidocious','monday','rocks','moon','magic','xerox','zero','alpha','random','hangman','zetta','market','hello','rain']
  word_list = []
  guessed = False
  
  #Greeting
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
  print('Choose a category')
  print('A for animals')
  print('S for sports')
  print('R for random')
  option = input("Enter the category: ")
#Wordlist is chosen
  if option.lower() == 'a':
    word_list = animals
  elif option.lower() =='s':
    word_list = sports
  elif option.lower() =='r':
    word_list = random_words
  else:
    print("Error! Please only input a, s, or r to choose the category!")
    break
  word = random.choice(word_list)
#Main gameplay loop
  def game_run():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    letters_guessed = []
    letters_correct = alphabet in word
    tries = 6
    guessed = False
    display_hangman(6)
    print()
    print("The word contains", len(word), 'letters')
    print()
    display_lines()

  #Guess loop
    while not guessed:
      print("\nLetters guessed thus far: ")
      for letter in letters_guessed:
        print(letter, end=" ")
      print(f"\nYou have this many tries left: {tries}")
  #User inputs letter  
      guess = input("\nEnter a letter: ").lower()
  #If user has a correct letter guess  
      if guess in word:
        display_hangman(tries)
        letters_guessed.append(guess)
        letters_correct = display_word(letters_guessed)
        display_lines()
  #If user has an incorrect letter guess
      else:
        tries -= 1
        letters_guessed.append(guess)
        display_hangman(tries)
        letters_correct = display_word(letters_guessed)
        display_lines()
        if tries == 0:
          break
    
        
    
#Displays lines underneath letters for clarity
  def display_lines():  
      print("\r")
      for char in word:
        print("\u203E", end=" ")

#Displays hangman ASCII art based on amount of incorrect answers
  def display_hangman(tries): 
    if tries == 6:
      print("\n  +---+  ")
      print("  |   |  ")
      print("      |  ")
      print("      |  ")
      print("      |  ")
      print("      |  ")
      print("=========")
    elif tries == 5:
      print("\n  +---+  ")
      print("  |   |  ")
      print("  O   |  ")
      print("      |  ")
      print("      |  ")
      print("      |  ")
      print("=========")
    elif tries == 4:
      print("\n  +---+  ")
      print("  |   |  ")
      print("  O   |  ")
      print("  |   |  ")
      print("      |  ")
      print("      |  ")
      print("=========")
    elif tries == 3:
      print("\n  +---+  ")
      print("  |   |  ")
      print("  O   |  ")
      print(" /|   |  ")
      print("      |  ")
      print("      |  ")
      print("=========")
    elif tries == 2:
      print("\n  +---+  ")
      print("  |   |  ")
      print("  O   |  ")
      print(" /|\  |  ")
      print("      |  ")
      print("      |  ")
      print("=========")
    elif tries == 1:
      print("\n  +---+  ")
      print("  |   |  ")
      print("  O   |  ")
      print(" /|\  |  ")
      print(" /    |  ")
      print("      |  ")
      print("=========")
    elif tries == 0:
      print("\n  +---+  ")
      print("  |   |  ")
      print("  O   |  ")
      print(" /|\  |  ")
      print(" / \  |  ")
      print("      |  ")
      print("=========")

  def display_word(letters_guessed):
      counter = 0
      correct_letters = 0
      for char in word:
        if(char in letters_guessed):
          print(word[counter], end=" ")
          correct_letters += 1
        else:
          print(" ", end = " ")
        counter += 1
  game_run()
  #Win and Loose
  if guessed == True:
    print(f"Congratulations, you win! The word was {word}!")
    print()
  else:
    print()
    print(f"Game over! The word was {word}!")
  #Try Again
  try_again = input("Press 1 to try again, 0 to exit. ")
  try:
      try_again = int(try_again)  # non-numeric input from user could otherwise crash at this point
      if try_again == 0:
          break # break out of this while loop
  except:
      print("Non number entered")