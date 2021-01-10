#Step 2

import random
word_list = ["nenem", "xupinho", "xerelete"]

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

tried_letters=[]

chosen_word = random.choice(word_list)

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

display = []
count_underscores = 0
for number in range(0, len(chosen_word)):
  display.append("_")
  count_underscores += 1

print(display)

errors = 0
found_letter = 0

while(count_underscores > 0 and errors < 6):
  print(stages[len(stages) - 1 - errors])
  guess = input("Guess a letter: ").lower()

  if guess not in tried_letters:
    tried_letters.append(guess)
    print(f"Letras tentadas: {tried_letters}")
  else:
    print("TENTA OUTRA LETRA!!!")

  word_length = len(chosen_word)
  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
      #print("Right")
      display[position] = letter
      count_underscores -= 1
      found_letter = 1
    else:
      #print("Wrong")
      if display[position] == "_":
        display[position] = "_"
  print(display)
  print(count_underscores)
  if found_letter == 0:
    errors += 1
    if(errors >= 6):
      print("Game over.")
      print(stages[0])
    found_letter = 0
  else:
    found_letter = 0

  print(f"O número de erros é igual a {errors}.")

if "_" not in display:
  print("You win! Congratulations!")